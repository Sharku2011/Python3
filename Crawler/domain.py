from urllib.parse import urlparse

#Get domain name
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''
        
def get_blog_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-3] + '.' + results[-2] + '.' + results[-1]
    except:
        return ''
        
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''