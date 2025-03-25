import cv2
import os

def extract_keyframes(video_path, scene_boundaries, output_dir):
    """
    Extract keyframes at scene boundaries.

    Args:
        video_path (str): Path to the video file.
        scene_boundaries (list): List of frame numbers for scene transitions.
        output_dir (str): Directory to save keyframes.
    """
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    for i, frame_no in enumerate(scene_boundaries):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret, frame = cap.read()
        if ret:
            output_path = os.path.join(output_dir, f"keyframe_{i + 1}.jpg")
            cv2.imwrite(output_path, frame)
    cap.release()

# Example usage:
# extract_keyframes("example.mp4", [100, 300, 500], "outputs/thumbnails/")