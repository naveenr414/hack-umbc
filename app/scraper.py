import requests, json
API_KEY = "AIzaSyBTUP5PZWwTFM6PP2ok5pAKYdBOW6pFARw"

def latLong(address):
    """ Finds the lattitude and longitude from address"""
    baseURL = "https://maps.googleapis.com/maps/api/geocode/json"
    payload = {"key":API_KEY,"address":address}
    r = requests.get(baseURL,params=payload)

    location = r.json()["results"][0]["geometry"]["location"]
    
    return (location["lat"],location["lng"])

def findDistrict(address):
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
                return contest["district"]["name"]
    
    return "No District Found"

district = findDistrict("7030 Preinkert Dr, College Park, MD 20742")
print(district)
