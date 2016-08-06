#Data For Nations
#Name, Govt, Region, Income Bracket, Population in millions
from decimal import *
cambodia=["Cambodia", "Monarchy", "Southeast Asia", "low income", 15]
thailand=["Thailand", "Monarchy", "Southeast Asia", "upper middle income", 67]
laos=["Laos", "Communist", "Southeast Asia", "lower middle income", 5]
vietnam = ["Vietnam", "Communist", "Southeast Asia", "lower middle income", 89]
malaysia = ["Malaysia", "Democracy", "Southeast Asia", "upper middle income", 30]
indonesia = ["Indonesia", "Democratic Republic", "Southeast Asia", "lower middle income", 257]
myanmar = ["Myanmar", "Parliamentary Republic", "Southeast Asia", "lower middle income", 54]
singapore = ["Singapore", "Constitutional Republic","Southeast Asia","High income", 5l]
easttimor = ["East Timor", "Democratic Republic", "Southeast Asia", "Lower Middle Income", 1 ]
brunei = ["Brunei", "Monarchy", "Southeast Asia", "High Income", 0.4 ]
philippines = ["The Philippines", "Southeast Asia", "Lower Middle Income", 98]

nationlist = [cambodia, thailand, vietnam, laos, malaysia, myanmar, singapore, indonesia , easttimor, brunei, philippines]
newlist = []


######Adding Nations to List#####

def addnation():
    global nationlist
    global newlist
    for i in range(0, len(nationlist)):
             print nationlist[i][0]
    newlen = input("Enter the number of countries to compare, up to 11, More than one country  ")
    if newlen < 12 and newlen > 1:
        for d in range(0, newlen):
             nationinput = raw_input("Enter the name of a country, case sensitive  ")
             for bindex in range(0, len(nationlist)):
                 if nationlist[bindex][0] == nationinput:
                         newlist.append(nationlist[bindex])
                         d = d + 1
                 else:
                     bindex = bindex + 1
        print newlist
    else:
        print "restarting"
        addnations()
                        
    
######Comparing populations#####


def comparepopulationslist():
    populationslist = []
    for x in range(0,(len(newlist))):
        populationslist.append([newlist[x][0], newlist[x][4]])
    print populationslist
    for index in range(1, len(populationslist)):
        currentpop = populationslist[index][1]
        currentname = populationslist[index][0]
        popposition = index
        while popposition > 0 and populationslist[popposition-1][1]>currentpop:
            populationslist[popposition]=populationslist[popposition-1]
            popposition = popposition - 1
        populationslist[popposition] = [currentname, currentpop]
    print populationslist
    for i in range(0, len(populationslist)-1):
        highcomparison = populationslist[i + 1][1]
        lowcomparison = populationslist[i][1]
        getcontext().prec = 3
        ratio = Decimal(Decimal(highcomparison)/Decimal(lowcomparison))
        print "the population of ", populationslist[i+1][0], "is approximately ", ratio, "times the population of ", populationslist[i][0]
        
def againprompt():
    global newlen
    global newlist
    print "press 1 to do a comparison again. Press 2 to quit."
    againanswer = input("Press 1 or 2   ")
    if againanswer == 1:
        newlist = []
        populationslist = []
        newlen = 0
        addnation()
        comparepopulationslist()
        againprompt()
    elif againanswer == 2:
        print "goodbye. Thank you for using this app"
    else:
        againprompt()

        
#Functions in Order        
        
def printinfo():
    print " welcome to nation ranking program"
    print " this program allows one to rank nations in population (in millions) "
    print " and see how much bigger each nation's population is "
    print " compared to the nation ranked below it"
    print " press 1 to start, or press 0 to quit"
    firstanswer = input("press 1   ")
    if firstanswer == 1:
        addnation()
        comparepopulationslist()
        againprompt()
    else:
        print "try again. Press 1"
        printinfo()
           
printinfo()
                       
        
        
    
    
