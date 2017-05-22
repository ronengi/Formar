#!/usr/bin/python

import json
from formar.fdata import InfoTom


class PageReader:

    def __init__(self, path=None):
        self.__path = path

    def __str__(self):
        return str('this page reader is bound to: {0}'.format(self.get_path()))

    def get_path(self):
        try:
            return str(self.__path)
        except (AttributeError, TypeError):
            # no such attribute or None
            return ''

    def get_page_info(self):
        path = self.get_path()
        try:
            f_reader = open(path, 'r')
        except FileNotFoundError as err:
            print(err)
            print(err.args)
            return []
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
            return InfoTom.InfoTom.decode(j_dict)
        return j_dict
