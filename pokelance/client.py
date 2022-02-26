import json
import random
from typing import Union, Optional


from .cache import Cache
from .sprites import Sprite
from .http import HTTPClient
from .pokemon import Pokemon
from .errors import CacheDisabled

__all__ = ("Client",)


class Client:
    """The Client class with all the methods related to Base API.

    This class is made to define an object which would send requests and receive raw data from the API.

    Parameters
    -----------
        cache_data: :class:`bool`
            A bool identifying if the Client should cache the response from URLs on every API request or not.
    """

    def __init__(self, cache_data: bool = True) -> None:
        self.http = HTTPClient()
        self._cache = Cache(self) if cache_data else None

    def _update_cache(self, data: dict) -> None:
        self._cache.pokemon_cache[data["id"]] = data
        self._cache.pokemon_cache[data["name"]] = data
        self._cache.sprite_cache[data["id"]] = data["sprites"]
        self._cache.sprite_cache[data["name"]] = data["sprites"]

    async def close_client_session(self) -> None:
        """Closes the current :class:`.Client` session."""
        await self.http.session.close()

    @property
    def cache(self) -> Optional[Cache]:
        """Returns the :class:`.Cache` object for the :class:`.Client` if cache is enabled"""
        if not self._cache:
            raise CacheDisabled()
        return self._cache

    def save_pokemon_cache(self) -> None:
        """Save all the cached Pokémon data into a JSON file named `cached_pokemons.json`"""
        cached_data = self.cache
        with open("cached_pokemons.json", "w") as cachefile:
            json.dump(cached_data._pokemon_cache_data, cachefile)

    def load_pokemon_cache(self) -> None:
        cached_data = self.cache
        with open("cached_pokemons.json", "r") as cachefile:
            data = json.load(cachefile)
            cached_data._pokemon_cache_data.update(data)

    async def get_pokemon(self, pokemon: Union[int, str] = None) -> Pokemon:
        """A method used to get the Pokémon.

        This method is used to get a :class:`Pokemon` object either from the cache or the API.

        Parameters
        ----------

        pokemon: :class:`Union[int, str]`
            The id or name of the Pokémon to get data about.
            Gets a random Pokemon if no value is provided.

        Returns
        -------

        :class:`Pokemon`
        """

        if not pokemon:
            pokemon = random.randint(1, 700)
        if self._cache is not None:
            cached_data = self._cache.pokemon_cache.get(str(pokemon))
            if cached_data:
                return Pokemon(self, cached_data)

        data = await self.http.fetch_pokemon_data(pokemon)

        if self._cache:
            self._update_cache(data)

        return Pokemon(self, data)

    async def get_sprite_for(self, pokemon: Union[Pokemon, int, str]) -> Sprite:
        if isinstance(pokemon, Pokemon):
            pokemon = pokemon.name

        if self._cache is not None:
            cached_data = self._cache.sprite_cache.get(str(pokemon))
            return Sprite(cached_data)

        data = await self.http.fetch_pokemon_data(pokemon)

        if self._cache:
            self._update_cache(data)

        return Sprite(data["sprites"])
