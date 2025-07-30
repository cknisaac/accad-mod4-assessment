from flask import Flask
import os
import pytest

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>This is Isaac's web app</p>"

if __name__ == "__main__":
    app.run(port=os.environ.get('PORT', 5000), host="0.0.0.0", debug=True)
