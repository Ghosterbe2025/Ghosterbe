
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/admin-login")
def admin_login():
    return render_template("admin_login.html")

@app.route("/agb.html")
def agb():
    return render_template("agb.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
