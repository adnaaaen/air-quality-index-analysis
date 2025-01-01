from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/home")

@app.route("/home/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/predict/", methods=["GET", "POST"])
def predict():
    return render_template("model.html")

@app.route("/dashboard/", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")

@app.route("/about/", methods=["GET", "POST"])
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

