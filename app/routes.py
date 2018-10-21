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
    state, district = apiscraper.findGeo(address)
    for x in find.query(state, district)[1]:
        return dumps(dict(x))
