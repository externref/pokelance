# pokelance
An asynchronous API wrapper for https://pokeapi.co/ (Unfinished)

[![](https://readthedocs.org/projects/pokelance/badge/?version=latest)](https://pokelance.readthedocs.io/en/latest/)
[![PyPI](https://img.shields.io/pypi/v/pokelance)](https://pypi.org/project/pokelance/)

## INSTALLATION
```bash
$python -m pip install pokelance
```
The PYPI version is not as updated as the current git branch so you may consider installing the library from git instead.
```bash
$python -m pip install git+https://github.com/sarthak-py/pokelance
```

## EXAMPLE
```py
#test.py 
import typing
import asyncio

import pokelance

client = pokelance.Client(cache_data=True)

async def main(pokemon: typing.Union[int, str] = None) -> typing.Optional[pokelance.Pokemon]:
    pokemon = await client.get_pokemon(pokemon)
    return pokemon

pokemon= asyncio.run(main()) 
print(pokemon)
```

```bash
$python test.py
makuhita
```

## NEED HELP?
Docs : https://pokelance.readthedocs.io/en/latest/

Discord Server : *soon*
