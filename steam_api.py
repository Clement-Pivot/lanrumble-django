import urllib.request, urllib.error, json, time, os
from dotenv import load_dotenv

load_dotenv()

multiplayer = {"id": 1, "description": "Multi-player"}
coop = {"id": 9, "description": "Co-op"}

content = urllib.request.urlopen(
    f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={os.environ['STEAM_API_KEY']}&format=json&steamid={os.environ['STEAM_USER_ID']}"
).read()
data = json.loads(content)

game_list = list(map(lambda game: game["appid"], data["response"]["games"]))

try:
    with open("multi", "r") as f:
        multiplayer_games = json.loads(f.read())
except IOError:
    multiplayer_games = []

try:
    with open("solo", "r") as f:
        solo_games = json.loads(f.read())
except IOError:
    solo_games = []

try:
    with open("unknown", "r") as f:
        unknown_games = json.loads(f.read())
except IOError:
    unknown_games = []

i = 0
max = len(game_list) - len(unknown_games) - len(multiplayer_games) - len(solo_games)

for app_id in game_list:
    if (
        app_id not in unknown_games
        and app_id not in list(map(lambda x: x["id"], multiplayer_games))
        and app_id not in list(map(lambda x: x["id"], solo_games))
    ):
        try:
            content = urllib.request.urlopen(
                f"https://store.steampowered.com/api/appdetails?appids={app_id}"
            ).read()
            data = json.loads(content)
            try:
                if multiplayer in data[f"{app_id}"]["data"]["categories"]:
                    print(
                        f"{i}/{max} : {app_id} MULTI => "
                        + data[f"{app_id}"]["data"]["name"]
                    )
                    multiplayer_games.append(
                        {"id": app_id, "name": data[f"{app_id}"]["data"]["name"]}
                    )
                else:
                    solo_games.append(
                        {"id": app_id, "name": data[f"{app_id}"]["data"]["name"]}
                    )
                    print(
                        f"{i}/{max} : {app_id} SOLO => "
                        + data[f"{app_id}"]["data"]["name"]
                    )
            except KeyError:
                print("Error game not found!")
                unknown_games.append(app_id)
        except urllib.error.HTTPError:
            print("HTTP Error")
            time.sleep(60)
            i -= 1
        i += 1
        if i >= 100:
            break

with open("multi", "w") as f:
    f.write(json.dumps(multiplayer_games))

with open("solo", "w") as f:
    f.write(json.dumps(solo_games))

with open("unknown", "w") as f:
    f.write(json.dumps(unknown_games))
