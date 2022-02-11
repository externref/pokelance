from typing import Optional


class Sprite:
    def __init__(self, raw_data:dict):
        self.data = raw_data

    @property
    def raw(self) -> dict:
        return self.data
    
    @property
    def front_default(self) -> Optional[str]:
        return self.data.get('front_default')
    
    @property
    def front_female(self) -> Optional[str]:
        return self.data.get('front_female')

    @property
    def front_shiny(self) -> Optional[str]:
        return self.data.get('front_shiny')

    @property
    def back_default(self) -> Optional[str] :
        return self.data.get('back_default')

sprites= {
    "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png",
    "back_female": None,
    "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/132.png",
    "back_shiny_female": None,
    "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png",
    "front_female": None,
    "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/132.png",
    "front_shiny_female": None,}