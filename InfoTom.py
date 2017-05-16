#!/usr/bin/python

class InfoTom:
    """Information Atom. Represents a basic unit of information.
    """


    _parent_bond = None
    _contents = None
    _level = 0


    def __init__(self, parent_bond=None, contents=None, level=0):
        self._parent_bond = parent_bond
        self._contents = contents
        self._level = level


    def __str__(self):
        return self._contents


    def is_valid(self):
        pass
