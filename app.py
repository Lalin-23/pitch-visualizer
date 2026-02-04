from flask import Flask, render_template, request
from services.text_segmentation import segment_text
from services.prompt_engineering import generate_visual_prompt
from services.image_generator import generate_image
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["story"]
        style = request.form["style"]

        segments = segment_text(text)
        storyboard = []

        for segment in segments:
            visual_prompt = generate_visual_prompt(segment, style)
            image_url = generate_image(visual_prompt)
            storyboard.append({
                "text": segment,
                "image": image_url
            })

        return render_template("storyboard.html", storyboard=storyboard)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

