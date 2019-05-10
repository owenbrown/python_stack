import os

from flask import Flask, session, redirect, render_template, request, url_for

from mysqlconnection import MySQLConnection

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET") or "SBV4T580VW81U0C2S6EFFVMU8QK8T730517UR07QW159BHI43A267J"


@app.route('/')
def index():
    print("get /")
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    print("post /")
    mysql = MySQLConnection('mydb')

    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form.get("comment", str())

    data = dict(name=name, location=location, language=language)
    if comment:
        print("yes comment")
        data["comment"] = comment
        comment_column = ", comment"
        comment_parameter = ", %(comment)s"
    else:
        print("no comment")
        comment_column = str()
        comment_parameter = str()

    query = f"INSERT INTO dojo_survey(name, location, language{comment_column}) " \
        f"VALUES (%(name)s, %(location)s, %(language)s{comment_parameter});"

    comment_id = mysql.query_db(query, data)
    session["comment_id"] = comment_id
    session["location"] = location
    session["language"] = language
    session["comment"] = comment

    return redirect(url_for('result'))


@app.route('/result')
def result():
    print("get /result")
    for field in ["comment_id", "location", "language", "comment"]:
        if field not in session:
            print("missing fields")
            return redirect('/')

    return render_template('result.html',
                    comment_id=session["comment_id"],
                    location=session["location"],
                    language=session["language"],
                    comment=session["comment"]
                    )


if __name__ == "__main__":
    app.run(debug=True)
