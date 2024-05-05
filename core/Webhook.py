import json
from discord_webhook import DiscordWebhook, DiscordEmbed

def SendWebhook(url,embed):
    # set webhook url
    webhook = DiscordWebhook(url=url)
    webhook.add_embed(embed)
    response = webhook.execute()

    return(response.json()['id'])

def SendWebhookn(url, message):
    # Set webhook url
    webhook = DiscordWebhook(url=url, content=message)
    response = webhook.execute()
def EditWebhook(url,id,embed):
    webhook = DiscordWebhook(url=url, id=id)
    webhook.add_embed(embed)
    response = webhook.edit()