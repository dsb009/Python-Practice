from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs) -> None:
        print(tag)
        #using list comprehension
        #[print('-> {} > {}'.format(*attr)) for attr in attrs]
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))
    
    def handle_startendtag(self, tag: str, attrs) -> None:
        print(tag)
        for attr in attrs:
             print("-> {} > {}".format(attr[0], attr[1]))
             

parser = MyHTMLParser()

n = int(input())
for _ in range(n):
    parser.feed(input())