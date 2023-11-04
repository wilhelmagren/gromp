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
Last updated: 2023-02-15
"""

from __future__ import annotations

import builtins

String = builtins.str

from typing import Union, Any
from requests import Response

from gromp.endpoint.base import NamedEndpoint
from gromp.api.league import Leaguev4Api

__all__ = ("Leaguev4",)


class Leaguev4(NamedEndpoint):
    def challenger_by_queue(
        self: Leaguev4,
        queue: String,
    ) -> Union[Response, Any]:
        """ """
        return self._request_api(
            Leaguev4Api("challenger_queue"),
            challenger_queue=queue,
        )

    def by_summoner_id(
        self: Leaguev4,
        summoner_id: String,
    ) -> Union[Response, Any]:
        """ """
        return self._request_api(
            Leaguev4Api("encrypted_summoner_id"),
            encrypted_summoner_id=summoner_id,
        )

    def by_queue_tier_division(
        self: Leaguev4,
        queue: String,
        tier: String,
        division: String,
    ) -> Union[Response, Any]:
        """ """
        return self._request_api(
            Leaguev4Api("by_queue_tier_division"),
            queue=queue,
            tier=tier,
            division=division,
        )

    def grandmaster_by_queue(
        self: Leaguev4,
        queue: String,
    ) -> Union[Response, Any]:
        """ """
        return self._request_api(
            Leaguev4Api("grandmaster_queue"),
            grandmaster_queue=queue,
        )

    def by_id(
        self: Leaguev4,
        league_id: String,
    ) -> Union[Response, Any]:
        """ """
        return self._request_api(
            Leaguev4Api("by_id"),
            league_id=league_id,
        )

    def master_by_queue(
        self: Leaguev4,
        queue: String,
    ) -> Union[Response, Any]:
        """ """
        return self._request_api(
            Leaguev4Api("master_queue"),
            master_queue=master_queue,
        )
