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
from gromp.api.league import TournamentStubv4Api

__all__ = (
    'TournamentStubv4',
)

class TournamentStubv4(NamedEndpoint):
    def codes(
        self: TournamentStubv4,
    ) -> Union[Response, Any]:
        """
        """
        return self._request_api(
            TournamentStubv4Api('codes'),
        )

    def events_by_code(
        self: TournamentStubv4,
        code: String,
    ) -> Union[Response, Any]:
        """
        """
        return self._request_api(
            TournamentStubv4Api('events_by_code'),
            tournament_code=code,
        )

    def providers(
        self: TournamentStubv4,
    ) -> Union[Response, Any]:
        """
        """
        return self._request_api(
            TournamentStubv4Api('providers'),
        )

    def tournaments(
        self: TournamentStubv4,
    ) -> Union[Response, Any]:
        """
        """
        return self._request_api(
            TournamentStubv4Api('tournaments'),
        )

