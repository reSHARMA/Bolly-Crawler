from bs4 import BeautifulSoup
import urllib
for i in range(65,65+26):
	i = str(unichr(i))
	r = urllib.urlopen('http://en.wikipedia.org/wiki/List_of_Bollywood_films_of_2017');
	soup = BeautifulSoup(r,'html.parser')
	print(soup)

