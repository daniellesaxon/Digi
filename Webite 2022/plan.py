from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DATABASE = "testxxx.db"


'''@app.route("/")
def home():
    return render_template("home.html")'''

'''
@app.route("/")
def judging():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute("SELECT name, difficulty FROM Skill;")
    results = cur.fetchall()
    return render_template("font.html", results = results)
'''
@app.route('/judge/<name>')
def pizza(name):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM name WHERE id = 1')
    results = cur.fetchone()
    return(f"you said {results}")

@app.route("/")
def judging():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute("SELECT name, difficulty FROM Skill;")
    results = cur.fetchall()
    return(f"you said {results}")
    #return render_template("judge.html")'''



'''
@app.route("/competitiors")
def competitors():
    return render_template("competitors.html")


@app.route("/scores")
def scores():
    return render_template("scores.html")'''


app.run(debug = True)    