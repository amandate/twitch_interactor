from constants.constants import API_TOKEN_FILE_PATH
from constants.json_response_keys import *
from constants.parameter_keys import AFTER_KEY, FIRST_KEY
from constants.personal_keys import *
from api.users_api import TwitchUsersAPI

import json
import random

class RandomFollowerGenerator:
    def __init__(self):
        self._parseTwitchJsonFile()
        self.TwitchUserFollowersAPI = TwitchUsersAPI(self.client_id, self.access_token)
        self.followers = []

    def _parseTwitchJsonFile(self):
        json_file = open(API_TOKEN_FILE_PATH)
        json_data = json.load(json_file)

        self.client_id = json_data[CLIENT_ID_KEY]
        self.access_token = json_data[ACCESS_TOKEN_KEY]
        self.user_id = json_data[MY_USER_ID_KEY]

    def _populateCurrentFollowers(self):
        cursor = ''
        params = {AFTER_KEY: cursor, FIRST_KEY: 100}
        while True:
            response = self.TwitchUserFollowersAPI.getUserFollowers(self.user_id, params)
            for user in response[DATA_KEY]:
                self.followers.append(user[FROM_NAME_KEY])

            if CURSOR_KEY not in response[PAGINATION_KEY]:
                return

            cursor = response[PAGINATION_KEY][CURSOR_KEY]
            params[AFTER_KEY] = cursor

    def getRandomFollower(self):
        if not self.followers:
            self._populateCurrentFollowers()
        follower = random.choice(self.followers)
        self.followers.remove(follower)
        return follower

if __name__ == "__main__":
    rfg = RandomFollowerGenerator()
    while True:
        userResponse = True if input("Grab random follower? (y/n): ") == "y" else False
        if userResponse:
            print(rfg.getRandomFollower())
        else:
            break
        
