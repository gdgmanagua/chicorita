import aiohttp
import asyncio
import json
import requests
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrappy():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://www.meetup.com/gdgmanagua/')
        req = requests.get('https://www.meetup.com/gdgmanagua/')
        content = req.content
        soup = BeautifulSoup(content, "html.parser")
        data = soup.find_all("script", {"data-react-helmet":"true"})[1]
        return json.loads(data.text)

loop = asyncio.get_event_loop()
loop.run_until_complete(scrappy())
