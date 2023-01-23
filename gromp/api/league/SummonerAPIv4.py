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
# Last updated: 2023-01-23
#

from gromp.api import BaseLeagueAPI

__all__ = (
    'SummonerAPIv4',
)

URL = {
    'rsoPUUID': '{platform}.api.riotgames.com/fulfillment/v1/summoners/by-puuid/{rsoPUUID}',
    'encryptedAccountId': '{platform}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{encryptedAccountId}',
    'summonerName': '{platform}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}',
    'encryptedPUUID': '{platform}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{encryptedPUUID}',
    'me': '{platform}.api.riotgames.com/lol/summoner/v4/summoners/me',
    'encryptedSummonerId': '{platform}.api.riotgames.com/lol/summoner/v4/summoners/{encryptedSummonerId}',
}

class SummonerAPIv4(BaseLeagueAPI):
    def __init__(self, platform='euw1', region='europe'):
        super().__init__(platform=platform, region=region)

    def rsoPUUID(self, token, rsoPUUID):
        http_response = self.get(
            token, 
            URL['rsoPUUID'],
            params={
                '{rsoPUUID}': rsoPUUID,
                '{platform}': self._platform,
            }
        )
        return http_response
    
    def encryptedAccountId(self, token, encryptedAccountId):
        http_response = self.get(
            token,
            URL['encryptedAccountId'],
            params={
                '{encryptedAccountId}': encryptedAccountId,
                '{platform}': self._platform,
            },
        )
    
    def summonerName(self, token, summonerName):
        http_response = self.get(
            token,
            URL['summonerName'],
            params={
                '{summonerName}': summonerName,
                '{platform}': self._platform,
            },
        ) 
        return http_response

    def encryptedPUUID(self, token, encryptedPUUID):
        http_response = self.get(
            token,
            URL['encryptedPUUID'],
            params={
                '{encryptedPUUID}': encryptedPUUID,
                '{platform}': self._platform,
            }
        )
        return http_response

    def me(self, token):
        http_response = self.get(
            token,
            URL['me'],
            params={
                '{platform}': self._platform,
            }
        ) 
        return http_response
    
    def encryptedSummonerId(self, token, encryptedSummonerId):
        http_response = self.get(
            token,
            URL['encryptedSummonerId'],
            params={
                '{encryptedSummonerId}': encryptedSummonerId,
                '{platform}': self._platform,
            }
        )
        return http_response
