from flask import Flask, render_template, redirect, send_from_directory, request
import pandas as pd

app = Flask(__name__)

UPLOAD_PATH = "uploads"


@app.route("/")
def index():
    return redirect("/home")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/home/", methods=["GET", "POST"])
def home():
    return render_template("home.html"), 200


@app.route("/model/", methods=["GET", "POST"])
def model():
    return render_template("model.html"), 200


@app.route("/model/predict/", methods=["GET", "POST"])
def predict():
    return render_template("predict.html"), 200


@app.route("/about/", methods=["GET", "POST"])
def about():
    return render_template("about.html", name="adnan"), 200


@app.post("/download/")
def download_csv_template():
    return send_from_directory(UPLOAD_PATH, "input_template.csv", as_attachment=True)


@app.post("/upload/")
def upload():
    data_path = request.files["csv"]
    if data_path:
        df = pd.read_csv(data_path)
        out = list(df.columns)
        return render_template("predict.html", prediction=out), 200
    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)
