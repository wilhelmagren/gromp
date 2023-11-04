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

File created: 2023-02-27
Last updated: 2023-11-04
"""

from __future__ import annotations

from typing import NoReturn
from gromp.api.base import TftApi

import builtins

String = builtins.str

__all__ = ("TftLeaguev1Api",)


class TftLeaguev1Api(TftApi):
    api = {
        "challenger": "challenger",
        "by_summoner_id": "entries/by-summoner/{summoner_id}",
        "by_tier_division": "entries/{tier}/{division}",
        "grandmaster": "grandmaster",
        "from_id": "leagues/{league_id}",
        "master": "master",
        "top_for_queue": "rated-ladders/{queue}/top",
    }

    def __init__(self, key: String) -> NoReturn:
        super(TftLeaguev1Api, self).__init__(
            "{platform}",
            f"league/v1/{self.api[key]}",
        )
