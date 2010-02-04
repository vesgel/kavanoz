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

import dbus
import gobject

class DeviceListener:
    def __init__(self):
        self.bus = dbus.SystemBus()
        
        self.hal_manager_obj = self.bus.get_object("org.freedesktop.Hal", "/org/freedesktop/Hal/Manager")
        self.hal_manager = dbus.Interface(self.hal_manager_obj, "org.freedesktop.Hal.Manager")
        
        self.hal_manager.connect_to_signal("DeviceAdded", self._filter)

    def _filter(self, udi):
        device_obj = self.bus.get_object("org.freedesktop.Hal", udi)
        device = dbus.Interface(device_obj, "org.freedesktop.Hal.Device")

        if device.QueryCapability("volume"):
            return self.print_info(device)

        if device.QueryCapability("volume"):
            return self.print_info(device)

        """
        if device.QueryCapability("storage"):
            return self.print_exinfo(device)
        """

    def print_info(self, volume):
        product = volume.GetProperty("info.product")
        device_file = volume.GetProperty("block.device")
        label = volume.GetProperty("volume.label")
        uuid = volume.GetProperty("volume.uuid")
        fstype = volume.GetProperty("volume.fstype")
        mounted = volume.GetProperty("volume.is_mounted")
        mount_point = volume.GetProperty("volume.mount_point")

        try:
            size = volume.GetProperty("volume.size")
        except:
            size = 0

        print "New storage device detected:"
        print "  product: %s" % product
        print "  device_file: %s" % device_file
        print "  label: %s" % label
        print "  uuid: %s" % uuid
        print "  fstype: %s" % fstype
        
        if mounted:
            print "  mount_point: %s" % mount_point
        else:
            print "  not mounted"
        print "  size: %s (%.2fGB)" % (size, float(size) / 1024**3)

    def print_exinfo(self, storage):
        serial = storage.GetProperty("storage.serial")

        print "serial: %s" % serial

if __name__ == '__main__':
    from dbus.mainloop.glib import DBusGMainLoop
    DBusGMainLoop(set_as_default=True)
    loop = gobject.MainLoop()
    DeviceListener()
    loop.run()
