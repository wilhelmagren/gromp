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
Last updated: 2023-02-12
"""

import sys
import logging
import unittest
from gromp.hook import League
from gromp.endpoint.league import (
    ChampionMasteryv4,
    Championv3,
    Clashv1,
    LeagueExpv4,
    Leaguev4,
    LolChallengesv1,
    LolStatusv4,
    Matchv5,
    Spectatorv4,
    Summonerv4,
    TournamentStubv4,
    Tournamentv4,
)
from gromp.utils import LeaguePlatforms, LeagueRegions
from gromp.handler import JsonHandler

logger = logging.getLogger(__name__)

class LeagueHookTest(unittest.TestCase):
    """
    Test all @property decorator functions for the League hook class.
    They return an initialized Endpoint class specific to the api.
    """

    def setUp(self):
        self.hook = League(
            '<fake-RGAPI-token>',
            platform=LeaguePlatforms.na1,
            region=LeagueRegions.americas,
            handlers=[JsonHandler()],
            keylen=1024,
            timeout=10,
        )

    def testChampionMasteryv4(self):
        logger.debug('Testing ChampionMasteryv4 endpoint...')
        endpoint = self.hook.mastery
        self.assertEqual(endpoint.__class__, ChampionMasteryv4)

    def testChampionv3(self):
        logger.debug('Testing Championv3 endpoint...')
        endpoint = self.hook.champion
        self.assertEqual(endpoint.__class__, Championv3)

    def testClashv1(self):
        logger.debug('Testing Clashv1 endpoint...')
        endpoint = self.hook.clash
        self.assertEqual(endpoint.__class__, Clashv1)

    def testLeagueExpv4(self):
        logger.debug('Testing LeagueExpv4 endpoint...')
        endpoint = self.hook.league_exp
        self.assertEqual(endpoint.__class__, LeagueExpv4)

    def testLeaguev4(self):
        logger.debug('Testing Leaguev4 endpoint...')
        endpoint = self.hook.league
        self.assertEqual(endpoint.__class__, Leaguev4)

    def testLolChallengesv1(self):
        logger.debug('Testing LolChallengesv1 endpoint...')
        endpoint = self.hook.challenges
        self.assertEqual(endpoint.__class__, LolChallengesv1)

    def testLolStatusv4(self):
        logger.debug('Testing LolStatusv4 endpoint...')
        endpoint = self.hook.status
        self.assertEqual(endpoint.__class__, LolStatusv4)

    def testMatchv5(self):
        logger.debug('Testing Matchv5 endpoint...')
        endpoint = self.hook.match
        self.assertEqual(endpoint.__class__, Matchv5)

    def testSpectatorv4(self):
        logger.debug('Testing Spectatorv4 endpoint...')
        endpoint = self.hook.spectator
        self.assertEqual(endpoint.__class__, Spectatorv4)

    def testSummonerv4(self):
        logger.debug('Testing Summonerv4 endpoint...')
        endpoint = self.hook.summoner
        self.assertEqual(endpoint.__class__, Summonerv4)

    def testTournamentStubv4(self):
        logger.debug('Testing TournamentStubv4 endpoint...')
        endpoint = self.hook.tournament_stub
        self.assertEqual(endpoint.__class__, TournamentStubv4)

    def testTournamentv4(self):
        logger.debug('Testing Tournamentv4 endpoint...')
        endpoint = self.hook.tournament
        self.assertEqual(endpoint.__class__, Tournamentv4)

