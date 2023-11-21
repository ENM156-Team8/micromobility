from flask import Flask, render_template, request, url_for, send_from_directory
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import *


app = Flask(__name__)  


@app.route('/', methods=['POST', 'GET'])
def index():
    trips: list = ['10', '20', '30', '40', '50', 'test']
    return render_template('index.html', trips=trips)


if __name__ == "__main__":
    app.run(debug=True)