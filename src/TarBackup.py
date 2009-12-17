#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, Aşkın Yollu <askin@askin.ws>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import tarfile
import time

class TarBackup:
    def __init__(self, backupName, originalPath):
        self.backupFileName = ""
        self.backupPath = ""
        self.backupDevice = []
        self.backupName = backupName
        self.archive_type = ""
        self.originalPath = originalPath

    # temp: device select path

    def setBackupFileName(self):
        current_time = time.localtime()
        self.backupFileName = "%s-%s-%s-%s.%s" % (self.backupName, current_time[0], current_time[1], current_time[2], self.archive_type)

    def setArchiveType(self, type):
        self.archive_type = type

    def backup(self):
        self.setBackupFileName()
        
        if(self.backupPath == ""):
            self.backupPath = "."
            
        filePath = "%s/%s" % (self.backupPath, self.backupFileName)
        tar = tarfile.open(filePath, "w:%s" % self.archive_type)
        tar.add(self.originalPath)
        tar.close()
