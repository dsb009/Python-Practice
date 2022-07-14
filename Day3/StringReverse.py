#function to reverse string
def strReverse(somestring):
    reverseString=""
    for i in somestring:
        reverseString= i + reverseString
    return reverseString

#driver code 
# Accept input as string
my_string = str(input("Enter the string you want to reverse: "))

str_rev = strReverse(my_string)
print("The reverse of the provided string is: ",str_rev)