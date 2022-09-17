from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")
    

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/pizza/<int:id>')
def pizza(id):
    conn = sqlite3.connect('pizza.db')
    cur = conn.cursor
    cur.execute('SELECT * FROM Pizza WHERE id = 1')
    results = cur.fetchone()
    return(f"you said {results}")
    # SELECT * FROM Pizza WHERE id=(id)

@app.route('/judging/<int:id>')
def judging(id):



if __name__ == "__main__":
    app.run(debug = True)
