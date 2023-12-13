import re

def checkCubes(line, color) -> int:
    print(color)
    print(line)
    colorInstance = re.findall(line , r'\d+') #r"\d+ \s" + 
    print (colorInstance)
    
    
with open('cubeGameInput.txt') as f:
    cubeInput = [line.rstrip('\n') for line in f]
for line in cubeInput:
    checkCubes(line, 'red')
    