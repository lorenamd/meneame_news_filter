
import urllib2
from bs4 import BeautifulSoup
import webbrowser
import unidecode

myFile = open('to_read.html', 'w')

total_stories = 0  # Start counting the number of stories to write

def read_and_select (quote_page): 
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')

	all_stories = {}

	stories = soup.find_all("div", attrs={"class": "news-body"})

	for i in range(len(stories)):
		title = stories[i].find("h2").text
		summary = stories[i].find("div", attrs={"class": "news-content"}).text
		url = stories[i].find("h2").contents[1].get('href')

		all_stories[i] = {"title":title, "summary":summary, "url":url}

	with open("words.txt") as f:
	    content = f.readlines()

	words = [unidecode.unidecode(x.decode('utf-8').lower().strip()) for x in content] 

	for i in range(len(all_stories)):
		title_lower_case = unidecode.unidecode(all_stories[i]["title"].lower())

		count = 0
		for word in words:
			if word in title_lower_case:
				count += 1
		if count == 0:
			global total_stories
			total_stories +=1
			default = "none"
			title = all_stories[i].get('title', default).encode('utf-8')
			summary = all_stories[i].get('summary', default).encode('utf-8')
			url = all_stories[i].get('url', default).encode('utf-8')
			
			myFile.write('<strong style = "font-size:20px">')
			myFile.write(title) 
			myFile.write('</strong>')
			myFile.write('<br>')
			myFile.write(summary)
			myFile.write('<br>')
			myFile.write('<a href="url">')
			myFile.write(url)
			myFile.write('</a>')
			myFile.write('<br><br><br><br>')


# Build the page
myFile.write('<html>')
myFile.write('<body style="margin:30px">')
myFile.write('<p>')
read_and_select("https://www.meneame.net")
read_and_select("https://www.meneame.net/?page=2")
read_and_select("https://www.meneame.net/?page=3")
read_and_select("https://www.meneame.net/?page=4")
myFile.write('<strong style = "font-size:20px">')
myFile.write(str(total_stories))
myFile.write(" stories of 100")
myFile.write('</strong>')
myFile.write('</p>')
myFile.write('</body>')
myFile.write('</html>')

myFile.close()


meneame = 'to_read.html'
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
webbrowser.get(chrome_path).open(meneame)




