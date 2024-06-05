#EXTRACTION OF GAME FRAMES
import cv2
import numpy as np
import os

cap = cv2.VideoCapture('input_video.mp4')

ret, ref_frame = cap.read()
if not ret:
    print("Failed to read the first frame.")
    exit()

ref_gray = cv2.cvtColor(ref_frame, cv2.COLOR_BGR2GRAY)
ref_hist = cv2.calcHist([ref_gray], [0], None, [256], [0, 256])

cv2.normalize(ref_hist, ref_hist, 0, 1, cv2.NORM_MINMAX)

threshold = 0.8 

output_dir = 'game_frames'
os.makedirs(output_dir, exist_ok=True)

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)

    similarity = cv2.compareHist(ref_hist, hist, cv2.HISTCMP_CORREL)

    if similarity >= threshold:
        output_path = os.path.join(output_dir, f'frame_{frame_count}.jpg')
        cv2.imwrite(output_path, frame)
        frame_count += 1

cap.release()

print(f'{frame_count} frames were extracted and saved to {output_dir}')