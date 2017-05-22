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
from formar.fweb.WebInfoTom import WebInfoTom
from formar.fdata.InfoTom import InfoTom
from formar.fdata.InfoCompound import InfoCompound
from formar.fdata.Bond import Bond


header = PageHeader()
header._title = 'Formar Objects Skeleton'
header.add_meta('charset="UTF-8"')
header.add_meta('name="viewport" content="width=device-width, initial-scale=1.0"')
header.add_script('/FormarWeb/js/drag_InfoTom.js')
header.add_script('/FormarWeb/js/drag_resizeHandle.js')
header.add_script('/FormarWeb/js/drag_and_drop_init.js')
header.add_script('/FormarWeb/js/page_init.js')
header.add_style('.FormarWeb/css/formar.css')
header.add_style('/FormarWeb/css/alerter.css')
header.add_style('/FormarWeb/css/InfoTom.css')

print(header)

print("<body>")

print('<br> <div style="max-width: 500px; margin: auto; padding: 15px;'
      + 'text-align: center; border: 2px solid red;">'
      + 'Information Nodes</div> <br>')

page_data = PageReader.get_page_data('../../FormarDB/page1')
for it in page_data:
    print('[', it.__class__.__name__, ']', end='<br>\n')
    if isinstance(it, InfoCompound):
        print(WebInfoTom(infotom=it))
    elif isinstance(it, InfoTom):
        print(WebInfoTom(infotom=it))
    elif isinstance(it, Bond):
        pass

print("<br>")

footer = PageFooter()
print(footer)

