# -*- coding: utf-8 -*-
from AppKit import NSAlert
alert = NSAlert.alloc().init()
alert.setMessageText_('Hello Python')
alert.runModal()