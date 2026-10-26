
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Render the application's home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the submitted text and return the emotion results."""
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Please provide text to analyze!", 400

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Unable to analyze the provided text.", 500

    result = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
