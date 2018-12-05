import asyncio
import json
import requests
from bs4 import BeautifulSoup

async def scrappy():
    req = requests.get('https://www.meetup.com/gdgmanagua/')
    content = req.content
    soup = BeautifulSoup(content, "html.parser")
    data = soup.find_all("script", {"data-react-helmet":"true"})[1]
    return json.loads(data.text)

if __name__ == '__main__':
    asyncio.run(scrappy())