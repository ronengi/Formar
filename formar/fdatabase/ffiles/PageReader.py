#!/usr/bin/python

from formar.fdata import InfoTom


class PageReader:

    def __init__(self, path=None):
        self._path = path

    def __str__(self):
        return str('this page reader is bound to: {0}'.format(self._path))

    def get_page_info(self):
        if '_path' not in vars(self) or self._path is None:
            return None
        try:
            f_reader = open(self._path, 'r')
        except FileNotFoundError as err:
            print(err)
            print(err.args)
        else:
            page1 = []
            for line in f_reader:
                it = InfoTom.InfoTom.decode(line)
                page1.append(it)
            return page1

        finally:
            try:
                f_reader.close()
            except NameError as err:
                print(err)
                print(err.args)

