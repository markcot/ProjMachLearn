# Import python modules for use in web service
import flask as fl
import numpy as np
# Silence tensorflowstartup warnings. Code adapted from
# https://stackoverflow.com/a/65215118
from silence_tensorflow import silence_tensorflow
silence_tensorflow()
import tensorflow.keras as kr

# Flask app. Code adapted from
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application and
# GMIT Data Represtation Project
app = fl.Flask(__name__, static_url_path='', static_folder='staticpages')

# Add root route.
@app.route('/')
def index():
   # return "hello"
   return app.send_static_file('index.html')

# Add number route.
# curl http://127.0.0.1:5000/api/number/5
@app.route('/api/number/<speed>')
def number(speed):
   s = float(speed)
   # get power from power curve model
   return {"power" : power_output(s)}

# # Add list route.
# @app.route('/api/list/<speeds>')
# def number_list():
#    return {"value": power_output(speeds)}

# Load Keras model from saved files "my_model.json" & "my_model.h5". Code adapted from
# https://machinelearningmastery.com/save-load-keras-deep-learning-models/
# load json and create model
json_file = open('my_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = kr.models.model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("my_model.h5")
#print("Loaded model from disk")

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

   # If wind speed is inside the cut off levels
   if windspeeds > minWS and windspeeds < maxWS:
      ws = np.array([windspeeds])
      return round(model.predict(ws/wsF)[0][0]*poF, 3)
   else:
      #print("Error")
      return 0

# Function test
# print(power_output(10))

# Run in debug mode
if __name__ == "__main__":
   app.run(debug=True)