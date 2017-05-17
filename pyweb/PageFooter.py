#!/usr/bin/python


class PageFooter:
    """Flexible HTML footer generator
    """

    _message = ''


    def __init__(self, message=''):
        self._message = message


    def __str__(self):
        footer_lines = []
        if self._message:
            footer_lines.append(self._message)
        footer_lines.append('{0}</body>'.format(' ' * 4))
        footer_lines.append('</html>')
        return "\n".join(footer_lines)
