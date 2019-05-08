from flask import Flask, render_template, request  # added request

app = Flask(__name__, template_folder='.')


# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("material.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)


if __name__ == "__main__":
    app.run(debug=True)
