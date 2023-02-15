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

File created: 2023-02-06
Last updated: 2023-02-15
"""

from __future__ import annotations

import builtins
String = builtins.str

from typing import Dict
from requests import Response
from gromp.handler.base import Handler

import logging
logger = logging.getLogger(__name__)

__all__ = (
    'LogHandler',
)

class LogHandler(Handler):
    def outgoing_request(
        self: LogHandler,
        platform: String,
        region: String,
        params: Dict,
        endpoint: String,
        request: String,
        **kwargs: Dict,
    ) -> String:
        logger.info(
            f'Preparing request {request} to endpoint {endpoint}.'
        )
        return request

    def incoming_response(
        self: LogHandler,
        platform: String,
        region: String,
        params: Dict,
        endpoint: String,
        response: Response,
        **kwargs: Dict,
    ) -> Response:
        logger.info(
            f'Got response {response} from endpoint {endpoint}.'
        )
        return response

