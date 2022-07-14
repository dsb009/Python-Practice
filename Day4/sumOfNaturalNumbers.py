# Formula = n(n+1) / 2
#function to calculate sum of Natural Numbers
def sumOfNaturalNumbers(param):
    # result = param * (param + 1)
    # result = result / 2
    # return result
    return (param* (param + 1) / 2)

num = float(input("Please enter the number: "))

if num > 0:
    print("The sum of n natural numbers is :", sumOfNaturalNumbers(num))
else:
    print("Please enter a valid number..!!")