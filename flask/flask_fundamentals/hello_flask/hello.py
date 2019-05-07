from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)  # Create a new instance of the Flask class called "app"


@app.route('/')  # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')
def dojo():
    print("dojo")
    return "Dojo!"


@app.route('/say/<s>')
def say(s):
    return str(s)


@app.route('/repeat/<n>/<s>')
def repeat(n, s):
    print(n)
    print(s)
    print(s * int(n))
    return str((s + ' ') * int(n))


if __name__ == "__main__":  # Ensure this file is being run directly and not from a different module
    app.run(debug=True)  # Run the app in debug mode.
