import pokelance
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
pokelance_client = pokelance.Client(cache_data=True)


@bot.command()
async def pokemon(ctx: commands.Context, pokemon_id: int) -> None:
    pokemon = await pokelance_client.get_pokemon(pokemon_id)
    pokelance_client.save_cache()
    await ctx.send(f"Pokemon with ID {pokemon_id} is {pokemon.name}")

@bot.event
async def on_disconnect():
    await pokelance_client.close_client_session()
    
bot.run("TOKEN")
