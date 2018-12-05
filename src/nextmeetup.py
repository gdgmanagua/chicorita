import requests, re, json
from bs4 import BeautifulSoup

req = requests.get("https://www.meetup.com/gdgmanagua/")
content = req.content

soup = BeautifulSoup(content, "html.parser")

relevant = soup.find_all("script", {"data-react-helmet":"true"})[1]

tags = re.findall('"([^"]*)"', str(relevant))

d = {}

d['name'] = tags[7]
d['url'] = tags[9]
d['startDate'] = tags[13]
d['endDate'] = tags[15]
d['place'] = tags[20]
d['address'] = tags[25]
d['city'] = tags[27]

json_file = json.dumps(d)
