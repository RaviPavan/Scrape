#!/usr/bin/env python
print('If you get error "ImportError: No module named \'six\'" install six:\n'+\
    '$ sudo pip install six');
print('To enable your free eval account and get CUSTOMER, YOURZONE and ' + \
    'YOURPASS, please contact sales@brightdata.com')
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import sys
print (sys.version_info[0])
import sys

if sys.version_info[0]==3:
    
    print("Inside")
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    url='https://www.linkedin.com/in/jay-joshi-ai09965/'
   
    import urllib.request
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler(
            {'http': 'http://brd-customer-hl_8ba463bf-zone-residential-country-in:zbz1ljzw9bas@zproxy.lum-superproxy.io:22225',
            'https': 'http://brd-customer-hl_8ba463bf-zone-residential-country-in:zbz1ljzw9bas@zproxy.lum-superproxy.io:22225'}))
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')]
    print(opener.open(url).read())