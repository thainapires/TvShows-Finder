from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html', randn = str(random.randint(101,4000)))

if __name__ == "__main__":
    app.run(debug=True)