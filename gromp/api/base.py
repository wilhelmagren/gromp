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

from typing import (
    Dict,
    Tuple,
    NoReturn,
)
import re
import builtins

String = builtins.str

__all__ = (
    "Api",
    "AccountsApi",
    "TftApi",
    "LeagueApi",
    "LorApi",
    "ValorantApi",
)


class Api(object):
    def __init__(
        self: Api,
        base: String,
        game: String,
        api: String,
    ) -> NoReturn:
        self._url = f"https://{base}.api.riotgames.com/{game}/{api}"

    @property
    def url(
        self: Api,
    ) -> String:
        return self._url

    def prepare_request(
        self: Api,
        **kwargs: Dict,
    ) -> Tuple:
        """
        Prepare a GET request by validating the url and extracting
        optional query parameters.
        """
        url_params = re.findall("{(\w*)}", self.url)

        for required in url_params:
            if required not in kwargs:
                raise ValueError(f"Missing required parameter in url, {required=}.")

        query_params = {key: val for key, val in kwargs.items()}

        request_url = self.url.format(**kwargs)
        return (request_url, query_params)


class AccountsApi(Api):
    def __init__(
        self,
        base: String,
        api: String,
    ) -> NoReturn:
        super(AccountsApi, self).__init__(base, "lol", api)


class LeagueApi(Api):
    def __init__(
        self: LeagueApi,
        base: String,
        api: String,
    ) -> NoReturn:
        super(LeagueApi, self).__init__(base, "lol", api)


class ValorantApi(Api):
    def __init__(
        self,
        base: String,
        api: String,
    ) -> NoReturn:
        super(ValorantApi, self).__init__(base, "val", api)


class TftApi(Api):
    def __init__(
        self,
        base: String,
        api: String,
    ) -> NoReturn:
        super(TftApi, self).__init__(base, "tft", api)


class LorApi(Api):
    def __init__(
        self,
        base: String,
        api: String,
    ) -> NoReturn:
        super(LorApi, self).__init__(base, "lor", api)
