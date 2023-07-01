from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def view_home():
    return "<h1>Flask guessing game</h1>"


if __name__ == "__main__":
    app.run(debug=True)