from app import app
from flask import render_template, redirect, url_for, request,session
from .forms import AddressForm
from . import apiscraper

""" This file says how to render each page """

@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def index():
    form = AddressForm()

    #If POST data was sent
    if(form.validate_on_submit()):
        session['address'] = request.form['address']
        return redirect(url_for("address")) #Navigate to the address view

    return render_template("index.html",title="Home",form=form)

@app.route('/address',methods=['GET', 'POST'])
def address():
    place = session['address']
    district = scraper.findDistrict(place)
    return render_template("address.html",title="Address",district=district)
