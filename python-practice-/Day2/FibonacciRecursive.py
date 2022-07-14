#Recursive function to print Fibonnaci

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)

index = int(input("Enter the index till you want the series: "))
if index < 0:
    print("Please enter a positive number")
else:
    for i in range(0,index):
        print(fibonacci(i))
