from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
f=open('movie.txt','r')
movie = f.readLines()
for i in movie:
	r =  urllib.request.urlopen('www.bollywoodhungama.com/movie/'+i+'/cast/').read()
	soup = BeautifulSoup(r,'html.parser')
	
f.close()
