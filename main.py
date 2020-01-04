from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    page = "Home"
    return render_template("home.html", page=page)

@app.route('/about')
def about():
    page = "About"
    return render_template("about.html", page=page)

@app.route('/contact')
def contact():
    page="Contact"
    return render_template("contact.html", page=page)

app.run(debug=True)