import requests, json
API_KEY = "AIzaSyBTUP5PZWwTFM6PP2ok5pAKYdBOW6pFARw"

def latLong(address):
    """ Finds the lattitude and longitude from address"""
    baseURL = "https://maps.googleapis.com/maps/api/geocode/json"
    formattedAddress = address.replace(" ","+")
    payload = {"key":API_KEY,"address":formattedAddress}
    r = requests.post(baseURL,params=payload)

    location = r.json()["results"][0]["geometry"]["location"]
    
    return (location["lat"],location["lng"])

loc = latLong("7030 Preinkert Dr, College Park, MD 20742")
print(loc)
