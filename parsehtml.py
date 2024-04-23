try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import os
import json
prefixed = [filename for filename in os.listdir('.') if filename.startswith("test")]
jsonjob={}
for fil in prefixed:
    with open(fil,'r') as f:
        html=f.read()
        parsed_html = BeautifulSoup(html,features="html.parser")
        jobs=parsed_html.body.find_all('div',attrs={'absolute'})
        for i in jobs:
            link=i.find('a')
            if link!=None:
                jsonjob[link['href']]=link.text

diffe={}
try:
    with open('jobs.json', 'r') as f:
        previous=json.loads(f.read())
        for i in jsonjob.keys():
            if i not in previous:
                diffe[i]=jsonjob[i]
except Exception as e:
    print(e)
    diffe=jsonjob
for i in diffe.keys():
    os.system("bash send.sh \"" + diffe[i].translate(str.maketrans({"-":  r"\-",
                                          "]":  r"\]",
                                          "\\": r"\\",
                                          "^":  r"\^",
                                          "$":  r"\$",
                                          "*":  r"\*",
                                          ".":  r"\.",
                                          "(":  r"\(",
                                          ")":  r"\)"})) + "\" \"" +i+"\"")
with open('jobs.json', 'w') as f:
        json.dump(jsonjob, f)

