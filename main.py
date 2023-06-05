from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def definition(word):

    df = pd.read_csv("dictionary.csv")  # reading the csv file
    word_definition = word.upper()  # setting a value for case of word outside dictionary

    for index, item in enumerate(df["word"]):
        if word == item:
            word_definition = df["definition"][index]
    return {"definition": word_definition,
            "word": word}


app.run(debug=True)
