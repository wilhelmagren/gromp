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
    'MatchAPIv5',
)

class urls:
    puuid = '{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids'
    matchId = '{region}.api.riotgames.com/lol/match/v5/matches/{matchId}'
    timeline = '{region}.api.riotgames.com/lol/match/v5/matches/{matchId}/timeline'

class MatchAPIv5(BaseLeagueAPI):
    """
    Official documentation:
    https://developer.riotgames.com/apis#match-v5
    """
    def __init__(self, platform=LeaguePLATFORMS.euw1, region=LeagueREGIONS.europe) -> None:
        super().__init__(self.__class__.__name__, platform=platform, region=region)
    
    def puuid(
        self,
        token,
        puuid,
        startTime=None,
        endTime=None,
        queue=None,
        type_=None,
        start=0,
        count=20
        ) -> requests.Response:
        """
        Get a list of match ids by puuid, supports a number of optional arguments.

        Parameters
        ----------
        token: str
            The Riot Games developer api token, unique.
        puuid: str
            The unique player uuid that you request match history for.
        startTime: int
            Epoch timestamp in seconds. The League of Legends matchlist only started storing
            timestamps on the 16th of June, 2021. So any matches played before that date
            won't be included in the results if the optional is set.
        endTime: int
            Epoch timestamp in seconds for upper range on matchlist filter.
        queue: int
            Filter the matchlist by specific queue id.
        type_: int
            Filter the matchlist by specific type of match.
        start: int
            Start index in the matchlist, defaults to 0.
        count: int
            The number of games to include in the matchlist, defaults to 20.

        """
        self.set_params(
            region=self.region,
            puuid=puuid,
            startTime=startTime,
            endTime=endTime,
            queue=queue,
            type=type_,
            start=start,
            count=count,
        )
        http_response = self.get(
            token,
            urls.puuid,
        )

        return http_response

    def matchId(self, token, matchId) -> requests.Response:
        """
        Get a match by match id and region.
        """
        self.set_params(region=self.region, matchId=matchId)
        http_response = self.get(
            token,
            urls.matchId,
        )

        return http_response

    def timeline(self, token, matchId) -> requests.Response:
        """
        Get a match timeline by match id and region.
        """
        self.set_params(region=self.region, matchId=matchId)
        http_response = self.get(
            token,
            urls.timeline,
        )

        return http_response
