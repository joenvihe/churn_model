churn_model
==============================

End to End Machine learning pipeline with MLOps tools

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
#   c h u r n _ m o d e l 
 
 

# Pasos desarrollados
## Instalar entorno
conda create -n myEnv python=3.7 -y 
conda activate myEnv

## Instalar plantilla cookiecutter
pip install cookiecutter
cookiecutter https://github.com/drivendata/cookiecutter-data-science
cd churn_model

## Subirlo al repositorio git, previamente se creo el repositorio
git init 
git add . 
git commit -m "Adding cookiecutter template"
git remote add origin https://github.com/joenvihe/churn_model.git
git branch -M main
git push -u origin main

## Descargar archivo train de kaggle, guardandolo en la carpeta ./data/external
train.csv

## Instalar dvc, previamente comentar la carpeta ./data/ en el archivo .gitignore de la raiz
pip install dvc 
dvc init 
dvc add ./data/external/train.csv

## instalar de mlflow
pip install mlflow

## Se levanto el servidor en  otro cmd anaconda powershell, pero en la carpeta del proyecto
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 127.0.0.1 -p 5000

## cambie el archivo params.yaml
mlflow config:
  remote_server_uri: http://127.0.0.1:5000

## se instalo algunas librerias aficionales
pip install joblib
pip install scikit-learn

## Se ejecuto el pipeline
dvc repro

## se cambia los parametros en params.yaml

## se crea la carpeta webapp

## se creo el archivo app.py

## se creo la carpeta test

## se instalo pytest
pip install pytest

## se ejecuto el test
pytest -v

## crear una app en heroku
Heroku will be used to deploy the application. Create an account in Heroku if you do not have one. After that follow the steps below to create the app and authorization token for the app.

* Go to https://dashboard.heroku.com/apps
* Click New and create a new app
* Give a name for the app and create it (I named it churnmodelprod)
* In the deployment method section, click Github.
* In the connect to Github section, enter the repo name and search. It will find the repo name for you. Then click connect.
* In the automatic deployed section, tick Wait for CI to pass before deploying and click enable the automatic deploy button.
* Then go to account setting → application → Authorizations → create authorization.
* Then enter the description in the box and click create.
* Copy and save the authorization token for future use (We need this in the next step to create secrets).

# se siguio los pasos anteriores
Se creo un archivo autorizathion.txt que contiene mi clave de autorization heroku
se agrego en el archivo .gitignore de la raiz

# se creo el archivo ci-cd.yaml dentro de la carpeta .github/workflows
Now we need to create two secrets inside GitHub as HEROKU_API_TOKEN and HEROKU_API_NAME to do the deployment.
* Select the repo and click the settings.
* Then click secrets in the left panel.
* Click new repository secrets. Need to create two secrets.
1. name: HEROKU_API_NAME |value: churnmodelprod
2. name: HEROKU_API_TOKEN |value: Authorization token saved in the last step

# se modifico el requeriments.txt

# PUSH a heroku
git add .
git commit -m "something"
git push -u origin main

# se adiciono el monitoreo del modelo
Se guardo el archivo train_new.csv en data/raw
Se guardo el codigo model_monitor.py en src/models
se agrego en requirements EvidentlyAI  (pip install evidently)
