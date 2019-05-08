from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    chosen = dict()
    fruit_list = ["strawberry", "raspberry", "apple", "blackberry"]
    total_quantity = 0
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    for fruit_name, quantity in request.form.items():
        if fruit_name in fruit_list and int(quantity) != 0:
            chosen[fruit_name] = quantity
            total_quantity += int(quantity)
    print(f"Charging {first_name} {last_name} for {str(total_quantity)} fruits")
    return render_template(
        "checkout.html",
        fruits=chosen,
        first_name=first_name,
        last_name=last_name,
        student_id=student_id
    )


@app.route('/fruits')
def fruits():
    images = ["apple.png", "blackberry.png", "raspberry.png", "strawberry.png"]
    return render_template("fruits.html", images=images)


if __name__ == "__main__":
    app.run(debug=True)
