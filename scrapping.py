import requests
from bs4 import BeautifulSoup

# a protest tuple has:
# (title, date, short description, protest link, image link)

def generate_posting_list(location):
	URL = "https://rallylist.com/?s=" + location.replace(" ", "+") + "&submit=Search"
	page = requests.get(URL)

	protest_html = page.content
	soup = BeautifulSoup(protest_html, "html.parser")

	results = soup.find(id="content-wrap")
	protest_elems = results.find_all("article", class_="entry")
	
	protests = []
	for protest_elem in protest_elems:

		protest_title = protest_elem.find("h2", class_= "entry-title")

		# checks to see if it's a real posting
		if (protest_title.text.strip() != "Submit" and protest_title.text.strip() != "Rally Alerts"):
			protest_date = protest_elem.find("div", class_="entry-byline-block entry-byline-tags")
			# this only gives the shortened description. more work needed for extended summary
			protest_description = protest_elem.find("div", class_="entry-summary")
			protest_image_link = protest_elem.find("img")['src']

			if None in (protest_title, protest_date, protest_description, protest_image_link):
				continue
		
			protest_link = protest_title.find("a")["href"]
			protest = protest_title.text.strip(), protest_date.text.strip()[8:], protest_description.text.strip()[:-11], protest_link, protest_image_link

			protests.append(protest)
	return protests
