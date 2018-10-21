from app import app
from flask import render_template, redirect, url_for, request,session, request
from .forms import AddressForm
from . import apiscraper
from mongoscraper import find

""" This file says how to render each page """

@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def index():
    form = AddressForm()

    return render_template("index.html",title="Home",form=form)

@app.route('/address',methods=['GET', 'POST'])
def address():
    args = request.args
    state, district = findState(args["address"]), findDistrict(address)
    return find.query(state,district)
