import os
import random

from flask import Flask, session, redirect, render_template, request, url_for

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = os.environ.get("SECRET_KEY") or 'keep it secret, keep it safe'


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", text=None, color=None)


@app.route('/', methods=['POST'])
def guess():
    print("guess")
    if "number" not in session:
        print("number not in session")
        session["number"] = random.randint(1, 100)
        session["number"] = 17
    else:
        print("number in sessioen")
        print(session["number"])

    if int(request.form['guess']) == session['number']:
        text = f"{session['number']} was the number!"
        color = "green"

    elif int(request.form['guess']) > session["number"]:
        text = "TooHigh"
        color = "red"
    else:
        text = "TooLow"
        color = "red"

    return render_template("index.html", text=text, color=color)


@app.route("/testurlfor")
def testurlfor():
    print(url_for(".reset"))
    return url_for(".reset")


@app.route('/reset')
def reset():
    if 'number' in session:
        session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
