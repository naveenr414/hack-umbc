import pymongo

myclient = pymongo.MongoClient()
mydb = myclient["mydb"]
hor = mydb["HoR"]
sen = mydb["Senator"]
gov = mydb["Governor"]

def query(level,state):
    if(level == "HOR"):
        return hor.find(state);
    elif(level == "SEN"):
        return sen.find(state);
    else:
        return gov.find(state);
