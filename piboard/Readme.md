# PiBoard

This project uses a button and a rotary encoder to control the volume of a a remote computer.  The remote computer _must_ expose a webservice with the following endpoints to allow for the control.

* {url}/up
* {url}/down
* {url}/mute

Future work will be done to convert this into a blue tooth keyboard instead of contorlling over WiFi


## Getting your enevironment set up

To use this project, you'll want to ensure you're in the correct environment and have all the dependencies downloaded:

```bash
source env/bin/activate
pip install -r requirements.txt
```

To update the requirements file:

```bash
pip freeze > requirements.txt
```

## Configuring Script to Run at Startup

```bash
sudo vim /etc/rc.local
```

Add the following before teh `exit 0`

```bash
python3 /home/pi/code/PiProject/piboard/volumeBoard.py &
```
