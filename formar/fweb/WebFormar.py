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


from formar.fweb import PageHeader
from formar.fweb import PageFooter
from formar.fweb import WebInfoTom
from formar.fdata import InfoTom

header = PageHeader.PageHeader()
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

page1 = []

it = InfoTom.InfoTom(contents='Horses', lang_rtl=True, left=300, top=450)
wit = WebInfoTom.WebInfoTom(info=it)
print(wit)

print("<br>")

footer = PageFooter.PageFooter()
print(footer)

