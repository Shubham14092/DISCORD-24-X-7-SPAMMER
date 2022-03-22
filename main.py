from webserver import keep_alive
import requests

channelID = 947002540292198410
headers = {
    "authorization":
    "ODAyMTgwNDgxMTA1Nzg4OTcx.Yji-Kw.x6jC3NqqJ6cYijba98TKfD_UC3A"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
