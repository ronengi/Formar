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

    def __init__(self, it_id=0, contents=None, lang_rtl=False,
                 left=0, top=0, width=0, height=0, parent_bond=None):
        self.__it_id = it_id
        self.__contents = contents
        self.__lang_rtl = lang_rtl
        self.__left = left
        self.__top = top
        self.__width = width
        self.__height = height
        self.__parent_bond = parent_bond

    def __str__(self):
        try:
            return str(self.__contents)
        except (AttributeError, TypeError):
            # no such attribute or None
            return ''

    def __eq__(self, other):
        if not isinstance(other, InfoTom):
            return False
        if self.get_contents() == other.get_contents() \
            and self.get_lang_rtl() == other.get_lang_rtl() \
            and self.get_left() == other.get_left() \
            and self.get_top() == other.get_top() \
            and self.get_width() == other.get_width() \
            and self.get_height() == other.get_height() \
            and self.get_parent_bond() == other.get_parent_bond():
            return True
        return False

    def get_it_id(self):
        try:
            return int(self.__it_id)
        except (AttributeError, TypeError):
            # no such attribute or None
            return 0

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

    # todo: return self.__parent_bond.encode()
    # todo: implement parent_bond with encode() method !
    def get_parent_bond(self):
        try:
            return self.__parent_bond
        except (AttributeError, TypeError):
            # no such attribute or None
            return None

    def encode(self):
        return dict(__InfoTom__=dict(
            it_id=self.get_it_id()
            , contents=self.get_contents()
            , lang_rtl=self.get_lang_rtl()
            , left=self.get_left()
            , top=self.get_top()
            , width=self.get_width()
            , height=self.get_height()
            , parent_bond=self.get_parent_bond()))

    @staticmethod
    def decode(j_dict):

        try:
            j_dict_infotom = j_dict['__InfoTom__']
        except KeyError:
            return None

        try:
            it_it_id = j_dict_infotom['it_id']
        except KeyError:
            it_it_id = 0

        try:
            it_contents = j_dict_infotom['contents']
        except KeyError:
            it_contents = None

        try:
            it_lang_rtl = j_dict_infotom['lang_rtl']
        except KeyError:
            it_lang_rtl=False

        try:
            it_left = j_dict_infotom['left']
        except KeyError:
            it_left = 0

        try:
            it_top = j_dict_infotom['top']
        except KeyError:
            it_top = 0

        try:
            it_width = j_dict_infotom['width']
        except KeyError:
            it_width = 0

        try:
            it_height = j_dict_infotom['height']
        except KeyError:
            it_height = 0

        try:
            # todo: take care of parent_bond decoding here
            it_parent_bond = j_dict_infotom['parent_bond']
        except KeyError:
            it_parent_bond = None

        it = InfoTom(it_id=it_it_id, contents=it_contents, lang_rtl=it_lang_rtl
                     , left=it_left, top=it_top
                     , width=it_width, height=it_height
                     , parent_bond=it_parent_bond)
        return it

