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
    'LeagueAPIv4',
)

class urls:
    challengerQueue = '{platform}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{challengerQueue}'
    encryptedSummonerId = '{platform}.api.riotgames.com/lol/league/v4/entries/by-summoner/{encryptedSummonerId}'
    queueTierDivision = '{platform}.api.riotgames.com/lol/league/v4/entries/{queue}/{tier}/{division}'
    grandmasterQueue = '{platform}.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{grandmasterQueue}'
    leagueId = '{platform}.api.riotgames.com/lol/league/v4/leagues/{leagueId}'
    masterQueue = '{platform}.api.riotgames.com/lol/league/v4/masterleagues/by-queue/{queue}'

class LeagueAPIv4(BaseLeagueAPI):
    """
    Official documentation:
    https://developer.riotgames.com/apis#league-v4
    """
    def __init__(self, platform=LeaguePLATFORMS.euw1, region=LeagueREGIONS.europe) -> None:
        super().__init__(self.__class__.__name__, platform, region)
    
    def challengerQueue(self, token, challengerQueue) -> requests.Response:
        """
        Get the challenger league for given queue and platform.
        """
        self.set_params(platform=self.platform, challengerQueue=challengerQueue)
        http_response = self.get(
            token,
            urls.challengerQueue,
        )

        return http_response

    def encryptedSummonerId(self, token, encryptedSummonerId) -> requests.Response:
        """
        Get the league entries in all queues for a given summoner ID and platform.
        """
        self.set_params(platform=self.platform, encryptedSummonerId=encryptedSummonerId)
        http_response = self.get(
            token,
            urls.encryptedSummonerId,
        )

        return http_response
    
    def queueTierDivision(self, token, queue, tier, division) -> requests.Response:
        """
        Get all the league entries for a platform.
        """
        self.set_params(platform=self.platform, queue=queue, tier=tier, division=division)
        http_response = self.get(
            token,
            urls.queueTierDivision,
        )

        return http_response

    def grandmasterQueue(self, token, grandmasterQueue) -> requests.Response:
        self.set_params(platform=self.platform, grandmasterQueue=grandmasterQueue)
        http_response = self.get(
            token,
            urls.grandmasterQueue,
        )

        return http_response

    def leagueId(self, token, leagueId) -> requests.Response:
        """
        Get the grandmaster league of a specific queue and platform.
        """
        self.set_params(platform=self.platform, leagueId=leagueId)
        http_response = self.get(
            token,
            urls.leagueId,
        )

        return http_response
    
    def masterQueue(self, token, masterQueue) -> requests.Response:
        """
        Get the master league for given queue and platform.
        """
        self.set_params(platform=self.platform, masterQueue=masterQueue)
        http_response = self.get(
            token,
            urls.masterQueue,
        )

        return http_response
