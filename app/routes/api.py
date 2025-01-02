from flask import Blueprint, render_template, redirect

app_bp = Blueprint('api', __name__)


@app_bp.route("/")
def index():
    return redirect("/home")


@app_bp.errorhandler(404)
def page_not_found():
    return render_template("404.html"), 404


@app_bp.route("/home/", methods=["GET", "POST"])
def home():
    return render_template("home.html"), 200


@app_bp.route("/model/", methods=["GET", "POST"])
def model():
    return render_template("model.html"), 200


@app_bp.route("/model/predict/", methods=["GET", "POST"])
def predict():
    return render_template("predict.html"), 200


@app_bp.route("/about/", methods=["GET", "POST"])
def about():
    return render_template("about.html"), 200
