#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Cameria System
# Copyright (C) 2008-2014 Hive Solutions Lda.
#
# This file is part of Hive Cameria System.
#
# Hive Cameria System is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Cameria System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Cameria System. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2014 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

from cameria import models

from cameria.main import app
from cameria.main import quorum

@app.route("/api/devices.json", methods = ("GET",), json = True)
@quorum.ensure("devices.list", json = True)
def list_devices_api():
    object = quorum.get_object(alias = True, find = True)
    object["sort"] = object.get("sort", [("name", 1)])
    devices = models.Device.find(map = True, **object)
    return dict(devices = devices)

@app.route("/api/devices/<device_id>.json", methods = ("GET",), json = True)
@quorum.ensure("devices.show", json = True)
def show_device_api(device_id):
    device = models.Device.get(map = True, device_id = device_id)
    return device
