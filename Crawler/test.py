from img_finder import ImgFinder
from urllib.request import urlopen

Page_url = 'http://creativeworks.tistory.com/266'
html_str = ''

response = urlopen(Page_url)
if response.getheader('Content-Type') == 'text/html; charset=utf-8':
    html_bytes = response.read()
    html_str = html_bytes.decode('utf-8')
finder = ImgFinder('http://creativeworks.tistory.com/', Page_url)
finder.feed(html_str)


for link in finder.page_links():
    print(link)


