
import requests, json
import random
import math

API_KEY = "AIzaSyBTUP5PZWwTFM6PP2ok5pAKYdBOW6pFARw"

def latLong(address):
    """ Finds the lattitude and longitude from address"""
    baseURL = "https://maps.googleapis.com/maps/api/geocode/json"
    payload = {"key":API_KEY,"address":address}
    r = requests.get(baseURL,params=payload)

    location = r.json()["results"][0]["geometry"]["location"]
    
    return (location["lat"],location["lng"])

def findGeo(address):
    """ Finds the congressional district for an address """
    baseURL = "https://www.googleapis.com/civicinfo/v2/voterinfo"
    payload = {"key":API_KEY,"address":address}
    r = requests.get(baseURL,params = payload)
    
    contests = r.json()["contests"]

    #Find which district it's in
    for contest in contests:
        houseElection = "office" in contest and contest["office"] == "U.S. Representative"
        if(houseElection):
            if("district" in contest and "name" in contest["district"]):
                info = contest["district"]["name"]
                state = info.split("'")[0]
                districtName = info.split(" ")[1][:-2]

                return state, districtName
    
    return "No District Found"

def findGeoLat(lat,long):
    """ Finds the congressional district for a latitude/longitude """

    works = False
    delta=.001
    n = 0

    while(not works):
        addy = reverseGeocode(lat,long)
        answer = ""
        try:
            answer = findGeo(addy)
        except:
            pass
        if(answer != "" and addy!=""):
            return answer
        lat+=delta*random.randint(1,1)
        long+=delta*random.randint(1,1)

        delta*=math.e**(n/10)
        n+=1
    

def reverseGeocode(lat,long):
    """ Return an address for a latitude longitude """
    
    baseURL = " https://maps.googleapis.com/maps/api/geocode/json"
    payload = {"key":API_KEY,"latlng":str(lat)+","+str(long),"result_type":"street_address"}
    r = requests.get(baseURL,params = payload)
    try:
        return r.json()["results"][0]["formatted_address"]
    except:
        return ""

district = findGeoLat(*latLong("7030 Preinkert Dr, College Park, MD 20742"))
print(district)
