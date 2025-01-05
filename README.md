[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=60&pause=2000&color=F7F7F7&width=1000&height=100&lines=Air+Quality+Index+Analysis;An+End-to-End+ML+Application)](https://www.linkedin.com/in/adnaaaen/)

>[!NOTE]
>
>**You must download the dataset before running notebooks.**
>
>To download the dataset, run the script located at `scripts/download_data.py`.
>
>You can execute the script by running:
> ```
> python scripts/download_data.py
> ```

```
Directory structure:
└── air-quality-index-analysis/
    ├── README.md
    ├── LICENSE
    ├── requirements.txt
    ├── .gitattributes
    ├── Dockerfile
    ├── run.py
    ├── app/
    │   ├── __init__.py
    │   ├── config/
    │   │   ├── __init__.py
    │   │   └── paths.py
    │   ├── routes/
    │   │   ├── __init__.py
    │   │   ├── api.py
    │   │   └── core.py
    │   ├── static/
    │   │   ├── css/
    │   │   │   └── style.css
    │   │   └── images/
    │   ├── templates/
    │   │   ├── 404.html
    │   │   ├── about.html
    │   │   ├── base.html
    │   │   ├── home.html
    │   │   ├── model.html
    │   │   └── predict.html
    │   ├── uploads/
    │   │   └── aqi_input_template.csv
    │   └── utils/
    │       ├── __init__.py
    │       └── model_prediction.py
    ├── data/
    │   └── raw/
    │       └── README.md
    ├── model/
    │   ├── encoders/
    │   │   ├── binary_encoder.joblib
    │   │   └── standard_scaler.joblib
    │   └── trained/
    │       └── random_forest_regressor.joblib
    ├── notebooks/
    │   ├── 01_data_cleaning.ipynb
    │   ├── 02_eda.ipynb
    │   ├── 03_preprocessing.ipynb
    │   └── 04_model_building.ipynb
    └── scripts/
        └── download_data.py

```
