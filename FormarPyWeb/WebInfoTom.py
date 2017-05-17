#!/usr/bin/python

class WebInfoTom:
    """Draws InfoTom on a web page.
    """

    def __init__(self, info=None):
        self._info = info


    def __repr__(self):
        if self._info is None:
            return ''
        return self._info.__repr__()
