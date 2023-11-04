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

import logging
import unittest

from requests import Session
from unittest.mock import patch
from gromp.hook import Lor

from gromp.utils import LorRegions

logger = logging.getLogger(__name__)


def _testEndpointRequests(ctx, mock, endpoint, funcs, args, return_values):
    for func, arg_, value in zip(funcs, args, return_values):
        logger.debug(f"{endpoint.__class__.__name__} {func} GET request...")
        mock.return_value.status_code = value
        response = getattr(endpoint, func)(*arg_)
        ctx.assertEqual(response.status_code, value)


class LorHookTest(unittest.TestCase):
    def setUp(self):
        self.hook = Lor(
            "<fake-RGAPI-token>",
            region=LorRegions.EUROPE,
            handlers=[],
            keylen=2048,
            timeout=19,
        )

    @patch.object(Session, "get")
    def testStatusv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.status,
            ["get"],
            [[]],
            [200],
        )

    @patch.object(Session, "get")
    def testRankedv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.ranked,
            ["get"],
            [[]],
            [200],
        )

    @patch.object(Session, "get")
    def testInventoryv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.inventory,
            ["me"],
            [[]],
            [200],
        )

    @patch.object(Session, "get")
    def testDeckv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.deck,
            [
                "my_decks",
                "create_deck",
                "create_deck",
            ],
            [
                [],
                [{"code": "xd", "name": "cool deck forsen"}],
                ["this is my deck"],
            ],
            [
                200,
                200,
                404,
            ],
        )

    @patch.object(Session, "get")
    def testMatchv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.match,
            [
                "matchlist_by_puuid",
                "matchlist_by_puuid",
                "by_id",
                "by_id",
            ],
            [
                ["8172481748"],
                ["kebaerino"],
                ["812748"],
                ["this is my best match"],
            ],
            [
                200,
                404,
                200,
                404,
            ],
        )
