import asyncio
import aiohttp

class PokeAPIException(Exception):
    ...

class PokemonNotFound(PokeAPIException):
    def __init__(self, entry) -> None:
        super().__init__("No Pokémon with name or ID \"{}\" was found. Check if your provided the correct arguments and the website is online.".format(entry))

class ConnectionError(aiohttp.ClientConnectionError, PokeAPIException):
    def __init__(self) ->None:
        super() .__init__('Unable to connect to the API, make sure you have a stable internet connection.')   