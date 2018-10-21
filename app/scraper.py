from bs4 import BeautifulSoup
import urllib.request as ur
import json

partyOneLetter = {"D":"Democrat","R":"Republican","I":"Independent","L":"Libertarian","G":"Green","N":"Independent"}
writeMongo = True
if(writeMongo):
    from mongoscraper import populate

currentMembers = open("legislators-current.csv").read().split("\n")[1:-1]
for i in range(len(currentMembers)):
    currentMembers[i] =" ".join(currentMembers[i].split(",")[0:2][::-1])

def findCandidateData(candidateName,candidateJson,infoLink = "http://www.ontheissues.org/Senate/"):
    infoLink+=candidateName.strip().replace(" ","_")+".htm"

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
    else:
        if("Jealous" in candidateName):
            print(infoLink)
    return candidateJson

def getData():
    allJsons = []

    #House Data
    r = open("house.txt",encoding="utf-8").read().split("\n")
    i = 0
    while(i<len(r)):
        if(r[i] == "Voting history"):
            location = r[i-3]

            contestants = r[i-2]
            candidateList = []
            if("SOLID" not in contestants):
                tempJson = {}
                tempJson["scope"] = "hor"

                state = location.split(", ")[0]
                district = location.split("District ")[1].split(" ")[0]
                if("large" in district.lower()):
                    district = "1"
                else:
                    district = str(int(district))

                print(contestants.strip().split(")"))

                contestantOne = contestants.split(" (")[0]
                contestantOneParty = partyOneLetter[contestants.split(" (")[1][0]]
                contestantTwo = contestants.split("vs. ")[1].split(" (")[0]
                contestantTwoParty = partyOneLetter[contestants.strip().split(")")[-2][-1]]
                tempJson["state"] = state

                candidateList = []
                candidateOneJson = {}
                candidateOneJson["name"] = contestantOne
                candidateOneJson["party"] = contestantOneParty
                candidateOneJson = findCandidateData(contestantOne,candidateOneJson,infoLink="http://www.ontheissues.org/")
                candidateTwoJson = {}
                candidateTwoJson["name"] = contestantTwo
                candidateTwoJson["party"] = contestantTwoParty
                candidateTwoJson = findCandidateData(contestantTwo,candidateTwoJson,infoLink="http://www.ontheissues.org/")

                if(contestantOne in currentMembers):
                    candidateOneJson["status"] = "incumbent"
                else:
                    candidateOneJson["status"] = "challenger"

                if(contestantTwo in currentMembers):
                    candidateTwoJson["status"] = "incumbent"
                else:
                    candidateTwoJson["status"] = "challenger"

                candidateList = [candidateOneJson,candidateTwoJson]
                tempJson["candidates"] = candidateList




                if(writeMongo):
                    populate.write(tempJson)

                allJsons.append(tempJson)
                
        i+=1
    
    #Governor Data
    governorSoup = BeautifulSoup(ur.urlopen("http://www.governing.com/governor-races-2018"),"html.parser")
    races = governorSoup.findAll("div",{"class":"state"})
    for race in races:
        stateName = race.findAll("h3")[0].text.split("\t")[0].strip()
        currentGovernor = race.findAll("em")[0].text.split(": ")[1].split(", ")[0]

        tempJson = {}
        tempJson["scope"] = "governor"
        tempJson["state"] = stateName

        nominees = race.findAll("div",{"class":"nominee"})
        candidateList = []
        for nominee in nominees:
            candidateJson = {}
            name = str(nominee.findAll("span",{"class":"cand-name"})[0]).split("<br/>")
            tempName = ""
            if("State" not in name[0] and "Rep." not in name[0] and "Gov." not in name[0] and "Mayor" not in name[0] and "School" not in name[0]):
                tempName = name[0].split(">")[1] + " "

            tempName+=name[1]
            tempName = tempName.replace("Rep.","")
            tempName = tempName.replace("County Executive","")
            tempName = tempName.replace("Treasurer","")

            party = nominee.findAll("small")[0].text.capitalize().split(" ")
            if(party[0]!=""):
                party = party[0]
            else:
                party = party[1]
            party = party.capitalize()

            incumbent = currentGovernor == tempName
        
            candidateJson["name"] = tempName
            candidateJson["state"] = stateName
            if(incumbent):
                candidateJson["status"] = "incumbent"
            else:
                candidateJson["status"] = "challenger"
            candidateJson["party"] = party
            candidateJson = findCandidateData(tempName,candidateJson,infoLink="http://www.ontheissues.org/")
            candidateList.append(candidateJson)
        tempJson["candidates"] = candidateList
        if(writeMongo):
            populate.write(tempJson)
        allJsons.append(tempJson)

    # Senator
    
    electionWebsite = "https://www.electoral-vote.com/evp2018/Senate/senate_races.html"
    electionSoup = BeautifulSoup(ur.urlopen(electionWebsite),"html.parser")

    states = list(map(lambda x: x.text.strip(),electionSoup.findAll("h2")))
    states = list(map(lambda x: x.split("-")[0],states))

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
            candidateJson = findCandidateData(name,candidateJson)
            candidateList.append(candidateJson)

        tempJson["candidates"] = candidateList

        if(writeMongo):
            populate.write(tempJson)
        
        allJsons.append(tempJson)


        
    return allJsons


c = getData()

