#
# MIT License
#
# Copyright (c) 2023 Wilhelm Ågren
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# File created: 2023-01-23
# Last updated: 2023-02-02
#

import requests
from gromp.api import BaseLeagueAPI
from gromp.utils import LeaguePLATFORMS, LeagueREGIONS

__all__ = (
    'SummonerAPIv4',
)

class urls:
    rsoPUUID = '{platform}.api.riotgames.com/fulfillment/v1/summoners/by-puuid/{rsoPUUID}'
    encryptedAccountId = '{platform}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{encryptedAccountId}'
    summonerName = '{platform}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}'
    encryptedPUUID = '{platform}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{encryptedPUUID}'
    me = '{platform}.api.riotgames.com/lol/summoner/v4/summoners/me'
    encryptedSummonerId = '{platform}.api.riotgames.com/lol/summoner/v4/summoners/{encryptedSummonerId}'

class SummonerAPIv4(BaseLeagueAPI):
    """
    Official documentation:
    https://developer.riotgames.com/apis#summoner-v4
    """
    def __init__(self, platform=LeaguePLATFORMS.euw1, region=LeagueREGIONS.europe) -> None:
        super().__init__(self.__class__.__name__, platform, region)

    def rsoPUUID(self, token, rsoPUUID) -> requests.Response:
        """
        Get a summoner by its RSO encrypted PUUID.
        """
        self.set_params(platform=self.platform, rsoPUUID=rsoPUUID)
        http_response = self.get(
            token, 
            urls.rsoPUUID,
        )

        return http_response
    
    def encryptedAccountId(self, token, encryptedAccountId) -> requests.Response:
        """
        Get a summoner by account ID.
        """
        self.set_params(platform=self.platform, encryptedAccountId=encryptedAccountId)
        http_response = self.get(
            token,
            urls.encryptedAccountId,
        )

        return http_response
    
    def summonerName(self, token, summonerName) -> requests.Response:
        """
        Get a summoner by summoner name.
        """
        self.set_params(platform=self.platform, summonerName=summonerName)
        http_response = self.get(
            token,
            urls.summonerName,
        ) 

        return http_response

    def encryptedPUUID(self, token, encryptedPUUID) -> requests.Response:
        """
        Get a summoner by PUUID.
        """
        self.set_params(platform=self.platform, encryptedPUUID=encryptedPUUID)
        http_response = self.get(
            token,
            urls.encryptedPUUID,
        )

        return http_response

    def me(self, token) -> requests.Response:
        """
        Get a summoner by access token.
        """
        self.set_params(platform=self.platform)
        http_response = self.get(
            token,
            urls.me,
        ) 

        return http_response
    
    def encryptedSummonerId(self, token, encryptedSummonerId) -> requests.Response:
        """
        Get a summoner by summoner ID.
        """
        self.set_params(platform=self.platform, encryptedSummonerId=encryptedSummonerId)
        http_response = self.get(
            token,
            urls.encryptedSummonerId,
        )

        return http_response
