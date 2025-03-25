import matplotlib.pyplot as plt

def plot_timeline(scenes, video_length, output_path):
    """
    Plot a timeline of scene changes.

    Args:
        scenes (list): List of scene boundaries (frame numbers).
        video_length (int): Total number of frames in the video.
        output_path (str): Path to save the timeline visualization.
    """
    plt.figure(figsize=(10, 2))
    for scene in scenes:
        plt.axvline(x=scene / video_length, color="red", linestyle="--")
    plt.title("Scene Timeline")
    plt.xlabel("Normalized Time")
    plt.savefig(output_path)
    plt.show()

# Example usage:
# plot_timeline([100, 300, 500], 1000, "outputs/visualizations/timeline.png")