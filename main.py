import json

from sanic import Sanic
from sanic import response
import aiohttp
import requests
from bs4 import BeautifulSoup

app = Sanic(__name__)


async def scrappy(session):
    async with session as response:
        req = requests.get('https://www.meetup.com/gdgmanagua/')
        content = req.content
        soup = BeautifulSoup(content, 'html.parser')
        data = json.loads(soup.find_all('script', {'data-react-helmet': 'true'})[1].text)[0]
        return {
            'name': data['name'],
            'url': data['url'],
            'start_date': data['startDate'],
            'end_date': data['endDate'],
            'description': data['description'],
            'location': {
                'name': data['location']['name'],
                'lat': data['location']['geo']['latitude'],
                'lon': data['location']['geo']['longitude']
            }
        }


@app.route('/')
async def handle_request(request):
    async with aiohttp.ClientSession() as session:
        data = await scrappy(session)
        return response.json(
            data,
            headers={
                'Access-Control-Allow-Origin': '*'
            },
        )


if __name__ == '__main__':
        app.run(host="0.0.0.0", port=8000)