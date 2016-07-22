#top level domain ex: github.com
#robots.txt is a place to put list of files you don't want google to crawl #
#Python Scanner
#Let's say you want to get information for website, like robots, ip, who owns the domain.
#that's what this tool does for you. It will allow you to input domain of your choice and
#returns all of the results into a text file with one click.
#Eliminates the need for typing the same terminal commands over and over
from general import *
from domain import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

ROOT_DIR = "sites"
create_dir(ROOT_DIR)

def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(url)
    nmap = get_nmap('-F', ip_address)
    robots = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, robots, whois)

def create_report(name, full_url, domain_name, nmap,robots, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots_txt.txt', robots)
    write_file(project_dir + '/whois', whois)
gather_info('reddit.com', 'https://www.reddit.com')