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
Last updated: 2023-02-15
"""

from __future__ import annotations

import builtins
import rsa
from rsa import PublicKey, PrivateKey
from requests import Response, session
from typing import (
    Dict,
    List,
    NoReturn,
)
from gromp.api.base import Api

String = builtins.str
Integer = builtins.int

__all__ = (
    'NamedEndpoint',
)

class NamedEndpoint(object):
    def __init__(
        self: NamedEndpoint,
        token: String,
        keys: Dict,
        handlers: List,
        platform: String,
        region: String,
        timeout: Integer,
        **kwargs: Dict,
    ) -> NoReturn:

        assert isinstance(keys['public'], PublicKey), \
            f'Provided rsa public key is not a PublicKey, {keys["public"]}.'

        assert isinstance(keys['private'], PrivateKey), \
            f'Provided rsa private key is not a PrivateKey.'

        config = {}
        config['token'] = self._encrypt_token(token, keys['public'])
        config['platform'] = platform
        config['region'] = region
        config['keys'] = keys
        config['timeout'] = timeout
        self._config = config
        self._handlers = handlers
        self._session = session()

    @staticmethod
    def _encrypt_token(token: String, public_key: PublicKey) -> String:
        return rsa.encrypt(
            token.encode(),
            public_key,
        )

    def _decrypt_token(self) -> String:
        return rsa.decrypt(
            self._config['token'],
            self._config['keys']['private'],
        )

    def _request_api(self, api: Api, **kwargs: Dict) -> Response:
        """ Perform a GET request to the provided REST api. """
        request, params = api.prepare_request(
            platform=self._config['platform'],
            region=self._config['region'],
            **kwargs,
        )

        extra = {}
        extra['timeout'] = self._config['timeout']
        
        for handler in self._handlers:
            handler_result = handler.outgoing_request(
                self._config['platform'],
                self._config['region'],
                params,
                self.__class__.__name__,
                request,
                **extra,
            )

            if isinstance(handler_result, str):
                request = handler_result

        response = self._session.get(
            request,
            params=params,
            headers={
                'Accept-Language': 'en-US,en;q=0.5',
                'X-Riot-Token': self._decrypt_token(),
            },
            **extra,
        )

        for handler in self._handlers:
            response = handler.incoming_response(
                self._config['platform'],
                self._config['region'],
                params,
                self.__class__.__name__,
                response,
                **extra,
            )

        return response

