from flask import (
    Blueprint,
    send_from_directory,
    request,
    render_template,
    redirect,
    url_for,
)
import pandas as pd

from app.utils import get_prediction

UPLOAD_PATH = "uploads"
ALLOWED_FILE_TYPES = ["csv"]

core_bp = Blueprint("core", __name__)


@core_bp.post("/download/")
def download_csv_template():
    return send_from_directory(
        UPLOAD_PATH, "aqi_input_template.csv", as_attachment=True
    )


@core_bp.post("/upload/")
def upload():
    data_path = request.files["csv"]
    if data_path and data_path.filename.split(".")[1] in ALLOWED_FILE_TYPES:
        df = pd.read_csv(data_path)
        prediction = list(get_prediction(df))
        return render_template("predict.html", prediction=prediction), 200
    return redirect(url_for("api.predict"))
