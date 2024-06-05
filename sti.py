import cv2
import os

# Function to stitch frames into an MP4 video
def frames_to_video(input_dir, output_path, fps):
    # Get list of frames sorted by filename
    frames = [cv2.imread(os.path.join(input_dir, f)) for f in sorted(os.listdir(input_dir)) if f.endswith('.jpg')]

    # Get frame size from the first frame
    frame_height, frame_width, _ = frames[0].shape

    # Initialize VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Write frames to video
    for frame in frames:
        out.write(frame)

    # Release VideoWriter object
    out.release()

    print(f"Video saved: {output_path}")

# Input directory containing frames
input_dir = 'final frames/frames_with_trajectory'
# Output path for the MP4 video
output_path = 'output_video.mp4'

# Frames per second of the output video
fps = 60

# Convert frames to video
frames_to_video(input_dir, output_path, fps)
