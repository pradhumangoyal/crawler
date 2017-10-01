from urllib.parse import urlparse

#Get Domain Name
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-3]+'.'+results[-2] + '.' + results[-1]
    except:
        return ''

# Get sub domain name (mail.name.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
