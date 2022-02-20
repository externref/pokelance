"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_packages


def long_description():
    with open("README.md") as fp:
        return fp.read()


version = __import__("pokelance.__init__").__version__
setup(
    name="pokelance",
    author="sarthak-py",
    author_email="shiva02939@gmail.com",
    url="https://github.com/sarthak-py/pokelance",
    description="An async API wrapper for pokeapi.co",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    version=version,
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
