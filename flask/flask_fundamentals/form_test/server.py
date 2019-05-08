from flask import Flask, render_template, request  # added request

app = Flask(__name__, template_folder='static')


# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    location = request.form['Location']
    comment = request.form['comment']
    # return "success posting"
    return render_template(
        "show.html", name=name_from_form, email=email_from_form, location=location, comment=comment )


@app.route('/template')
def template():
    return render_template("backup_template.html")


if __name__ == "__main__":
    app.run(debug=True)
