class Trebuchet():
    ###numberDict: store each number spelled and replace it with the integer form
    #replace them with the number plus the first and last letter of the number as they might be used to spell a different number.
    #ex: twothreeight would be 23ight if you just replaced it with the integer directly, not 
    numberDict = {"one" : "o1e", 
                  "two" : "t2o",
                  "three" : "t3e",
                  "four" : "f4r",
                  "five" : "f5e",
                  "six" : "s6x",
                  "seven" : "s7n",
                  "eight" : "e8t",
                  "nine" : "n9e"
                  }
    def __init__(self,
                    calibrationInputList,
                    calibratedTotal):
        self.calibrationInputList = calibrationInputList
        self.calibratedTotal = 0
    

    #member function that calculates the coordinates from a list by combining the first and last numbers as strings and then adding that number to the total
    #just updates member variables
    def calculateCoordinates(self):
        firstNum = lastNum = 0
        print(self.calibrationInputList)

        for i in self.calibrationInputList:
            for k in i:
                if k.isdigit():
                    firstNum = k
                    break
            for n in reversed(i):
                if n.isdigit():
                    lastNum = n
                    break
            catStr = firstNum+lastNum
            self.calibratedTotal += int(catStr)
    #member function that takes a list of strings, iterates through the list, iterates through our number dict to see if there are any numbers spelled out, and replaces them with a string version of the interger + the first and last letter of each number spelled out
    def convertToInt(self):
        newList = []
        for i in range(len(self.calibrationInputList)):
            newStr = ""
            for key in self.numberDict.keys():
                self.calibrationInputList[i] = self.calibrationInputList[i].replace(key, self.numberDict[key])
            
                    
                
        
            
            
calInput = []
calTotal = 0
with open('trebuchetInput.txt') as f:
    calInput = [line.rstrip('\n') for line in f]
    
t = Trebuchet(calInput, calTotal)
t.convertToInt()
t.calculateCoordinates()

print(t.calibratedTotal)
        