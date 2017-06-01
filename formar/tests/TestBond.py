#!/usr/bin/python

import unittest
from formar.fdata.Bond import Bond
from formar.fdata.InfoTom import InfoTom


class TestBond(unittest.TestCase):

    def test_str(self):
        b = Bond(b_id=123, infotom1=456, infotom2=789, level=7, description='vim:Configuration')
        self.assertEqual(str(b), 'vim:Configuration')

    def test_encode(self):
        b = Bond(b_id=123, infotom1=456, infotom2=789, level=1, description='vim:Configuration')
        j_dict = {'__Bond__': {
            'b_id': 123
            , 'infotom1': 456, 'infotom2': 789
            , 'level': 1
            , 'description': 'vim:Configuration'}}
        self.assertEqual(b.encode(), j_dict)

    def test_decode(self):
        b = Bond(b_id=123, infotom1=456, infotom2=789, level=3, description='vim:Configuration')
        j_dict = {'__Bond__': {
            'b_id': 123
            , 'infotom1': 456, 'infotom2': 789
            , 'level': 3
            , 'description': 'vim:Configuration'}}
        self.assertEqual(Bond.decode(j_dict), b)

if __name__ == '__main__':
    unittest.main()

