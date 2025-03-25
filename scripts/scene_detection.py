import cv2
import numpy as np
from tqdm import tqdm

def detect_scenes(video_path, threshold=30):
    """
    Detect scenes in a video by analyzing frame differences.

    Args:
        video_path (str): Path to the video file.
        threshold (float): Scene detection threshold.

    Returns:
        list: Frame numbers where scene transitions occur.
    """
    cap = cv2.VideoCapture(video_path)
    prev_frame = None
    scene_boundaries = []
    frame_count = 0

    pbar = tqdm(total=int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), desc="Detecting scenes")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if prev_frame is not None:
            diff = cv2.absdiff(prev_frame, gray).mean()
            if diff > threshold:
                scene_boundaries.append(frame_count)
        prev_frame = gray
        frame_count += 1
        pbar.update(1)

    cap.release()
    pbar.close()
    return scene_boundaries

# Example usage:
# scenes = detect_scenes("example.mp4", threshold=30)
# print(scenes)