"""
Hiro Nakae's Flask API.
"""

from flask import Flask, render_template
import os.path
from os import path

app = Flask(__name__)

@app.route("/")
def hello(message="200/OK"):
    return render_template('index.html', msg=message)

@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def error_403(e):
    return render_template('403.html'), 403

if __name__ == "__main__":
    app.run(debug=True, 
            host='0.0.0.0', 
            port=5000)
