__author__ = 'God'
# total = 100
#fingerExercise = 10
#problemSets = 40
#midTerm1 = 10
#midTerm2 = 10
#final = 30

#fingerExercisesTotal =
#problemSetTotal =
#midTerm1Total = 98
#midTerm2Total =
#finalTotal =


#   progress is

fExList = [5, 75, 109, 105, 80, 40, 50, 0, 0, 0, 0, 0, 0]
pSetList = [0, 0, 0, 95, 0, 0, 0, 0, 0, 0]
midTermsList = [85, 0]
finalsList = [0]


def fEx(fExList):
    fExTotal = sum([5, 75, 109, 105, 80, 40, 75, 0, 0, 0, 0, 0, 0])
    fExScore = sum(fExList)
    fExAvg = fExTotal * 100.0 / fExScore
    return fExAvg * 1 / 10


def pSets(pSetList):
    pSetTotal = sum([50, 75, 100, 95, 65, 0, 0, 0, 0, 0])
    pSetScore = sum(pSetList)
    pSetAvg = pSetScore * 100.0 / pSetTotal
    return pSetAvg * 4 / 10


def midTerms(midTermsList):
    midTermsTotal = sum([98,98])
    midTermsScore = sum(midTermsList)
    midTermsAvg = midTermsScore * 100.0 / midTermsTotal
    return midTermsAvg * 2 / 10


def finals(finalsList):
    finalsTotal = sum([100])
    finalsScore = sum(finalsList)
    finalsAvg = finalsScore * 100.0 / finalsTotal
    return finalsAvg * 3 / 10


cProgress = [fEx(fExList), pSets(pSetList), midTerms(midTermsList), finals(finalsList)]



#fs = (25)*1.0 / 110 #out of 1100
#ps = (860-225)*4.0 / 86 #out of 860
#mts = (100 - (85*100/98))*1/10.0 + 0

#scoreLost = [mts, ps, fs]
#print pSets(pSetList)
print(sum(cProgress),cProgress)



#assume 75 per. 3 / 10