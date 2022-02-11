import random
import asyncio
from typing import Union

import aiohttp

from.cache import CacheImpl
from.pokemon import Pokemon
from.errors import PokemonNotFound, ConnectionError

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


class Client:
    """The Client class with all the methods related to Base API.

    This class is made to define a object which would send requests and recieve raw data from the API.
    
    Parameters:
    -----------

    cache: :class:`bool`
        A bool identifying if the Client should cache response from urls on every API requests or not.
        True will cache the data, False won't (defaulted to True).
    
    Attributes:
    -----------

    cache: :class:`CacheImpl`
        The cache class with all the cached data.
    
    """
    def __init__(self , cache : bool=True) -> None:
        self.cache = None
        if cache:
            self.cache = CacheImpl(self)

    async def get_pokemon(self, pokemon: Union[int, str] = None) -> Pokemon:
        """A method used to get the Pokémon.

        This method is used to get a `Pokemon` object either from the cache or the API.

        Parameters:
        -----------

        pokemon: :class:`Union[int, str]`
            The id or name of the Pokémon to get data of.
            Gets a random Pokemon if no value provided
        
        Returns:
        --------

        :class:`Pokemon` 
        """

        if not pokemon:
            pokemon = random.randint(1, 500)
        req_url = f"{BASE_URL}{pokemon}"
        cached_data = self.cache.pokemon_cache.get(pokemon)
        if cached_data:
            return cached_data

        async with aiohttp.ClientSession() as session:

            try:
                response = await session.get(req_url)
            except aiohttp.ClientConnectionError:
                raise ConnectionError()

        if response.status == 404:
            raise PokemonNotFound(pokemon)

        data = await response.json()
        self.cache.pokemon_cache[data['id']] = data
        self.cache.pokemon_cache[data['name']] = data

        return Pokemon(self, data)
