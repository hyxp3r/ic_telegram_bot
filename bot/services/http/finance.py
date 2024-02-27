import aiohttp
from aiohttp.client import _RequestContextManager

from bot.services.http import settings


async def get_finance(api_key:str):
    headers = {
        "Authorization": f"Bearer {api_key}",
        }
    async with aiohttp.ClientSession(headers=headers) as session:
        response = await session.get(url = settings.check_finance)
    return response