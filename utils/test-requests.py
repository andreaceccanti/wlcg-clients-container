import requests
import logging
import os
import sys

try:
    from http.client import HTTPConnection  # py3
except ImportError:
    from httplib import HTTPConnection  # py2


HTTPConnection.debuglevel = 1
logging.basicConfig(level=logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

dst = 'https://storm.example:8443/wlcg/test-not-found'
headers = {'Authorization': "Bearer %s" % os.getenv('BEARER_TOKEN')}

s = requests.Session()
for i in range(1, 2):
    head = s.head(dst, headers=headers)
    print("Head 1 data:", head.text)
    head = s.head(dst, headers=headers)
    print("Head 1 data:", head.text)
    propfind = s.request('PROPFIND', dst, headers=headers)
    print("Propfind 1 data:", propfind.text)
    head = s.head(dst, headers=headers)
    print("Head 2 data:", head.text)
    propfind = s.request('PROPFIND', dst, headers=headers)
    print("Propfind 2 data:", propfind.text)
