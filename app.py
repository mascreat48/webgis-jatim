from flask import Flask, render_template_string, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    min_pop = request.args.get("min_pop", default=0, type=int)
    keyword = request.args.get("keyword", default="", type=str)

    df = pd.read_csv("data.csv")

    # filter populasi
    df = df[df["populasi"] >= min_pop]

    # filter nama
    if keyword:
        df = df[df["nama"].str.contains(keyword, case=False)]

    return render_template_string(
        open("index.html").read(),
        data=df.to_dict("records"),
        min_pop=min_pop,
        keyword=keyword
    )

app.run(debug=True)
