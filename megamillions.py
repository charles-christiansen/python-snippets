import random
import sys

class MegaMillions:
    drawings=[]
    megas=[]
    numDraws=104
    chosenNums=[0]*70
    chosenMegas=[0]*25
    mostFrequent=[]
    mostFrequentCount=0
    mostFrequentPct="0.0%"
    mostFrequentMega=[]
    mostFrequentMegaCount=0
    mostFrequentMegaPct="0.0%"
    leastFrequent=[]
    leastFrequentCount=156001
    leastFrequentPct="0.0%"
    leastFrequentMega=[]
    leastFrequentMegaCount=156001
    leastFrequentMegaPct="0.0%"
    spend=numDraws*2
    winnings=0
    totalWins=0
    totalWinPct="0.0%"
    playerPick=[]
    playerMega=0
    wins={
        "0m": 0,
        "0md": 0,
        "1m": 0,
        "1md": 0,
        "2m": 0,
        "2md": 0,
        "3": 0,
        "3d": 0,
        "3m": 0,
        "3md": 0,
        "4": 0,
        "4d": 0,
        "4m": 0,
        "4md": 0,
        "5": 0,
        "5d": 0,
        "5m": 0,
        "5md": 0
    }
    qp=False

    def pickBall(self,isMegaBall):
        topRange=25 if isMegaBall else 70
        n=random.randint(1,topRange)
        return n

    def doDrawing(self):
        nums=[]
        for i in range(5):
            n=self.pickBall(False)
            while n in nums:
                n=self.pickBall(False)
            nums.append(n)
            self.chosenNums[n-1]+=1
        nums.sort()
        self.drawings.append(nums)
        pb=self.pickBall(True)
        self.megas.append(pb)
        self.chosenMegas[pb-1]+=1

    def evaluateDrawings(self):
        idx=0
        for drawing in self.drawings:
            win=False
            matches=len(set(drawing)&set(self.playerPick))
            matchStr=str(matches)
            powerMatch=self.megas[idx]==self.playerMega
            if powerMatch:
                matchStr+="m"
                self.wins[matchStr]+=1
                win=True
            elif not powerMatch and matches>=3:
                self.wins[str(matches)]+=1
                win=True
            if matches >= 4:
                print(matchStr + "  ***  " + " ".join(str(d) for d in drawing) + "     " + str(self.megas[idx]))
            if win:
                matchStrWin=matchStr+"d"
                amt=0
                match matchStrWin:
                    case "0md":
                        amt=2
                    case "1md":
                        amt=4
                    case "2md":
                        amt=10
                    case "3d":
                        amt=10
                    case "3md":
                        amt=200
                    case "4d":
                        amt=500
                    case "4md":
                        amt=10000
                    case "5d":
                        amt=1000000
                    case "5md":
                        amt=640000000
                self.wins[matchStrWin]+=amt
                self.winnings+=amt
                self.totalWins+=1
            idx+=1
        self.totalWinPct=str(self.totalWins / self.numDraws * 100) + "%"

        for i in range(len(self.chosenNums)):
            if self.chosenNums[i] > self.mostFrequentCount:
                self.mostFrequent=[i+1]
                self.mostFrequentCount=self.chosenNums[i]
            elif self.chosenNums[i] == self.mostFrequentCount:
                self.mostFrequent.append(i+1)

            if self.chosenNums[i] < self.leastFrequentCount:
                self.leastFrequent=[i+1]
                self.leastFrequentCount=self.chosenNums[i]
            elif self.chosenNums[i] == self.leastFrequentCount:
                self.leastFrequent.append(i+1)

        self.mostFrequentPct=str(self.mostFrequentCount / self.numDraws * 100) + "%"
        self.leastFrequentPct=str(self.leastFrequentCount / self.numDraws * 100) + "%"

        for i in range(len(self.chosenMegas)):
            if self.chosenMegas[i] > self.mostFrequentMegaCount:
                self.mostFrequentMega=[i+1]
                self.mostFrequentMegaCount=self.chosenMegas[i]
            elif self.chosenMegas[i] == self.mostFrequentMegaCount:
                self.mostFrequentMega.append(i+1)

            if self.chosenMegas[i] < self.leastFrequentMegaCount:
                self.leastFrequentMega=[i+1]
                self.leastFrequentMegaCount=self.chosenMegas[i]
            elif self.chosenMegas[i] == self.leastFrequentMegaCount:
                self.leastFrequentMega.append(i+1)

        self.mostFrequentMegaPct=str(self.mostFrequentMegaCount / self.numDraws * 100) + "%"
        self.leastFrequentMegaPct=str(self.leastFrequentMegaCount / self.numDraws * 100) + "%"

    def debug(self):
        for i in range(len(self.chosenNums)):
            print(str(i+1) + ": " + str(self.chosenNums[i]))

    def getPlayerNumbers(self):
        if self.qp:
            pp="qp"
        else:
            print("Enter FIVE numbers (1-70) separated by a space, or enter qp for a quick pick")
            pp=input()
        if pp=="qp":
            nums=[]
            for i in range(5):
                n=self.pickBall(False)
                while n in nums:
                    n=self.pickBall(False)
                nums.append(n)

            nums.sort()
            self.playerPick=nums
            self.playerMega=self.pickBall(True)
        else:
            try:
                self.playerPick=pp.split(" ")
                if not self.validateInput(False):
                    print("Invalid number selection, try again")
                    return False
                self.playerPick=[int(pick) for pick in self.playerPick]
                self.playerPick.sort()
            except Exception as e:
                print(e)
                print("Invalid number selection, try again")
                return False

        return True

    def getPlayerMegaMillions(self):
        print("Enter your MegaMillions number (1-25)")
        try:
            self.playerMega=int(input())
            if not self.validateInput(True):
                print("Invalid MegaMillions selection, try again")
                return False
        except Exception as e:
            print(e)
            print("Invalid MegaMillions selection, try again")
            return False

        return True

    def validateInput(self,isMegaBall):
        if isMegaBall:
            try:
                x=self.playerMega + 0
                return x >= 1 and x <= 25
            except:
                return False
        else:
            if len(self.playerPick) != 5:
                return False
            if not all(n.isdigit() for n in self.playerPick):
                return False
            for n in self.playerPick:
                if int(n) < 1 or int(n) > 70:
                    return False
            return True

    def printDraws(self):
        print(" ".join(str(n) for n in self.playerPick)+"     "+str(self.playerMega))
        print("\n\n")

mm=MegaMillions()
if len(sys.argv) >= 2 and sys.argv[1]=="qp":
    mm.qp=True

gotPN=False
while not gotPN:
    gotPN=mm.getPlayerNumbers()

if mm.playerMega==0:
    gotPMega=False
    while not gotPMega:
        gotPMega=mm.getPlayerMegaMillions()

for i in range(mm.numDraws):
    mm.doDrawing()
mm.printDraws()
mm.evaluateDrawings()

for k,v in mm.wins.items():
    if v > 0:
        print(k + ": " + str(v))

print ("\nYOU WON SOMETHING IN " + str(mm.totalWins) + " OUT OF " + str(mm.numDraws) + " DRAWS (" + mm.totalWinPct + ")\n")
print("Most chosen number(s) was/were " + ",".join(str(mf) for mf in mm.mostFrequent) + ", picked in " + str(mm.mostFrequentCount) + " (" + mm.mostFrequentPct + ") draws")
print("Least chosen number(s) was/were " + ",".join(str(lf) for lf in mm.leastFrequent) + ", picked in " + str(mm.leastFrequentCount) + " (" + mm.leastFrequentPct + ") draws")

print("Most chosen MegaMillions(s) was/were " + ",".join(str(mf) for mf in mm.mostFrequentMega) + ", picked in " + str(mm.mostFrequentMegaCount) + " (" + mm.mostFrequentMegaPct + ") draws")
print("Least chosen MegaMillions(s) was/were " + ",".join(str(lf) for lf in mm.leastFrequentMega) + ", picked in " + str(mm.leastFrequentMegaCount) + " (" + mm.leastFrequentMegaPct + ") draws")

print("SPENT:       $" + str(mm.spend))
print("WINNINGS:    $" + str(mm.winnings))
if mm.winnings > mm.spend:
    print("YOU WON:     $" + str(mm.winnings - mm.spend))
else:
    print("YOU LOST:    $" + str(mm.spend - mm.winnings))

# mm.debug()

