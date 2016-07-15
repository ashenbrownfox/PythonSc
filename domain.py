# import the top level of domain name in settings, package mangager if not available
from tld import get_tld

def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name

print(get_domain_name('https://www.espn.com'))