import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import gettemp #import fuction for reading temperature

#ids of ds18b20 sensors:
id_inside = '28-000001cbe681'
id_outside = '10-000800ba9da0'

app = Flask(__name__)

# Create a dictionary called pins to store the pin number, name, and pin state:

pins = {
11: {'name':'heater_1_of_3', 'state': GPIO.LOW}
       }

GPIO.setmode(GPIO.BOARD) #use PCB numberig
GPIO.setwarnings(False) #turn of warnings about port usage

for pin in pins:
    GPIO.setup(pin, GPIO.OUT) #set pin on borad as output
    GPIO.output(pin, GPIO.LOW) # set pin in low state

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   gettemp.gettemp(id_inside)
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins, 
      'message1': 'Temp inside: ' + str(gettemp.gettemp(id_inside)) + ' ' + u'\xb0'+'C',
      'message2': 'Temp outside: ' + str(gettemp.gettemp(id_outside)) + ' ' + u'\xb0'+'C'
                  }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)
 

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."
   if action == "toggle":
      # Read the pin and set it to whatever it isn't (that is, toggle it):
      GPIO.output(changePin, not GPIO.input(changePin))
      message = "Toggled " + deviceName + "."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'message' : message,
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
