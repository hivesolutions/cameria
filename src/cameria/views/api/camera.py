#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Cameria System
# Copyright (C) 2008-2015 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2015 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

from cameria import models

from cameria.main import app
from cameria.main import quorum

@app.route("/api/cameras.json", methods = ("GET",), json = True)
@quorum.ensure("cameras.list", json = True)
def list_cameras_api():
    object = quorum.get_object(alias = True, find = True)
    object["sort"] = object.get("sort", [("camera_id", 1)])
    cameras = models.Camera.find_a(map = True, **object)
    return dict(cameras = cameras)

@app.route("/api/cameras/<camera_id>.json", methods = ("GET",), json = True)
@quorum.ensure("cameras.show", json = True)
def show_camera_api(camera_id):
    camera = models.Camera.get_a(map = True, camera_id = camera_id)
    return camera

@app.route("/api/cameras_m.json", methods = ("GET",), json = True)
@quorum.ensure("cameras.list", json = True)
def list_cameras_m_api():
    object = quorum.get_object(alias = True, find = True)
    object["sort"] = object.get("sort", [("camera_id", 1)])
    cameras = models.Camera.find_a(**object)
    for camera in cameras:
        camera.merge_device()
        camera.filter_device()
    return dict(cameras = cameras)
