import sys

def check_if_color_code(*args):
    for i in args:
        print(i[0])
        print(i[1])
        print(i[2])
        print(i[3])
        print(i[4])
        # if i[1] =='#':
        #     print(i + "first if")
        #     if 3 <= len(i) <= 6:
        #         print(i+ "second if")
        #         if str(i) in (1,2,3,4,5,6,7,8,9,0,'A','B','C','D','E','F','a','b','c','d','e','f'):
        #             print(i + "third if") 
if __name__ == '__main__':
    number_of_lines = int(input("Enter the total number of lines of code:" ))
    #https://stackoverflow.com/questions/58612826/how-to-read-n-lines-at-a-time-from-stdin
    code=[sys.stdin.readline().strip() for _ in range(number_of_lines)]
    # print(type(code))
    check_if_color_code(code)