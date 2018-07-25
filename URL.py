from urllib.request import urlopen
link = 'http://python.org/'
def getHtml():
    try:
        f = urlopen(link)
        print(f)
        html = f.read()
        #print(html)
        htmldecoded = html.decode()
        #print(htmldecoded)
    except Exception as ex:
        print('*** Failed to get HTML! ***\n\n' + str(ex))
    else:
        return htmldecoded

