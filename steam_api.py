import urllib.request, urllib.error, json, time, os
from dotenv import load_dotenv


class SteamApi:
    multiplayer_tag = {"id": 1, "description": "Multi-player"}
    coop_tag = {"id": 9, "description": "Co-op"}
    multiplayer_games = []
    solo_games = []
    unknown_games = []

    def __init__(self):
        load_dotenv()
        self.load()

    def load(self):
        try:
            with open("multi", "r") as f:
                self.multiplayer_games = json.loads(f.read())
        except IOError:
            self.multiplayer_games = []

        try:
            with open("solo", "r") as f:
                self.solo_games = json.loads(f.read())
        except IOError:
            self.solo_games = []

        try:
            with open("unknown", "r") as f:
                self.unknown_games = json.loads(f.read())
        except IOError:
            self.unknown_games = []

    def fetch_user(self, user_id):
        content = urllib.request.urlopen(
            f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={os.environ['STEAM_API_KEY']}&format=json&steamid={user_id}"
        ).read()
        data = json.loads(content)

        game_list = list(map(lambda game: game["appid"], data["response"]["games"]))

        for app_id in game_list:
            if (
                app_id not in self.unknown_games
                and app_id not in list(map(lambda x: x["id"], self.multiplayer_games))
                and app_id not in list(map(lambda x: x["id"], self.solo_games))
            ):
                try:
                    self.fetch_game(app_id)
                except urllib.error.HTTPError:
                    print("HTTP Error")
                    time.sleep(60)

    def fetch_game_by_id(self, app_id):
        content = urllib.request.urlopen(
            f"https://store.steampowered.com/api/appdetails?appids={app_id}"
        ).read()
        data = json.loads(content)
        try:
            if self.multiplayer_tag in data[f"{app_id}"]["data"]["categories"]:
                self.multiplayer_games.append(
                    {
                        "id": app_id,
                        "name": data[f"{app_id}"]["data"]["name"],
                    }
                )
            else:
                self.solo_games.append(
                    {
                        "id": app_id,
                        "name": data[f"{app_id}"]["data"]["name"],
                    }
                )
            return data[f"{app_id}"]["data"]
        except KeyError:
            print(f"Error game {app_id} not found!")
            self.unknown_games.append(app_id)

    def save(self):
        with open("multi", "w") as f:
            f.write(json.dumps(self.multiplayer_games))

        with open("solo", "w") as f:
            f.write(json.dumps(self.solo_games))

        with open("unknown", "w") as f:
            f.write(json.dumps(self.unknown_games))


if __name__ == "__main__":
    steamApi = SteamApi()
    # print(steamApi.multiplayer_games)
    # steamApi.fetch_user(os.environ["STEAM_USER_ID"])
    print(steamApi.fetch_game_by_id(493520))
