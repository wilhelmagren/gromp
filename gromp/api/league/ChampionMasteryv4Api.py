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

File created: 2023-02-13
Last updated: 2023-11-10
"""

from __future__ import annotations

from typing import NoReturn
from gromp.api.base import LeagueApi

import builtins

String = builtins.str

__all__ = ("ChampionMasteryv4Api",)


class ChampionMasteryv4Api(LeagueApi):
    """ """

    api = {
        "all_by_puuid": "champion-masteries/by-puuid/{encrypted_puuid}",
        "champion_by_puuid": "champion-masteries/by-puuid/{encrypted_puuid}/by-champion/{champion_id}",
        "top_by_puuid": "champion-masteries/by-puuid/{encrypted_puuid}/top",
        "puuid_total_score": "scores/by-puuid/{encrypted_puuid}",
        "all_for_summoner": "champion-masteries/by-summoner/{encrypted_summoner_id}",
        "champion_for_summoner": "champion-masteries/by-summoner/{encrypted_summoner_id}/by-champion/{champion_id}",
        "top_for_summoner": "champion-masteries/by-summoner/{encrypted_summoner_id}/top",
        "summoner_total_score": "scores/by-summoner/{encrypted_summoner_id}",
    }

    def __init__(
        self: ChampionMasteryv4Api,
        key: String,
    ) -> NoReturn:
        super(ChampionMasteryv4Api, self).__init__(
            "{platform}",
            f"champion-mastery/v4/{self.api[key]}",
        )
