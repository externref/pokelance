from typing import Optional


class Sprite:
    """The sprites for the Pokémon Object."""

    def __init__(self, raw_data: dict):
        self.data = raw_data

    @property
    def raw(self) -> dict:
        """Raw :class:`dict` data of the sprite."""
        return self.data

    @property
    def official_artwork(self) -> Optional[str]:
        """Offical artwork from the Company """
        return (self.data["other"]["official-artwork"]).get("front_default")

    @property
    def front_default(self) -> Optional[str]:
        """The default front image of the Pokémon"""
        return self.data.get("front_default")

    @property
    def front_female(self) -> Optional[str]:
        """Default front image for female Pokémon"""
        return self.data.get("front_female")

    @property
    def front_shiny(self) -> Optional[str]:
        """Shiny Image for the Pokémon (front)"""
        return self.data.get("front_shiny")

    @property
    def front_shiny_female(self) -> Optional[str]:
        """Shiny Image for the Pokémon (female)"""
        return self.data.get("front_shiny_female")

    @property
    def back_default(self) -> Optional[str]:
        """Default back sprite for the Pokémon"""
        return self.data.get("back_default")

    @property
    def back_female(self) -> Optional[str]:
        """Back sprite for the Pokémon (female)"""
        return self.data.get("back_female")

    @property
    def back_shiny(self) -> Optional[str]:
        """Back sprite for the Pokémon ( shiny )"""
        return self.data.get("back_shiny")

    @property
    def back_shiny_female(self) -> Optional[str]:
        """Shiny Back female sprite for the Pokémon"""
        return self.data.get("back_shiny_female")
