import argparse
from scripts.metadata_extraction import extract_metadata
from scripts.scene_detection import detect_scenes
from scripts.keyframe_extraction import extract_keyframes
from scripts.summarize_video import create_summary
from scripts.visualize import plot_timeline

def main():
    parser = argparse.ArgumentParser(description="Video Scene Summarizer - Process videos, detect scenes, and create summaries.")
    parser.add_argument("--input", required=True, help="Path to the input video file.")
    parser.add_argument("--output", default="outputs/summary_videos/summary.mp4", help="Path to save the output summarized video.")
    parser.add_argument("--threshold", type=float, default=30, help="Threshold for scene detection.")
    parser.add_argument("--metadata", action="store_true", help="Extract and display video metadata.")
    parser.add_argument("--visualize", action="store_true", help="Generate visualizations for detected scenes.")
    parser.add_argument("--keyframes", action="store_true", help="Extract keyframes for detected scenes.")
    args = parser.parse_args()

    # Extract metadata if requested
    if args.metadata:
        print("[INFO] Extracting video metadata...")
        metadata = extract_metadata(args.input)
        print("[METADATA]", metadata)

    # Detect scenes
    print("[INFO] Detecting scenes...")
    scenes = detect_scenes(args.input, args.threshold)
    print(f"[INFO] Detected {len(scenes)} scenes: {scenes}")

    # Visualize timeline if requested
    if args.visualize:
        print("[INFO] Generating visualizations...")
        timeline_path = "outputs/visualizations/timeline.png"
        plot_timeline(scenes, int(args.input.split('.')[0]), timeline_path)
        print(f"[INFO] Timeline saved at {timeline_path}")

    # Extract keyframes if requested
    if args.keyframes:
        print("[INFO] Extracting keyframes...")
        keyframes_dir = "outputs/thumbnails/"
        extract_keyframes(args.input, scenes, keyframes_dir)
        print(f"[INFO] Keyframes saved in {keyframes_dir}")

    # Create video summary
    print("[INFO] Creating video summary...")
    create_summary(args.input, scenes, args.output)
    print(f"[INFO] Video summary saved at {args.output}")

if __name__ == "__main__":
    main()
