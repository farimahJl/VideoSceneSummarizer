import argparse
from scripts.metadata_extraction import extract_metadata
from scripts.scene_detection import detect_scenes
from scripts.keyframe_extraction import extract_keyframes
from scripts.summarize_video import create_summary
from scripts.visualize import plot_timeline

def main():
    parser = argparse.ArgumentParser(description="Video Scene Summarizer")
    parser.add_argument("--input", required=True, help="Path to input video")
    parser.add_argument("--output", help="Path to output summary video")
    parser.add_argument("--threshold", type=int, default=30, help="Scene detection threshold")
    parser.add_argument("--metadata", action="store_true", help="Extract video metadata")
    parser.add_argument("--visualize", action="store_true", help="Generate visualizations")
    args = parser.parse_args()

    print("Starting video summarization...")
    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")

    # Extract metadata if requested
    if args.metadata:
        metadata = extract_metadata(args.input)
        print("Video Metadata:")
        print(metadata)

    # Detect scenes
    scenes = detect_scenes(args.input, threshold=args.threshold)
    print(f"Detected scenes: {scenes}")

    # Visualize if requested
    if args.visualize:
        plot_timeline(scenes, 1000, "outputs/visualizations/timeline.png")
        print("Timeline visualization saved.")

    # Create summary video if output is specified
    if args.output:
        create_summary(args.input, scenes, args.output)
        print(f"Summary video saved at {args.output}")

if __name__ == "__main__":
    main()
