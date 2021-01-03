# Import python modules for use in web service
from flask import Flask
import numpy as np
# Silence tensorflowstartup warnings. Code adapted from
# https://stackoverflow.com/a/65215118
from silence_tensorflow import silence_tensorflow
silence_tensorflow()
import tensorflow.keras as kr

# Load Keras model from saved files "my_model.h5". Code adapted from
# https://www.christopherlovell.co.uk/blog/2016/04/27/h5py-intro.html
model = kr.models.load_model("my_model.h5")
# print("Loaded model from disk")

# Function to predict power output based on inputted wind speeds
# Variant of function from Project.ipynb
def power_output(windspeed):
   """ Function to predict power output based on inputted wind speed
      Acceptable input is a single number
   """
   # Set the cut off wind speeds
   minWS, maxWS = 3, 24.5
   # Set normalisation factors
   wsF, poF = 25, 120
   # If wind speed is in allowable range for cut in/off
   if windspeed > minWS and windspeed < maxWS:
      ws = np.array([windspeed])
      # Estimate power output
      return round(model.predict(ws/wsF)[0][0]*poF, 3)
   else:
      # Otherwise set power output to zero
      return 0

# Function test. Also initialise the function.
test = power_output(10)
# print(f"Wind speed: 10 gives power: {test}")

# ws_arr_test = [1, 3, 3.001, 5, 10, 20, 24, 24.499, 24.5, 27]
# for i in ws_arr_test:
#    print(f"Wind speed: {i} gives power: {power_output(i)}")

# Flask app. Code adapted from
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application and
# GMIT Data Represtation lectures
app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Add root route.
@app.route('/')
def index():
   # return "hello"
   return app.send_static_file('index.html')

# Add power route.
# curl http://127.0.0.1:5000/api/power/5
@app.route('/api/power/<speed>')
def power(speed):
   s = float(speed)
   # get power from power curve model
   return {"power" : power_output(s)}

# Run in debug mode
if __name__ == "__main__":
   app.run(debug=True)