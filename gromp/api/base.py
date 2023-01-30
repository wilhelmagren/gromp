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
# Last updated: 2023-01-23
#

import logging
import sys
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

__all__ = (
    'BaseAPI',
    'BaseLeagueAPI',
    'BaseValorantAPI',
)

class BaseAPI(object):
    def __init__(self, game, api, platform, region):
        self._game = game
        self._api = api
        self._platform = platform
        self._region = region

    @property
    def platform(self):
        return self._platform
    
    @property
    def region(self):
        return self._region

    @property
    def params(self):
        return self._params

    def set_params(self, **kwargs):
        """ Set the interally stored parameter dictionary. """
        params = {}
        for k, value in kwargs.items():
            key = '{' + f'{k}' + '}'
            params[key] = value

        self._params = params
    
    def get(self, token, endpoint):
        """ Perform a GET request. """
        url = f'https://{endpoint}?api_key={token}'

        for key, value in self.params.items():
            url = url.replace(key, value)
        
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=Retry)
        session.mount('https://', adapter)

        logger.info(f'GET {url}')
        response = session.get(url)
        return response

class BaseLeagueAPI(BaseAPI):
    def __init__(self, api, platform, region):
        super().__init__('league', api, platform, region)

class BaseValorantAPI(BaseAPI):
    def __init__(self, api, platform, region):
        super().__init__('valorant', api, platform, region)
