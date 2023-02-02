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
# File created: 2023-02-02
# Last updated: 2023-02-02
#

import requests
from gromp.api import BaseLeagueAPI
from gromp.utils import LeaguePLATFORMS, LeagueREGIONS

__all__ = (
    'SpectatorAPIv4',
)

class urls:
    encryptedSummonerId = '{platform}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{encryptedSummonerId}'
    featuredGames = '{platform}.api.riotgames.com/lol/spectator/v4/featured-games'

class SpectatorAPIv4(BaseLeagueAPI):
    """
    Official documentation:
    https://developer.riotgames.com/apis#spectator-v4
    """
    def __init__(self, platform=LeaguePLATFORMS.euw1, region=LeagueREGIONS.europe) -> None:
        super().__init__(self.__class__.__name__, platform, region)
    
    def encryptedSummonerId(self, token, encryptedSummonerId) -> requests.Response:
        """
        Get current game information for the given summoner ID and platform.
        """
        self.set_params(platform=self.platform, encryptedSummonerId=encryptedSummonerId)
        http_response = self.get(
            token,
            urls.encryptedSummonerId,
        )

        return http_response

    def featuredGames(self, token) -> requests.Response:
        """
        Get list of featured games for platform.
        """
        self.set_params(platform=self.platform)
        http_response = self.get(
            token,
            urls.featuredGames,
        )

        return http_response
