from flask import Flask, render_template, g, url_for
import sqlite3


DATABASE = "products.db"
app = Flask(__name__)
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


app = Flask(__name__)

@app.route("/")
def recipes():
    return render_template("recipes.html")


@app.route("/orders")
def orders():
    cursor = get_db().cursor()
    sql = ("SELECT * FROM Products")
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("orders.html", results=results)



@app.route("/vegan-chocolate-cake")
def chocolate_cake():
    return render_template("chocolate_cake.html")

@app.route("/vegan-dumplings")
def dumplings():
    return render_template("dumplings.html")

@app.route("/vegan-vanilla-cake")
def vanilla_cake():
    return render_template("vanilla_cake.html")

@app.route("/vegan-sufganiot")
def sufganiot():
    return render_template("sufganiot.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/vegan-red-velvet-cake")
def red_velvet_cake():
    return render_template("red_velvet_cake.html")

@app.route("/vegan-apple-cinnamon-cake")
def apple_cinnamon_cake():
    return render_template("apple_cinnamon_cake.html")


if __name__ == "__main__":
    app.run(debug=True)


