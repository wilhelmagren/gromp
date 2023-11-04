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
Last updated: 2023-02-15
"""

from __future__ import annotations

import builtins

String = builtins.str

from typing import NoReturn
from gromp.api.base import LeagueApi

__all__ = ("Tournamentv4Api",)


class Tournamentv4Api(LeagueApi):
    api = {
        "codes": "codes",
        "dto_by_code": "codes/{tournament_code}",
        "events_by_code": "lobby-events/by-code/{tournament_code}",
        "providers": "providers",
        "tournaments": "tournaments",
    }

    def __init__(
        self: Tournamentv4Api,
        key: String,
    ) -> NoReturn:
        super(Tournamentv4Api, self).__init__(
            "{platform}",
            f"tournament/v4/{self.api[key]}",
        )
