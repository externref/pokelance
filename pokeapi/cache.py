from typing import Union, Optional

from .pokemon import Pokemon


class CacheImpl:
    """The class managing cache for the Client.

    Saving data from API into dictionaries based on categories .

    Parameters:
    -----------

        client: :class:`.Client`
        The Client class cache is based upon.

    Attributes:
    -----------

        pokemon_cache: :class:`dict`
        A dictionary of the Pokémon's cached data.

        sprite_cache: :class:`dict`
        A dictionary of Pokémon sprites saved.

    """

    def __init__(self, client) -> None:
        self.pokemon_cache_impl = {}
        self.sprites_cache_impl = {}
        self.client = client

    @property
    def pokemon_cache(self) -> dict:
        return self.pokemon_cache_impl

    @property
    def sprite_cache(self) -> dict:
        return self.sprites_cache_impl

    def get_pokemon(self, identity: Union[int, str]) -> Optional[dict]:
        return self.pokemon_cache.get(identity)

    def get_sprite_for(self, pokemon: Union[Pokemon, int, str]) -> Optional[dict]:
        if isinstance(pokemon, Pokemon):
            pokemon = pokemon.name
        return self.sprites_cache_impl.get(pokemon)
