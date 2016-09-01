import sys
def whois(ip):
    import requests
    import pprint
    import json
    url="http://ip-api.com/json/"
    r=requests.get(url+ip,headers={'Accept': 'application/json/'})
    results = r.json()
    As = results['as']
    org = results['org']
    cnt = results['countryCode']
    isp = results['isp']

    pprint.pprint('{0}    {1}    {2}    {3}   =1'.format(As,org,cnt,isp))


if __name__ == '__main__':
        for x in sys.stdin:
            x=x.strip()
            x=str(x)
            if(x != "N/A"):
               whois(str(x))
