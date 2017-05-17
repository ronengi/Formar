#!/usr/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()


print("Content-Type: text/html;charset=utf-8")
print()


import pyweb.PageHeader
import pyweb.PageFooter

header = pyweb.PageHeader.PageHeader()
header._title = 'Formar Objects Skeleton'
header.add_meta('charset="UTF-8"')
header.add_meta('name="viewport" content="width=device-width, initial-scale=1.0"')
header.add_script('js/drag_InfoTom.js')
header.add_script('js/drag_resizeHandle.js')
header.add_script('js/drag_and_drop_init.js')
header.add_script('js/page_init.js')
header.add_style('formar.css')

print(header)

print("<body>")
print("Hello World!")



footer = pyweb.PageFooter.PageFooter("Goodbye Now")
print(footer)
