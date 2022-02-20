from lib2to3.pgen2.token import OP
import aiohttp
from typing import Union, Optional
from .pokemon import Pokemon
from .errors import PokemonNotFound, ConnectionError

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

__all__ = ('HTTPClient',)

class HTTPClient:
    async def fetch_pokemon_data(
        self, pokemon: Union[int, str] = None
    ) -> Optional[Pokemon]:

        req_url = f"{BASE_URL}{pokemon}"
        async with aiohttp.ClientSession() as session:

            try:
                response = await session.get(req_url)
            except aiohttp.ClientConnectionError:
                raise ConnectionError()

        if response.status == 404:
            raise PokemonNotFound(pokemon)

        data = await response.json()
        return data
