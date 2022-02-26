from typing import Any, Union, Optional, Dict

from .sprites import Sprite
from .pokemon import Pokemon

__all__ = ("Cache",)


class Cache:
    """The class managing cache for the Client.

    Saving data from API into dictionaries based on categories .

    Parameters
    ----------

        client: :class:`.Client`
            The Client class cache is based upon.
    """

    def __init__(self, client) -> None:
        self._pokemon_cache_data: Dict[str, Any] = {}
        self._sprites_cache_data: Dict[str, Union[str, Dict]] = {}
        self.client = client

    @property
    def pokemon_cache(self) -> Dict[str, Any]:
        """Returns all the cached data about pokémons in a dictionary form."""
        return self._pokemon_cache_data

    @property
    def sprite_cache(self) -> Dict[str, Union[str, Dict]]:
        """Returns all the cached sprite data in a dictionary form."""
        return self._sprites_cache_data

    def get_pokemon(self, identity: Union[int, str]) -> Optional[Pokemon]:
        """Get's the cached :class:`.Pokemon` for the `identity` entered."""
        return (
            Pokemon(self.client, self.pokemon_cache.get(str(identity)))
            if self.pokemon_cache.get(str(identity))
            else None
        )

    def get_sprite_for(self, pokemon: Union[Pokemon, int, str]) -> Optional[Sprite]:
        """Get's the cached :class:`.Sprite` for the pokemon entered."""
        if isinstance(pokemon, Pokemon):
            pokemon = pokemon.name
        return (
            Sprite(self._sprites_cache_data.get(str(pokemon)))
            if self._sprites_cache_data.get(str(pokemon))
            else None
        )
