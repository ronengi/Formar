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


class InfoTom:
    """Information Atom. Represents a basic unit of information.
    """

    def __init__(self, parent_bond=None, contents=None, level=0, lang_rtl=False, left=0, top=0):
        self._parent_bond = parent_bond
        self._contents = contents
        self._level = level
        self._lang_rtl = lang_rtl
        self._left = left
        self._top = top

    def __str__(self):
        if self._contents is None:
            return ''
        return str(self._contents)

    def is_valid(self):
        pass
