from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__, template_folder=".")  # Create a new instance of the Flask class called "app"


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route('/')  # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')
def dojo():
    print("dojo")
    return "Dojo!"


@app.route('/say/<s>')
def say(s):
    if not isinstance(s, str):
        return "not a string"
    return 'hi' + str(s)


@app.route('/repeat/<n>/<s>')
def repeat(n, s):
    if not n.isdigit():
        return "n wasn't an integer"
    if not isinstance(s, str):
        return "s wasn't a string"

    print(s)
    print(s * int(n))
    return str((s + ' ') * int(n))


@app.route("/play")
def play():
    return render_template("play.html", n=3, color="blue")


@app.route("/play/<n>")
def play_2(n):
    return render_template("play.html", n=int(n), color="blue")


@app.route("/play/<n>/<color>")
def play_3(n, color):
    return render_template("play.html", n=int(n), color=color)


def get_color(row, column):
    if (row + column) % 2 == 0:
        return "black"
    else:
        return "red"


@app.route("/checkers")
def checkers():
    return render_template("checkers.html", get_color=get_color)

if __name__ == "__main__":  # Ensure this file is being run directly and not from a different module
    app.run(debug=True)  # Run the app in debug mode.
