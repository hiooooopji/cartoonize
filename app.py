from flask import Flask, request, render_template, send_from_directory
import os
from cartoonizer import cartoonize
from sketchpen import sketchpen

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            effect = request.form.get("effect")

            if effect == "cartoon":
                output_path = os.path.join(PROCESSED_FOLDER, "cartoon_" + file.filename)
                cartoonize(filepath, output_path)
            elif effect == "sketchpen":
                output_path = os.path.join(PROCESSED_FOLDER, "sketchpen_" + file.filename)
                sketchpen(filepath, output_path)

            return render_template("index.html", filename=os.path.basename(output_path))
    
    return render_template("index.html", filename=None)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(PROCESSED_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
