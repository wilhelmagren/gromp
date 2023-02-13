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
Last updated: 2023-02-14
"""

from gromp.endpoint.base import NamedEndpoint
from gromp.api.league import ChampionMasteryv4Api

__all__ = (
    'ChampionMasteryv4',
)

class ChampionMasteryv4(NamedEndpoint):
    def all_for_summoner(self, summoner_id: str):
        """
        """
        return self._request_api(
            ChampionMasteryv4Api('all_for_summoner'),
            encrypted_summoner_id=summoner_id,
        )

    def champion_for_summoner(self, summoner_id: str, champion_id: str):
        """
        """
        return self._request_api(
            ChampionMasteryv4Api('champion_for_summoner'),
            encrypted_summoner_id=summoner_id,
            champion_id=champion_id,
        )

    def top_for_summoner(self, summoner_id: str):
        """
        """
        return self._request_api(
            ChampionMasteryv4Api('top_for_summoner'),
            encrypted_summoner_id=summoner_id,
        )

    def total_score_for_summoner(self, summoner_id: str):
        """
        """
        return self._request_api(
            ChampionMasteryv4Api('summoner_total_score'),
            encrypted_summoner_id=summoner_id,
        )

