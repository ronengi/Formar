#!/usr/bin/python

import unittest
import json
from formar.fdata.InfoTom import InfoTom


class TestEncodeDecode(unittest.TestCase):

    def test_encode_decode(self):
        it = InfoTom(contents='Horses', lang_rtl=True,
                     left=12, top=34, width=56, height=78,
                     level=12, parent_bond=None)
        self.assertEqual(it, InfoTom.decode(it.encode()))

    def test_encode(self):
        it = InfoTom(contents='Horses', lang_rtl=True,
                     left=12, top=34, width=56, height=78,
                     level=12, parent_bond=None)
        j_str = '{"__InfoTom__": {"contents": "Horses", "lang_rtl": true, "left": 12, "top": 34, "width": 56, "height": 78, "level": 12, "parent_bond": null}}'
        self.assertEqual(it.encode(), json.loads(j_str))

    def test_decode(self):
        it = InfoTom(contents='Horses', lang_rtl=True,
                     left=12, top=34, width=56, height=78,
                     level=12, parent_bond=None)
        j_str = '{"__InfoTom__": {"contents": "Horses", "lang_rtl": true, "left": 12, "top": 34, "width": 56, "height": 78, "level": 12, "parent_bond": null}}'

        self.assertEqual(InfoTom.decode(json.loads(j_str)), it)


if __name__ == '__main__':
    unittest.main()

