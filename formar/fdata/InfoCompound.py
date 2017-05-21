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

from formar.fdata import InfoTom


class InfoCompound(InfoTom.InfoTom):
    """A higher information unit.
    
    This is a unit of information in itself, which contains other atoms
    or groups.
    It is the same as InfoTom, except in display: it displays all
    information units which link to it, and it has more display options.
    """

    def __init__(self, contents=None, lang_rtl=False,
                 left=0, top=0, width=0, height=0,
                 level=0, parent_bond=None):
        super(InfoCompound, self).__init__(contents, lang_rtl,
                                           left, top, width, height,
                                           level, parent_bond)

    def __str__(self):
        if self.__contents is None:
            return ''
        return str(self.__contents)
