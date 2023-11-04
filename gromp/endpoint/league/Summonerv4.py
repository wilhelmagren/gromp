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
Last updated: 2023-11-04
"""

from __future__ import annotations

from typing import Union, Any
from requests import Response

from gromp.endpoint.base import NamedEndpoint
from gromp.api.league import Summonerv4Api

import builtins

String = builtins.str

__all__ = ("Summonerv4",)


class Summonerv4(NamedEndpoint):
    def by_account(
        self: Summonerv4,
        encrypted_account_id: String,
    ) -> Union[Response, Any]:
        """
        Get a summoner by their encrypted account ID.
        """
        return self._request_api(
            Summonerv4Api("encrypted_account_id"),
            encrypted_account_id=encrypted_account_id,
        )

    def by_name(
        self: Summonerv4,
        summoner_name: String,
    ) -> Union[Response, Any]:
        """
        Get a summoner by their summoner name.
        """
        return self._request_api(
            Summonerv4Api("summoner_name"),
            summoner_name=summoner_name,
        )

    def by_puuid(
        self: Summonerv4,
        encrypted_puuid: String,
    ) -> Union[Response, Any]:
        """
        Get a summoner by their encrypted puuid.
        """
        return self._request_api(
            Summonerv4Api("encrypted_puuid"),
            encrypted_puuid=encrypted_puuid,
        )

    def by_id(
        self: Summonerv4,
        encrypted_summoner_id: String,
    ) -> Union[Response, Any]:
        """
        Get a summoner by their encrypted summoner ID.

        `Consistently looking up summoner ids that don't
            exist will result in a blacklist.`
        """
        return self._request_api(
            Summonerv4Api("encrypted_summoner_id"),
            encrypted_summoner_id=encrypted_summoner_id,
        )
