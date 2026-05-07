# Problem 1.23, Page 17 — Gale-Shapley
# Label: exr:gale-shapley
# An Introduction to the Analysis of Algorithms (4th Edition)

import sys

class AGirl():
    def __init__(self, girlName, preferences):
        self.name = girlName
        self.preferences = preferences
        self.spouse = None
        self.ranking = {}
        for rank in range(len(preferences)):
            self.ranking[preferences[rank]] = rank

class ABoy():
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.spouse = None
        self.candidatePos = 0
    def GetNextProposal(self):
        nextGirl = self.preferences[self.candidatePos]
        self.candidatePos += 1
        return nextGirl

def LoadSimData(fName):
    peopleSet = []
    with open(fName) as fStream:
        lines = fStream.readlines()
    boys = len(lines) // 2
    j = 0
    k = 0
    for personData in lines:
        name = "b" + str(j + 1)
        if j >= boys:
            name = "g" + str(k + 1)
            k += 1
        if name:
            preferences = personData.strip().split('<')
            for i in range(len(preferences)):
                preferences[i] = preferences[i].strip()
            peopleSet.append((name.strip(), preferences))
        j += 1
    return peopleSet

def runAlgo():
    people = LoadSimData(sys.argv[1])
    boysList = people[0:(len(people) // 2)]
    boys = dict()
    for boy in boysList:
        boys[boy[0]] = ABoy(boy[0], boy[1])
    suitors = sorted(boys.keys())

    girlsList = people[len(people) // 2:]
    girls = dict()
    for girl in girlsList:
        girls[girl[0]] = AGirl(girl[0], girl[1])

    iterations = 1
    while len(suitors) > 0:

        print("Iteration #", iterations)
        boy = boys[suitors[0]]
        girl = girls[boy.GetNextProposal()]

        print(boy.name, 'proposed to', girl.name)

        if girl.spouse is None or (girl.ranking[boy.name] < girl.ranking[girl.spouse]):
            print(' ', girl.name, 'accepts the proposal from', boy.name)

            if girl.spouse:
                boys[girl.spouse].spouse = None
                suitors.append(boys[girl.spouse].name)
                print(girl.name, 'traded up')
            suitors.remove(boy.name)
            girl.spouse = boy.name
            boy.spouse = girl.name
        else:
            print('\t', girl.name, 'does not want to become engaged to',
                  boy.name.strip(), ', she prefers', girl.spouse)
        iterations += 1

        print("Potential Marriages:")
        for b in sorted(boys.keys()):
            print(boys[b].name.strip() + '-' + str(boys[b].spouse).strip())
        print()

    print("'Stable' Marriages after", iterations, "iterations:")
    for b in sorted(boys.keys()):
        print(boys[b].name + '-' + boys[b].spouse)

runAlgo()
