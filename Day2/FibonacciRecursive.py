#function to print fibonacci series 

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-2)+ fibonacci(i-1) 

index = int(input(" Enter the last index for the Fibonacci series: "))

for i in range(0,index):
    print(fibonacci(i))
    