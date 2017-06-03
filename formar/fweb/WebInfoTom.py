#!/usr/bin/python

"""
    Copyright 2017 Ronen Gilead-Raz

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


from HTMLTag import HTMLTag
from formar.fdata.InfoTom import InfoTom


class WebInfoTom:
    """Draws InfoTom on a web page."""

    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def validate(obj=None):
        if not isinstance(obj, InfoTom):
            raise TypeError('InfoTom expected')

    @classmethod
    def get_t_class(cls):
        return 'InfoTom'

    @classmethod
    def append_contents(cls, root: dict={}, contents: dict={}):
        root['div']['t_contents'].append(contents)

    @staticmethod
    def add_resize_handle(it_id='') -> dict:
        tag = dict()
        tag['t_id'] = 'rh_{0}'.format(it_id)
        tag['t_classes'] = ['resizeHandle']
        tag['t_styles'] = dict(right='1px', bottom='1px', height='12px', width='8px')
        tag['t_properties'] = {'draggable': 'true'}
        tag['t_contents'] = [' &square; ']
        return dict(div=tag)

    @classmethod
    def generate_tag_info(cls, obj=None) -> dict:
        cls.validate(obj=obj)
        tag = dict()
        tag['t_id'] = obj.get_it_id()
        tag['t_classes'] = ['{0}'.format(cls.get_t_class())]
        if obj.get_lang_rtl():
            tag['t_classes'].append('lang_rtl')
        tag['t_styles'] = dict()
        tag['t_styles']['left'] = '{0}px'.format(str(obj.get_left()))
        tag['t_styles']['top'] = '{0}px'.format(str(obj.get_top()))
        tag['t_styles']['width'] = '{0}px'.format(str(obj.get_width()))
        tag['t_styles']['height'] = '{0}px'.format(str(obj.get_height()))
        tag['t_properties'] = {'draggable': 'true'}
        tag['t_contents'] = [obj.get_contents()]
        tag['t_contents'].append(WebInfoTom.add_resize_handle(it_id='it_id_{0}'.format(obj.get_it_id())))
        return dict(div=tag)

    @classmethod
    def generate_html(cls, obj=None) -> str:
        cls.validate(obj=obj)
        tag_info = cls.generate_tag_info(obj=obj)
        # return tag_info
        return HTMLTag.generate(tag_info)
