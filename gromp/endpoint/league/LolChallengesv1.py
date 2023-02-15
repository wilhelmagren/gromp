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
Last updated: 2023-02-15
"""

from __future__ import annotations

import builtins
String = builtins.str

from typing import Union, Any, Optional
from requests import Response

from gromp.endpoint.base import NamedEndpoint
from gromp.api.league import LolChallengesv1Api

__all__ = (
    'LolChallengesv1',
)

class LolChallengesv1(NamedEndpoint):
    def config(
        self: LolChallengesv1,
    ) -> Union[Response, Any]:
        """
        """
        return self._request_api(
            LolChallengesv1Api('config'),
        )

    def percentiles(
        self: LolChallengesv1,
    ) -> Union[Response, Any]:
        """
        """
        return self._request_api(
            LolChallengesv1Api('percentiles'),
        )

    def challenge_config(
        self: LolChallengesv1,
        challenge_id: String,
    ) -> Union[Response, Any]:
        """
        """
        return self._request_api(
            LolChallengesv1Api('challenge_config'),
            challenge_id=challenge_id,
        )

    def top_players_for_challenge(
        self: LolChallengesv1,
        challenge_id: String,
        level: String,
        limit: Optional[String] = None,
    ) -> Union[Response, Any]:
        """
        """
        return self._request_api(
            LolChallengesv1Api('top_players_for_challenge'),
            challenge_id=challenge_id,
            level=level,
            limit=limit,
        )

    def challenge_percentile(
        self: LolChallengesv1,
        challenge_id: String,
    ) -> Union[Response, Any]:
        """
        """
        return self._request_api(
            LolChallengesv1Api('challenge_percentiles'),
            challenge_id=challenge_id,
        )

    def player_data_by_puuid(
        self: LolChallengesv1,
        puuid: String,
    ) -> Union[Response, Any]:
        """
        """
        return self._request_api(
            LolChallengesv1Api('player_data_by_puuid'),
            puuid=puuid,
        )

