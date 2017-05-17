#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import sys
#sys.path.append('../Formar')
sys.path.append('/archive/devel/stimpy/Formar/Formar')

import PageHeader
import PageFooter

import InfoTom
import WebInfoTom


# enable web debugging
import cgitb
cgitb.enable()


print("Content-Type: text/html;charset=utf-8")
print()


header = PageHeader.PageHeader()
header._title = 'Formar Objects Skeleton'
header.add_meta('charset="UTF-8"')
header.add_meta('name="viewport" content="width=device-width, initial-scale=1.0"')
header.add_script('../../FormarWeb/js/drag_InfoTom.js')
header.add_script('../../FormarWeb/js/drag_resizeHandle.js')
header.add_script('../../FormarWeb/js/drag_and_drop_init.js')
header.add_script('../../FormarWeb/js/page_init.js')
header.add_style('../../FormarWeb/css/formar.css')
header.add_style('../../FormarWeb/css/alerter.css')
header.add_style('../../FormarWeb/css/InfoTom.css')

print(header)

print("<body>")

print("First try: dynamic display of InfoTom")

print("<br>")

it = InfoTom.InfoTom(contents='<div class="InfoTom lang_rtl" style="left: 300px; top: 450px;" draggable="true">'
                     + 'Horses'
                     + '<div class="resizeHandle" style="right: 1px; bottom: 1px;" draggable="true"> &Congruent; </div>'
                     + '</div>')

wit = WebInfoTom.WebInfoTom(info=it)
print(wit)

print("<br>")

footer = PageFooter.PageFooter("Goodbye Now")
print(footer)
