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
Last updated: 2023-02-23
"""

import sys
import logging
import unittest

from requests import Session
from unittest.mock import patch
from gromp.hook import Accounts
from gromp.endpoint.accounts import Accountv1
from gromp.api.accounts import Accountv1Api
from gromp.utils import AccountsRegions
from gromp.handler import JsonHandler

logger = logging.getLogger(__name__)

def _testEndpointRequests(ctx, mock, endpoint, funcs, args, return_values):
    for func, arg_, value in zip(funcs, args, return_values):
        logger.debug(f'{endpoint.__class__.__name__} {func} GET request...')
        mock.return_value.status_code = value
        response = getattr(endpoint, func)(*arg_)
        ctx.assertEqual(response.status_code, value)

class AccountsHookTest(unittest.TestCase):

    def setUp(self):
        self.hook = Accounts(
            '<fake-RGAPI-token>',
            region=AccountsRegions.ESPORTS,
            handlers=[],
            keylen=1278,
            timeout=30,
        )

    def testAccountv1Property(self):
        logger.debug('Accountv1 property...')
        endpoint = self.hook.account
        self.assertEqual(endpoint.__class__, Accountv1)

    def testAccountv1PrepareRequestValueError(self):
        logger.debug('Accountv1 PrepareRequest ValueError...')
        api = Accountv1Api('active_shard')
        self.assertRaises(
            ValueError, 
            api.prepare_request,
            platform=None,
            region=AccountsRegions.EUROPE,
            game='val',
        )

    @patch.object(Session, 'get')
    def testAccountv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.account,
            [
                'by_puuid', 'by_puuid',
                'by_riot_id', 'by_riot_id',
                'me',
                'active_shard', 'active_shard',
            ],
            [
                ['178238127'], ['this is my puuid'],
                ['Phreak', 'Tons of damage'], ['thisisme', 'my cool tag line'],
                [],
                ['val', '128378'], ['league', 'mypuuidsecret'],
            ],
            [
                200, 404,
                200, 404,
                200,
                200, 404,
            ],
        )

