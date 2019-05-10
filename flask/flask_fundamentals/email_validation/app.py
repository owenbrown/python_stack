import os
import re

from flask import Flask, flash, redirect, render_template, request, url_for

from mysqlconnection import MySQLConnection

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET") or "SBV4T580VW81U0C2S6EFFVMU8QK8T730517UR07QW159BHI43A267J"


def __is_valid_email(s: str) -> bool:
    """return whether the address is valid"""
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    return bool(email_regex.match(s))


@app.route('/')
def index():
    print("get /")
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    print("post /")

    email = request.form['email']

    if not __is_valid_email(email):  # test whether a field matches the pattern
        flash("Invalid email address!", "error")
        return redirect("/")

    mysql = MySQLConnection('mydb')
    query = "INSERT into email_only(email_address) VALUE(%(email)s);"
    data = dict(email=email)
    mysql.query_db(query, data)

    return redirect(url_for('success'))


@app.route('/success')
def success():
    print("get /success")
    flash('You were successfully logged in')

    mysql = MySQLConnection("mydb")
    query = "SELECT email_address " \
            "FROM email_only;"
    emails = [r["email_address"] for r in mysql.query_db(query)]

    return render_template('success.html', emails=emails)


if __name__ == "__main__":
    app.run(debug=True)
