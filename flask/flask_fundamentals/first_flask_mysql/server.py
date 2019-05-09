from flask import Flask, redirect, render_template, request

from mysqlconnection import connectToMySQL  # import the function that will return an instance of a connection

app = Flask(__name__)


@app.route("/")
def index():
    mysql = connectToMySQL('mydb')  # call the function, passing in the name of our db
    pets = mysql.query_db('SELECT * FROM pets;')  # call the query_db function, pass in the query as a string

    return render_template("index.html", pets=pets)


@app.route("/add_pet", methods=["POST"])
def add_pet():
    print("post hit")
    name = request.form['name']
    pet_type = request.form['type']

    mysql = connectToMySQL('mydb')  # call the function, passing in the name of our db
    query = "INSERT into pets(name, type) VALUE (%(name)s, %(type)s);"
    data = dict(name=name, type=pet_type)
    row_id = mysql.query_db(query, data)

    print("row_id: ", row_id)

    return redirect("/")


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
