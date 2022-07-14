#Function that counts the length of the Given string
def strLength(somestring):
    len_count= 0
    for i in somestring:
        len_count = len_count + 1
    return len_count

my_string = str(input("Please enter the string: "))

str_len = strLength(my_string)
print("The length of the provided string is: ", str_len)