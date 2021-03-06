#!/usr/bin/python

"""
    Copyright 2017 Ronen Gilead-Raz

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


class PageFooter:
    """Flexible HTML footer generator
    """

    _message = ''

    def __init__(self, message=''):
        self._message = message

    def __str__(self):
        footer_lines = []
        if self._message:
            footer_lines.append(self._message)
        footer_lines.append('<div id="alerter" class="alerter">alerter</div>')
        footer_lines.append('{0}</body>'.format(' ' * 4))
        footer_lines.append('</html>')
        return "\n".join(footer_lines)
