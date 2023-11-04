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
Last updated: 2023-02-27
"""

from __future__ import annotations

import builtins

String = builtins.str

from typing import NoReturn, Dict
from gromp.hook.base import Hook
from gromp.endpoint.base import NamedEndpoint
from gromp.endpoint.tft import (
    TftLeaguev1,
    TftMatchv1,
    TftStatusv1,
    TftSummonerv1,
)

from gromp.utils import TftPlatforms, TftRegions

__all__ = ("Tft",)


class Tft(Hook):
    def __init__(self, token: String, **kwargs: Dict) -> NoReturn:
        super(Tft, self).__init__(
            token=token,
            game=self.__class__.__name__,
            **kwargs,
        )

    @property
    def league(self) -> TftLeaguev1:
        return self._setup_named_endpoint(TftLeaguev1)

    @property
    def match(self) -> TftMatchv1:
        return self._setup_named_endpoint(TftMatchv1)

    @property
    def status(self) -> TftStatusv1:
        return self._setup_named_endpoint(TftStatusv1)

    @property
    def summoner(self) -> TftSummonerv1:
        return self._setup_named_endpoint(TftSummonerv1)
