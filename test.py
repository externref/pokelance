import asyncio
from discmon import Client, Pokemon

client = Client()


async def main():
    pokemon: Pokemon = await client.get_pokemon("charmander")
    print(client.cache.pokemon_cache.keys())


asyncio.run(main())
