import os

from flask import Flask, session, redirect

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = os.environ.get("SECRET_KEY") or 'keep it secret, keep it safe'


@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1

    return f"counter: {session['count']}"


@app.route('/destroy_session')
def destroy_session():
    if 'count' in session:
        session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
