from cgi import parse_multipart


def isLeapYear(param):
    if ((param % 400 == 0) | (param % 100 != 0) & (param % 4 == 0)):
            print("It's a leap year..!!")
    else:
            print("It's not a leap year.")

year  = int(input("Please enter the year: "))
isLeapYear(year)