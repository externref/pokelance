from typing import Union

import aiohttp

__all__ = (
    "PokelanceException",
    "PokemonNotFound",
    "ConnectionError",
    "CacheDisabled",
)


class PokelanceException(Exception):
    """Base Exception for all the errors raise by the wrapper."""

    ...


class PokemonNotFound(PokelanceException):
    """Raised when no Pokémon with the ID/name provided in :class:`Client.get_pokemon` is found.

    Attributes
    ----------
        identity: :class:`Union[int, str]`
            The argument supplied to get the Pokémon
    """

    identity: Union[int, str]

    def __init__(self, entry) -> None:
        super().__init__(
            'No Pokémon with name or ID "{}" was found. Check if you provided the correct arguments and the website is online.'.format(
                entry
            )
        )
        self.identity = entry


class ConnectionError(aiohttp.ClientConnectionError, PokelanceException):
    """Raised when the Client is unable to connect with the API."""

    def __init__(self) -> None:
        super().__init__(
            "Unable to connect to the API, make sure you have a stable internet connection."
        )


class CacheDisabled(PokelanceException):
    """Raised when user tries to access :class:`Client.cache` with cache options set to false."""

    def __init__(self) -> None:
        super().__init__("Cache is disable for the client.")
