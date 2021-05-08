import requests
from bs4 import BeautifulSoup
import sys
from termcolor import colored, cprint


while True:
	try:
		texty = colored('#######made with love by v3nom <3########', 'blue')
		print(texty)
		text = colored('Enter the name of anime:', 'cyan')
		anime = input(text)
		ending = colored('press ctrl+c for exit', 'blue', attrs=['reverse', 'blink'])
		print(ending)
		url = ("https://www.anime-planet.com/anime/"+ anime)
		response = requests.get(url)
		resp = response.text

		soup = BeautifulSoup(resp, "html.parser")

		episode = soup.find(class_="pure-1 md 1-5")
		subepisode = soup.find("span").get_text()
		sub = colored('total number of episodes are', 'blue')
		print(f"{sub} :\t\n {subepisode}\n")


		year = soup.find(class_="iconYear").get_text()
		subyear = colored('year in which anime falls:', 'blue')
		print(f"{subyear}\t {year}\n")


		rating = soup.find(class_="avgRating")
		subrating = rating.find("span").get_text()
		subr = colored('ratings of viewers are:', 'blue')
		print(f"{subr}\t{subrating}")

		para = soup.find(class_="pure-1 md-3-5")
		subpara = para.find("p").get_text()
		subp = colored('About Anime:', 'blue')
		print(f"{subp}\n \t\t{subpara}\n")

		ptags = soup.find(class_="tags")
		subtags = ptags.find("ul").get_text()
		ptags = colored('The tags are:', 'blue')
		print(f"{ptags}\n{subtags}")
	except AttributeError:
		print('Anime not found')
	except KeyboardInterrupt:
		print('\nThnanx for using this little script')
		sys.exit()
