from flask import Flask
import random

random_number = random.randint(0, 9)
print(f"hello: {random_number}")
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9<h1>" \
           "<img src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif', alt = 'homegif'>"

@app.route("/<int:value_web>")
def user_value(value_web):

    if value_web == random_number:
        return "<h1>You found me<h1>" \
               "<img src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt = 'equalgif'>"
    elif value_web > random_number:
        return "<h1>Too High<h1>" \
               "<img src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt = 'highgif'>"
    elif value_web < random_number:
        return "<h1>Too Low<h1>" \
               "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt = 'lowgif'>"





if __name__ == "__main__":
    app.run(debug=True)


