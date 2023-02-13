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
Last updated: 2023-02-14
"""

import rsa
from gromp.utils import (
    is_platform,
    is_region,
    Platforms,
    Regions,
)
from gromp.endpoint.base import NamedEndpoint
from gromp.handler.log import LogHandler
from gromp.handler.json import JsonHandler

__all__ = (
    'Hook',
)

class Hook(object):
    def __init__(
        self,
        token: str = None,
        game: str = None,
        platform: str = None,
        region: str = None,
        handlers: list = None,
        keylen: int = 512,
        timeout: int = 5,
        **kwargs
    ) -> None:

        assert is_platform(platform, game.lower()), \
            f'User provided platform is not valid, {platform=}.\n' \
            f'Valid platforms are: {vars(getattr(PLATFORMS, game)).values()}.'

        assert is_region(region, game.lower()), \
            f'User provided region is not valid, {region=}.\n' \
            f'Valid regions are: {vars(getattr(REGIONS, game)).values()}.'

        assert timeout > 0, \
            f'You have provided a timeout value <= 0 which is not valid.\n' \
            f'This sets the allowed time to wait for response, defaults to 5 seconds.'

        public_key, private_key = rsa.newkeys(keylen)
        encrypted_token = rsa.encrypt(
            token.encode(),
            public_key,
        )

        if handlers is None:
            handlers = [
                LogHandler(),
                JsonHandler(),
            ]

        keys = {}
        keys['public'] = public_key
        keys['private'] = private_key

        config = {}
        config['token'] = encrypted_token
        config['game'] = game
        config['platform'] = platform
        config['region'] = region
        config['keys'] = keys
        config['timeout'] = timeout
        self._config = config
        self._handlers = handlers

    @property
    def token(self) -> str:
        return rsa.decrypt(
            self._config['token'],
            self._config['keys']['private'],
        ).decode()

    @property
    def game(self) -> str:
        return self._config['game']

    @property
    def platform(self) -> str:
        return self._config['platform']
    
    @property
    def region(self) -> str:
        return self._config['region']

    @property
    def timeout(self) -> int:
        return self._config['timeout']

    @property
    def keys(self) -> dict:
        return self._config['keys']

    @property
    def public_key(self) -> rsa.PublicKey:
        return self._config['keys']['public_key']

    @property
    def config(self) -> dict:
        return self._config

    @property
    def handlers(self) -> list:
        return self._handlers

    def _setup_named_endpoint(
        self,
        endpoint: NamedEndpoint,
        **kwargs
    ) -> NamedEndpoint:
        """ """
        return endpoint(
            self.token,
            self.keys,
            self.handlers,
            self.platform,
            self.region,
            self.timeout,
            **kwargs,
        )

