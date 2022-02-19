# Getting Started

[![PyPI](https://img.shields.io/pypi/v/discmon)](https://pypi.org/project/discmon/)

## Installation
```bash
$python -m pip install discmon
```
The PYPI version is not as updated as the current git branch so you may consider installing the library from git instead.
```bash
$python -m pip install git+https://github.com/sarthak-py/discmon
```
## Example
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