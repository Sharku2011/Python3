import re, sys, urllib.request

def extractimgs(html):
    exp = re.compile(r'http://cfile([0-9]+).uf.tistory.com/image/([A-Za-z0-9]+)')
    imgs = exp.search(html)
    if len(imgs) == 0:
        print("There is no imgs")
    else:
        print(imgs)
    return imgs

def main(argv):
    if len(argv) != 2:
        print('Usage: extractimgs.py <filename>')
        return 1
    f = open(argv[1], 'r', encoding='utf-8')
    html = f.read()
    f.close()
    imgs = extractimgs(html)
    if len(imgs) == 0:
        print('No images!',file = sys.stderr)
        return 1
    for img in imgs:
        filepath = 'C:\\Users\\admin\\Desktop\\images\\{0}'.format(img[1])
        imgfile = open(filepath,'wb')
        #print(img[0]) 4     full url
        #print(img[1])      file name
        #print(img[2])      extension
        web = urllib.request.urlopen(img[0])
        imgfile.write(web)
        web.close()
        imgfile.close()
    return 0
    
#if __name__ == '__main__':
#    sys.exit(main(sys.argv))

main(['gethtml.py','crawl1.html'])