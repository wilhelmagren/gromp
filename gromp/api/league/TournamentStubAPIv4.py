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
    'TournamentStubAPIv4',
)

class urls:
    codes = '{region}.api.riotgames.com/lol/tournament-stub/v4/codes'
    tournamentCode = '{region}.api.riotgames.com/lol/tournament-stub/v4/lobby-events/by-code/{tournamentCode}'
    providers = '{region}.api.riotgames.com/lol/tournament-stub/v4/providers'
    tournaments = '{region}.api.riotgames.com/lol/tournament-sub/v4/tournaments'

class TournamentStubAPIv4(BaseLeagueAPI):
    """
    The tournament-stub API is a stand in that simulates the behavior of the tournament API.
    Developers looking to apply for tournament API access should use the stub to mock their
    implementation before applying for a production key.

    Official documentation:
    https://developer.riotgames.com/apis#tournament-stub-v4
    """
    def __init__(self, platform=LeaguePLATFORMS.euw1, region=LeagueREGIONS.europe) -> None:
        super().__init__(self.__class__.__name__, platform, region)

    def codes(self, token) -> requests.Response:
        """
        Create a mock tournament code for the given tournament.
        """
        self.set_params(region=self.region) 
        http_response = self.get(
            token,
            urls.codes,
        )

        return http_response
    
    def tournamentCode(self, token, tournamentCode) -> requests.Response:
        """
        Gets a mock list of lobby events by tournament code.
        """
        self.set_params(region=self.region, tournamentCode=tournamentCode)
        http_response = self.get(
            token,
            urls.tournamentCode,
        )
    
        return http_response
    
    def providers(self, token) -> requests.Response:
        """
        Creates a mock tournament provider and returns its ID.
        """
        self.set_params(region=self.region)
        http_response = self.get(
            token,
            urls.providers,
        )

        return http_response

    def tournaments(self, token) -> requests.Response:
        """
        Creates a mock tournament and returns its ID.
        """
        self.set_params(region=self.region)
        http_response = self.get(
            token,
            urls.tournaments,
        )
        
        return http_response
