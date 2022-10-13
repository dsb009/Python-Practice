import re

def startEnd(s,k):
    # while len(s):
    #     return (s.find(k[0]),s.find(k[-1]))
    m = re.pos(k,s)
    return (m.start(),m.end())

if __name__ == '__main__':
    str = input("Enter the string: ")
    substr = input("Enter the substring: ")
    print(startEnd(str,substr))

