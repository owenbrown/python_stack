from flask import Flask, render_template, session
from places import places

app = Flask(__name__)


@app.route('/')
def index():
    gold = session.get('gold') or 0
    return render_template("index.html", gold=gold, places=places)


@app.route("/sample")
def sample():
    return render_template("backup_template.html", places=places)


if __name__ == "__main__":
    app.run(debug=True)
