from urllib.request import urlopen

def savefile(contents, filename):
    f = open(filename,'w', encoding = 'utf-8')
    f.write(contents)
    f.close()

def gethtml(url):
    response = urlopen(url)
    if response.getheader('Content-Type') == 'text/html; charset=utf-8':
        html_bytes = response.read()
        html_str = html_bytes.decode('utf-8')
        return html_str
    return response.read()

def main(argv):
    if len(argv) != 3:
        print('Usage: gethtml.py <url> <save_dest>')
        return 1
    url = argv[1]
    print("{} 의 html 태그를 가져오는 중입니다...".format(url))
    save_dest = argv[2]
    
    html = gethtml(url)
    savefile(html, save_dest)
    return 0

if __name__ == 'main':
    sys.exit(main(sys.argv))

main(['gethtml.py','http://creativeworks.tistory.com/1', 'crawl1.html'])