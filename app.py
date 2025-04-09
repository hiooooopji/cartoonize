from flask import Flask, render_template, request, send_from_directory, jsonify
import os
import sys
import cv2

# Add src directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from cartoonizer import cartoonize
from sketchpen import sketchpen_effect
from sketchpen_color import sketchpen_color_effect

app = Flask(__name__, template_folder="templates")

UPLOAD_FOLDER = os.path.join(os.getcwd(), "images")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create images folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    if not file:
        return jsonify({"error": "No file uploaded!"})

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], "uploaded.jpg")
    file.save(file_path)

    return jsonify({"message": "File uploaded!", "image_url": f"/images/uploaded.jpg?{os.path.getmtime(file_path)}"})

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    effect = data.get("effect")
    input_path = os.path.join(app.config["UPLOAD_FOLDER"], "uploaded.jpg")
    
    if not os.path.exists(input_path):
        return jsonify({"error": "No uploaded image found!"})

    if effect == "cartoon":
        output = cartoonize(input_path)
        output_filename = "cartoon_output.jpg"
    elif effect == "sketch":
        output = sketchpen_effect(input_path)
        output_filename = "sketch_output.jpg"
    elif effect == "sketch_color":
        output = sketchpen_color_effect(input_path)
        output_filename = "sketch_color_output.jpg"
    else:
        return jsonify({"error": "Invalid effect!"})

    output_path = os.path.join(app.config["UPLOAD_FOLDER"], output_filename)
    cv2.imwrite(output_path, output)

    return jsonify({"image_url": f"/images/{output_filename}?{os.path.getmtime(output_path)}"})

@app.route("/images/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)
