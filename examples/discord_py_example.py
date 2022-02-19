import discmon
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
discmon_client = discmon.Client(cache_data=True)


@bot.command()
async def pokemon(ctx: commands.Context, pokemon_id: int) -> None:
    pokemon = await discmon_client.get_pokemon(pokemon_id)
    discmon_client.save_cache()
    await ctx.send(f"Pokemon with ID {pokemon_id} is {pokemon.name}")


bot.run("TOKEN")
