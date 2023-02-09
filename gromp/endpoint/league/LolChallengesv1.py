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
from gromp.url.league import LolChallengesv1Url

__all__ = (
    'LolChallengesv1',
)

class LolChallengesv1(NamedEndpoint):
    def config(self):
        """
        """
        return self._request_api(
            LolChallengesv1Url('config'),
        )

    def percentiles(self):
        """
        """
        return self._request_api(
            LolChallengesv1Url('percentiles'),
        )

    def challenge_config(self, challenge_id: str):
        """
        """
        return self._request_api(
            LolChallengesv1Url('challenge_config'),
            challenge_id=challenge_id,
        )

    def top_players_for_challenge(self, challenge_id: str, level):
        """
        """
        return self._request_api(
            LolChallengesv1Url('top_players_for_challenge'),
            challenge_id=challenge_id,
            level=level,
        )

    def challenge_percentile(self, challenge_id: str):
        """
        """
        return self._request_api(
            LolChallengesv1Url('challenge_percentiles'),
            challenge_id=challenge_id,
        )

    def player_data_by_puuid(self, puuid: str):
        """
        """
        return self._request_api(
            LolChallengesv1Url('player_data_by_puuid'),
            puuid=puuid,
        )
