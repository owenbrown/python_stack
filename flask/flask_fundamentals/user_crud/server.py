from flask import Flask, redirect, render_template, request, url_for

from mysqlconnection import connectToMySQL  # import the function that will return an instance of a connection

app = Flask(__name__)


@app.route("/users")
def view_users():
    mysql = connectToMySQL('mydb')
    users = mysql.query_db('SELECT * FROM ninjauser;')

    return render_template("all_users.html", users=users)


@app.route("/users/new")
def new_user():
    return render_template("add_user.html")


@app.route("/users/new", methods=["POST"])
def new_user_post():
    mysql = connectToMySQL('mydb')
    query = "INSERT into ninjauser(first_name, last_name, email) " \
            "VALUE " \
            "(%(first_name)s, %(last_name)s, %(email)s);"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    user_id = mysql.query_db(query, data)
    return redirect(f"/users/{user_id}")


@app.route("/users/<user_id>")
def view_user(user_id):
    mysql = connectToMySQL('mydb')
    query = "SELECT first_name, last_name, email, user_id, created_ts, updated_ts " \
            "FROM ninjauser " \
            "WHERE user_id = %(user_id)s;"
    data = dict(user_id=user_id)
    users = mysql.query_db(query, data)
    if not users:
        return "sorry, this user is missing"
    else:
        user = users[0]

    return render_template("view_user.html", user=user)


@app.route("/users/<user_id>/update")
def edit_user(user_id):
    mysql = connectToMySQL('mydb')
    query = "SELECT first_name, last_name, email, user_id " \
            "FROM ninjauser " \
            "WHERE user_id = %(user_id)s;"
    data = dict(user_id=user_id)
    users = mysql.query_db(query, data)
    if not users:
        return "sorry muchaso, this user is missing"
    else:
        user = users[0]

    return render_template("edit_user.html", user=user)


@app.route("/users/<user_id>/update", methods=["POST"])
def edit_user_post(user_id):
    mysql = connectToMySQL('mydb')
    query = "UPDATE ninjauser " \
            "SET first_name = %(first_name)s" \
            ", last_name = %(last_name)s" \
            ", email = %(email)" \
            "WHERE user_id = %(user_id);"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "user_id": user_id
    }
    mysql.query_db(query=query, data=data)
    return redirect(url_for("view_user", user_id=user_id))


@app.route("/users/<user_id>/delete", methods=["GET"])
def delete_user_get(user_id):
    print("delete user get")
    return __delete_user(user_id)


@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    print("delete user delete")
    return __delete_user(user_id)


def __delete_user(user_id):
    mysql = connectToMySQL('mydb')
    query = "DELETE from ninjauser " \
            "WHERE user_id = %(user_id)s;"
    data = dict(user_id=int(user_id))
    mysql.query_db(query, data)
    return redirect("/users")


@app.route("/jack/<user_id>")
def jack():
    return "jack"


if __name__ == "__main__":
    app.run(debug=True)
    mysql = connectToMySQL('mydb')  # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(friends)

    # query = "UPDATE friends SET name=%(new_name)s WHERE name=%(old_name)s;"
    # data = {
    #     "new_name": "doofus",
    #     "old_name": "Ringo"
    # }

    # find_ring = mysql.query_db(query, data)
    # joke = mysql.query_db(query, data)
    # print(joke)
