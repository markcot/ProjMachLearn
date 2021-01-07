# Assessment Project

**Author:** Mark Cotter
**Email:**  g00376335@gmit.ie

## Introduction

This is the project assessment README file for the GMIT module Machine Learning and Statistics.

## Project Description and Setup

In this GitHub [1] repository, a base dataset **"powerproduction.txt"** has been provided for the project. A Jupyter [2] notebook **"Project.ipynb"** has been used to review and fit a model to this dataset using the Python programming language [3]. Jupyter comes as part of the part the Anaconda [4] distribution of Python and is also available from the Jupyter website [2]. A local copy of this reposition can be downloaded to your PC noting the project license of use included in the repository.

Having the required Jupyter and Python software installed on your PC, you can open the Jupyter notebook from a command line or Terminal starting in the folder/directory where the local copy of the repository is stored. The command to open the notebook is **jupyter notebook**. With the Jupyter Notebook open in your browser clicking on the file **"Project.ipynb"** will open the notebook in another browser tab. After opening the notebook file, it is good practice to use the command **"Restart & Run All"** from the **"Kernel"** menu to refresh all the notebook cells, code and displays. Further guidance is available from the Jupyter website [2].

## Data Modelling

Known value pairs of "wind speed" and associated "power output" are listed in the dataset. To estimate power output of the wind turbine based on an inputted wind speed, a Keras [5] machine learning model has been trained in the **"Project.ipynb"** file to approximate the wind turbine power output curve. The structure and state of this trained model is saved to the **"my_model.h5"** file included in the repository.

The Keras model is loaded into a python Flask web server application called **"web-service.py"** for use with the html user interface html page **"Index.html"**.

## Local Virtual Environment
Anaconda Python (conda) was used on a Windows machine to create a localhost Virtual Environment (venvMLP) for running the server locally. The following Windows command line pip and python commands can be used to create venvMLP, install and save packages for venvMLP, set the flask_app server and server mode, run the server, stop the server and finally deactivate venvMLP. Testing of the flask server showed that there appears to be a conflict with the current version of tensorflow version 2.4.0 and the FLASK_APP. As such tensorflow had to be downgraded to version 2.3.0 including its associated Python packages including numpy.

```bash
λ conda create --name venvMLP python=3.8
λ conda activate venvMLP
(venvMLP)λ pip install flask==1.1.2
(venvMLP)λ pip install tensorflow==2.3.0
(venvMLP)λ pip install silence-tensorflow==1.1.1
(venvMLP)λ pip install scipy==1.4.1
(venvMLP)λ pip freeze > requirements.txt
(venvMLP)λ set FLASK_APP=web-server.py
(venvMLP)λ set FLASK_ENV=development
(venvMLP)λ flask run
 * Running on http://127.0.0.1:5000/

 * Press: Crtl+c

(venvMLP)λ conda deactivate
```

The package requirements can also be installed from the list included in the file **"requirements.txt"** within the virtual environment using the following pip command

```bash
(venv)λ pip install -r requirements.txt
```

## How to run the web service
Code adapted from https://flask.palletsprojects.com/en/1.1.x/quickstart/ & https://stackoverflow.com/a/57400523. Setting the virtual environment to development allows lazy loading that automatically restarts the web server if changes are made to the code used for the web service.

### In a Windows virtual environment

```bash
set FLASK_APP=web-service.py
set FLASK_ENV=development
flask run
 * Running on http://127.0.0.1:5000/
```

### In a Linux virtual environment

```bash
export FLASK_APP=web-service.py
export FLASK_ENV=development
flask run
 * Running on http://127.0.0.1:5000/
```

### Creating and running in a Docker container environment (linux base)
NOTE that to construct the docker linux virtual machine image, the time taken to download update and install the base image and requirements can take up to approximately two hours on the first run. After the initial docker layers are built, the docker image can be reconstructed more quickly if only the later image layers are changed.
When the container set to run and while the Keras model is being initialised, the server may required five or six minutes of waiting time before the web service user interface html page is ready to serve. Afterward this initial wait, the web-service operates normally.

```bash
docker build . -t web-service-image
docker run --name web-service-container -d -p 5000:5000 web-service-image
 * Running on http://127.0.0.1:5000/
```

## References

[1] GitHub; GitHub Inc.; https://github.com/

[2] Jupyter; Project Jupyter; https://jupyter.org/

[3] Python;  Python Software Foundation; https://www.python.org/

[4] Anaconda; Anaconda Inc.; https://www.anaconda.com/

[5] Keras; https://keras.io/