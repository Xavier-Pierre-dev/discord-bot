from discord_webhook import DiscordWebhook, DiscordEmbed

# create an embed message and send to your discord channel

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/961263992460935178/d3D88lbXZEt6WivuGwRAhH0n6KfIrYaUP4kHJ5TPTQfmFpTmPhf9dIFZEk4NWEMrKtd6"
                         , avatar_url="")

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