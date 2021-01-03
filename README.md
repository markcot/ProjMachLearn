# Assessment Project

**Author:** Mark Cotter
**Email:**  g00376335@gmit.ie

## Introduction

This is the project assessment README file for the GMIT module Machine Learning and Statistics.

***

## Project Description

The project dataset **"powerproduction.txt"** is reviewed and modelled in a Jupyter [1] Notebook **"Project.ipynb"** using the Python programming language [2] included in this GitHub [3] repository. Jupyter comes as part of the part the Anaconda [4] distribution of Python and is also available from the Jupyter website [1]. A local copy of this reposition can be downloaded to your PC noting the requirement of the license of use included in the repository.

Having the required Jupyter software installed on your PC, you can open the Jupyter Notebook from a command line or Terminal in the folder/directory where the local copy of the repository is stored. The command to open the notebook is **jupyter notebook**. With Jupyter Notebook open in your browser clicking on the file **"Project.ipynb"** will open the notebook in another browser tab. After opening the **"Project.ipynb"** file, it is a good idea to use the command **"Restart & Run All"** from **"Kernel"** menu to refresh all the notebook cells, code and displays. Further guidance is available from the Jupyter website [1].

***

## Data Modelling

This project involved estimating power output of a wind turbine based a trained model built from the project dataset that includes known values of "wind speed" and associated "power output". A Keras [5] model for estimating the power output curve is created and trained in the **"Project.ipynb"** file based on the project dataset. This model is saved to the **"my_model.h5"** file in this repository.

The Keras model is loaded into a python Flask web server application called **"web-service.py"** for use with the html user interface html page **"Index.html"**.

***

## Local Virtual Environment
Conda was used to create a localhost Virtual Environment (venvMLP) for running the server locally. The following Windows command line python commands can be used to create venvMLP, install and save packages for venvMLP, set the flask_app server and server mode, run the server, stop the server and finally deactivate venvMLP. Testing of the flask server showed that there appears to be a conflict with the current version of tensorflow version 2.4.0 and the FLASK_APP. As such I downgraded tensorflow to version 2.3.0 with its associated packages including numpy.

```bash
λ conda create --name venvMLP python=3.8
λ conda activate venvMLP
(venvMLP)λ pip install flask==1.1.2
(venvMLP)λ pip install tensorflow==2.3.0
(venvMLP)λ pip install silence-tensorflow==1.1.1
(venvMLP)λ pip freeze > requirements.txt
(venvMLP)λ set FLASK_APP=web-server.py
(venvMLP)λ set FLASK_ENV=development
(venvMLP)λ python -m flask run
 * Running on http://127.0.0.1:5000/

 * Press: Crtl+c

(venvMLP)λ conda deactivate
```

The package requirements can also be install from the list in the file **"requirements.txt"** using the venv command

```bash
(venv)λ pip install -r requirements.txt
```

***

## How to run the web service
Code adapted from https://flask.palletsprojects.com/en/1.1.x/quickstart/

### In Windows virtual environment

```bash
set FLASK_APP=web-service.py
set FLASK_ENV=development
python -m flask run
 * Running on http://127.0.0.1:5000/
```

### In Linux virtual environment

```bash
export FLASK_APP=web-service.py
export FLASK_ENV=development
python3 -m flask run
 * Running on http://127.0.0.1:5000/
```

### In Docker environment (linux base)

During the DockerFile testing, it was noted that ubuntu:16.04 and ubuntu:18.04 use python version 2.7. To use python version 3, the base ubuntu:20.04 image had to used. This change also required the Linux base python commands to be changed to python3 and pip3.

```bash
docker build . -t web-service-image
docker run --name web-service-container -d -p 5000:5000 web-service-image
 * Running on http://127.0.0.1:5000/
```

***

## References

[1] Jupyter; Project Jupyter; https://jupyter.org/

[2] Python;  Python Software Foundation; https://www.python.org/

[3] GitHub; GitHub Inc.; https://github.com/

[4] Anaconda; Anaconda Inc.; https://www.anaconda.com/

[5] Keras; https://keras.io/