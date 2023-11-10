<div align="center">
<br/>
<div align="left">
<br/>
<p align="center">
<a href="https://github.com/wilhelmagren/gromp">
<img align="center" width=75% src="./docs/images/gromp-banner.png"></img>
</a>
</p>
</div>

[![PyPI - Version](https://img.shields.io/pypi/v/gromp)](https://pypi.org/project/gromp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/wilhelmagren/gromp/branch/main/graph/badge.svg?token=52WSCE8Q09)](https://codecov.io/gh/willeagren/gromp)
[![CI](https://github.com/wilhelmagren/gromp/actions/workflows/ci.yml/badge.svg)](https://github.com/wilhelmagren/gromp/actions/workflows/ci.yml)
[![CD](https://github.com/wilhelmagren/gromp/actions/workflows/cd.yml/badge.svg)](https://github.com/wilhelmagren/gromp/actions/workflows/cd.yml)
[![Tests](https://github.com/wilhelmagren/gromp/actions/workflows/tests.yml/badge.svg)](https://github.com/wilhelmagren/gromp/actions/workflows/tests.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Lint style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

</div>

## 🔎 Overview
*gromp* is a holistic wrapper of the public [Riot Games developer API](https://developer.riotgames.com/apis), 
written in Python. **All public methods are, as of 2023-11-10, implemented.**

The core principle of the wrapper is to offer a complete, yet simple, interface which implements some of the core functionality that a developer might want to communicate with the Riot Games developer API.

For a full list of all available requests, see each respective endpoint documentation.

## 🔑 Requirements

- To perform requests you need an API key from Riot Games, get yours [here](https://developer.riotgames.com/).

## 📦 Installation
Either clone this repository and perform a local install with [poetry](https://github.com/python-poetry/poetry/tree/master) accordingly
```
git clone https://github.com/wilhelmagren/gromp.git
cd gromp
poetry install
```
or install the most recent release from the Python Package Index (PyPI).
```
pip install gromp
```


## 🚀 Example usage
Any HTTP errors that are returned by the requested API are propagated and, as of writing this, not handled.
```python
import gromp
from gromp import (
    LeaguePlatforms,
    LeagueRegions,
)

platform = LeaguePlatforms.euw1
region = LeagueRegions.EUROPE
token = '<api-key>'

# Here we setup a hook for League of Legends. We specify platform and region
# to perform all REST requests to, the length of the RSA keys used to encrypt
# our token, and the number of seconds to wait before a timeout.
hook = gromp.hook.League(
    token,
    platform=platform,
    region=region,
    keylen=1024,
    timeout=10,
)

# One of the default handlers parses the HTTP response as a JSON
# dictionary, see all available attributes for the object at the
# Riot Games API documentation https://developer.riotgames.com/apis
summoner = hook.summoner.by_name('1 900 976 JUICE')

# We can also get the summoner if we know the encrypted
# puuid, lets try and see if they are actually the same...
summoner_from_puuid = hook.summoner.by_puuid(summoner['puuid'])

assert summoner == summoner_from_puuid

# Great, we get the same summoner, me. Let's try and get
# some of my played games from the match API endpoint.
matches = hook.match.matchlist_by_puuid(
    summoner['puuid'],
    start=10,
    count=5,
)

assert len(matches) == 5

# Now we can request the match data for all the match id's which we
# got from the previous request. This is unfortunately the only 
# process of getting specific match data... it is rather tedious.
for match_id in matches:
    m = hook.match.by_id(match_id)
    for participant in m['info']['participants']:
        if participant['puuid'] == summoner['puuid']:
            print(participant['win'])

```

## 💡 Gromp facts
His real name is Lord Grompulus Kevin Ribbiton of Croaksworth, and he likes to eat small insects, mushrooms, and people ([source](https://leagueoflegends.fandom.com/wiki/Gromp)). 

## 📋 License
All code is to be held under a general MIT license, please see [LICENSE](https://github.com/willeagren/gromp/blob/main/LICENSE) for specific information.

