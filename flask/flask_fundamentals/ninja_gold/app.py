import os

from flask import Flask, render_template, redirect, session

from places import places

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET") or "8FSBV4T580VW81U0C2S6EFFVMU8QK8T730517UR07QW15X869BHI43A267J"


@app.route('/', methods=["GET"])
def index():
    print("received get")
    gold = session['gold'] or 0
    messages = session['messages'] or []
    return render_template("index.html", gold=gold, places=places, messages=messages)


@app.route('/process_money', methods=["POST"])
def process_money():
    print("received post")

    place_name = "casino"
    delta = places[place_name].find_gold()
    session['gold'] = session.get('gold', 0) + delta

    msg = f"Your earned {delta} gold at the {place_name}. Total gold is {session['gold']}"
    if 'messages' in session:
        session['messages'].append(msg)
    else:
        session['messages'] = [msg]

    return redirect("/")


@app.route("/sample")
def sample():
    return render_template("backup_template.html", places=places)


if __name__ == "__main__":
    app.run(debug=True)
