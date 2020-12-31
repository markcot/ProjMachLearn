# Assessment Project

**Author:** Mark Cotter
**Email:**  g00376335@gmit.ie

This is my README file for the GMIT module Machine Learning and Statistics.

***

This project has been implemented in a Jupyter Notebook [1] using the Python programming language [1]. Jupyter Notebook comes as part of the part the Anaconda [3] distribution of Python. Jupyter software is also available from the Jupyter website [1].

The Jupyer Notebook containing the assessment is called **"Project.ipynb"** and is included in this GitHub [4] repository. A local copy of this reposition can be downloaded to your PC noting the requirement of the license of use included in the repository.

Having the required Jupyter software [1] installed on your PC, you can open the Jupyter Notebook from a command line or Terminal in the folder/directory where the local copy of the repository is stored. The command to open the notebook is **jupyter notebook**. With Jupyter Notebook open in your browser clicking on the file **"Tasks.ipynb"** will open the notebook in another tab.

When opening the **"Project.ipynb"** file, it is a good idea to use the command **"Restart & Run All"** from **"Kernel"** menu to refresh all the notebook cells, code and displays. Further guidance is available from the Jupyter website [1].

***

This project involved estimating power output of wind turbine based on a machine learning model built from a wind "wind speed" versus "power output" dataset called **"powerproduction.txt"** included in this repository.

A Keras [5] model for estimating the power output curve is created and trained in the **"Project.ipynb"** file based on the **"powerproduction.txt"** input data. This model is saved to **"my_model.JSON"** and **"my_model.H5"** files.

The Keras model is loaded into a python Flask web server application called **"web-service.py"** for use with the static html page **"Index.html"**.

***

### Virtual environment
Conda was used to create a localhost Virtual Environment (venvMLP) for running the server. The following Windows command line python commands can be to create venvMLP, install and save packages for venvMLP, set the flask_app server and server mode, run the server, stop the server and finally deactivate venvMLP.

* λ conda create --name venvMLP python=3.8
* λ conda activate venvMLP
* (venvMLP)λ pip install flask
* (venvMLP)λ pip install tensorflow
* (venvMLP)λ pip install silence-tensorflow
* (venvMLP)λ pip install numpy==1.19.2
* (venvMLP)λ pip freeze > requirements.txt
* (venvMLP)λ set FLASK_APP=web-server.py
* (venvMLP)λ set FLASK_ENV=development
* (venvMLP)λ python -m flask run
* Running on http://127.0.0.1:5000/
* Crtl+c
* (venvMLP)λ conda deactivate

The package requirements can also be install from the list in the file **"requirements.txt"** using the venv command
* (venv)λ pip install -r requirements.txt

### How to run the web service
Code adapted from https://flask.palletsprojects.com/en/1.1.x/quickstart/

#### In Linux environment
```bash
export FLASK_APP=web-service.py
export FLASK_ENV=development
python3 -m flask run
 * Running on http://127.0.0.1:5000/
```

#### In Windows environment
```bash
set FLASK_APP=web-service.py
set FLASK_ENV=development
python -m flask run
 * Running on http://127.0.0.1:5000/
```

#### In Docker environment
```bash
docker build . -t web-service-image
docker run --name web-service-container -d -p 5000:5000 web-service-image
 * Running on http://127.0.0.1:5000/
```

***

### References

[1] Jupyter; Project Jupyter; https://jupyter.org/

[2] Python;  Python Software Foundation; https://www.python.org/

[3] Anaconda; Anaconda Inc.; https://www.anaconda.com/

[4] GitHub; GitHub Inc.; https://github.com/

[5] Keras; https://keras.io/
