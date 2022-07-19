'''
Problem Statement: https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=false
'''
'''
ref: 
about regex:
https://www.w3schools.com/python/python_regex.asp#findall
https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/?ref=lbp

to validate regex: https://regex101.com/r/I58yAU/1
'''
import sys,time,re
if __name__ == '__main__':
    start = time.time()
    number_of_lines = int(input("Enter the total number of lines of code:" ))
    '''
    explanation for below line in:
    https://stackoverflow.com/questions/58612826/how-to-read-n-lines-at-a-time-from-stdin
    '''
    code=[sys.stdin.readline().strip() for _ in range(number_of_lines)]
    for i in code:
       color_code = re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})[\s:;,)]',i,re.IGNORECASE)
       #print(*color_code)
       for j in color_code:
        print(j)
    # color_code= [j for j in for i in code re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})[\s:;,)]',i,re.IGNORECASE)]
    end = time.time()
    print("Time taken in {}".format(start-end))