# discmon

An async python API wrapper for [pokeapi.co](https://www.pokeapi.co) .

## Introduction

    import typing
    import asyncio

    import discmon

    client = discmon.Client(cache=True)

    async def pokemon_getter(identifier:typing.Union[int, str] = None):
        """Gets pokemon by name or ID, returns a random pokemon if identifier is None"""
        return await client.get_pokemon(identifier)

    asyncio.run(pokemon_getter())


