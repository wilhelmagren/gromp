# Gromp [![PyPi version](https://img.shields.io/pypi/v/gromp.svg)](https://pypi.org/project/gromp/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![codecov](https://codecov.io/gh/willeagren/gromp/branch/main/graph/badge.svg?token=52WSCE8Q09)](https://codecov.io/gh/willeagren/gromp)

Gromp is a minimal wrapper of the public [Riot Games developer API](https://developer.riotgames.com/apis), 
written in Python. All public methods as of 2023-02-07 are implemented.

The core princpile of the wrapper is to offer a holistic, yet simple, interface which implements some of the core functionality that a developer might want to communicate with the Riot Games developer API.

For a full list of all available requests, see each respective endpoint documentation.

## :lock: Requirements

- A fairly recent version of Python, preferably 3.7 or greater.
- If installing locally, you need the dependencies found in the [requirements.txt](https://github.com/willeagren/gromp/blob/55a99e52138a7c9f3b5faa446c30bc6b66c9295d/requirements.txt) file.
- To perform requests you need an API key from Riot Games, get yours [here](https://developer.riotgames.com/).

## :package: Installation

Either clone this repository and perform a local install accordingly
```
git clone https://github.com/willeagren/gromp.git
cd gromp
pip install -e .
```
or install the most recent release from the Python Package Index (PyPI).
```
pip install gromp
```


## :rocket: Example usage
Any HTTP errors that are returned by the requested API are propagated and, as of writing this, not handled.
```python
import gromp
from gromp.utils import LeaguePlatforms, LeagueRegions

platform = LeaguePlatforms.euw1
region = LeagueRegions.europe
token = '<api-key>'

# Here we setup a hook for League of Legends. We specify platform and region
# to perform all REST requests to, the length of the RSA keys used to encrypt
# out token, and the number of seconds to wait before a timeout.
hook = gromp.League(
    token,
    platform=platform,
    region=region,
    keylen=1024,
    timeout=10,
)

# One of the default handlers parses the HTTP response as a JSON
# dictionary, see all available attributes for the object at the
# Riot Games API documentation, https://developer.riotgames.com/apis
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

asssert len(matches) == 5

# Now we can request the match data for all the match id's which we
# got from the previous request. This is unfortunately the only 
# process of getting specific match data... it is rather tedious.
for match_id in matches:
    m = hook.match.by_id(match_id)
    for participant in m['info']['participants']:
        if participant['puuid'] == summoner['puuid']:
            print(participant['win'])

```

## :bulb: Gromp facts
His real name is Lord Grompulus Kevin Ribbiton of Croaksworth, and he likes to eat small insects, mushrooms, and people ([source](https://leagueoflegends.fandom.com/wiki/Gromp)). 

## :clipboard: License
All code is to be held under a general MIT license, please see [LICENSE](https://github.com/willeagren/gromp/blob/main/LICENSE) for specific information.

