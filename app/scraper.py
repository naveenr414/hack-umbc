from bs4 import BeautifulSoup
import urllib.request as ur
import json

partyOneLetter = {"D":"Democrat","R":"Republican","I":"Independent"}
writeMongo = False
if(writeMongo):
    from mongoscraper import populate

def getData():
    jsonList = []
    
    electionWebsite = "https://www.electoral-vote.com/evp2018/Senate/senate_races.html"
    electionSoup = BeautifulSoup(ur.urlopen(electionWebsite),"html.parser")

    states = list(map(lambda x: x.text.strip(),electionSoup.findAll("h2")))
    states = list(map(lambda x: x.split("-")[0],states))

    allJsons = []
    races = electionSoup.findAll("table",{"summary":"candidate"})
    for raceNum,race in enumerate(races):
        tempJson = {}

        state = states[raceNum]
        tempJson["scope"] = "senate"
        tempJson["state"] = state

        
        candidates = race.findAll("td",{"class":"senator"})
        candidateList = []
        for candidateNumber,candidate in enumerate(candidates):
            candidateJson = {}
            name = candidate.find("img")['alt']
            candidateJson["name"] = name
            candidateJson["state"] = state

            if(candidateNumber == 0):
                candidateJson["status"] = "incumbent"
            else:
                candidateJson["status"] = "challenger"

            party = ""
            for link in candidate.findAll("a"):
                t = link.text.strip()
                if(len(t)==3 and t[0]=="(" and t[2]==")"):
                    party = partyOneLetter[t[1]]
                    candidateJson["party"] = party


            infoLink = "http://www.ontheissues.org/Senate/"
            infoLink+=name.replace(" ","_")+".htm"

            works = True
            
            try:
                ur.urlopen(infoLink)
            except:
                works = False

            fields = range(1,21)
            fields = list(map(lambda x: "position_"+str(x),fields))

            for field in fields:
                candidateJson[field] = "Unknown"

            if(works):
                candidateSoup = BeautifulSoup(ur.urlopen(infoLink),"html.parser")
                tableList = candidateSoup.findAll("tr")

                for row in tableList:
                    if(row.find("a")!=None and row.find("a").has_attr("name") and row.find("a")["name"][0]=="q"):
                        num = row.find("b").find("a")["name"][1:]      
                        stance = row.find("b").text.strip()+" the idea that "+row.findAll("a")[1].text
                        candidateJson["position_"+num] = stance
        
            candidateList.append(candidateJson)

        tempJson["candidates"] = candidateList

        if(writeMongo):
            populate.write(tempJson)
        
        allJsons.append(tempJson)
            
        
    return allJsons


c = getData()
