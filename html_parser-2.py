from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data: str) -> None:
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data.strip())
        else:
            print(">>> Single-line Comment")
            print(data.strip())
    def handle_data(self, data: str) -> None:
        if '\n' in data:
            data=data.replace("\n", "")
        else:
            print(">>> Data")
            print(data)

html = ""       
for i in range(int(input())):
    html += input().strip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
