#!/usr/bin/python


class InfoTom:
    """Information Atom. Represents a basic unit of information.
    """

    def __init__(self, parent_bond=None, contents=None, level=0):
        self._parent_bond = parent_bond
        self._contents = contents
        self._level = level

    def __str__(self):
        if self._contents is None:
            return ''
        return self._contents

    def is_valid(self):
        pass
