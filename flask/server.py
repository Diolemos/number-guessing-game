from flask import Flask, render_template
import random

secret_number = random.randint(1,10)

app = Flask(__name__)

@app.route("/")
def view_home():
    return render_template("index.html")


@app.route('/<string:user_guess>')
def guessing_game(user_guess):

    
    if int(user_guess) < 1 or int(user_guess) > 10:
        return render_template('out_of_bounds.html')
           
    
    if int(user_guess) < secret_number:
        return render_template("too_low.html")
    elif int(user_guess) > secret_number:
        return render_template("too_high.html")
    else:
        return render_template('right_guess.html')
print(f"***pssss*** the secret number is {secret_number}")

if __name__ == "__main__":
    app.run(debug=True)