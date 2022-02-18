from typing import Optional


class Sprite:
    """The sprites for the Pokémon Object."""

    def __init__(self, raw_data: dict):
        self.data = raw_data

    @property
    def raw(self) -> dict:
        return self.data

    @property
    def official_framework(self) -> Optional[str]:
        return (self.data["other"]["official-artwork"]).get("front_default")

    @property
    def front_default(self) -> Optional[str]:
        return self.data.get("front_default")

    @property
    def front_female(self) -> Optional[str]:
        return self.data.get("front_female")

    @property
    def front_shiny(self) -> Optional[str]:
        return self.data.get("front_shiny")

    @property
    def front_shiny_female(self) -> Optional[str]:
        return self.data.get("front_shiny_female")

    @property
    def back_default(self) -> Optional[str]:
        return self.data.get("back_default")

    @property
    def back_female(self) -> Optional[str]:
        return self.data.get("back_female")

    @property
    def back_shiny(self) -> Optional[str]:
        return self.data.get("back_shiny")

    @property
    def back_shiny_female(self) -> Optional[str]:
        return self.data.get("back_shiny_female")
