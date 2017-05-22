#!/usr/bin/python

import unittest
from formar.fdata.InfoCompound import InfoCompound


class TestInfoCompound(unittest.TestCase):

    def test_str(self):
        ic = InfoCompound(contents='vim', lang_rtl=True,
                          left=12, top=34, width=56, height=78,
                          level=2, parent_bond=None)
        self.assertEqual(str(ic), 'vim')

    def test_encode(self):
        ic = InfoCompound(contents='vim', lang_rtl=True,
                          left=12, top=34, width=56, height=78,
                          level=2, parent_bond=None)
        j_dict = {'__InfoTom__': {'contents': 'vim', 'lang_rtl': True, 'left': 12, 'top': 34, 'width': 56, 'height': 78, 'level': 2, 'parent_bond': None}}
        self.assertEqual(ic.encode(), j_dict)


if __name__ == '__main__':
    unittest.main()
