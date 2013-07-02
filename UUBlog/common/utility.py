#-*- coding:utf-8 -*-

import time,datetime
import os
import re


def RemoveTags(str_html):
    return re.compile('</?\w+[^>]*>').sub('',str_html)



















