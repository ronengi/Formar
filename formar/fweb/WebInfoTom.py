#!/usr/bin/python


class WebInfoTom:
    """Draws InfoTom on a web page.
    """

    def __init__(self, info=None):
        self._info = info

    def __str__(self):
        return 'hello'
        if self._info is not None:
            return self._info.__repr__
        return ''
