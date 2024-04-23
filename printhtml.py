
try:
        from BeautifulSoup import BeautifulSoup
except ImportError:
        from bs4 import BeautifulSoup
import os
import json
prefixed = [filename for filename in os.listdir('.') if filename.startswith("test")]
jsonjob={}
prefixed.sort()
prev=[]
for fil in prefixed:
    cache=[]
    with open(fil,'r') as f:
        html=f.read()
        parsed_html = BeautifulSoup(html,features="html.parser")
        jobs=parsed_html.body.find_all('div',attrs={'absolute'})
        for i in jobs:
            link=i.find('a')
            if link!=None:
                cache.append(link.text)
        if cache==prev:
            raise Exception("2")
        else:
            prev=cache.copy()
