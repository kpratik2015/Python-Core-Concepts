import requests
from bs4 import BeautifulSoup
import re

url = input("Enter a movie to get the list of searches from IMDB.com : ")
url = url.replace(" ", "+").lower()

base_url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+url+'&s=tt'

imdb_r = requests.get(base_url) # response code

# print(imdb_r.status_code) # 200

imdb_soup = BeautifulSoup(imdb_r.text, 'html.parser')

# print(imdb_soup.prettify())
# print(imdb_soup.findAll('a'))

for link in imdb_soup.findAll('tr', class_="findResult"):
	searchObj = re.match(r'(.*)<td class="result_text"> <a href="/title/(.*)\/\?ref_=(.*)">(.*)</a>(.*)</td>',str(link), re.I)
	if searchObj:
		nestedSearchObj = re.match(r'(.*)\/\?ref_(.*)">(.*)</a>(.*)<br/>(.*)',searchObj.group(2), re.I)
		if nestedSearchObj:
			print(nestedSearchObj.group(3)+nestedSearchObj.group(4)+" : "+"http://www.imdb.com/title/"+nestedSearchObj.group(1)+"/")
		else:
			print(searchObj.group(4)+searchObj.group(5)+" : "+"http://www.imdb.com/title/"+searchObj.group(2)+"/")

	# print("----------------")
	# print(link)
	# print("----------------")
	# # print(link.get("href"))