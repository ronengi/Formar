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


from formar.fdata import InfoTom


# todo: implement a separate <div> creator
# todo: after that implement a general <tag> creator
class WebInfoTom:
    """Draws InfoTom on a web page.
    """

    def __init__(self, infotom=None):
        self.__infotom = infotom

    def __str__(self):
        it = self.__infotom
        if it is None:
            return ''

        if not isinstance(it, InfoTom.InfoTom):
            raise TypeError('InfoTom expected')

        html_div = {'it_id': self.__infotom.get_it_id()
                    , 'classes': []
                    , 'styles': []
                    , 'properties': []
                    , 'contents': []}

        if it.get_lang_rtl():
            html_div['classes'].append('lang_rtl')

        html_div['styles'].append('left: {0}px;'.format(str(it.get_left())))
        html_div['styles'].append('top: {0}px;'.format(str(it.get_top())))
        html_div['styles'].append('width: {0}px;'.format(str(it.get_width())))
        html_div['styles'].append('height: {0}px;'.format(str(it.get_height())))

        if isinstance(it, InfoTom.InfoTom):
            html_div['classes'].append('InfoTom')
            html_div['properties'].append('draggable="true"')
            html_div['contents'].append(str(it))
            html_div['contents'].append(WebInfoTom.add_resize_handle(it_id=html_div['it_id']))

        div = '<div id="{0}" class="{1}" style="{2}" {3}>{4}</div>'.format(
            html_div['it_id']
            , ' '.join(html_div['classes'])
            , ' '.join(html_div['styles'])
            , ' '.join(html_div['properties'])
            , '\n'.join(html_div['contents']))

        return div

    @staticmethod
    def add_resize_handle(it_id=''):
        handle = '<div id="rh{0}" class="resizeHandle" style="right: 1px; bottom: 1px; height:12px; width: 8px;"  draggable="true"> &square; </div>'.format(it_id)
        return handle
