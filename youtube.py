import json
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
f=open("trailer.txt",'a')
#f1=open("all_data.json",'a')
lines = (line.rstrip('\n') for line in open("movie1.txt"))
s = ''
count=0
for line in lines:
        try:
     
            line=line.replace(' ','+').replace('<U+0096>','')
            print(line)
            url="https://www.youtube.com/results?sp=EgIQAVAU&q="+line+"+trailer"
            print(url) 
            response = urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html)
            soup1=soup.findAll(attrs={'class':'yt-lockup-meta-info'})[0].text[11:-5].replace(',','').replace('o','').replace('g','')
            if(len(soup1)==0):
                    f.write('null\n')
                    count=count+1
            else:
                    print(soup1)
                    f.write(soup1+'\n')
                    count=count+1
        except:
                f.write('null\n')

print(count)
f.close()

