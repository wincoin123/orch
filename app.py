from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    time.sleep(10)

    return render_template("index.html")

if __name__ == '__main__':
    app.run()
