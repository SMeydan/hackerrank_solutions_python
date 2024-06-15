from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for attr, value in attrs:
                if attr == 'class':
                    print(f"-> class > {value}")
                else:
                    print(f"-> {attr} > {value}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        if attrs:
            print("Empty :", tag)
            for attr, value in attrs:
                if attr == 'class':
                    print(f"-> class > {value}")
                else:
                    print(f"-> {attr} > {value}")
        else:
            print("Empty :", tag)

parser = MyHTMLParser()
html_content= ""
for _ in range(int(input())):
    html_content += input()
parser.feed(html_content)
