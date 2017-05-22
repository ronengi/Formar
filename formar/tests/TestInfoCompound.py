#!/usr/bin/python

import unittest
from formar.fdata.InfoCompound import InfoCompound


class TestInfoCompound(unittest.TestCase):

    def test_str(self):
        ic = InfoCompound(it_id=123, contents='vim', lang_rtl=True,
                          left=12, top=34, width=56, height=78,
                          parent_bond=None)
        self.assertEqual(str(ic), 'vim')

    def test_encode(self):
        ic = InfoCompound(it_id=123, contents='vim', lang_rtl=True,
                          left=12, top=34, width=56, height=78,
                          parent_bond=None)
        j_dict = {'__InfoCompound__': {'it_id': 123, 'contents': 'vim', 'lang_rtl': True, 'left': 12, 'top': 34, 'width': 56, 'height': 78, 'parent_bond': None}}
        self.assertEqual(ic.encode(), j_dict)

    def test_decode(self):
        ic = InfoCompound(it_id=123, contents='vim', lang_rtl=True,
                          left=12, top=34, width=56, height=78,
                          parent_bond=None)
        j_dict = {'__InfoCompound__': {'it_id': 123, 'contents': 'vim', 'lang_rtl': True, 'left': 12, 'top': 34, 'width': 56, 'height': 78, 'parent_bond': None}}

        self.assertEqual(InfoCompound.decode(j_dict), ic)

if __name__ == '__main__':
    unittest.main()
