from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/up")
def up():
    return "up"

@app.route("/down")
def down():
    return "down"

@app.route("/mute")
def mute():
    return "mute"

if __name__ == "__main__":
    app.run()
