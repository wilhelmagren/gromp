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

File created: 2023-01-23
Last updated: 2023-02-13
"""

from gromp.hook.base import Hook
from gromp.endpoint import NamedEndpoint
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

__all__ = (
    'League',
)

class League(Hook):
    def __init__(self, token: str, **kwargs) -> None:
        super(League, self).__init__(
            token=token,
            game=self.__class__.__name__,
            **kwargs
        )
    
    @property
    def mastery(self) -> ChampionMasteryv4:
        return self._setup_named_endpoint(ChampionMasteryv4)

    @property
    def champion(self) -> Championv3:
        return self._setup_named_endpoint(Championv3)
    
    @property
    def clash(self) -> Clashv1:
        return self._setup_named_endpoint(Clashv1)
    
    @property
    def league_exp(self) -> LeagueExpv4:
        return self._setup_named_endpoint(LeagueExpv4)

    @property
    def league(self) -> Leaguev4:
        return self._setup_named_endpoint(Leaguev4)

    @property
    def challenges(self) -> LolChallengesv1:
        return self._setup_named_endpoint(LolChallengesv1)

    @property
    def status(self) -> LolStatusv4:
        return self._setup_named_endpoint(LolStatusv4)

    @property
    def match(self) -> Matchv5:
        return self._setup_named_endpoint(Matchv5)

    @property
    def spectator(self) -> Spectatorv4:
        return self._setup_named_endpoint(Spectatorv4)

    @property
    def summoner(self) -> Summonerv4:
        return self._setup_named_endpoint(Summonerv4)

    @property
    def tournament_stub(self) -> TournamentStubv4:
        return self._setup_named_endpoint(TournamentStubv4)

    @property
    def tournament(self) -> Tournamentv4:
        return self._setup_named_endpoint(Tournamentv4)

