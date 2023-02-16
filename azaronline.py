import requests
import os
import sys


if len(sys.argv) != 2:
    print(f'USAGE ERROR\n USAGE: python azaronline.py <domain name>')

domain = sys.argv[1]

def ping(domain):
    print('\n\n-----------PING-----------\n\n')
    os.system(f'ping {domain}')

def trace(domain):
    print('\n\n-----------Trace-----------\n\n')
    os.system(f'tracert {domain}')
def dns(domain):
    print('\n\n-----------DNS-----------\n\n')

    api_url = 'https://api.api-ninjas.com/v1/dnslookup?domain={}'.format(domain)
    response = requests.get(api_url, headers={'X-Api-Key': ''})
    if response.status_code == requests.codes.ok:
        for items in response.json():
            for item in items:
                print(item, '-->', items[item], '     ', end='')
            print('\n\n----------------------\n')
    else:
        print("Error:", response.status_code, response.text)

dns(domain)
ping(domain)
trace(domain)