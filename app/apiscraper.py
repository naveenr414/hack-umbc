from app.bs5 import BeautifulSoup
import app.requests, json
import random
import urllib.request as ur
import math

API_KEY = "AIzaSyBTUP5PZWwTFM6PP2ok5pAKYdBOW6pFARw"
initialToState = {'AL': 'Alabama', 'MT': 'Montana', 'AK': 'Alaska', 'NE': 'Nebraska', 'AZ': 'Arizona', 'NV': 'Nevada', 'AR': 'Arkansas', 'NH': 'New Hampshire', 'CA': 'California', 'NJ': 'New Jersey', 'CO': 'Colorado', 'NM': 'New Mexico', 'CT': 'Connecticut', 'NY': 'New York', 'DE': 'Delaware', 'NC': 'North Carolina', 'FL': 'Florida', 'ND': 'North Dakota', 'GA': 'Georgia', 'OH': 'Ohio', 'HI': 'Hawaii', 'OK': 'Oklahoma', 'ID': 'Idaho', 'OR': 'Oregon', 'IL': 'Illinois', 'PA': 'Pennsylvania', 'IN': 'Indiana', 'RI': 'Rhode Island', 'IA': 'Iowa', 'SC': 'South Carolina', 'KS': 'Kansas', 'SD': 'South Dakota', 'KY': 'Kentucky', 'TN': 'Tennessee', 'LA': 'Louisiana', 'TX': 'Texas', 'ME': 'Maine', 'UT': 'Utah', 'MD': 'Maryland', 'VT': 'Vermont', 'MA': 'Massachusetts', 'VA': 'Virginia', 'MI': 'Michigan', 'WA': 'Washington', 'MN': 'Minnesota', 'WV': 'West Virginia', 'MS': 'Mississippi', 'WI': 'Wisconsin', 'MO': 'Missouri', 'WY': 'Wyoming'}

def latLong(address):
    """ Finds the lattitude and longitude from address"""
    baseURL = "https://maps.googleapis.com/maps/api/geocode/json"
    payload = {"key":API_KEY,"address":address}
    r = requests.get(baseURL,params=payload)
        
    location = r.json()["results"][0]["geometry"]["location"]
    
    return (location["lat"],location["lng"])

def findGeo(address):
    return findGeoLat(*latLong(address))

def findGeoLat(lat,long):
    """ Finds the congressional district for a latitude/longitude """

    baseURL = "https://maps.googleapis.com/maps/api/geocode/json"
    payload = {"key":API_KEY,"latlng":str(lat)+","+str(long)}
    r = requests.get(baseURL,params=payload)

    zipcode = r.json()["results"][0]["address_components"]

    for i in zipcode:
        if("long_name" in i and "types" in i and "postal_code" in i["types"]):
            zipcode = i["long_name"]
            break
    
    link = "https://whoismyrepresentative.com/getall_mems.php?zip="+zipcode
    r = BeautifulSoup(ur.urlopen(link),"html.parser")
    print("Zipcode",zipcode)
    r = r.find("rep")
    district = r["district"]
    state = r["state"]
    
    return initialToState[state],district
    

def reverseGeocode(lat,long):
    """ Return an address for a latitude longitude """
    
    baseURL = " https://maps.googleapis.com/maps/api/geocode/json"
    payload = {"key":API_KEY,"latlng":str(lat)+","+str(long),"result_type":"street_address"}
    r = requests.get(baseURL,params = payload)
    try:
        return r.json()["results"][0]["formatted_address"]["long_name"]
    except:
        return ""


