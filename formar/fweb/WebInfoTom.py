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

    def __init__(self, info=None):
        self._info = info

    def __str__(self):
        info = self._info
        if info is None:
            return ''

        html_div = {'classes': []
                    , 'styles': []
                    , 'properties': []
                    , 'contents': []}

        if hasattr(info, '_lang_rtl') and info._lang_rtl:
            html_div['classes'].append('lang_rtl')

        if hasattr(info, '_left'):
            html_div['styles'].append('left: {0}px;'.format(str(info._left)))

        if hasattr(info, '_top'):
            html_div['styles'].append('top: {0}px;'.format(str(info._top)))

        # todo: these also need to be attributes of info
        html_div['styles'].append('width: {0}px;'.format('350')) # str(info._width)))
        html_div['styles'].append('height: {0}px;'.format('20')) # str(info._height)))


        if isinstance(info, InfoTom.InfoTom):
            html_div['classes'].append('InfoTom')
            html_div['properties'].append('draggable="true"')
            html_div['contents'].append(str(info))
            html_div['contents'].append(self.add_resize_handle())

        div = '<div class="{0}" style="{1}" {2}>{3}</div>'.format(
            ' '.join(html_div['classes'])
            , ' '.join(html_div['styles'])
            , ' '.join(html_div['properties'])
            , '\n'.join(html_div['contents']))

        return div

    @staticmethod
    def add_resize_handle():
        handle = '<div class="resizeHandle"  style="right: 1px; bottom: 1px;"  draggable="true">  &Congruent;  </div>'
        return handle
