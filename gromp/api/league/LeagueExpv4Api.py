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
Last updated: 2023-11-04
"""

from __future__ import annotations

from typing import NoReturn
from gromp.api.base import LeagueApi

import builtins

String = builtins.str

__all__ = ("LeagueExpv4Api",)


class LeagueExpv4Api(LeagueApi):
    api = {
        "by_queue_tier_division": "entries/{queue}/{tier}/{division}",
    }

    def __init__(
        self: LeagueExpv4Api,
        key: String,
    ) -> NoReturn:
        super(LeagueExpv4Api, self).__init__(
            "{platform}",
            f"league-exp/v4/{self.api[key]}",
        )
