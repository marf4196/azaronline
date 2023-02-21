import requests
import os
import sys
import chilkat


def ping(domain):
    print('\n\n-----------PING-----------\n\n')
    os.system(f'ping -n 10 {domain}')

def trace(domain):
    print('\n\n-----------Trace-----------\n\n')
    os.system(f'tracert {domain}')

def dns(domain):
    print('\n\n-----------DNS-----------\n\n')

    api_url = 'https://api.api-ninjas.com/v1/dnslookup?domain={}'.format(domain)
    response = requests.get(api_url, headers={'X-Api-Key': 'x59le7mMpk9FQDnjQNfl5w==AKEmYvoyZkJ46nTn'})
    if response.status_code == requests.codes.ok:
        for items in response.json():
            for item in items:
                print(item, '-->', items[item], '     ', end='')
            print('\n\n----------------------\n')
    else:
        print("Error:", response.status_code, response.text)

def check_ssh(ip):
    print('\n\n-----------SSH-----------\n\n')
    ssh = chilkat.CkSsh()
    success = ssh.Connect(str(ip),22)

    if (success != True):
        print(ssh.lastErrorText())

    connected = ssh.get_IsConnected()
    if (connected == True):
        connected = ssh.SendIgnore()

    print("ssh connection for = " + str(connected))



if len(sys.argv) == 1:
    print(f'USAGE ERROR\n type python azaronline.py -h to display help message.')
    exit()

if len(sys.argv) == 2:
    if str(sys.argv[1]) == '-h':
        help_message = '''
        in order to use this package you need another python package and an API_KEY.
        here is a link to download and install that specefic package:

        https://www.chilkatsoft.com/installWinPython.asp

        and here is a link to the website to get your API_KEY:

        https://api-ninjas.com/

        this project is under heavy development, feel free to add comments and ask for new features.

        right now there is three options:
        
        -h      display this help
        -d      specify domain
        -i      specify ip  

        -d:
        usage would be like: python azaronline.py -d <DOMAIN>
        and the expected output would contain DNS records, ping and trace to that domain.

        -i:
        usage would be like: python azaronline.py -i <IP>
        and the expected output would connection ssh conection results, ping and trace to that IP
        
        '''
        print(help_message)
        exit()
    if str(sys.argv[1]) == '-d':
        print(f'USAGE ERROR\nyou should specify a domain\ntype python azaronline.py -h to display help message.')
        exit()

    if str(sys.argv[1]) == '-i':
        print(f'USAGE ERROR\nyou should specify an IP\ntype python azaronline.py -h to display help message.')
        exit()

if len(sys.argv) == 3:
    if str(sys.argv[1]) == '-d':
        domain = sys.argv[2]
        dns(domain)
        ping(domain)
        trace(domain)
        exit()
    if str(sys.argv[1]) == '-i':
        ip = sys.argv[2]
        check_ssh(ip)
        ping(ip)
        trace(ip)
        exit()

print(f'USAGE ERROR\n type python azaronline.py -h to display help message.')