from flask import Flask,flash, redirect, render_template, request, session, abort
import pymedtermino
from dotenv import load_dotenv
import os
import json
import numpy as np

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
DATA_DIR1 = os.environ.get("DATA_DIR")
LANGUAGE1 = os.environ.get("LANGUAGE")
REMOVE_SUPPRESSED_CONCEPTS1 = os.environ.get("REMOVE_SUPPRESSED_CONCEPTS")
REMOVE_SUPPRESSED_TERMS1 = os.environ.get("REMOVE_SUPPRESSED_TERMS")
REMOVE_SUPPRESSED_RELATIONS1 = os.environ.get("REMOVE_SUPPRESSED_RELATIONS")

pymedtermino.LANGUAGE = LANGUAGE1
pymedtermino.DATA_DIR = DATA_DIR1
pymedtermino.REMOVE_SUPPRESSED_CONCEPTS = REMOVE_SUPPRESSED_CONCEPTS1
pymedtermino.REMOVE_SUPPRESSED_TERMS = REMOVE_SUPPRESSED_TERMS1
pymedtermino.REMOVE_SUPPRESSED_RELATIONS = REMOVE_SUPPRESSED_RELATIONS1

from pymedtermino.all import *
from pymedtermino import *
from pymedtermino.icd10 import *


app = Flask(__name__)

def getmember(name):
    print(name)

    result = ICD10.search(name)
    return json.dump(result)

@app.route("/icdpackage/")
def index():
    name = request.args.get("x")
    ret = getmember(name)

    print(type(ret))
    print(ret)
    s = " * "
    s = s.join(ret)
    print(s)
    print(type(s))
    return "retu"

@app.route("/testtest/")
def strname():
    name = request.args.get("x")
    print(name)
    return name

@app.route("/hello")
def hello():
    return "You are in hello world"

@app.route("/members/<string:name>/")
def getmember(name):
    print(name)
    result = ICD10.search(name)
    return result

@app.route("/icd/<string:name>/",methods=['GET'])
def icd(name):
    return render_template(
    'index.html',name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
