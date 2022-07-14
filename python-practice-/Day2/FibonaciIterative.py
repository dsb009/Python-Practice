# series is 0,1,1,2,3...

index= int(input("Enter the last index for the fibonaci series: "))

firstnumber = 0
secondnumber = 1
temp = 0

fibonaciList = []
print(firstnumber)
print(secondnumber)

for i in range(0,index):
    temp= firstnumber + secondnumber
    firstnumber = secondnumber
    secondnumber = temp
    print(temp)
