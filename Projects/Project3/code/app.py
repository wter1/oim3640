import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from prototype import find_stop_near

load_dotenv()

app = Flask(__name__)

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    place = request.form.get("place")

    if not place or not place.strip():
        return render_template(
            "index.html",
            error="Please enter a place name or address."
        )

    try:
        result = find_stop_near(place)

        return render_template(
            "result.html",
            result=result,
            mapbox_token=MAPBOX_TOKEN
        )

    except Exception as error:
        return render_template(
            "index.html",
            error=f"Sorry, something went wrong: {error}"
        )


if __name__ == "__main__":
    app.run(debug=True)