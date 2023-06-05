from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")  # reading the csv file here, will be executed once
# in function, it would be executed as many times as user wants (we save resources)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def api(word):
    word_definition = word.upper()  # setting a value for case of word outside dictionary
    for index, item in enumerate(df["word"]):
        if word == item:
            word_definition = df["definition"][index]
    return {"definition": word_definition,
            "word": word}


app.run(debug=True)
