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

File created: 2023-02-22
Last updated: 2023-11-04
"""

from __future__ import annotations

from typing import Union, Any
from requests import Response

from gromp.endpoint.base import NamedEndpoint
from gromp.api.valorant import ValMatchv1Api

import builtins

String = builtins.str

__all__ = ("ValMatchv1",)


class ValMatchv1(NamedEndpoint):
    def by_id(self, match_id: String) -> Union[Response, Any]:
        return self._request_api(
            ValMatchv1Api("by_id"),
            match_id=match_id,
        )

    def matchlist_by_puuid(self, puuid: String) -> Union[Response, Any]:
        return self._request_api(
            ValMatchv1Api("matchlist_by_puuid"),
            puuid=puuid,
        )

    def recent_by_queue(self, queue: String) -> Union[Response, Any]:
        return self._request_api(
            ValMatchv1Api("recent_by_queue"),
            queue=queue,
        )
