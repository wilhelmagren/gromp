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
Last updated: 2023-11-04
"""

from __future__ import annotations

from requests import Response
from typing import Any, Union

from gromp.endpoint.base import NamedEndpoint
from gromp.api.league import Clashv1Api

import builtins

String = builtins.str

__all__ = ("Clashv1",)


class Clashv1(NamedEndpoint):
    def summoner_by_id(
        self: Clashv1,
        summoner_id: String,
    ) -> Union[Response, Any]:
        """ """
        return self._request_api(
            Clashv1Api("summoner_by_id"),
            summoner_id=summoner_id,
        )

    def team_by_id(
        self: Clashv1,
        team_id: String,
    ) -> Union[Response, Any]:
        """ """
        return self._request_api(
            Clashv1Api("team_by_id"),
            team_id=team_id,
        )

    def tournaments(
        self: Clashv1,
    ) -> Union[Response, Any]:
        """ """
        return self._request_api(
            Clashv1Api("tournaments"),
        )

    def tournament_by_team(
        self: Clashv1,
        team_id: String,
    ) -> Union[Response, Any]:
        """ """
        return self._request_api(
            Clashv1Api("tournament_by_team_id"),
            team_id=team_id,
        )

    def tournament_by_id(
        self: Clashv1,
        tournament_id: String,
    ) -> Union[Response, Any]:
        """ """
        return self._request_api(
            Clashv1Api("tournament_by_id"),
            tournament_id=tournament_id,
        )
