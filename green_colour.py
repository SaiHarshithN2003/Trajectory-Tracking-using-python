import cv2
import os
import numpy as np

# Function to segment out the green ball from a frame while preserving other colors
def segment_green_ball(frame):
    # Define lower and upper bounds for green color in HSV color space
    lower_green = np.array([60, 30, 70])
    upper_green = np.array([120, 80, 100])

    # Convert frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only green colors
    green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)

    # Invert the mask to preserve other colors
    other_colors_mask = cv2.bitwise_not(green_mask)

    # Bitwise-AND mask and original image to get segmented image
    segmented_frame = cv2.bitwise_and(frame, frame, mask=other_colors_mask)

    return segmented_frame

# Function to process all frames in a directory
def process_frames_in_directory(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    frame_count = 0

    # Process each frame in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg"):
            frame_count += 1
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            # Read frame
            frame = cv2.imread(input_path)

            # Segment out green ball while preserving other colors
            segmented_frame = segment_green_ball(frame)

            # Save segmented frame
            cv2.imwrite(output_path, segmented_frame)

    return frame_count

# Input and output directories
input_dir = 'test_frames'  # Directory containing extracted game frames
output_dir = 'tes_seg'  # Directory to save segmented frames with other colors

# Process frames in the input directory
total_frames = process_frames_in_directory(input_dir, output_dir)

print(f"Segmentation completed. {total_frames} frames segmented and saved in '{output_dir}' folder.")
