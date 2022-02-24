from typing import Any, Optional, Dict

__all__ = ("Sprite", "DreamWorldSprite")


class DreamWorldSprite:
    """Dream world sprites for Pokémon

    Attributes
    ----------
        front_default: :class:`Optional[str]`
            The default front dream world image of the Pokémon.

        front_female: :class:`Optional[str]`
            The default front dream world image of the Pokémon (female).
    """

    front_default: Optional[str]
    front_female: Optional[str]

    def __init__(self, data: Dict[str, Optional[str]]) -> None:
        self.front_default = data["front_default"]
        self.front_female = data["front_female"]


class HomeSprite:
    """ """


class Sprite:
    """The sprites for the Pokémon Object.

    Attributes
    ----------
        front_default: :class:`Optional[str]`
            The default front image of the Pokémon.

        back_default: :class:`Optional[str]`
            Default back sprite for the Pokémon.

        front_female: :class:`Optional[str]`
            Default front image for female Pokémon.

        back_female: :class:`Optional[str]`
            Back sprite for the Pokémon (female).

        front_shiny: :class:`Optional[str]`
            Shiny Image for the Pokémon (front).

        back_shiny: :class:`Optional[str]`
            Back sprite for the Pokémon (shiny).

        front_shiny_female: :class:`Optional[str]`
            Shiny Image for the Pokémon (female).

        back_shiny_female: :class:`Optional[str]`
            Shiny Back sprite for the Pokémon (female).

    """

    front_default: Optional[str]
    back_default: Optional[str]
    front_female: Optional[str]
    back_female: Optional[str]
    front_shiny: Optional[str]
    back_shiny: Optional[str]
    front_shiny_female: Optional[str]
    back_shiny_female: Optional[str]

    def __init__(self, raw_data: Dict[str, Any]) -> None:
        self.data = raw_data
        self.initalise_base_sprites()

    def initalise_base_sprites(self) -> None:
        self.front_default = self.data["front_default"]
        self.back_default = self.data["back_default"]
        self.front_female = self.data["front_female"]
        self.back_female = self.data["back_female"]
        self.front_shiny = self.data["front_shiny"]
        self.back_shiny = self.data["back_shiny"]
        self.front_shiny_female = self.data["front_shiny_female"]
        self.back_shiny_female = self.data["back_shiny_female"]

    @property
    def raw(self) -> Dict[str, Any]:
        """Raw :class:`dict` data of the sprite."""
        return self.data

    @property
    def official_artwork(self) -> Optional[str]:
        """Official artwork from the Company"""
        return (self.data["other"]["official-artwork"]).get("front_default")

    @property
    def dream_world(self) -> DreamWorldSprite:
        """:class:`.DreamWorldSprite` category for the Pokémon's sprites"""
        return DreamWorldSprite(self.data.get("dream_world"))
