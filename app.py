
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/admin-login")
def admin_login():
    return render_template("admin_login.html")

if __name__ == "__main__":
    app.run()
