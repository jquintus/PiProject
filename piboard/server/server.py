from flask import Flask
from sound import Sound

"""
Flask webservice that conrols the volume on a windows computer.

Uses https://github.com/Paradoxis/Windows-Sound-Manager for the sound management

To run:
    python server.py
"""

app = Flask(__name__)


@app.route("/up")
def up():
    Sound.volume_up()
    current = str(Sound.current_volume())
    return current


@app.route("/down")
def down():
    Sound.volume_down()
    current = str(Sound.current_volume())
    return current


@app.route("/mute")
def mute():
    Sound.mute()
    current = str(Sound.current_volume())
    return current


if __name__ == "__main__":
    app.run()
