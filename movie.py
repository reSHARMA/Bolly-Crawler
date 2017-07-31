from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
f=open('movie.txt','w')
s = ''
for i in range(65,65+26):
    i = str(chr(i))
    r =  urllib.request.urlopen('http://www.bollywoodhungama.com/directory/movies-list/alphabet/'+i).read()
    soup = BeautifulSoup(r,'html.parser',from_encoding='utf-8')
    page = int(soup.select('.dots + a')[0].string)
    for x in range(1,page):
        rr =  urllib.request.urlopen('http://www.bollywoodhungama.com/directory/movies-list/alphabet/'+i+'/page/'+str(x)).read()
        soupp = BeautifulSoup(rr,'html.parser')
        souppp = soupp.select('.directory--movie li a')
        for b in souppp:
            s =  str(b.attrs['title'].encode(encoding='utf-8',errors='ignore'))[2:-1]
            year = s.split()[-1]
            s=s[:-5].lower().replace(' ','-')
           # print(s)
            if(int(year)>=2004):
                #f.write(s)
                try: 
                    b1=urllib.request.urlopen('http://www.bollywoodhungama.com/movie/'+s+'/box-office/').read()
                    bud=BeautifulSoup(b1,'html.parser')
                    budd=bud.select('.bh-movie-box-office .lifetime')
                #budget=budd.find_all("td")
                    try:
                        f.write(s+' '+budd[1].text+'\n')
                    except:
                        pass
                except:
                    pass
                
f.close()
