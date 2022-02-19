import hikari 
import discmon

bot = hikari.GatewayBot(token='TOKEN')
discmon_client= discmon.Client(cache_data=True)

@bot.listen()
async def message(event: hikari.MessageCreateEvent):
    if event.message.content.startswith('!pokemon'):
        pokemon_id = [arg for arg in event.message.content.split() if arg != ' '][1]
        pokemon = await discmon_client.get_pokemon(pokemon_id)
        discmon_client.save_cache()
        await event.message.respond(f"Pokemon with ID {pokemon_id} is {pokemon.name}")

bot.run()
      