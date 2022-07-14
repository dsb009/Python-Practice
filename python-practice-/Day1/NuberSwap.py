#swapping two numbers without a third variable 

num1 = int(input("Enter number 1: " ))
num2 = int(input("Enter number 2: " ))

if num1 < num2:
    print(" In if - Before sawp num1 is {}, num2 is {}".format(num1,num2))

    num2 = num2+num1 #num2=30
    num1 = num2-num1 #num1=20
    num2 = num2-num1 #num2=10

    print("In if - After swap num1 is {}, num2 is {} ".format(num1,num2))
else:
    print("In else - Before sawp num1 is {}, num2 is {}".format(num1,num2))

    num1 = num1+num2 #num1=30
    num2 = num1-num2 #num2=20
    num1 = num1-num2 #num1=10

    print("In else - After swap num1 is {}, num2 is {}".format(num1, num2))
