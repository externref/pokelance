import typing
import asyncio

import pokelance

client = pokelance.Client(cache_data=True)


async def main(
    pokemon: typing.Union[int, str] = None
) -> typing.Optional[pokelance.Pokemon]:
    pokemon = await client.get_pokemon(pokemon)
    await client.close_client_session()
    return pokemon


pokemon = asyncio.run(main())
print(pokemon)
