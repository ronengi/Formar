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


from formar.fdata.InfoTom import InfoTom
from formar.fdata.InfoCompound import InfoCompound


class Bond:

    def __init__(self, b_id=0, infotom1=None, infotom2=None, level=0, description=''):
        self.__b_id = b_id
        self.__infotom1 = infotom1
        self.__infotom2 = infotom2
        self.__level = level
        self.__description = description

    def __str__(self):
        try:
            return str(self.__description)
        except (AttributeError, TypeError):
            # no such attribute or None
            return ''

    def __eq__(self, other):
        if not isinstance(other, Bond):
            return False
        if self.get_infotom1() == other.get_infotom1() \
                and self.get_infotom2() == other.get_infotom2() \
                and self.get_level() == other.get_level() \
                and self.get_description() == other.get_description():
            return True
        return False

    def get_b_id(self):
        try:
            return self.__b_id
        except (AttributeError, TypeError):
            # no such attribute or None
            return None

    def get_infotom1(self):
        try:
            return self.__infotom1
        except (AttributeError, TypeError):
            # no such attribute or None
            return None

    def get_infotom2(self):
        try:
            return self.__infotom2
        except (AttributeError, TypeError):
            # no such attribute or None
            return None

    def get_level(self):
        try:
            return int(self.__level)
        except (AttributeError, TypeError):
            # no such attribute or None
            return 0

    def get_description(self):
        try:
            return str(self.__description)
        except (AttributeError, TypeError):
            # no such attribute or None
            return ''

    def encode(self):
        return dict(__Bond__=dict(
            b_id=self.get_b_id(),
            infotom1=self.get_infotom1(),
            infotom2=self.get_infotom2(),
            description=self.get_description()))

    @staticmethod
    def decode(j_dict):
        try:
            j_dict_bond = j_dict['__Bond__']
        except KeyError:
            return None

        try:
            b_b_id = j_dict_bond['b_id']
        except KeyError:
            b_b_id = None

        try:
            b_infotom1 = j_dict_bond['infotom1']
        except KeyError:
            b_infotom1 = None

        try:
            b_infotom2 = j_dict_bond['infotom2']
        except KeyError:
            b_infotom2 = None

        try:
            b_description = j_dict_bond['description']
        except KeyError:
            b_description = ''

        b = Bond(b_id=b_b_id, infotom1=b_infotom1, infotom2=b_infotom2
                 , description=b_description)
        return b

