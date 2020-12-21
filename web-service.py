# Import python modules for use in web service
import flask as fl
from flask import Flask
import numpy as np
import tensorflow.keras as kr

# import Keras model from saved folder "my_model". Code adapted from
# https://www.tensorflow.org/guide/keras/save_and_serialize
model = kr.models.load_model("my_model")

# Copy of variables and function from Project.ipynb
# Set normalisation factors
wsF = 25
poF = 120
# Function to predict power output based on inputted wind speeds
def power_output(windspeeds):
   """ Function to predict power output based on inputted wind speeds
      Acceptable inputs include numbers or a list of numbers
   """
   # Set the cut off wind speeds
   minWS, maxWS = 3, 24.5
      
   # If input is a list with a number as the first element
   if type(windspeeds) == list:
      #print("List")
      # Result list
      res = []
      # For each item in the list
      for i in range(len(windspeeds)):
         #print(windspeeds[i])
         # Check if each item in the list is a number
         if type(windspeeds[i]) == str:
               #print("Error")
               return [-1] * len(windspeeds)
         # If wind speed is inside the cut off levels
         if windspeeds[i] > minWS and windspeeds[i] < maxWS:
               # Set resultant power output to 0
               ws = np.array([windspeeds[i]])
               po = round(model.predict(ws/wsF)[0][0]*poF, 3)
               res.append(po)
         else:
               # Otherwise set value to zero
               res.append(0)
      return res
   
   # If input is a single number
   elif type(windspeeds) == float or type(windspeeds) == int:
      #print("Float/Int")
      # If wind speed is inside the cut off levels
      if windspeeds > minWS and windspeeds < maxWS:
         ws = np.array([windspeeds])
         return round(model.predict(ws/wsF)[0][0]*poF, 3)
      else:
         # Otherwise set value to zero
         return 0
      
   else:
      #print("Error")
      return -1

# Function test
# print(power_output(10))

# Flask app. Cade adapted from
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
app = Flask(__name__)

# Add root route.
@app.route('/')
def home():
   return app.send_static_file('index.html')

# Add number route.
@app.route('/api/number/<float:speed>')
def uniform():
   return {"value": power_output(speed)}

# Add list route.
@app.route('/api/list/<list:speeds>')
def normal():
   return {"value": power_output(speeds)}
