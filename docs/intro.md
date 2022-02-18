# Introduction

```py
# test.py
import typing
import asyncio

import discmon

client = discmon.Client(cache=True)

async def main(pokemon: typing.Union[int, str] = None) -> typing.Optional[discmon.Pokemon]:
    pokemon = await client.get_pokemon(pokemon)
    return pokemon

pokemon= asyncio.run(main()) 
print(pokemon)
```

```bash
$python test.py
makuhita
```