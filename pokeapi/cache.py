from typing import Union, Optional 

class CacheImpl:
    def __init__(self, client) -> None:
        self.pokemon_cache_impl = {}
        self.client = client 
    
    @property
    def pokemon_cache(self) -> dict :
        return self.pokemon_cache_impl
    
    def get_pokemon(self, identity:Union[int, str] )->Optional[dict]:
        return self.pokemon_cache.get(identity)

        