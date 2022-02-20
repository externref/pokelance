import hikari
import pokelance

bot = hikari.GatewayBot(token="TOKEN")
pokelance_client = pokelance.Client(cache_data=True)


@bot.listen()
async def message(event: hikari.MessageCreateEvent):
    if event.message.content.startswith("!pokemon"):
        pokemon_id = [arg for arg in event.message.content.split() if arg != " "][1]
        pokemon = await pokelance_client.get_pokemon(pokemon_id)
        pokelance_client.save_cache()
        await event.message.respond(f"Pokemon with ID {pokemon_id} is {pokemon.name}")


bot.run()
