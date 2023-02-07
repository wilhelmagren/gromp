![Gromp](https://github.com/willeagren/gromp/blob/2b4d6727a5d1470f183739e27c62df6744d2ad66/assets/gromp.png)
# Gromp [![PyPi version](https://img.shields.io/pypi/v/gromp.svg)](https://pypi.org/project/gromp/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Gromp is a minimal wrapper of the public [Riot Games developer API](https://developer.riotgames.com/apis), 
written in Python. All public methods as of 2023-02-02 are implemented.

The core princpile of the wrapper is to offer a simple user interface which implements the core functionality 
that a developer might want to communicate with the Riot Games developer API. In practice you operate with hooks based 
on the game you are performing REST requests to. 

For a full list of all available requests, see the respective games hook documentation.

## Setup
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

## Example usage
```python
from gromp import LeagueHook
from gromp.utils import LeaguePLATFORMS, LeagueREGIONS

platform = LeaguePLATFORMS.euw1
region = LeagueREGIONS.europe
token = '<api-key>'

hook = LeagueHook(token, platform=platform, region=region)

# The objects are returned as json objects (dictionaries)
# as per the specification on the official Riot API.
summoner = hook.summoner_by_name('1 900 976 JUICE')

# We can also get the summoner if we know the encrypted
# puuid, lets try and see if they are actually the same...
summoner_from_puuid = hook.summoner_by_puuid(summoner['puuid'])

assert summoner == summoner_from_puuid

# Great, we get the same summoner, me. Let's try and get
# some of my played games from the match API endpoint.
matches = hook.matches_by_puuid(
    summoner['puuid'],
    count=10,
)

# Now we can request the match data for all the match id's
# which we got from above. This is unfortunately the only
# process of getting match history data... rather tedious.
for match_id in matches:
    m = hook.match_by_id(match_id)
    for participant in m['info']['participants']:
        if participant['puuid'] == summoner['puuid']:
            print(participant['win'])


```

## Gromp facts
His real name is Lord Grompulus Kevin Ribbiton of Croaksworth, and he likes to eat small insects, mushrooms, and people ([source](https://leagueoflegends.fandom.com/wiki/Gromp)). 

## License
All code is to be held under a general MIT license, please see [LICENSE](https://github.com/willeagren/gromp/blob/main/LICENSE) for specific information. Any images used are neither owned nor monetized by me, and retains the specific license it was created with.
