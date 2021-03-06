from flask import Flask, render_template, request, jsonify
import os
import numpy as np
import yaml
import joblib 
import sys
import requests
import json

webapp_root = "webapp"
params_path = "params.yaml"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir,template_folder=template_dir)

class  NotANumber(Exception):
    def __init__(self, message="Values entered are not Numerical"):
        self.message = message
        super().__init__(self.message)

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_dir_path = config["model_webapp_dir"]
    model = joblib.load(model_dir_path)
    list_predict = model.predict(data).tolist()
    prediction = list_predict[0]
    print('PREDICTION:{}'.format(str(list_predict)), file=sys.stderr)
    return prediction 

def predict_api(data):
    config = read_params(params_path)
    api_url = config["api_webapp_url"]
    data_params = ",".join(str(e) for e in data[0])
    api_url = str(api_url).format(data_params)
    r = requests.get(api_url)
    try:
        prediction = json.loads(r.text)
        prediction= prediction["data"]
    except Exception as e:
        print(e)
    print("LLAMADA DESDE EL API")
    print('PREDICTION:{}'.format(prediction), file=sys.stderr)
    return prediction 

def validate_input(dict_request):
    for _, val in dict_request.items():
        try:
            val=int(val)
        except Exception as e:
            raise NotANumber
    return True

def form_response(dict_request):
    try:
        if validate_input(dict_request):
            data = dict_request.values()
            data = [list(map(int, data))]
            print('DATA:{}'.format(str(data)), file=sys.stderr)
            #response = predict(data)
            response = predict_api(data)
            print('RESPONSE 2:{}'.format(response), file=sys.stderr)
            return response
    except NotANumber as e:
        response =  str(e)
        return response 

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                dict_req = dict(request.form)
                response = form_response(dict_req)
                print('RESPONSE:{}'.format(response), file=sys.stderr)
                return render_template("index.html", response=response)
        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!! Try again later!"}
            error = {"error": e}
            return render_template("404.html", error=error)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    #app.run_server(debug=True)