from flask import Flask, render_template
import random

secret_number = random.randint(1,10)
print(f"pssss, the secret number is {secret_number}")
app = Flask(__name__)

@app.route("/")
def view_home():
    return render_template("index.html")


@app.route('/<string:user_guess>')
def guessing_game(user_guess):

    
    if int(user_guess) < 1 or int(user_guess) > 10:
        return "<h1>out of bounds, page not Found </h1>"
           
    
    if int(user_guess) < secret_number:
        return render_template("too_low.html")
    elif int(user_guess) > secret_number:
        return render_template("too_high.html")
    else:
        return render_template('right_guess.html')


if __name__ == "__main__":
    app.run(debug=True)