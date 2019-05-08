from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__, template_folder=".")  # Create a new instance of the Flask class called "app"


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


def get_color(row, column):
    print("get_color")
    if (row + column) % 2 == 0:
        return "black"
    else:
        return "red"


@app.route("/checkers")
def checkers():
    print("checkers")
    return render_template("checkers.html", get_color=get_color)


if __name__ == "__main__":  # Ensure this file is being run directly and not from a different module
    app.run(debug=True)  # Run the app in debug mode.
