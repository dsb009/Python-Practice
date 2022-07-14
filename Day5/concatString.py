
def concatstring(param):
    result = ""
    for i in range(1,param + 1):
        result = result + str(i)
    return result


input = int(input("Enter any digit: "))
print("The concatenated string is ",concatstring(input))