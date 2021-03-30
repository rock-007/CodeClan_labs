# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

evenNumbers = []
for eachNumber in numbers:
    if eachNumber % 2 == 0:
        evenNumbers.append(eachNumber)
print("# 1")
print(evenNumbers)
        

# 2. Print the difference between the largest and smallest value:
minValue= min(numbers)
maxValue= max(numbers)
print("# 2")
print(maxValue-minValue)

# 3. Print True if the list contains a 2 next to a 2 somewhere.

totalLength=len(numbers)
print(numbers)  
currentIndex=0
for index, currentElement in enumerate(numbers[:-1]):
    for nextElement in numbers[index+1:]:
        if (currentElement== nextElement==2):
            print("# 3")
            print(True)


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

totalSum=0
excedeSeven=True
exceedSix=False
for currentElement in numbers:
    if (currentElement==6):
        excedeSeven= False
    elif (excedeSeven):
        totalSum +=currentElement
    elif (currentElement==7):
        excedeSeven=True
print("# 4")
print(totalSum)






# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
totalSumNew=0
ignoreIndex=-1

for index, currentElement in enumerate(numbers):
   
    if(currentElement==int(13) and index != len(numbers)-1):
        ignoreIndex=index+1
    elif(index !=ignoreIndex):
        totalSumNew=totalSumNew+currentElement
      
print("# 5")
print(totalSumNew)







