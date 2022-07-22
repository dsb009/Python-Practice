'''
Problem Statement: 

https://www.hackerrank.com/challenges/html-parser-part-1/problem
'''
from html.parser import HTMLParser
import time

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs):
        print("Start :", tag.strip())
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))
    def handle_endtag(self, tag: str):
        print("End   :",tag.strip())
    def handle_startendtag(self, tag: str, attrs):
        print("Empty :", tag.strip())
        for name,value in attrs:
            print("->",name+" >",value)
parser = MyHTMLParser()

start = time.time()
n = int(input())
for _ in range(n):
    parser.feed(input())
end= time.time()

print(start-end)
