from app import app
from flask import render_template, redirect, url_for, request,session, request, jsonify
from . import apiscraper
from app.mongoscraper import find
import json
from bson.json_util import dumps

""" This file says how to render each page """

@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def index():
    return render_template("index.html",title="Home")

@app.route('/address',methods=['GET', 'POST'])
def address():
    args = request.args
    forms = request.form
    address = ""
    lat = 0
    lon = 0
    if("address" in args):
        address = args["address"]
    elif("address" in forms):
        address = forms["address"]
    elif("lat" in forms and "lon" in forms):
        lat = float(forms["lat"])
        lon = float(forms["lon"])
    elif("lat" in args and "lon" in args):
        lat = float(args["lat"])
        lon = float(args["lon"])
    state = ""
    district = ""
    
    if(address!=""):
        state, district = apiscraper.findGeo(address)
    else:
        print("Finding latlong",lat,)
        state, district = apiscraper.findGeoLat(lat,lon)
    
    print("STATE",state,district)

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

    races["state"] = state
    races["district"] = district

    print(races)

    return dumps(dict(races))
