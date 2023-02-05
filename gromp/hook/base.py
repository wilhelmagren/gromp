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
Last updated: 2023-02-05
"""

import rsa
from gromp.utils import (
    is_platform,
    is_region,
    PLATFORMS,
    REGIONS,
)
from gromp.endpoint import NamedEndpoint

__all__ = (
    'Hook',
)

class Hook(object):
    def __init__(
        self,
        token: str,
        game: str,
        platform: str,
        region: str,
        keylen: int = 512,
        timeout: int = 5,
        **kwargs
    ) -> None:

        assert is_platform(platform, game), \
            f'User provided platform is not valid, {platform=}. ' \
            f'Valid platforms are: {PLATFORMS}'
        assert is_region(region, game), \
            f'User provided region is not valid, {region=}. ' \
            f'Valid regions are: {REGIONS}'
        assert timeout > 0, \
            f'You have provided a timeout value <= 0 which is not valid, ' \
            f'This is the allowed time to wait for response, defaults to 5 second.'

        public_key, private_key = rsa.newkeys(keylen)
        encrypted_token = rsa.encrypt(
            token.encode(),
            public_key,
        )

        # TODO implement handlers and specify default sequential orders...
        handler_chain = [
            '.',
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
        self._handlers = handler_chain

    @property
    def token(self) -> str:
        return rsa.decrypt(
            self._config['token'],
            self._config['private_key'],
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
    def public_key(self) -> rsa.PublicKey:
        return self._config['keys']['public_key']

    @property
    def config(self) -> dict:
        return self._config

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
            **kwargs,
        )






