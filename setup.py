"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_packages

setup(
    name="discmon",
    author="sarthak-py",
    author_email="shiva02939@gmail.com",
    url="https://github.com/sarthak-py/discmon",
    description="An (Unfinished) async API wrapper for https://pokeapi.co for Discord Bots ( can be used in any asyncio program )",
    version="0.1.0",
    packages=find_packages(where=".", exclude=["tests"]),
    keywords=["pokemon", "pokeapi", "pokecord"],
    install_requires=[
        "setuptools",
        "aiohttp",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
