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
Last updated: 2023-02-15
"""

import builtins
String = builtins.str
Boolean = builtins.bool

from typing import Optional

__all__ = (
    'is_platform',
    'is_region',
    'platform_to_region',
    'LeaguePlatforms',
    'LeagueRegions',
    'ValorantRegions',
    'AccountsRegions',
    'Platforms',
    'Regions',
)

def is_platform(string: String, game: String) -> Boolean:
    """ Return true if the string is a valid platform for the specified game. """
    return string in vars(getattr(Platforms, game)).values()

def is_region(string: String, game: String) -> Boolean:
    """ Return true if the string is a valid region for the specified game. """
    return string in vars(getattr(Regions, game)).values()

def platform_to_region(platform: String) -> Optional[String]:
    """ Map the provided platform to its related region, return it as a string. """
    p2r = {
        'br1': 'americas',
        'eun1': 'europe',
        'euw1': 'europe',
        'jp1': 'asia',
        'kr': 'asia',
        'la1': 'americas',
        'la2': 'americas',
        'na1': 'americas',
        'oc1': 'sea',
        'tr1': 'europe',
        'ru': 'europe',
        'ph2': 'asia',
        'sg2': 'asia',
        'th2': 'asia',
        'tw2': 'asia',
        'vn2': 'asia',
    }
    return p2r.get(platform, None)

class LeaguePlatforms:
    br1 = 'br1'
    eun1 = 'eun1'
    euw1 = 'euw1'
    jp1 = 'jp1'
    kr = 'kr'
    la1 = 'la1'
    la2 = 'la2'
    na1 = 'na1'
    oc1 = 'oc1'
    tr1 = 'tr1'
    ru = 'ru'
    ph2 = 'ph2'
    sg2 = 'sg2'
    th2 = 'th2'
    tw2 = 'tw2'
    vn2 = 'vn2'

class LeagueRegions:
    americas = 'americas'
    asia = 'asia'
    europe = 'europe'
    sea = 'sea'

class ValorantRegions:
    AP = 'AP'
    BR = 'BR'
    ESPORTS = 'ESPORTS'
    EU = 'EU'
    KR = 'KR'
    LATAM = 'LATAM'
    NA = 'NA'

class AccountsRegions:
    AMERICAS = 'AMERICAS'
    ASIA = 'ASIA'
    ESPORTS = 'ESPORTS'
    EUROPE = 'EUROPE'

class Platforms: 
    league = LeaguePlatforms

class Regions:
    league = LeagueRegions
    valorant = ValorantRegions
    accounts = AccountsRegions

