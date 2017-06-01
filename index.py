#!/usr/bin/python
# -*- coding: UTF-8 -*-

# enable web debugging
import cgitb
cgitb.enable()

from os import path
import sys
sys.path.append(path.abspath('../HTMLTag/'))


print("Content-Type: text/html;charset=utf-8")
print()

# print(sys.path)

import formar.fweb.WebFormar

