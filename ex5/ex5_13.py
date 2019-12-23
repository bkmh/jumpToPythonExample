import random

randomList = []

while len(randomList) < 6:
    
    tempVal = random.randrange(1, 45)

    if tempVal not in randomList:
        randomList.append(tempVal)


print(randomList)
