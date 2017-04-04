#! python3
# this script download every single xkcd comic.

import requests, os, bs4

url	= 'https://xkcd.com' #starting url
os.makedirs('xkcd', exist_ok=True) #store comics in ./xkcd
while not url.endswith('#'):
	#download the page.
	print('Downloading page %s...' %url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, "lxml")

	#find the url of the comic image
	comicElem = soup.select('#comic img')
	#print(type(comicElem[0].get('src')))
	if comicElem == []:
		print('Could not find comic image')
	else:
		comicUrl = comicElem[0].get('src')
		comicUrl = 'https:' + comicUrl
		print(comicUrl)
		#download the image.
		print('Downoading image %s....' %(comicUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()

		#save the image tp ./xkcd
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(10000):
			imageFile.write(chunk)
		imageFile.close()

	#get Prev button url
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'https://xkcd.com' + prevLink.get('href')
print("doneself.")
