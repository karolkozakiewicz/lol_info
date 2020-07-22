import requests
import datetime
import json


class Champions:
    def __init__(self):
        self.url = "http://ddragon.leagueoflegends.com/cdn/10.14.1/data/en_US/champion.json"
        self.champion_list = requests.get("http://ddragon.leagueoflegends.com/cdn/10.14.1/data/en_US/champion.json").\
            json()
        self.list = ""
        self.champions_list()

    def champions_list(self):
        for key, value in self.champion_list['data'].items():
            roles = ""
            for role in value['tags']:
                roles += f"{role} "
            self.list += f"|-- {key.upper()}\n" \
                         f"|-- {value['key']}\n" \
                         f"|------ {roles}\n" \
                         f"|--------------------------------\n"

    def get_champion_name(self, champion_id):
        for key, value in self.champion_list['data'].items():
            if int(value['key']) == int(champion_id):
                print(key)
                print(value)


class LoL:

    def __init__(self, nick, region):
        self.champions = Champions()
        self.api = "RGAPI-90549562-ba86-4193-96b2-a3027e44a956"
        self.nick = nick
        self.region = region
        self.user_information()
        self.user = self.user_information()
        self.user_id = self.user['id']
        self.user_account_id = self.user['accountId']
        self.user_puuid = self.user['puuid']
        self.user_name = self.user['name']
        self.user_profile_icon_id = self.user['profileIconId']
        self.user_revision_iate = self.user['revisionDate']
        self.user_summoner_ievel = self.user['summonerLevel']

    def user_information(self):
        return requests.get(f"https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
                            f"{self.nick}?api_key={self.api}").json()

    def user_information_formatted(self):
        return requests.get(f"https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
                            f"{self.nick}?api_key={self.api}").json()

    def get_user_matches_info(self):
        return requests.get(f"https://{self.region}.api.riotgames.com/lol/match/v4/matchlists/by-account/"
                            f"{self.user_account_id}?api_key={self.api}").json()

    def user_matches_timestamps(self):
        for data in self.get_user_matches_info()['matches']:
            print(datetime.datetime.fromtimestamp(data['timestamp']//1000))


lol = LoL("SpirittoX", "eun1")

#print(Champions().champion_list)

#print(lol.champions.list)
lol.champions.get_champion_name(143)
# print(lol.user_matches_info()) #mecze
# print(json.dumps(lol.user_information_formatted(), indent=4))
