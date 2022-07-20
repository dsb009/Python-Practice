'''
Problem Statement: 

https://www.hackerrank.com/challenges/html-parser-part-1/problem
'''
from html.parser import HTMLParser
import sys


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs):
        print("Start : ", tag)
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))
    def handle_endtag(self, tag: str,attrs):
        print("End   : ",tag)
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))
    def handle_startendtag(self, tag: str, attrs):
        print("Empty : ", tag)
parser = MyHTMLParser()

n = int(input())
for _ in range(n):
    code =sys.stdin.readline()
    parser.feed(code)

    
   