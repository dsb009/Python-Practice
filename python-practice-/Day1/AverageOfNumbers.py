#function to collect all the numbers 
def collectNumbers(totalNumbers):
    print("Please enter", totalNumbers,"numbers")
    for i in range(0,totalNumbers):
        ele = float(input())
        myList.append(ele)

#function to calculate average 
def calculateAverage():
    total=0
    for i in range(0,len(myList)):
        total = total + myList[i]
    return (total/totalNumbers)


myList = []

# Collect the total number of items in the list 

totalNumbers = int(input("How many numbers to calculate average for:  "))
collectNumbers(totalNumbers) #Calling function to collect all the numbers

#calculate average 

average = calculateAverage()
print("The average of {} is: {}".format(myList,average ))
