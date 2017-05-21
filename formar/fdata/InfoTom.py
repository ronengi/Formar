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
                 left=0, top=0, width=0, height=0,
                 level=0, parent_bond=None):
        self.__contents = contents
        self.__lang_rtl = lang_rtl
        self.__left = left
        self.__top = top
        self.__width = width
        self.__height = height
        self.__level = level
        self.__parent_bond = parent_bond

    def __str__(self):
        try:
            return str(self.__contents)
        except (AttributeError, TypeError):
            # no such attribute or None
            return ''

    # todo: __contents may be any kind of object
    def get_contents(self):
        try:
            return str(self.__contents)
        except (AttributeError, TypeError):
            # no such attribute or None
            return ''

    def get_lang_rtl(self):
        try:
            return bool(self.__lang_rtl)
        except (AttributeError, TypeError):
            # no such attribute or None
            return False

    def get_left(self):
        try:
            return int(self.__left)
        except (AttributeError, TypeError):
            # no such attribute or None
            return 0

    def get_top(self):
        try:
            return int(self.__top)
        except (AttributeError, TypeError):
            # no such attribute or None
            return 0

    def get_width(self):
        try:
            return int(self.__width)
        except (AttributeError, TypeError):
            # no such attribute or None
            return 0

    def get_height(self):
        try:
            return int(self.__height)
        except (AttributeError, TypeError):
            # no such attribute or None
            return 0

    def get_level(self):
        try:
            return int(self.__level)
        except (AttributeError, TypeError):
            # no such attribute or None
            return 0

    # todo: return self.__parent_bond.encode()
    # todo: implement parent_bond with encode() method !
    def get_parent_bond(self):
        try:
            return self.__parent_bond
        except (AttributeError, TypeError):
            # no such attribute or None
            return None

    def encode(self):
        return json.dumps(dict(
            Class='InfoTom'
            , contents=self.get_contents()
            , lang_rtl=self.get_lang_rtl()
            , left=self.get_left()
            , top=self.get_top()
            , width=self.get_width()
            , height=self.get_height()
            , level=self.get_level()
            , parent_bond=self.get_parent_bond()))

    # @staticmethod
    # def decode(j_str):
    #     j_dict = json.loads(j_str)
    @staticmethod
    def decode(j_dict):
        # if j_dict['Class'] != 'InfoTom':
        # todo: raise an exception
        #   return None
        # todo: take care of parent_bond decoding here
        it = InfoTom(contents=j_dict['contents']
                     , lang_rtl=j_dict['lang_rtl']
                     , left=j_dict['left']
                     , top=j_dict['top']
                     , width=j_dict['width']
                     , height=j_dict['height']
                     , level=j_dict['level']
                     , parent_bond=j_dict['parent_bond'])
        return it

