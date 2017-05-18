#!/usr/bin/python


class PageHeader:
    """Flexible HTML header generator
    """

    def __init__(self, title=None, metas=[], scripts=[], styles=[]):
        self._title = title
        self._metas = metas
        self._scripts = scripts
        self._styles = styles

    def __repr__(self):
        header = ['<!DOCTYPE html>',
                  '<html>',
                  '{0}<head>'.format(' ' * 4)]
        if self._title is not None:
            header.append('{0}<title>{1}</title>'.format(' ' * 8, self._title))
        for meta in self._metas:
            header.append('{0}<meta {1}>'.format(' ' * 8, meta))
        for script in self._scripts:
            header.append('{0}<script src="{1}"></script>'.format(' ' * 8, script))
        for style in self._styles:
            header.append('{0}<link rel="stylesheet" href="{1}">'.format(' ' * 8, style))
        header.append('{0}</head>'.format(' ' * 4))
        header.append('{0}<body>'.format(' ' * 4))
        return "\n".join(header)

    def set_title(self, title):
        self._title = title

    def set_metas(self, metas):
        self._metas= metas

    def set_scripts(self, scripts):
        self._scripts = scripts

    def set_styles(self, styles):
        self._styles = styles

    def add_meta(self, meta):
        self._metas.append(meta)

    def add_script(self, script):
        self._scripts.append(script)

    def add_style(self, style):
        self._styles.append(style)