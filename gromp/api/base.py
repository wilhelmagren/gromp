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
# File created: 2023-01-23
# Last updated: 2023-01-31
#

import logging
import sys
import requests

strformat = '%(asctime)s %(message)s'
logging.basicConfig(
    level=logging.DEBUG,
    format=strformat,
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

__all__ = (
    'BaseAPI',
    'BaseLeagueAPI',
    'BaseValorantAPI',
)

class BaseAPI(object):
    def __init__(self, game, api, platform, region) -> None:
        self._game = game
        self._api = api
        self._platform = platform
        self._region = region

    @property
    def platform(self) -> str:
        """ Return the set API platform, e.g., euw1 for League of Legends. """
        return self._platform
    
    @property
    def region(self) -> str:
        """ Return the set API region, e.g., europe for League of Legends. """
        return self._region

    @property
    def params(self) -> dict:
        """ Return the internal parameter dictionary. """
        return self._params

    def set_params(self, **kwargs) -> None:
        """
        Set the internal parameter dictionary with the provided key-value pairs.
        For example, `region`: `europe`, or `platform`: `euw1`.

        Parameters
        ----------
        **kwargs: dict
            The dictionary of parameters which is later used in the substitution
            during the GET request. Keys are subtituted for corresponding values.

        """
        params = {}
        for k, value in kwargs.items():
            key = '{' + f'{k}' + '}'
            params[key] = value

        self._params = params
    
    def get(self, token, endpoint) -> requests.Response:
        """
        Perform a GET request to the REST endpoint provided by Riot Games.
        The token required is never stored internally, as it is personal.

        Parameters
        ----------
        token: str
            The token identifying your access rights to the Riot Games
            developer api, personal, provided at runtime to Hook.
        endpoint: str
            The api endpoint to perform a GET request to.
        
        Returns
        -------
        The HTTP response from the GET request to the endpoint. See
        requests.Response for all possible HTTP response codes.

        """
        url = f'https://{endpoint}?api_key={token}'

        for key, value in self.params.items():
            url = url.replace(key, value)
        
        response = requests.get(url)

        return response

class BaseLeagueAPI(BaseAPI):
    """ """
    def __init__(self, api, platform, region) -> None:
        super().__init__('league', api, platform, region)

class BaseValorantAPI(BaseAPI):
    """ """
    def __init__(self, api, platform, region) -> None:
        super().__init__('valorant', api, platform, region)
