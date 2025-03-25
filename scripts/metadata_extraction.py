import subprocess
import json

def extract_metadata(video_path):
    """
    Extract metadata from a video using FFmpeg.

    Args:
        video_path (str): Path to the video file.

    Returns:
        dict: Metadata as a dictionary.
    """
    cmd = [
        "ffprobe",
        "-v", "quiet",
        "-print_format", "json",
        "-show_format",
        "-show_streams",
        video_path
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    metadata = json.loads(result.stdout)
    return metadata

# Example usage:
# metadata = extract_metadata("example.mp4")
# print(metadata)
