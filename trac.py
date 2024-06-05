import cv2
import os
import numpy as np

# Function to segment out the light green ball from a frame while preserving other colors
def segment_light_green_ball(frame):
    # Define lower and upper bounds for light green color in HSV color space
    lower_light_green = np.array([35, 50, 50])
    upper_light_green = np.array([90, 255, 255])

    # Convert frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only light green colors
    light_green_mask = cv2.inRange(hsv_frame, lower_light_green, upper_light_green)

    # Find contours in the mask
    contours, _ = cv2.findContours(light_green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize centroid coordinates
    centroid = None

    # Proceed if at least one contour is found
    if contours:
        # Calculate centroid of the largest light green contour
        max_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(max_contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            centroid = (cX, cY)

    return centroid

# Function to track light green ball in a sequence of frames and save them with trajectory
def track_and_save_frames(frames, output_dir):
    prev_centroid = None
    trajectory = []

    # Define boundary limits (4 points) for ROI
    roi_points = np.array([[329, 262], [1543, 246], [1555, 832], [363, 832]])
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, frame in enumerate(frames):
        # Detect centroid of light green ball
        centroid = segment_light_green_ball(frame)

        # Check if the centroid is within the ROI
        if centroid is not None and cv2.pointPolygonTest(roi_points, centroid, False) >= 0:
            # Store centroid coordinates
            trajectory.append(centroid)

        # Draw lines connecting trajectory points
        for j in range(1, len(trajectory)):
            cv2.line(frame, trajectory[j - 1], trajectory[j], (0, 255, 0), 2)

        # Draw rectangle around the ROI
        cv2.polylines(frame, [roi_points], True, (255, 0, 0), 2)

        # Draw circle around the centroid
        if centroid is not None:
            cv2.circle(frame, centroid, 10, (0, 0, 255), -1)

        # Save the frame with trajectory
        output_path = os.path.join(output_dir, f"frame_{i}.jpg")
        cv2.imwrite(output_path, frame)

    print(f"Frames saved in directory: {output_dir}")

# Read frames from a directory (change as needed)
input_dir = 'tes_seg'  # Directory containing frames
frames = [cv2.imread(os.path.join(input_dir, f)) for f in sorted(os.listdir(input_dir)) if f.endswith('.jpg')]

# Output directory to save frames with trajectory
output_dir = 'frames_with_trajectory_test'
# Track light green ball in the sequence of frames and save them with trajectory
track_and_save_frames(frames, output_dir)
