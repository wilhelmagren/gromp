"""
MIT License

Copyright (c) 2023 Wilhelm Ågren

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

File created: 2023-02-09
Last updated: 2023-02-09
"""

from gromp.endpoint import NamedEndpoint
from gromp.url.league import Clashv1Url

__all__ = (
    'Clashv1',
)

class Clashv1(NamedEndpoint):
    def summoner_by_id(self, summoner_id: str):
        """
        """
        return self._request_api(
            Clashv1Url('summoner_by_id'),
            summoner_id=summoner_id,
        )

    def team_by_id(self, team_id: str):
        """
        """
        return self._request_api(
            Clashv1Url('team_by_id'),
            team_id=team_id,
        )

    def tournaments(self):
        """
        """
        return self._request_api(
            Clashv1Url('tournaments'),
        )

    def tournament_by_team(self, team_id: str):
        """
        """
        return self._request_api(
            Clashv1Url('tournament_by_team_id'),
            team_id=team_id,
        )

    def tournament_by_id(self, tournament_id: str):
        """
        """
        return self._request_api(
            Clashv1Url('tournament_by_id'),
            tournament_id=tournament_id,
        )

