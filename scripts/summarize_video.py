import os
import subprocess

def create_summary(input_video, scenes, output_path):
    """
    Create a summarized video from detected scenes.

    Args:
        input_video (str): Path to the input video.
        scenes (list): List of frame numbers where scenes start.
        output_path (str): Path to save the summary video.
    """
    temp_dir = "temp_clips"
    os.makedirs(temp_dir, exist_ok=True)

    for i, scene in enumerate(scenes):
        start_time = max(0, scene / 30 - 2)  # Assuming 30 FPS
        duration = 4
        clip_path = os.path.join(temp_dir, f"clip_{i}.mp4")
        subprocess.call([
            "ffmpeg", "-i", input_video, "-ss", str(start_time),
            "-t", str(duration), "-c:v", "libx264", clip_path
        ])

    # Concatenate clips
    concat_file = "concat_list.txt"
    with open(concat_file, "w") as f:
        for clip in sorted(os.listdir(temp_dir)):
            f.write(f"file '{os.path.join(temp_dir, clip)}'\n")
    subprocess.call(["ffmpeg", "-f", "concat", "-safe", "0", "-i", concat_file,
                     "-c", "copy", output_path])

# Example usage:
# create_summary("example.mp4", [100, 300, 500], "outputs/summary_videos/summary.mp4")