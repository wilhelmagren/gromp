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
# Last updated: 2023-01-31
#

from gromp.hook import BaseHook
from gromp.api.league import *
from gromp.utils import LeaguePLATFORMS, LeagueREGIONS

__all__ = (
    'LeagueHook',
)

class LeagueHook(BaseHook):
    def __init__(self, token, platform=LeaguePLATFORMS.euw1, region=LeagueREGIONS.europe):
        super().__init__(token, 'league', platform, region)

    def get_summoner_by_name(self, summonerName, platform=None, region=None):
        if platform is None:
            platform = self._platform
        
        if region is None:
            region = self._region

        api = SummonerAPIv4(platform=platform, region=region)
        response = api.summonerName(self._token, summonerName)
        summoner = response.json()

        return summoner
    
    def get_matches_by_puuid(self, puuid, platform=None, region=None):
        if platform is None:
            platform = self._platform
        
        if region is None:
            region = self._region
        
        api = MatchAPIv5(platform=platform, region=region)
        response = api.puuid(self._token, puuid)
        matches = response.json()

        return matches

