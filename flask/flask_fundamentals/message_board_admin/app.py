import os
import re
import secrets

from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_bcrypt import Bcrypt

from mysqlconnection import MySQLConnection

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET') or "38#&TN#)H3NT2HSN2TEH2OU2NHU22OE"

b_crypt = Bcrypt(app)


def __is_valid_email(s: str) -> bool:
    """return whether the address is valid"""
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    return bool(email_regex.match(s))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    if not (first_name and last_name and email):
        flash("Our form validation failed!", "error")
        return redirect("index.html")

    password = request.form['password']
    password_hash = b_crypt.generate_password_hash(password)

    mysql = MySQLConnection("mydb")
    query = "INSERT into peak_user(first_name, last_name, email, password_hash) " \
            "VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s)"
    data = dict(first_name=first_name, last_name=last_name, email=email, password_hash=password_hash)
    r = mysql.query_db(query, data)
    if r is False:
        flash("Sadly, something is broken with our database. Whoops!")
        return redirect(url_for("index"))
    session["token"] = "valid"
    session["email"] = email
    flash("Success registering!")
    return redirect(url_for("wall"))


def __get_password_hash(email: str) -> str:
    mysql = MySQLConnection("mydb")
    query = "SELECT password_hash " \
            "FROM peak_user " \
            "WHERE email = %(email)s"
    data = dict(email=email)
    r = mysql.query_db(query, data)

    if r:
        return r[0]["password_hash"]


@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    if not (email and password):
        flash("Our form validation failed!")
        return redirect(url_for("index"))

    password_hash = __get_password_hash(email)
    if not password_hash:
        flash("We don't have a record of this email")
        return redirect(url_for("index"))
    try:
        if b_crypt.check_password_hash(__get_password_hash(email), password):
            session["token"] = "valid"
            session["email"] = email
            flash("Welcome back")
            return redirect(url_for("wall"))
    except ValueError:
        pass

    flash("That password is incorrect")
    return redirect(url_for("index"))


@app.route("/success")
def success():
    if session.get("token") != "valid":
        flash("You must be logged in to view this page")
        return redirect(url_for("index"))

    return render_template("success.html")


@app.route("/logout")
def logout():
    if "token" in session:
        del session["token"]
        flash("I've logged you out")
    else:
        flash("You weren't logged in.")

    return redirect(url_for("index"))


@app.route("/wall")
def wall():
    print("get /wall")
    print(session.get("token"))
    if session.get("token") != "valid":
        flash("You must be logged in to view this page")
        return redirect(url_for("index"))

    # Display link to user page for admins
    mysql = MySQLConnection("mydb")
    query = "SELECT admin_level " \
            "FROM peak_user " \
            "WHERE email = %(email)s"
    data = dict(email=session['email'])
    res = mysql.query_db(query, data)
    if res:
        admin_level = res[0]["admin_level"]
    else:
        admin_level = 1

    # Get other messages
    mysql = MySQLConnection("mydb")
    query = "SELECT sender, content, ts " \
            "FROM board_message " \
            "WHERE recipient = %(email)s" \
            "ORDER BY ts desc " \
            "LIMIT 20;"
    data = dict(email=session['email'])
    messages = mysql.query_db(query, data)
    if messages is False:
        flash("Sadly, there was an error with query 1")
        return redirect(url_for("index"))

    # Get other users
    mysql = MySQLConnection("mydb")
    query = "SELECT first_name, email " \
            "FROM peak_user " \
            "ORDER BY first_name;"
    users = mysql.query_db(query)
    if users is False:
        flash("Sadly, there was an error with query 2")
        return redirect(url_for("index"))
    # for message in messages:
    #     message["ts"] = str(message["ts"])

    return render_template("wall.html", email=session["email"], messages=messages, users=users,
                           admin_level=admin_level)


@app.route("/wall", methods=["POST"])
def send_message():
    print("post /wall")
    mysql = MySQLConnection("mydb")
    query = "INSERT INTO board_message(sender, recipient, content) " \
            "VALUE (%(sender)s, %(recipient)s, %(content)s);"
    data = dict(
        sender=session["email"],
        recipient=request.form["recipient"],
        content=request.form["content"])
    mysql.query_db(query, data)

    flash(f"You sent a message to {request.form['recipient']}")

    return redirect(url_for("wall"))


@app.route("/wall/ts/<ts>", methods=["GET"])
def delete_message(ts):
    print("get /wall")
    mysql = MySQLConnection("mydb")
    query = "DELETE FROM board_message " \
            "WHERE ts = %(ts)s;"
    data = dict(ts=ts)
    mysql.query_db(query, data)

    flash(f"You deleted a message")

    return redirect(url_for("wall"))


@app.route("/bone")
def bone():
    return "bone"


@app.route("/user2")
def user():
    print("get /user")
    if 'email' not in session:
        flash("you're not signed in")
        return redirect(url_for('index'))

    mysql = MySQLConnection("mydb")
    query = "SELECT admin_level " \
            "FROM peak_user " \
            "WHERE email = %(email)s"
    data = dict(email=session['email'])
    res = mysql.query_db(query, data)
    if not res:
        flash("you're not signed in")
        return redirect(url_for("index"))
    if res[0]["admin_level"] != 9:
        flash("Sorry, you aren't an admin")
        return redirect(url_for("wall"))

    mysql = MySQLConnection("mydb")
    query = "SELECT first_name, last_name, email, admin_level " \
            "FROM peak_user " \
            "ORDER BY email;"
    users = mysql.query_db(query)

    return render_template("users.html", users=users)


@app.route("/user/<target_email>/suspend")
def suspend(target_email):
    if 'email' in session:
        print("get /admin")
        mysql = MySQLConnection("mydb")
        query = "SELECT admin_level " \
                "FROM peak_user " \
                "WHERE email = %(admin_email)s"
        data = dict(admin_email=session['email'])
        res = mysql.query_db(query, data)

    if not ('email' in session and res):
        flash("you're not signed in")
        return redirect(url_for("index"))

    if res[0]["admin_level"] != 9:
        flash("Sorry, you aren't an admin")
        return redirect(url_for("wall"))

    mysql = MySQLConnection("mydb")

    query = "UPDATE peak_user " \
        f"SET password_hash = '{b_crypt.generate_password_hash(str(secrets.token_hex(33)))}' " \
        f"WHERE email = %(email)s;"
    data = dict(email=target_email)
    mysql.query_db(query, data)

    flash("If the user exists, we've locked them out of their account by changing their password.")
    return redirect(url_for("user"))


@app.route("/user/<target_email>/make_admin")
def make_admin(target_email):
    if 'email' in session:
        print("get /make_admin")
        mysql = MySQLConnection("mydb")
        query = "SELECT admin_level " \
                "FROM peak_user " \
                "WHERE email = %(admin_email)s"
        data = dict(admin_email=session['email'])
        res = mysql.query_db(query, data)

    if not ('email' in session and res):
        flash("you're not signed in")
        return redirect(url_for("index"))

    if res[0]["admin_level"] != 9:
        flash("Sorry, you aren't an admin")
        return redirect(url_for("wall"))

    mysql = MySQLConnection("mydb")
    query = "UPDATE peak_user " \
        f"SET admin_level = 9 " \
        f"WHERE email = %(email)s;"
    data = dict(email=target_email)
    mysql.query_db(query, data)

    flash(f"increased {target_email}'s admin level")

    return redirect(url_for("user"))


@app.route("/user/<target_email>/remove_admin")
def remove_admin(target_email):
    if 'email' in session:
        print("get /remove_admin")
        mysql = MySQLConnection("mydb")
        query = "SELECT admin_level " \
                "FROM peak_user " \
                "WHERE email = %(admin_email)s"
        data = dict(admin_email=session['email'])
        res = mysql.query_db(query, data)

    if not ('email' in session and res):
        flash("you're not signed in")
        return redirect(url_for("index"))

    if res[0]["admin_level"] != 9:
        flash("Sorry, you aren't an admin")
        return redirect(url_for("wall"))

    mysql = MySQLConnection("mydb")
    query = "UPDATE peak_user " \
        f"SET admin_level = 1 " \
        f"WHERE email = %(email)s;"
    data = dict(email=target_email)
    mysql.query_db(query, data)

    flash(f"lowered {target_email}'s admin level")

    return redirect(url_for("user"))


if __name__ == '__main__':
    app.run(debug=True)
