from mongoscraper import populate
from bs4 import BeautifulSoup
import urllib.request as ur
import json

partyOneLetter = {"D":"Democrat","R":"Republican","I":"Independent"}

def getData():
    jsonList = []
    
    electionWebsite = "https://www.electoral-vote.com/evp2018/Senate/senate_races.html"
    electionSoup = BeautifulSoup(ur.urlopen(electionWebsite),"html.parser")

    states = list(map(lambda x: x.text.strip(),electionSoup.findAll("h2")))
    states = list(map(lambda x: x.split("-")[0],states))

    print(states.diff(list(set(states))))

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

            candidateList.append(candidateJson)                    

        tempJson["candidates"] = candidateList
        populate.write(candidateList)
        
        allJsons.append(tempJson)
            
        
    return allJsons


c = getData()
