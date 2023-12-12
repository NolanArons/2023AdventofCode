class CubeGame():
    def __init__(self,
                 cubeGameInput,
                 transformedInput,
                 possibleOutcomes,
                 addedTotal):
        self.cubeGameInput = cubeGameInput
        self.transformedInput = []
        self.possibleOutcomes = 0
        self.addedTotal = 0
    
    def transformInput(self):
        
        for i in self.cubeGameInput:
            self.transformedInput.append(i.split(':')[1].lstrip().split(';'))#Makes a list of lists where each sublist is one "game"
            #self.transformedInput is now a list of all the games now we need to add up how many colors were rolled each time.
    def colorCounting(self):
        gameIndex = 1
        for i in self.transformedInput:
            colors = {'red':0, 'green':0, 'blue':0}# make the dict with the colors 0 and they will be updated in by the second loop.
            for j in i:#j is each handfull
                red = green = blue = 0
                j = j.split(',')
                for k in j:
                    k = k.lstrip()
                    k = k.split(' ')
                    if k[1] == 'red':
                        colors['red']+= int(k[0])
                    if k[1] == 'green':
                        colors['green']+= int(k[0])
                    if k[1] == 'blue':
                        colors['blue']+= int(k[0])
            print (colors)
            if (self.checkColors(colors)):
                self.addedTotal+=gameIndex
                print(self.addedTotal)
            gameIndex+=1
                
                
            
            
    def checkColors(self, colors):
        if(colors['red'] > 12):
            return False
        if(colors['green'] > 13):
            return False
        if(colors['blue'] > 14):
            return False
        return True
        
                
                
            
            
            #     blue = green = red = 0
            #     print(j)
            #     if (j.find('red') != -1):
            #         red += int(j[j.find('red')-2])
            #         print(red)
            #     if (j.find('blue') != -1):
            #         blue += int(j[j.find('blue')-2])
            #     if (j.find('green') != -1):
            #         green += int(j[j.find('green')-2])
            # colors['red'] = red
            # colors['blue'] = blue
            # colors['green'] = green
            # print(colors)
                        
                    
                
cubeInput = possibleOutcomes = []
transformedInput = {}
addedTotal = 0
with open('cubeGameInput.txt') as f:
    cubeInput = [line.rstrip('\n') for line in f]
    
answer = CubeGame(cubeInput, transformedInput, possibleOutcomes, addedTotal)
answer.transformInput()
answer.colorCounting()
print(answer.addedTotal)
