from flask import Flask, render_template, request
from movies import movies

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    name = request.form["name"]
    genre = request.form["genre"]
    language = request.form["language"]
    mood = request.form["mood"]

    recommendations = []

    for movie in movies:

        score = 0

        if movie["genre"] == genre:
            score = score + 3

        if movie["language"] == language:
            score = score + 2

        if movie["mood"] == mood:
            score = score + 2

        if score > 0:
            recommendations.append({
                "name": movie["name"],
                "genre": movie["genre"],
                "language": movie["language"],
                "mood": movie["mood"],
                "score": score
            })

    recommendations.sort(key=lambda x: x["score"], reverse=True)

    recommendations = recommendations[:5]

    return render_template(
        "result.html",
        name=name,
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)