from flask import Flask, render_template, request
from prototype import find_stop_near

app = Flask(__name__)


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
        stop_name, wheelchair_accessible = find_stop_near(place)

        return render_template(
            "result.html",
            place=place,
            stop_name=stop_name,
            wheelchair_accessible=wheelchair_accessible
        )

    except Exception as error:
        return render_template(
            "index.html",
            error=f"Sorry, something went wrong: {error}"
        )


if __name__ == "__main__":
    app.run(debug=True)