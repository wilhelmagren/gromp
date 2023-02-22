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

File created: 2023-02-12
Last updated: 2023-02-22
"""

from __future__ import annotations

import builtins
String = builtins.str

from typing import NoReturn, Dict
from gromp.hook.base import Hook
from gromp.endpoint.valorant import (
    ValContentv1,
    ValMatchv1,
    ValRankedv1,
    ValStatusv1,
)
from gromp.utils import ValorantRegions

__all__ = (
    'Valorant',
)

class Valorant(Hook):
    def __init__(
        self: Valorant,
        token: String,
        **kwargs: Dict,
    ) -> NoReturn:
        super(Valorant, self).__init__(
            token=token,
            game=self.__class__.__name__,
            **kwargs,
        )

    @property
    def content(self) -> ValContentv1:
        return self._setup_named_endpoint(ValContentv1)

    @property
    def match(self) -> ValMatchv1:
        return self._setup_named_endpoint(ValMatchv1)

    @property
    def ranked(self) -> ValRankedv1:
        return self._setup_named_endpoint(ValRankedv1)

    @property
    def status(self) -> ValStatusv1:
        return self._setup_named_endpoint(ValStatusv1)

