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

import sys
import logging
import unittest

from requests import Session
from unittest.mock import patch
from gromp.hook import Tft
from gromp.endpoint.tft import (
    TftSummonerv1,
    TftStatusv1,
    TftMatchv1,
    TftLeaguev1,
)

from gromp.utils import TftRegions, TftPlatforms

logger = logging.getLogger(__name__)


def _testEndpointRequests(ctx, mock, endpoint, funcs, args, return_values):
    for func, arg_, value in zip(funcs, args, return_values):
        logger.debug(f'{endpoint.__class__.__name__} {func} GET request...')
        mock.return_value.status_code = value 
        response = getattr(endpoint, func)(*arg_)
        ctx.assertEqual(response.status_code, value)

class TftHookTest(unittest.TestCase):
    def setUp(self):
        self.hook = Tft(
            '<fake-RGAPI-token>',
            region=TftRegions.ASIA,
            platform=TftPlatforms.kr,
            handlers=[],
            keylen=2048,
            timeout=19,
        )

    @patch.object(Session, 'get')
    def testSummonerv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.summoner,
            [
                'by_account_id', 'by_account_id',
                'by_summoner_name', 'by_summoner_name',
                'by_puuid', 'by_puuid',
                'me',
                'by_summoner_id', 'by_summoner_id',
            ],
            [
                ['19823791'], ['this is my id'],
                ['1 900 976 JUICE'], ['pure4silver'],
                ['1927488917481'], ['gaierji987'],
                [],
                ['f878fajo8'], ['cool summoner id'],
            ],
            [
                200, 404,
                200, 404,
                200, 404,
                200,
                200, 404,
            ],
        )

    @patch.object(Session, 'get')
    def testStatusv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.status,
            [
                'get',
            ],
            [[]],
            [200],
        )

    @patch.object(Session, 'get')
    def testLeaguev1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.league,
            [
                'challenger',
                'by_summoner_id', 'by_summoner_id',
                'by_tier_division', 'by_tier_division',
                'grandmaster',
                'from_id', 'from_id',
                'master',
                'top_for_queue', 'top_for_queue',
            ],
            [
                [],
                ['8172487178'], ['guhahaha'],
                ['silver', '4'], ['rock', '29'],
                [],
                ['18297814781fhj8127'], ['giaraoraergo'],
                [],
                ['master'], ['challenger'],
            ],
            [
                200,
                200, 404,
                200, 404,
                200,
                200, 404,
                200,
                200, 404,
            ],
        )

    @patch.object(Session, 'get')
    def testMatchv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.match,
            [
                'matchlist_by_puuid', 'matchlist_by_puuid',
                'by_id', 'by_id',
            ],
            [
                ['187238172841'], ['kebab'],
                ['87182478'], ['shawarma'],
            ],
            [
                200, 404,
                200, 404,
            ],
        )

