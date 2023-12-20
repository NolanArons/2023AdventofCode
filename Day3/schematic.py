import re


def checkAdjacent(schematicLineList) -> int:
    total = 0
    for line in range(len(schematicLineList)): 
        numberLocations = re.finditer(r'\d+', schematicLineList[line])
        for match in numberLocations:
            if line == 0:#if the number is the first or last char of the string, it doesn't get checked
                same = re.search(r'[^\w\.]', schematicLineList[line][match.start()-1:match.end()+1])
                next = re.search(r'[^\w\.]', schematicLineList[line+1][match.start()-1:match.end()+1])
                if(same != None or next != None):
                    print(match.group())
                    total+= int(match.group())
            elif line == len(schematicLineList)-1:
                same = re.search(r'[^\w\.]', schematicLineList[line][match.start()-1:match.end()+1])
                previous = re.search(r'[^\w\.]', schematicLineList[line-1][match.start()-1:match.end()+1])
                if(same != None or previous != None):
                    print(match.group())
                    total+= int(match.group())
            else:
                same = re.search(r'[^\w\.]', schematicLineList[line][match.start()-1:match.end()+1])
                next = re.search(r'[^\w\.]', schematicLineList[line+1][match.start()-1:match.end()+1])
                previous = re.search(r'[^\w\.]', schematicLineList[line-1][match.start()-1:match.end()+1])
                if(same != None or previous != None or next != None):
                    print(match.group())
                    total+= int(match.group())
    return total
    
    
def findGearPower(thisLine, prevLine, nextLine):
    gearLocations = re.finditer(r'\*', thisLine)

def findGearPower(thisLine, otherLine):
    gearLocations = re.finditer(r'\*', thisLine)
        

def setUpGears(machineInput):
    for line in range(len(machineInput)):
        if line == 0: 
            findGearPower( machineInput[line], machineInput[line+1])
        elif line == len(machineInput)-1:
            findGearPower( machineInput[line], machineInput[line-1])
        else:
            findGearPower( machineInput[line], machineInput[line-1], machineInput[line+1])

     
# def gearRatio(machineInput):
#     # stringy = "Hows are you doing 12?"
#     # this = re.search(r'\d+', stringy)
#     # newstring = stringy[this.start()-1::-1]
#     # print(newstring)
#     total = 0
#     for line in range(len(machineInput)): 
#         numberLocations = re.finditer(r'\*', machineInput[line])
#         for match in numberLocations:
#             num = []
#             if line == 0:
#                 checkString = machineInput[line][match.start()-1::-1]
#                 findIfNumber(checkString, num)
#                 checkString = machineInput[line+1][match.start()::-1]
#                 findIfNumber(checkString, num)
#                 checkString = machineInput[line][match.end():len(checkString)-1]
#                 findIfNumber(checkString, num)
#                 checkString = machineInput[line+1][match.end():len(checkString)-1]
#                 findIfNumber(checkString, num)
#                 if len(num) == 2:
#                     total += num[0]*num[1]
#             elif line == len(machineInput):
#                 checkString = machineInput[line][match.start()-1::-1]
#                 findIfNumber(checkString, num)
#                 checkString = machineInput[line-1][match.start()::-1]
#                 findIfNumber(checkString, num)
#                 checkString = machineInput[line][match.end():len(checkString)-1]
#                 findIfNumber(checkString, num)
#                 checkString = machineInput[line-1][match.end():len(checkString)-1]
#                 findIfNumber(checkString, num)
#                 if len(num) == 2:
#                     total += num[0]*num[1]
#             else:
#                 checkString = machineInput[line][match.start()-1::-1]
#                 findIfNumber(checkString, num)
#                 checkString = machineInput[line+1][match.start()::-1]
#                 findIfNumber(checkString, num)
#                 checkString = machineInput[line][match.end():len(checkString)-1]
#                 findIfNumber(checkString, num)
#                 checkString = machineInput[line+1][match.end():len(checkString)-1]
#                 findIfNumber(checkString, num)
#                 checkString = machineInput[line-1][match.start()::-1]
#                 findIfNumber(checkString, num)
#                 checkString = machineInput[line-1][match.end():len(checkString)-1]
#                 findIfNumber(checkString, num)
#                 if len(num) == 2:
#                     total += num[0]*num[1]
#     return total
                
# def findIfNumber(string, list):
#     print(string)
#     if string[0].isdigit():
#         x = re.search(r'\d+', string)
#         list.append(x.group())
       
with open('SchematicInput.txt') as f:#get the input from a text file
        machineInput = [line.rstrip('\n') for line in f ] #read it in line by line and store it in cubeInput
for line in range(len(machineInput)):
    machineInput[line] = "." + machineInput[line] + "."
        

#print(checkAdjacent(machineInput))
print(gearRatio(machineInput))