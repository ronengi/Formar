#!/usr/bin/python

import json
from formar.fdata.InfoTom import InfoTom
from formar.fdata.InfoCompound import  InfoCompound
from formar.fdata.Bond import Bond


class PageReader:

    @staticmethod
    def get_page_data(path):
        try:
            f_reader = open(path, 'r')
            # todo: implement a more forgiving, flexible file parser
            return json.load(f_reader, object_hook=PageReader.formar_hooks)
        except FileNotFoundError:
            print('Failed to open file "{0}"'.format(path), end='<br>\n')
            return []
        except json.JSONDecodeError as err:
            print('Malformed data file "{0}"'.format(path), end='<br>\n')
            print('Error details: "{0}"'.format(err), end='<br>\n')
            return []
        finally:
            try:
                f_reader.close()
            except NameError:
                print('Failed to close file "{0}"'.format(path), end='<br>\n')

    @staticmethod
    def formar_hooks(j_dict):
        if '__InfoTom__' in j_dict:
            return InfoTom.decode(j_dict)
        elif '__InfoCompound__' in j_dict:
            return InfoCompound.decode(j_dict)
        elif '__Bond__' in j_dict:
            return Bond.decode(j_dict)
        return j_dict

