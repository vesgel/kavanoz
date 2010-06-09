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
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = ConfigParser.RawConfigParser()

    def items(self, section):
	self.readFile()
	return self.config.items(section)

    def sections(self):
        self.readFile()
        return self.config.sections()

    def setValue(self, section, key, value):
        self.config.set(section, key, value)
        self.writeFile()

    def getValue(self, section, key):
        self.readFile()
        return self.config.get(section, key)
        
    def getIntValue(self, section, key):
	self.readFile()
	return self.config.getInt(section, key)
	
    def getFloatValue(self, section, key):
        self.readFile()
        return self.config.getFloat(section, key)

    def getBooleanValue(self, section, key):
        self.readFile()
        return self.config.getBoolean(section, key)

    def removeData(self, section, key):
        self.config.remove_option(section, key)
        self.writeFile()

    def addSection(self, section):
        self.config.add_section(section)
        self.writeFile()

    def removeSection(self, section):
        self.config.remove_section(section)
        self.writeFile()

    def writeFile(self):
        with open(self.config_file, 'wb') as configfile:
            self.config.write(configfile)

    def readFile(self):
        self.config.read(self.config_file)
