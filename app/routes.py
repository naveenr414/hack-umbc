from app import app
from flask import render_template, redirect, url_for, request,session, request, jsonify
from .forms import AddressForm
from . import apiscraper
from app.mongoscraper import find
import json
from bson.json_util import dumps

""" This file says how to render each page """

@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def index():
    form = AddressForm()

    return render_template("index.html",title="Home",form=form)

@app.route('/address',methods=['GET', 'POST'])
def address():
    args = request.args
    forms = request.form
    address = ""
    if("address" in args):
        address = args["address"]
    elif("address" in forms):
        address = forms["address"]
    elif("lat" in forms and "lon" in forms):
        address = apiscraper.reverseGeocode(forms["lat"],forms["lon"])
    elif("lat" in args and "lon" in args):
        address = apiscraper.reverseGeocode(forms["lat"],forms["lon"])
    state, district = apiscraper.findGeo(address)
    races = {}
    races["house"] = []
    races["senate"] = []
    races["governor"] = []

    for x in find.query(state, district)[0]:
        races["house"].append(dict(x))

    for x in find.query(state, district)[1]:
        races["senate"].append(dict(x))

    for x in find.query(state, district)[2]:
        races["governor"].append(dict(x))

    return dumps(dict(races))
