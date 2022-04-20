from discord_webhook import DiscordWebhook, DiscordEmbed
import os
from dotenv import load_dotenv, find_dotenv

# create an embed message and send to your discord channel
load_dotenv(find_dotenv())
URL_WEBHOOK = os.getenv("URL_WEBHOOK")
webhook = DiscordWebhook(url=URL_WEBHOOK, avatar_url="")

embed = DiscordEmbed(title="Title of your embed message", color=242424)
embed.set_author(name="author name", url="", icon_url="")
embed.set_footer(text="please subscribe")
embed.set_timestamp()
embed.add_embed_field(name="field description 1", value="value field 1")
embed.add_embed_field(name="field description 2", value="value field 2")
embed.set_image(url="")
embed.set_thumbnail(url="")

webhook.add_embed(embed=embed)
webhook.execute()