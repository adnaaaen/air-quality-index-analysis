# from app import create_app
#
# app = create_app()
#
# if __name__ == "__main__":
#     app.run(debug=True)


import pandas as pd
from app.utils import get_prediction

df = pd.read_csv("~/Downloads/aqi_input_template.csv")
out = get_prediction(df)

print(out)
