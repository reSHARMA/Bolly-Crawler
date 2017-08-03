from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
f=open('movie.txt','w')
for i in range(65,65+27):
	temp = i
	if(temp != 91):
		i = str(chr(i))
	else:
		i = "NUM"
	r =  urllib.request.urlopen('http://www.bollywoodhungama.com/directory/movies-list/alphabet/'+i).read()
	soup = BeautifulSoup(r,'html.parser')
	page = 1
	try:
		temp = int(soup.select('.page-numbers')[-2].text)
		page = temp
	except:
		print("index error")
	page = page + 1
	for x in range(1,page):
		rr =  urllib.request.urlopen('http://www.bollywoodhungama.com/directory/movies-list/alphabet/'+i+'/page/'+str(x)).read()
		soupp = BeautifulSoup(rr,'html.parser')
		souppp = soupp.select('.directory--movie li a')
		for b in souppp:
			s =  str(b.attrs['title'].encode(encoding='UTF-8',errors='ignore')) + '\n'
			print(s)
			f.write(s)
f.close()
