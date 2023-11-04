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

File created: 2023-02-23
Last updated: 2023-11-04
"""

import logging
import unittest

from requests import Session
from unittest.mock import patch
from gromp.hook import Valorant
from gromp.endpoint.valorant import (
    ValContentv1,
    ValMatchv1,
    ValRankedv1,
    ValStatusv1,
)

from gromp.utils import ValorantRegions

logger = logging.getLogger(__name__)


def _testEndpointRequests(ctx, mock, endpoint, funcs, args, return_values):
    for func, arg_, value in zip(funcs, args, return_values):
        logger.debug(f"{endpoint.__class__.__name__} {func} GET request...")
        mock.return_value.status_code = value
        response = getattr(endpoint, func)(*arg_)
        ctx.assertEqual(response.status_code, value)


class ValorantHookTest(unittest.TestCase):
    """
    Test all @property decorator functions for the Valorant hook class.
    They return an initialized NamedEndpoint class specific to the api.

    Mock requests.session.get() calls to the API which the NamedEndpoint
    is pointint to, specify expected return values.
    """

    def setUp(self):
        self.hook = Valorant(
            "<fake-RGAPI-token>",
            region=ValorantRegions.EU,
            handlers=[],
            keylen=854,
            timeout=8,
        )

    def testContentv1Property(self):
        logger.debug("Contentv1 property...")
        endpoint = self.hook.content
        self.assertEqual(endpoint.__class__, ValContentv1)

    @patch.object(Session, "get")
    def testContentv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.content,
            ["get"],
            [[]],
            [200],
        )

    def testMatchv1Property(self):
        logger.debug("Matchv1 property...")
        endpoint = self.hook.match
        self.assertEqual(endpoint.__class__, ValMatchv1)

    @patch.object(Session, "get")
    def testMatchv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.match,
            [
                "by_id",
                "by_id",
                "matchlist_by_puuid",
                "matchlist_by_puuid",
                "recent_by_queue",
                "recent_by_queue",
            ],
            [
                [123998],
                ["lolbigID"],
                [81479878],
                ["thisisaPUUID"],
                [2],
                ["diamond-pro-gamer-queue"],
            ],
            [200, 404, 200, 404, 200, 404],
        )

    def testRankedv1Property(self):
        logger.debug("Rankedv1 property...")
        endpoint = self.hook.ranked
        self.assertEqual(endpoint.__class__, ValRankedv1)

    @patch.object(Session, "get")
    def testRankedv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.ranked,
            [
                "by_act",
                "by_act",
            ],
            [
                [18],
                ["cool-act"],
            ],
            [
                200,
                400,
            ],
        )

    def testStatusv1Property(self):
        logger.debug("Statusv1 property...")
        endpoint = self.hook.status
        self.assertEqual(endpoint.__class__, ValStatusv1)

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
