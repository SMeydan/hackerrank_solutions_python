from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        lines = data.split('\n')
        if len(lines) > 1:
            print(">>> Multi-line Comment")
            for line in lines:
                print(line)
        else:
            print(">>> Single-line Comment")
            print(data)
    
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)
html = ""
for _ in range(int(input().strip())):
    html += input()
    html += '\n'
parser = MyHTMLParser()
parser.feed(html)
parser.close()
