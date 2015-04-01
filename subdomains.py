import argparse
import sys
from urlparse import urlparse
try:
    from google import search
except Exception, err:
    print "Please install requirements.txt => pip install -r requirements.txt"


description = """
    This script finds subdomains with google.\n
    Example :
    python subdomains.py -d website.com -c 20
"""
parser = argparse.ArgumentParser("subdomain", description=description)
parser.add_argument("--domain", "-d", help="URL, format : site.com")
parser.add_argument("--count", "-c", help="The number of URLs to look at Google")
args = parser.parse_args()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print parser.print_help()
        exit(0)

    subdomain_list = []
    if not args.domain.startswith(("http", "https")):
        args.domain = "http://%s" % (args.domain, )

    domain = urlparse(args.domain).netloc

    if domain == "":
        print parser.print_help()
        exit(0)

    if domain.startswith("www."):
        domain = domain[4:]

    query = "site:%s -www.%s" % (domain, domain)
    try:
        for url in search(query, stop=int(args.count)):
            url = urlparse(url).netloc
            if url not in subdomain_list:
                subdomain_list.append(url)
                print url
    except Exception, err:
        print err