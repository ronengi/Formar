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


import json


class InfoTom:
    """Information Atom. Represents a basic unit of information.
    """

    def __init__(self, contents=None, lang_rtl=False,
                 left=0, top=0,
                 level=0, parent_bond=None):
        self._contents = contents
        self._lang_rtl = lang_rtl
        self._left = left
        self._top = top
        self._level = level
        self._parent_bond = parent_bond

    def __str__(self):
        if self._contents is None:
            return ''
        return str(self._contents)

    # todo: this is very useful function to implement
    def is_valid(self):
        pass

    # todo: _contents may be any kind of object
    def get_contents(self):
        if '_contents' not in vars(self):
            return None
        return str(self._contents)

    def get_lang_rtl(self):
        if '_lang_rtl' not in vars(self):
            return False
        return bool(self._lang_rtl)

    def get_left(self):
        if '_left' not in vars(self) or self._left is None:
            return 0
        return int(self._left)

    def get_top(self):
        if '_top' not in vars(self) or self._top is None:
            return 0
        return int(self._top)

    def get_level(self):
        if '_level' not in vars(self) or self._level is None:
            return 0
        return int(self._level)

    # todo: return self._parent_bond.encode()
    # todo: implement parent_bond with encode() method !
    def get_parent_bond(self):
        if '_parent_bond' not in vars(self):
            return None
        return self._parent_bond

    def encode(self):
        return json.dumps(dict(
            Class='InfoTom'
            , contents=self.get_contents()
            , lang_rtl=self.get_lang_rtl()
            , left=self.get_left()
            , top=self.get_top()
            , level=self.get_level()
            , parent_bond=self.get_parent_bond()))

    @staticmethod
    def decode(j_str):
        j_dict = json.loads(j_str)
        if j_dict['Class'] != 'InfoTom':
            # todo: raise an exception
            return None
        # todo: take care of parent_bond decoding here
        it = InfoTom(contents=j_dict['contents']
                     , lang_rtl=j_dict['lang_rtl']
                     , left=j_dict['left']
                     , top=j_dict['top']
                     , level=j_dict['level']
                     , parent_bond=j_dict['parent_bond'])
        return it

