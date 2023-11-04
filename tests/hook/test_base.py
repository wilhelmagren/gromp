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

File created: 2023-02-16
Last updated: 2023-11-04
"""

import logging
import unittest
import rsa

from gromp import set_logging_level
from gromp.hook import Hook
from gromp.utils import (
    LeagueRegions,
    LeaguePlatforms,
    ValorantRegions,
)

logger = logging.getLogger(__name__)


class HookTest(unittest.TestCase):
    def testValidConstructor(self):
        logger.debug("Hook properties...")
        hook = Hook(
            "<fake-RGAPI-token>",
            "League",
            LeaguePlatforms.euw1,
            LeagueRegions.EUROPE,
            keylen=1024,
            timeout=10,
        )

        set_logging_level(logging.WARNING)

        self.assertTrue(isinstance(hook, Hook))

        game = hook.game
        pkey = hook.public_key
        config = hook.config

        self.assertTrue(isinstance(game, str))
        self.assertTrue(isinstance(pkey, rsa.PublicKey))
        self.assertTrue(isinstance(config, dict))
        self.assertEqual(game, config["game"])
        self.assertEqual(pkey, config["keys"]["public"])

    def testNoPlatformValorant(self):
        logger.debug("no platform for Valorant..")
        hook = Hook(
            "<fake-RGAPI-token>",
            "Valorant",
            platform=None,
            region=ValorantRegions.EU,
        )

        handlers = hook.handlers

        self.assertTrue(isinstance(hook, Hook))
        self.assertTrue(isinstance(handlers, list))

    def testNoPlatformNoRegionLeague(self):
        logger.debug("no platform no region for League..")
        self.assertRaises(
            AssertionError,
            Hook,
            "<fake-RGAPI-token>",
            "League",
            platform=None,
            region=None,
        )

    def testNoRegionValorant(self):
        self.assertRaises(
            AssertionError,
            Hook,
            "<fake-RGAPI-token>",
            "Valorant",
        )

    def testNoRegionLeague(self):
        logger.debug("no region for League..")
        self.assertRaises(
            AssertionError,
            Hook,
            "<fake-RGAPI-token>",
            "League",
            platform=LeaguePlatforms.na1,
        )

    def testInvalidKeylen(self):
        logger.debug("invalid RSA key length..")
        self.assertRaises(
            AssertionError,
            Hook,
            "<fake-RGAPI-token>",
            "Valorant",
            region=ValorantRegions.KR,
            keylen=-256,
        )

    def testInvalidTimeout(self):
        logger.debug("invalid requests timeout param..")
        self.assertRaises(
            AssertionError,
            Hook,
            "<fake-RGAPI-token>",
            "Valorant",
            region=ValorantRegions.NA,
            timeout=-10,
        )
