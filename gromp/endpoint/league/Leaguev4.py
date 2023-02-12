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

File created: 2023-02-05
Last updated: 2023-02-12
"""

from gromp.endpoint import NamedEndpoint
from gromp.url.league import Leaguev4Url

__all__ = (
    'Leaguev4',
)

class Leaguev4(NamedEndpoint):
    def challenger_by_queue(self, queue: str):
        """
        """
        return self._request_api(
            Leaguev4Url('challenger_queue'),
            challenger_queue=queue,

        )

    def by_summoner_id(self, summoner_id: str):
        """
        """
        return self._request_api(
            Leaguev4Url('encrypted_summoner_id'),
            encrypted_summoner_id=summoner_id,
        )

    def by_queue_tier_division(self, queue: str, tier: str, divion: str):
        """
        """
        return self._request_api(
            Leaguev4Url('by_queue_tier_division'),
            queue=queue,
            tier=tier,
            division=division,
        )

    def grandmaster_by_queue(self, queue: str):
        """
        """
        return self._request_api(
            Leaguev4Url('grandmaster_queue'),
            grandmaster_queue=queue,
        )
    
    def by_id(self, league_id: str):
        """
        """
        return self._request_api(
            Leaguev4Url('by_id'),
            league_id=league_id,
        )

    def master_by_queue(self, queue: str):
        """
        """
        return self._request_api(
            Leaguev4Url('master_queue'),
            master_queue=master_queue,
        )

