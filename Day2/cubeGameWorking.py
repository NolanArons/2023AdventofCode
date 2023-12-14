import re
### howManyCubes
# line: a string that represents one "Game" of the dice game
# The color we wish to check
# return: an integer list of all of the specified color dice numbers in a given game
#This function uses regex to check for the color and the number that comes before the color
def howManyCubes(line, color) -> list:
    colorList = re.findall( r'\d+ ' + re.escape(color) , line)#check for any number followed by the color specified. Do this by contstructing a regex string that consists of \d+ (any number) + regular expression of the color we pass in
    colorString = "".join(str(x)for x in colorList) #Make it a string so we can use findall on it again
    return list(map(int,re.findall(r'\d+', colorString)))#use findall to find the strings, map it to an int list and return it. Make it an int list so that the values in the list behave as integers not strings NOTE: When it was a string, "max" returned the wrong integer as the max value
    
    
count = 1 #Instead of saving the Game Number, I just used a count as the game number
total = 0 #This will be our answer
with open('cubeGameInput.txt') as f:#get the input from a text file
    cubeInput = [line.rstrip('\n') for line in f] #read it in line by line and store it in cubeInput
for line in cubeInput: #iterate through all of the lines in cubeInput
    if (int(max(howManyCubes(line, 'red')))) <= 12 and (int(max(howManyCubes(line, 'green')))) <= 13 and (int(max(howManyCubes(line, 'blue')))) <= 14: #call howManyCubes, which returns a list of the cubes of the color it is called with. If the max number in that list meets the rules:
        total += count#add the game number to our total
    count+=1
print(total) #print the answer
    