import requests
from bs4 import BeautifulSoup

class Protest:
	def __init__(self, title, date, description, link, img):
		self.title = title
		self.date = date
		self.description = description
		self.link = link
		self.img = img

	def __hash__(self):
		return hash(self.title)

	def __eq__(self, other):
		if self.title == other.title:
			return True
		else:
			return False


# generates a protests list containing all protests in a certain city/state
def generate_protests_list(location):
	URL = "https://rallylist.com/?s=" + location.replace(" ", "+") + "&submit=Search"
	page = requests.get(URL)

	protest_html = page.content
	soup = BeautifulSoup(protest_html, "html.parser")

	protests = []
	results = soup.find(id="content-wrap")

	try:
		protest_elems = results.find_all("article", class_="entry")
	except:
		return protests

	for protest_elem in protest_elems:

		protest_title = protest_elem.find("h2", class_= "entry-title")

		try:
			protest_date = protest_elem.find("div", class_="entry-byline-block entry-byline-tags")
			# this only gives the shortened description. more work needed for extended summary
			protest_description = protest_elem.find("div", class_="entry-summary")
			protest_image_link = protest_elem.find("img")['src']

			if None in (protest_title, protest_date, protest_description, protest_image_link):
				continue
		
			protest_link = protest_title.find("a")["href"]
			protest = Protest(protest_title.text.strip(), protest_date.text.strip()[8:], protest_description.text.strip()[:-11], protest_link, protest_image_link)

			protests.append(protest)
		except:
			pass

	return protests

state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
for state in state_names:
	generate_protests_list(state)