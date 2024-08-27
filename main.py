import cv2
import numpy as np
import multiprocessing as mp
import os
import time
from moviepy.editor import VideoFileClip, AudioFileClip

def process_frame(frame, new_width, new_height):
    # Apply Gaussian Blur to the frame
    blurred = cv2.GaussianBlur(frame, (101, 101), 0)
    # Resize the blurred frame to the new dimensions
    blurred_resized = cv2.resize(blurred, (new_width, new_height))
    # Calculate the y-offset to center the original frame on the blurred background
    y_offset = (new_height - frame.shape[0]) // 2
    # Overlay the original frame onto the blurred and resized frame
    blurred_resized[y_offset:y_offset+frame.shape[0], 0:frame.shape[1]] = frame
    return blurred_resized

def convert_16_9_to_9_16_with_audio(input_path, output_path, progress_callback=print):
    start_time = time.time()

    # Open the video file
    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Define new dimensions for the output video (9:16 aspect ratio)
    new_height = width * 16 // 9
    new_width = width

    # Temporary output video file
    temp_output = "temp_output.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(temp_output, fourcc, fps, (new_width, new_height))

    # Set up multiprocessing
    num_processes = mp.cpu_count()
    pool = mp.Pool(processes=num_processes)

    batch_size = 128  # Number of frames to process in a batch # adjust based on your specs
    frame_count = 0  # Counter for processed frames

    progress_callback(f"Processing video: {0.01:.2f}%")

    while True:
        frames = []
        for _ in range(batch_size):
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)

        if not frames:
            break

        # Process the frames using multiprocessing
        processed_frames = pool.starmap(process_frame, [(f, new_width, new_height) for f in frames])

        # Write processed frames to the output video
        for frame in processed_frames:
            out.write(frame)

        frame_count += len(frames)
        progress = (frame_count / total_frames) * 100
        progress_callback(f"Processing video: {progress:.2f}%")

    # Clean up
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    pool.close()
    pool.join()

    progress_callback("Video processing completed. Now adding audio...")

    # Add audio to the processed video
    video = VideoFileClip(temp_output)
    audio = AudioFileClip(input_path)
    final_clip = video.set_audio(audio)
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", threads=num_processes)

    # Remove the temporary output video
    os.remove(temp_output)

    elapsed_time = time.time() - start_time
    progress_callback(f"Video conversion with audio completed in {elapsed_time:.2f} seconds!")

def main():
    input_video = "input.mp4"
    output_video = "out/output.mp4"

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_video), exist_ok=True)

    convert_16_9_to_9_16_with_audio(input_video, output_video)

if __name__ == "__main__":
    main()