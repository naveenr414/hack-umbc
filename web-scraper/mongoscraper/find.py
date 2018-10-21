import pymongo

myclient = pymongo.MongoClient()
mydb = myclient["mydb"]
hor = mydb["HoR"]
sen = mydb["Senator"]
gov = mydb["Governor"]

def query(state, district):
    x = { "state" : state }
    y = { "state" : state + district }
    z = [hor.find(y), sen.find(x), gov.find(x)]
    return z

