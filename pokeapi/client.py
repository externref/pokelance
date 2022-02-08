import aiohttp
import random
import typing
import asyncio
from .pokemon import Pokemon

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


class Client:
    def __init__(self) -> None:
        self.cache = {} # url : res format


    async def get_pokemon(self, pokemon: typing.Union[int, str] = None) -> Pokemon:
        """
        This method is used to get a `Pokemon` object either from the cache or the API
        """
        if not pokemon:
            pokemon = random.randint(1, 500)
        req_url = f"{BASE_URL}{pokemon}"
        cached_data =self.cache.get(req_url)
        if cached_data : return cached_data
        async with aiohttp.ClientSession() as session:
            try : 
                response = await session.get(req_url)
            except asyncio.TimeoutError:
                raise asyncio.TimeoutError('Unable to connect to the API (https://pokeapi.co/)')
        if response.status == 404:
            raise 
        data = await  response.json()
        self.cache[req_url] = data
        return Pokemon(data)
