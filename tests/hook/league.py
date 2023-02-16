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
Last updated: 2023-02-16
"""

import sys
import logging
import unittest

from requests import Session
from unittest.mock import patch
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

def _testEndpointRequests(ctx, mock, endpoint, funcs, args, return_values):
    for func, arg_, value in zip(funcs, args, return_values):
        logger.debug(f'{endpoint.__class__.__name__} {func} GET request...')
        mock.return_value.status_code = value 
        response = getattr(endpoint, func)(*arg_)
        ctx.assertEqual(response.status_code, value)

class LeagueHookTest(unittest.TestCase):
    """
    Test all @property decorator functions for the League hook class.
    They return an initialized Endpoint class specific to the api.

    Mock requests.session.get() calls to the API which the Endpoint is
    pointing to, specify expected return values. We can't make real
    API calls in tests, bad for bandwidth and consistency.

    """

    def setUp(self):
        self.hook = League(
            '<fake-RGAPI-token>',
            platform=LeaguePlatforms.na1,
            region=LeagueRegions.americas,
            handlers=[],
            keylen=1024,
            timeout=10,
        )

    def testChampionMasteryv4Property(self):
        logger.debug('ChampionMasteryv4 property...')
        endpoint = self.hook.mastery
        self.assertEqual(endpoint.__class__, ChampionMasteryv4)
    
    @patch.object(Session, 'get')
    def testChampionMasteryv4Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.mastery,
            [
                'all_for_summoner', 'all_for_summoner',
                'champion_for_summoner', 'champion_for_summoner',
                'top_for_summoner', 'top_for_summoner',
                'total_score_for_summoner',
            ],
            [
                ['1010101'], ['xd'],
                ['1010101', '10'], ['xd', '19419419'],
                ['1010101'], ['xd'],
                ['1010101'], ['xd'],
            ],
            [
                200, 404,
                200, 404,
                200, 404,
                200, 404,
            ],
        )

    def testChampionv3(self):
        logger.debug('Championv3 property...')
        endpoint = self.hook.champion
        self.assertEqual(endpoint.__class__, Championv3)

    @patch.object(Session, 'get')
    def testChampionv3Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.champion,
            [
                'rotations',
            ],
            [[]],
            [200],
        )

    def testClashv1(self):
        logger.debug('Clashv1 property...')
        endpoint = self.hook.clash
        self.assertEqual(endpoint.__class__, Clashv1)

    @patch.object(Session, 'get')
    def testClashv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.clash,
            [
                'summoner_by_id', 'summoner_by_id',
                'team_by_id', 'team_by_id',
                'tournaments',
                'tournament_by_team', 'tournament_by_team',
                'tournament_by_id', 'tournament_by_id',
            ],
            [
                ['1010101'], ['lolxdahaha'],
                ['14'], ['this is a really good team!'],
                [],
                ['94'], ['this is not a good team!'],
                ['1337'], ['LEC420xd'],
            ],
            [
                200, 404,
                200, 404,
                200,
                200, 404,
                200, 404,
            ],
        )

    def testLeagueExpv4(self):
        logger.debug('LeagueExpv4 property...')
        endpoint = self.hook.league_exp
        self.assertEqual(endpoint.__class__, LeagueExpv4)

    @patch.object(Session, 'get')
    def testLeagueExpv4Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.league_exp,
            [
                'by_queue_tier_division',
                'by_queue_tier_division',
                'by_queue_tier_division',
                'by_queue_tier_division',
            ],
            [
                ['2', '1', '3'],
                ['superSigma', 'based', 'bateman'],
                ['4', '2', '5'],
                ['xdlol', 'tier', '4'],
            ],
            [
                200,
                404,
                200,
                404,
            ],
        )

    def testLeaguev4(self):
        logger.debug('Leaguev4 property...')
        endpoint = self.hook.league
        self.assertEqual(endpoint.__class__, Leaguev4)

    @patch.object(Session, 'get')
    def testLeaguev4Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.league,
            [
                'challenger_by_queue', 'challenger_by_queue',
                'by_summoner_id', 'by_summoner_id',
                'by_queue_tier_division', 'by_queue_tier_division',
                'grandmaster_by_queue', 'grandmaster_by_queue',
                'by_id', 'by_id',
                'master_by_queue', 'master_by_queue',
            ],
            [
                ['2'], ['xdlolhaha'],
                ['1010101'], ['this is my super sigma id'],
                ['2', '1', '3'], ['based', 'bateman', 'gamer'],
                ['1'], ['big man queue'],
                ['1928491841'], ['secret ID dont look'],
                ['1'], ['coffee queue'],
            ],
            [
                200, 404,
                200, 404,
                200, 404,
                200, 404,
                200, 404,
            ],
        )

    def testLolChallengesv1(self):
        logger.debug('LolChallengesv1 property...')
        endpoint = self.hook.challenges
        self.assertEqual(endpoint.__class__, LolChallengesv1)

    @patch.object(Session, 'get')
    def testLolChallengesv1Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.challenges,
            [
                'config',
                'percentiles',
                'challenge_config', 'challenge_config',
                'top_players_for_challenge', 'top_players_for_challenge',
                'top_players_for_challenge',
                'challenge_percentile', 'challenge_percentile',
                'player_data_by_puuid', 'player_data_by_puuid',
            ],
            [
                [],
                [],
                ['400'], ['big banana challenge'],
                ['123', '2'], ['41', '2', '20'],
                ['xd lol ahha', 'avocado'],
                ['85'], ['this is a challenge id i promise'],
                ['91849189481948149'], ['this is my secret puuid'],
            ],
            [
                200,
                200,
                200, 404,
                200, 200,
                404,
                200, 404,
                200, 404,
            ],
        )

    def testLolStatusv4(self):
        logger.debug('LolStatusv4 property...')
        endpoint = self.hook.status
        self.assertEqual(endpoint.__class__, LolStatusv4)

    @patch.object(Session, 'get')
    def testLolStatusv4Respones(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.status,
            ['get'],
            [[]],
            [200],
        )

    def testMatchv5(self):
        logger.debug('Matchv5 property...')
        endpoint = self.hook.match
        self.assertEqual(endpoint.__class__, Matchv5)

    @patch.object(Session, 'get')
    def testMatchv5Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.match,
            [
                'matchlist_by_puuid', 'matchlist_by_puuid',
                'matchlist_by_puuid', 'matchlist_by_puuid',
                'by_id', 'by_id',
                'timeline_by_id', 'timeline_by_id',
            ],
            [
                ['41412081729837'], ['81723871283', '2', '1', '5', '10'],
                ['cookie man'], ['elden ring goty'],
                ['948194'], ['this is a match id i promise'],
                ['9481927'], ['this is not a match id'],
            ],
            [
                200, 200,
                404, 404,
                200, 404,
                200, 404,
            ],
        )

    def testSpectatorv4(self):
        logger.debug('Spectatorv4 property...')
        endpoint = self.hook.spectator
        self.assertEqual(endpoint.__class__, Spectatorv4)

    @patch.object(Session, 'get')
    def testSpectatorv4Respones(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.spectator,
            [
                'by_summoner_id', 'by_summoner_id',
                'featured_games',
            ],
            [
                ['1481274819'], ['baby yoda'],
                [],
            ],
            [
                200, 404,
                200,
            ],
        )

    def testSummonerv4(self):
        logger.debug('Summonerv4 property...')
        endpoint = self.hook.summoner
        self.assertEqual(endpoint.__class__, Summonerv4)

    @patch.object(Session, 'get')
    def testSummonerv4Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.summoner,
            [
                'by_account', 'by_account',
                'by_name', 'by_name',
                'by_puuid', 'by_puuid',
                'by_id', 'by_id',
            ],
            [
                ['f183798f19jk98'], ['slime rancher'],
                ['1 900 976 JUICE'], ['pure4silver'],
                ['981293816471'], ['water man'],
                ['faa89ajhg8ga546124'], ['encrypted summoner id xd'],
            ],
            [
                200, 404,
                200, 404,
                200, 404,
                200, 404,
            ],
        )

    def testTournamentStubv4(self):
        logger.debug('TournamentStubv4 property...')
        endpoint = self.hook.tournament_stub
        self.assertEqual(endpoint.__class__, TournamentStubv4)

    @patch.object(Session, 'get')
    def testTournamentStubv4Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.tournament_stub,
            [
                'codes',
                'events_by_code', 'events_by_code', 
                'providers',
                'tournaments',
            ],
            [
                [],
                ['87149812814'], ['super secret LEC code'],
                [],
                [],
            ],
            [
                200,
                200, 404,
                200,
                200,
            ],
        )

    def testTournamentv4(self):
        logger.debug('Tournamentv4 property...')
        endpoint = self.hook.tournament
        self.assertEqual(endpoint.__class__, Tournamentv4)

    @patch.object(Session, 'get')
    def testTournamentv4Responses(self, mock_get):
        _testEndpointRequests(
            self,
            mock_get,
            self.hook.tournament,
            [
                'codes',
                'dto_by_code', 'dto_by_code',
                'events_by_code', 'events_by_code',
                'providers',
                'tournaments',
            ],
            [
                [],
                ['98afhufy87561287'], ['coderino'],
                ['1927488varf878ga'], ['book book book'],
                [],
                [],
            ],
            [
                200,
                200, 404,
                200, 404,
                200,
                200,
            ],
        )

