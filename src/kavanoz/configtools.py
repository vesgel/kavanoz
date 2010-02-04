#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010, Kavanoz Authors
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import ConfigParser

class ConfigTool:
    def __init__(self):
        self.config_file = "my.conf"
        
        self.initialize("write")

    def initialize(self, mode):
        if mode == "read":
            self.config = ConfigParser.ConfigParser()
        elif mode == "write":
            self.config = ConfigParser.RawConfigParser()

    def setData(self, section, key, value):
        self.config.set(section, key, value)

    def addSection(self, section):
        self.config.add_section(section)

    def writeFile(self):
        with open(self.config_file, 'wb') as configfile:
            self.config.write(configfile)

    def readFile(self):        
        self.config.read(self.config_file)

    def getData(self, section, key):
        data = self.config.get(section, key)
        print data

    def removeData(self, section, key):
        self.config.remove_option(section, key)

    # TODO :: Add moveData function
