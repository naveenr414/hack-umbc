import pymongo

myclient = pymongo.MongoClient()
mydb = myclient["mydb"]
hor = mydb["HoR"]
sen = mydb["Senator"]
gov = mydb["Governor"]

def write(fileJSON):
    myDoc = fileJSON
    if( "hor" in myDoc.values()):
        hor.insert_one(myDoc)
    elif( "senate" in myDoc.values()):
        sen.insert_one(myDoc)
    else:
        gov.insert_one(myDoc)

def deletes():
    for x in sen.find():
        sen.delete_one(x)

def prints():
    for x in sen.find():
        print(x)

