from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
f=open('movie.txt','w')
s = ''
for i in range(65,65+26):
	i = str(chr(i))
	r =  urllib.request.urlopen('http://www.bollywoodhungama.com/directory/movies-list/alphabet/'+i).read()
	soup = BeautifulSoup(r,'html.parser')
	page = int(soup.select('.dots + a')[0].string)
	for x in range(1,page):
		rr =  urllib.request.urlopen('http://www.bollywoodhungama.com/directory/movies-list/alphabet/'+i+'/page/'+str(x)).read()
		soupp = BeautifulSoup(rr,'html.parser')
		souppp = soupp.select('.directory--movie li a')
		for b in souppp:
			s =  str(b.attrs['title'].encode(encoding='UTF-8',errors='ignore')) + '\n'
#			s = `'\n'.join(b.attrs[3])
			f.write(s)
#f.write(s)
f.close()
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
            s =  str(b.attrs['title'].encode(encoding='ascii',errors='ignore')) + '\n'
            year = s.split()[-1].rstrip("'")
            if(int(year)>=2004):
                f.write(s)
#f.write(s)
f.close()
