import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'CreativeWorks'
HOMEPAGE = 'http://creativeworks.tistory.com/'

DOMAIN_NAME = get_blog_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/Queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/Crawled.txt'
NUM_OF_THREAD = 4

queue = Queue()

a = Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

a.crawl_imgs('images','http://creativeworks.tistory.com/266')