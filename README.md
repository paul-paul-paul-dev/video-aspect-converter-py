# video-aspect-converter-py

## Description

**video-aspect-converter-py** is a Python script designed to convert videos from a 16:9 aspect ratio to 9:16. It applies a Gaussian blur to the original video, resizes the blurred version to fit the new aspect ratio, and overlays the original video in the center. This results in a visually appealing vertical video that retains the original content in focus. The script also retains the original audio, providing a complete video processing solution.

## Features

- Converts videos from 16:9 to 9:16 aspect ratio.
- Applies a blurred background to fill the 9:16 frame.
- Retains the original audio track from the input video.
- Supports multiprocessing for faster video processing.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/paul-paul-paul-dev/video-aspect-converter-py
    cd video-aspect-converter-py
    ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

4. Install the required Python packages:

    ```bash
    pip install --upgrade -r requirements.txt
    ```

## Usage

Place your input video in the same directory as the script or provide a path to it. The script will output the processed video to the specified output directory.

### Example command

```bash
python main.py
```

### Custoxmize input and output paths

To use different input and output paths, modify the input_video and output_video variables in the main() function.

### Customize output aspect ratio

```python
    # Define new dimensions for the output video (9:16 aspect ratio)
    new_height = width * 16 // 9 # change to 1 // 1 or 3 // 2 or something else
    new_width = width
```

## Examples: Video Before and After

Below are examples showing the transformation of a video from a 16:9 aspect ratio to 9:16 using VideoAspectConverter.

Before Conversion (16:9)

![before_input](img/input.gif)

After Conversion (9:16)

![after_output9-16](img/output_9-16.gif)

After Conversion (1:1)

![after_output1-1](img/output_1-1.gif)

In the example above, notice how the original content remains clear and focused in the center, while the blurred version of the video fills the background, maintaining a full-frame view.

Note: Replace the image URLs with actual screenshots from your processed videos.

## Dependencies

```sh
opencv-python
numpy
moviepy
```

These dependencies will be installed automatically with the requirements.txt.
