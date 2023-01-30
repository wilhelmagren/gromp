#
# MIT License
#
# Copyright (c) 2023 Wilhelm Ågren
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# File created: 2023-01-30
# Last updated: 2023-01-30
#

__all__ = (
    'LeaguePLATFORMS',
    'LeagueREGIONS',
    'PLATFORMS',
    'REGIONS',
    'is_platform',
    'is_region',
)

class LeaguePLATFORMS:
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

class LeagueREGIONS:
    americas = 'americas'
    asia = 'asia'
    europe = 'europe'
    sea = 'sea'

class PLATFORMS:
    league = LeaguePLATFORMS

class REGIONS:
    league = LeagueREGIONS

def is_platform(string, game) -> bool:
    """ Return `true` if the provided string is a valid platform, else `false`. """
    return string in vars(getattr(PLATFORMS, game)).values()

def is_region(string, game) -> bool:
    """ Return `true` if the provided string is a valid region, else `false`. """
    return string in vars(getattr(REGIONS, game)).values()
