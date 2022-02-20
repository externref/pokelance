from .sprites import Sprite


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
            Pokemon Order
    """

    id: int
    name: str
    height: int
    weight: int
    order: int

    def __init__(self, client, data: dict) -> None:
        self.data = data
        self._client = client
        self.add_basic_attrs(data)

    def __str__(self) -> str:
        return self.name

    @property
    def raw(self) -> dict:
        """The raw JSON data about the Pokémon got from the API's response"""
        return self.data

    def add_basic_attrs(self, data) -> None:
        self.name = data["name"]
        self.id = data["id"]
        self.height = data["height"]
        self.weight = data["weight"]
        self.order = data["order"]

    @property
    def sprites(self) -> Sprite:
        """:class:`.Sprite` object for the Pokémon with properties for URLs"""
        return Sprite(self.data["sprites"])
