from typing import Any, Dict, Union, Optional

import aiohttp

from .errors import PokemonNotFound, ConnectionError

__all__ = ("HTTPClient",)

BASE_URL = "https://pokeapi.co/api/v2"


class HTTPClient:
    """
    Class which deals with all the Requests made to the API.
    """

    def __init__(self) -> None:
        self.session = aiohttp.ClientSession()

    async def fetch_pokemon_data(
        self, pokemon: Union[int, str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Getting a JSON response from API for the Pokémon ID provided
        """

        req_url = f"{BASE_URL}/pokemon/{pokemon}"
        try:
            response = await self.session.get(req_url)
        except aiohttp.ClientConnectionError:
            raise ConnectionError()

        if response.status == 404:
            raise PokemonNotFound(pokemon)

        data = await response.json()
        return data
