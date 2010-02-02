#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, Kavanoz Authors
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import filecmp
import shutil
import os

class dir2dir:
    def __init__(self, dir1, dir2):
	self.first_dir = dir1
	self.second_dir = dir2

    def syncDir(self, current_dir):
	print("current %s : " % current_dir)
	dir1 = os.path.join(self.first_dir, current_dir)
	dir2 = os.path.join(self.second_dir, current_dir)
	print("dir1 %s : " % dir1)
	
	cmp = filecmp.dircmp(dir1, dir2)

	for dir in cmp.common_dirs:
	    if(current_dir == ""):
		self.syncDir("%s" % dir)
	    else:
		self.syncDir("%s/%s" % (current_dir, dir))

	# delete old files(dirs)
	for _file in cmp.right_only:
	    full_dir2 = os.path.join(self.second_dir, current_dir, _file)
	    if(os.path.isdir(full_dir2)):
	        shutil.rmtree(full_dir2)
	    else:
		os.remove(full_dir2)

	# copy changed of new added files(dirs)
	for _file in cmp.diff_files + cmp.left_only:
	    full_dir1 = os.path.join(self.first_dir, current_dir, _file)
	    full_dir2 = os.path.join(self.second_dir, current_dir, _file)
	    if(os.path.isdir(full_dir1)):
	        shutil.copytree(full_dir1, full_dir2)
	    else:
		shutil.copy(full_dir1, full_dir2)
