# app.py

from flask import render_template
import connexion
from connexion.resolver import RestyResolver
from flask_cors import CORS

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml" ,resolver=RestyResolver('c64aas'))

CORS(app.app)

@app.route("/")

def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6464)

