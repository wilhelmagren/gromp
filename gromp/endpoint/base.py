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

File created: 2023-02-05
Last updated: 2023-02-06
"""

import rsa
from rsa import PublicKey, PrivateKey
from requests import Response, session
from gromp.url import Url

class NamedEndpoint(object):
    def __init__(
        self,
        token: str,
        keys: dict,
        handlers: list,
        platform: str,
        region: str,
        timeout: int,
        **kwargs
    ) -> None:

        assert isinstance(keys['public'], PublicKey), \
            f'Provided rsa public key is not a PublicKey, {keys["public"]}.'
        assert isinstance(keys['private'], PrivateKey), \
            f'Provided rsa private key is not a PrivateKey, {keys["private"]}.'

        config = {}
        config['token'] = self._encrypt_token(token, keys['public'])
        config['platform'] = platform
        config['region'] = region
        config['keys'] = keys
        config['timeout'] = timeout
        self._config = config
        self._handlers = handlers
        self._session = session()

    def _encrypt_token(self, token: str, key: PublicKey) -> str:
        return rsa.encrypt(
            token.encode(),
            key,
        )

    def _decrypt_token(self) -> str:
        return rsa.decrypt(
            self._config['token'],
            self._config['keys']['private'],
        )

    def _request_api(
        self,
        api: Url,
        **kwargs
    ) -> Response:
        request, params = api.prepare_request(
            platform=self._config['platform'],
            region=self._config['region'],
            **kwargs,
        )

        extra = {}
        extra['timeout'] = self._config['timeout']
        response = self._session.get(
            request,
            params=params,
            headers={'X-Riot-Token': self._decrypt_token()},
            **extra,
        )

        return response

