from typing import Union, Optional

from .sprites import Sprite
from .pokemon import Pokemon

__all__ = ("CacheImpl",)


class CacheImpl:
    """The class managing cache for the Client.

    Saving data from API into dictionaries based on categories .

    Parameters
    ----------

        client: :class:`.Client`
            The Client class cache is based upon.
    """

    def __init__(self, client) -> None:
        self.pokemon_cache_impl = {}
        self.sprites_cache_impl = {}
        self.client = client

    @property
    def pokemon_cache(self) -> dict:
        """Returns all the cached data about pokémons in a dictionary form."""
        return self.pokemon_cache_impl

    @property
    def sprite_cache(self) -> dict:
        """Returns all the cached sprite data in a dictionary form."""
        return self.sprites_cache_impl

    def get_pokemon(self, identity: Union[int, str]) -> Optional[dict]:
        """Get's the cached :class:`dict` for the `identity` entered."""
        return self.pokemon_cache.get(identity)

    def get_sprite_for(self, pokemon: Union[Pokemon, int, str]) -> Optional[dict]:
        """Get's the cached :class:`dict` for the `identity` entered."""
        if isinstance(pokemon, Pokemon):
            pokemon = pokemon.name
        return self.sprites_cache_impl.get(pokemon)
