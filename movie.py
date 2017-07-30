from bs4 import BeautifulSoup
import urllib
f=open('movie.txt','w')
for i in range(65,65+26):
	i = str(unichr(i))
	r =  urllib.urlopen('http://www.bollywoodhungama.com/directory/movies-list/alphabet/'+i).read()
	soup = BeautifulSoup(r,'html.parser')
	page = int(soup.select('.dots + a')[0].string)
	for x in range(1,page):
		rr =  urllib.urlopen('http://www.bollywoodhungama.com/directory/movies-list/alphabet/'+i+'/page/'+str(x)).read()
		soupp = BeautifulSoup(rr,'html.parser')
		souppp = soupp.select('.directory--movie li a')
		for b in souppp:
			s = '\n'.join(b.attrs['title'].encode(encoding='UTF-8',errors='ignore'))
#			s = `'\n'.join(b.attrs[3])
f.write(s)
f.close()
