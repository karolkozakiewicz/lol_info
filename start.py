import requests
import json
import datetime
import time

class Champions:
    def __init__(self):
        self.url = "http://ddragon.leagueoflegends.com/cdn/10.14.1/data/en_US/champion.json"
        self.champion_list = requests.get("http://ddragon.leagueoflegends.com/cdn/10.14.1/data/en_US/champion.json").json()

    def champions_list(self):
        print(json.dumps(self.champion_list['data'], indent=4))
        # for key, value in self.champion_list['data'].items():
        #
        #     print(f"|-- {key} - KEY: {value['key']}")
        #     print('|---', *value['tags'],sep=' ')
        #     print("|-----------------------------")













champions = Champions()

class LoL:

    def __init__(self, nick, region):
        self.api = "RGAPI-90549562-ba86-4193-96b2-a3027e44a956"
        self.nick = nick
        self.region = region
        self.get_user_information()
        self.user = self.get_user_information()
        self.user_id = self.user['id']
        self.user_accountId = self.user['accountId']
        self.user_puuid = self.user['puuid']
        self.user_name = self.user['name']
        self.user_profileIconId = self.user['profileIconId']
        self.user_revisionDate = self.user['revisionDate']
        self.user_summonerLevel = self.user['summonerLevel']



    def get_user_information(self):
        return requests.get(f"https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.nick}?api_key={self.api}").json()

    def get_user_information_formatted(self):
        return requests.get(
            f"https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.nick}?api_key={self.api}").json()

    def get_user_matches_info(self):
        return requests.get(f"https://{self.region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{self.accountId}?api_key={self.api}").json()

    def user_matches_timestamps(self):
        matches_info = self.get_user_matches_info()
        for data in matches_info['matches']:
            print(datetime.datetime.fromtimestamp(data['timestamp']//1000))

champions.champions_list()

lol = LoL("SpirittoX", "eun1")


#print(json.dumps(lol.get_user_information_formatted("SpirittoX", "eun1"), indent=4)) #user
#print(json.dumps(lol.get_user_matches_info(lol.user_accountId), indent=4)) #mecze
#print(lol.get_user_information_formatted())


