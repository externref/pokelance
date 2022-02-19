"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_packages

def long_description():
    with open("README.md") as fp:
        return fp.read()

setup(
    name="discmon",
    author="sarthak-py",
    author_email="shiva02939@gmail.com",
    url="https://github.com/sarthak-py/discmon",
    description="An async API wrapper for pokeapi.co",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    version="0.1.0.dev2",
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
