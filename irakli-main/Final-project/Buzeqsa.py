from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    anime_titles = ['1', '2', '3', '4', '5', '6', '7', '8',
                    '9', '10']
    return render_template('home.html', anime_titles=anime_titles)


@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/anime/<anime_id>")
def anime(anime_id):
    return render_template(f"anime_{anime_id}.html")


if __name__ == "__main__":
    app.run(debug=True)
