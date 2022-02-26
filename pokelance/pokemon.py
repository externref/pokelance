from .sprites import Sprite

__all__ = ("Pokemon",)


class Pokemon:
    """Class for a Pokémon with most of the information about the Pokémons available as an attribute.
    Complete info can be accessed with :class:`Pokemon.raw` as a dictionary ( JSON response from the API ).

    Attributes
    ----------
        id: :class:`int`
            ID of the Pokémon
        name: :class:`str`
            Name of the Pokémon
        height: :class:`int`
            Height of the Pokémon
        weight: :class:`int`
            Weight of the Pokémon
        order: :class:`int`
            Pokémon Order
        is_default: :class:`bool`
            Is the Pokémon a default one
    """

    id: int
    name: str
    height: int
    weight: int
    order: int
    is_default: bool

    def __init__(self, client, data: dict) -> None:
        self.data = data
        self._client = client
        self._add_basic_attrs(data)

    def __str__(self) -> str:
        return self.name

    @property
    def raw(self) -> dict:
        """The raw JSON data about the Pokémon got from the API's response"""
        return self.data

    def _add_basic_attrs(self, data) -> None:
        self.name = data["name"]
        self.id = data["id"]
        self.height = data["height"]
        self.weight = data["weight"]
        self.order = data["order"]
        self.is_default = data["is_default"]

    @property
    def sprites(self) -> Sprite:
        """:class:`.Sprite` object for the Pokémon with properties for URLs"""
        return Sprite(self.data["sprites"])
