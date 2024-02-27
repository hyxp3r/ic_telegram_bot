import aiohttp
from bot.services.http import settings



async def send_verification_code(personal_number:str):
    params = {"personal_number":personal_number}
    async with aiohttp.ClientSession() as session:
        response = await session.get(
                                url = settings.send_code,
                                params = params)
    return response

async def verify_code(personal_number:str, verification_code:str):
    params = {
        "personal_number":personal_number,
        "verification_code": verification_code}
    async with aiohttp.ClientSession() as session:
        response = await session.get(
                                url = settings.verify_code,
                                params = params)
    return response