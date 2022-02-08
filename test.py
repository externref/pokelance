import asyncio
from pokeapi import Client

client = Client()


async def main():
    pokemon = await client.get_pokemon("charmander")
    print(pokemon)


asyncio.run(main())
