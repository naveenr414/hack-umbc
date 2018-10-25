import pymongo

myclient = pymongo.MongoClient()
mydb = myclient["mydb"]
hor = mydb["HoR"]
sen = mydb["Senator"]
gov = mydb["Governor"]

def query(state, district):
    x = { "state" : state+"_"+district }
    y = { "state" : state }
    z = [hor.find(x), sen.find(y), gov.find(y)]
    return z

