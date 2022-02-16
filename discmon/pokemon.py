from .sprites import Sprite


class Pokemon:
    """
    Class for a Pokémon with most of the information about the Pokémons avaiable as an attribute.
    Complete info can be accessed with `Pokemon.raw` as an dictionary ( json response from the API ).
    """

    def __init__(self, client, data: dict) -> None:
        self.data = data
        self._client = client

    def __str__(self) -> str:
        return self.name

    @property
    def raw(self) -> dict:
        """The raw json data about the Pokémon got from the API's response"""
        return self.data

    @property
    def id(self) -> int:
        """The ID of the Pokémon"""
        return self.data["id"]

    @property
    def name(self) -> str:
        """Name of the Pokémon"""
        return self.data["name"]

    @property
    def sprites(self) -> Sprite:
        """`Sprite` object for the Pokémon with properites for urls"""
        return Sprite(self.data["sprites"])
