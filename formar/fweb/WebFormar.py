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

"""Main Application Controller.

      Provides these functions:
        The user's access point to the information.
        Imports all modules.
        Simulates the correct flow of the application,
"""

# todo: gradually transfer functionality to specialized modules

from formar.fweb.PageHeader import PageHeader
from formar.fweb.PageFooter import PageFooter
from formar.fdatabase.ffiles.PageReader import PageReader
from formar.fdata.InfoTom import InfoTom
from formar.fdata.InfoCompound import InfoCompound
from formar.fdata.Bond import Bond
from formar.fweb.WebInfoTom import WebInfoTom
from formar.fweb.WebInfoCompound import WebInfoCompound
from HTMLTag import HTMLTag

def find_item(root_obj=None, id=''):
    if root_obj.__class__.__name__ == 'list':
        for item in root_obj:
            found = find_item(item, id)
            if found != None:
                return found
    elif root_obj.__class__.__name__ == 'dict':
        try:
            found = root_obj['div']['t_id']
            if found == id:
                return root_obj
        except:
            return None
    return None

header = PageHeader()
header._title = 'Formar Objects Skeleton'

header.add_meta('charset="UTF-8"')
header.add_meta('name="viewport" content="width=device-width, initial-scale=1.0"')

header.add_script('/FormarWeb/js/DragAndDropListener.js')
header.add_script('/FormarWeb/js/InfoTom.js')
header.add_script('/FormarWeb/js/InfoCompound.js')
header.add_script('/FormarWeb/js/ResizeHandle.js')
header.add_script('/FormarWeb/js/page_init.js')

header.add_style('/FormarWeb/css/alerter.css')
header.add_style('/FormarWeb/css/InfoCompound.css')
header.add_style('/FormarWeb/css/InfoTom.css')
header.add_style('/FormarWeb/css/ResizeHandle.css')

print(header)

print("<body>")

print('<br> <div style="max-width: 500px; margin: auto; padding: 15px;'
      + 'text-align: center; border: 2px solid red;">'
      + 'Information Nodes</div> <br>')

page_objects = PageReader.get_page_data('../../FormarDB/page1')
# it's possible here to apply a filter

# start dict-before-html representation of page
page_dict = []
for it in page_objects:
    if isinstance(it, InfoCompound):
        # print('[{0}: {1}] <br>\n'.format(it.get_it_id(), it.__class__.__name__))
        # print(WebInfoCompound.generate_html(obj=it))
        page_dict.append(WebInfoCompound.generate_tag_info(obj=it))
    elif isinstance(it, InfoTom):
        # print('[{0}: {1}] <br>\n'.format(it.get_it_id(), it.__class__.__name__))
        # print(WebInfoTom.generate_html(obj=it))
        page_dict.append(WebInfoTom.generate_tag_info(obj=it))
    elif isinstance(it, Bond):
        # bonds must come after all objects exist in memory
        # print('[{0}: {1}] <br>\n'.format(it.get_b_id(), it.__class__.__name__))
        pass

# print('<br>\n')
# print(page_dict)
# print('<br>\n')

for it in page_objects:
    if isinstance(it, Bond):
        id1 = it.get_infotom1()
        id2 = it.get_infotom2()
        root = find_item(page_dict, id1)
        contents = find_item(page_dict, id2)
        # print(root)
        # print('<br>\n')
        # print(contents)
        # print('<br>\n')
        try:
            WebInfoTom.append_contents(root, contents)
        except TypeError:
            pass
            # print('<br>\n')
            # print(root['div']['t_contents'])
            # print('<br>\n')
        # del ...

for it in page_dict:
    print(HTMLTag.generate(it))

print("<br>")

footer = PageFooter()
print(footer)
