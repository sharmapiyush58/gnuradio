import urllib2
import simplejson
import json
import webbrowser

# A test url
basic_url = 'http://gnuradio.org/doc/doxygen/search/all_2.js'


#To overcome http error 403
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

basic_req = urllib2.Request(basic_url, headers=hdr)

try:
    basic_response = urllib2.urlopen(basic_req)
except urllib2.HTTPError, e:
    br1 = e.fp.read()

basic_html = basic_response.read()
basic_html = basic_html[15:-1]
temp = basic_html

temp = temp.replace("'", '"')

# A test key
key = 'block__set_relative_rate'

parsed = simplejson.loads(temp)
for k in range(len(parsed)):
    if parsed[k][1][0] == key:
        block_url = 'http://gnuradio.org/doc/doxygen' + (repr(parsed[k][1][1][0][2:])[1:-1])
webbrowser.open(block_url)
