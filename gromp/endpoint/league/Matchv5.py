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
Last updated: 2023-02-14
"""

from gromp.endpoint.base import NamedEndpoint
from gromp.api.league import Matchv5Api

__all__ = (
    'Matchv5',
)

class Matchv5(NamedEndpoint):
    def matchlist_by_puuid(
        self,
        puuid: str,
        start_time: int = None,
        end_time: int = None,
        queue: int = None,
        type_: str = None,
        start: int = None,
        count: int = None,
    ):
        """
        Get a matchlist for ranked games played on the account associated with the puuid.
        Supports filtering on queue, type of game (default ranked game), when in time
        to consider games for the matchlist, and the number of games to include.
        """
        return self._request_api(
            Matchv5Api('matchlist_by_puuid'),
            puuid=puuid,
            startTime=start_time,
            endTime=end_time,
            queue=queue,
            type=type_,
            start=start,
            count=count,
        )

    def by_id(self, match_id: str):
        """
        Get the history of a match by the match ID.
        """
        return self._request_api(
            Matchv5Api('by_id'),
            match_id=match_id,
        )

    def timeline_by_id(self, match_id: str):
        """
        Get the timeline of a match by the match ID.
        """
        return self._request_api(
            Matchv5Api('timeline_by_id'),
            match_id=match_id,
        )

