import random
import sys

class Powerball:
    drawings=[]
    powers=[]
    numDraws=15600
    chosenNums=[0]*69
    chosenPBs=[0]*26
    mostFrequent=[]
    mostFrequentCount=0
    mostFrequentPct="0.0%"
    mostFrequentPB=[]
    mostFrequentPBCount=0
    mostFrequentPBPct="0.0%"
    leastFrequent=[]
    leastFrequentCount=156001
    leastFrequentPct="0.0%"
    leastFrequentPB=[]
    leastFrequentPBCount=156001
    leastFrequentPBPct="0.0%"
    spend=numDraws*2
    winnings=0
    totalWins=0
    totalWinPct="0.0%"
    playerPick=[]
    playerPower=0
    wins={
        "0p": 0,
        "0pd": 0,
        "1p": 0,
        "1pd": 0,
        "2p": 0,
        "2pd": 0,
        "3": 0,
        "3d": 0,
        "3p": 0,
        "3pd": 0,
        "4": 0,
        "4d": 0,
        "4p": 0,
        "4pd": 0,
        "5": 0,
        "5d": 0,
        "5p": 0,
        "5pd": 0
    }
    qp=False

    def pickBall(self,isPowerball):
        topRange=26 if isPowerball else 69
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
        self.powers.append(pb)
        self.chosenPBs[pb-1]+=1

    def evaluateDrawings(self):
        idx=0
        for drawing in self.drawings:
            win=False
            matches=len(set(drawing)&set(self.playerPick))
            matchStr=str(matches)
            powerMatch=self.powers[idx]==self.playerPower
            if powerMatch:
                matchStr+="p"
                self.wins[matchStr]+=1
                win=True
            elif not powerMatch and matches>=3:
                self.wins[str(matches)]+=1
                win=True
            if matches >= 4:
                print(matchStr + "  ***  " + " ".join(str(d) for d in drawing) + "     " + str(self.powers[idx]))
            if win:
                matchStrWin=matchStr+"d"
                amt=0
                match matchStrWin:
                    case "0pd":
                        amt=4
                    case "1pd":
                        amt=4
                    case "2pd":
                        amt=7
                    case "3d":
                        amt=7
                    case "3pd":
                        amt=100
                    case "4d":
                        amt=100
                    case "4pd":
                        amt=50000
                    case "5d":
                        amt=1000000
                    case "5pd":
                        amt=875000000
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

        for i in range(len(self.chosenPBs)):
            if self.chosenPBs[i] > self.mostFrequentPBCount:
                self.mostFrequentPB=[i+1]
                self.mostFrequentPBCount=self.chosenPBs[i]
            elif self.chosenPBs[i] == self.mostFrequentPBCount:
                self.mostFrequentPB.append(i+1)

            if self.chosenPBs[i] < self.leastFrequentPBCount:
                self.leastFrequentPB=[i+1]
                self.leastFrequentPBCount=self.chosenPBs[i]
            elif self.chosenPBs[i] == self.leastFrequentPBCount:
                self.leastFrequentPB.append(i+1)

        self.mostFrequentPBPct=str(self.mostFrequentPBCount / self.numDraws * 100) + "%"
        self.leastFrequentPBPct=str(self.leastFrequentPBCount / self.numDraws * 100) + "%"

    def debug(self):
        for i in range(len(self.chosenNums)):
            print(str(i+1) + ": " + str(self.chosenNums[i]))

    def getPlayerNumbers(self):
        if self.qp:
            pp="qp"
        else:
            print("Enter FIVE numbers (1-69) separated by a space, or enter qp for a quick pick")
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
            self.playerPower=random.randint(1,26)
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

    def getPlayerPowerball(self):
        print("Enter your Powerball number (1-26)")
        try:
            self.playerPower=int(input())
            if not self.validateInput(True):
                print("Invalid Powerball selection, try again")
                return False
        except Exception as e:
            print(e)
            print("Invalid Powerball selection, try again")
            return False

        return True

    def validateInput(self,isPowerball):
        if isPowerball:
            try:
                x=self.playerPower + 0
                return x >= 1 and x <= 26
            except:
                return False
        else:
            if len(self.playerPick) != 5:
                return False
            if not all(n.isdigit() for n in self.playerPick):
                return False
            for n in self.playerPick:
                if int(n) < 1 or int(n) > 69:
                    return False
            return True

    def printDraws(self):
        print(" ".join(str(n) for n in self.playerPick)+"     "+str(self.playerPower))
        print("\n\n")

pb=Powerball()
if len(sys.argv) >= 2 and sys.argv[1]=="qp":
    pb.qp=True

gotPN=False
while not gotPN:
    gotPN=pb.getPlayerNumbers()

if pb.playerPower==0:
    gotPPB=False
    while not gotPPB:
        gotPPB=pb.getPlayerPowerball()

for i in range(pb.numDraws):
    pb.doDrawing()
pb.printDraws()
pb.evaluateDrawings()

for k,v in pb.wins.items():
    if v > 0:
        print(k + ": " + str(v))

print ("\nYOU WON SOMETHING IN " + str(pb.totalWins) + " OUT OF " + str(pb.numDraws) + " DRAWS (" + pb.totalWinPct + ")\n")
print("Most chosen number(s) was/were " + ",".join(str(mf) for mf in pb.mostFrequent) + ", picked in " + str(pb.mostFrequentCount) + " (" + pb.mostFrequentPct + ") draws")
print("Least chosen number(s) was/were " + ",".join(str(lf) for lf in pb.leastFrequent) + ", picked in " + str(pb.leastFrequentCount) + " (" + pb.leastFrequentPct + ") draws")

print("Most chosen Powerball(s) was/were " + ",".join(str(mf) for mf in pb.mostFrequentPB) + ", picked in " + str(pb.mostFrequentPBCount) + " (" + pb.mostFrequentPBPct + ") draws")
print("Least chosen Powerball(s) was/were " + ",".join(str(lf) for lf in pb.leastFrequentPB) + ", picked in " + str(pb.leastFrequentPBCount) + " (" + pb.leastFrequentPBPct + ") draws")

print("SPENT:       $" + str(pb.spend))
print("WINNINGS:    $" + str(pb.winnings))
if pb.winnings > pb.spend:
    print("YOU WON:     $" + str(pb.winnings - pb.spend))
else:
    print("YOU LOST:    $" + str(pb.spend - pb.winnings))

# pb.debug()

