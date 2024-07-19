# Trajectory Tracking using Python
This project involves tracking a light green ball's trajectory from a video of a game. The steps include extracting frames from the video, segmenting the green ball, processin frames to visualize the trajectory, and creating an output video. The following scripts are used in the process:
1. `extraction.py`: Extracts game frames from a video
2. `green_colour.py`: Segments the green ball while preserving other colours
3. `sti.py`: Stitches processed frames into an MP4 video
4. `trac.py`: Tracks the light green ball in the frames and saves the frames with the visualized trajectory

## Prerequisites
- Python 3.x
- OpenCV
- NumPy
- A video file (`input_video.mp4`) for processing

## Running the scripts

1. Extract frames from the video:
   ```
   python extraction.py
   ```
2. Segment the green ball in the frames:
   ```
   python green_colour.py
   ```
3. Track the green ball and save the frames with trajectory:
   ```
   python trac.py
   ```
4. Create a video from the processed frames:
   ```
   python sti.py
   ```

## Output
- The extracted frames will be saved in the `game_frames` directory.
- The segmented frames will be saved in the `segmented_frames` directory.
- The frames with the visualized trajectory will be saved in the `frames_with_trajectory` directory.
- The final output video will be saved as `output_video.mp4`
