import urllib2
import simplejson
import json
import webbrowser
import links_for_each_block

keys = links_for_each_block.all_keys
links = links_for_each_block.all_final_links
key = keys[0] #Test case
link = links[0] #Test case

for i in range(len(link)):
    flag = 0 #checking if operation successful 
    js_url = link[i]


    #To overcome http error 403
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    js_req = urllib2.Request(js_url, headers=hdr)

    try:
        js_response = urllib2.urlopen(js_req)
    except urllib2.HTTPError, e:
        br1 = e.fp.read()

    js_html = js_response.read()
    basic_html = js_html[15:-1]
    temp = basic_html

    temp = temp.replace("'", '"')

    parsed = simplejson.loads(temp)

    if key[-2:-1]+key[-1] == 'xx':
        end_index = -2
    elif key[-1] == 'x':
        end_index = -1
    else:
        end_index = None

    for k in range(len(parsed)):
            
        if parsed[k][1][0][:end_index] == key[:end_index]:
            block_url = 'http://gnuradio.org/doc/doxygen' + (repr(parsed[k][1][1][0][2:])[1:-1])
            print(block_url)
            webbrowser.open(block_url)
            flag = 1 #checking if operation successful
            break
    if flag == 1:
        break
