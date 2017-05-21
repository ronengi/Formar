#!/usr/bin/python

import json
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
                try:
                    page1.append(
                        json.loads(
                            line, object_hook=PageReader.as_infotom))
                except json.JSONDecodeError as err:
                    print(err.args)
            return page1

        finally:
            try:
                f_reader.close()
            except NameError as err:
                print(err)
                print(err.args)

    @staticmethod
    def as_infotom(j_dict):
        if '__InfoTom__' in j_dict:
            return InfoTom.InfoTom.decode(j_dict['__InfoTom__'])
        return j_dict
