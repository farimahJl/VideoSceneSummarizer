from flask import Flask, request, jsonify
import os
from scene_detection import detect_scenes
from summarize_video import create_summary

app = Flask(__name__)
UPLOAD_FOLDER = "data/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/detect-scenes", methods=["POST"])
def detect_scenes_api():
    video = request.files['video']
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    video.save(video_path)
    scenes = detect_scenes(video_path)
    return jsonify({"scenes": scenes})

@app.route("/summarize", methods=["POST"])
def summarize_api():
    video = request.files['video']
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    video.save(video_path)
    threshold = int(request.form.get("threshold", 30))
    scenes = detect_scenes(video_path, threshold)
    output_path = "outputs/summary_videos/summary.mp4"
    create_summary(video_path, scenes, output_path)
    return jsonify({"message": "Summary created", "path": output_path})

if __name__ == "__main__":
    app.run(debug=True)