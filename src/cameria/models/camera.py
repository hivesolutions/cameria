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

import flask

import quorum

from cameria.models import spec
from cameria.models import device

class Camera(spec.Spec):

    camera_id = dict(
        index = True,
        immutable = True,
        default = True
    )

    url = dict(
        index = True
    )

    camera = dict()

    username = dict()

    password = dict()

    protocol = dict()

    device = dict(
        type = quorum.reference(
            device.Device,
            name = "device_id",
            eager = True
        )
    )

    @classmethod
    def validate(cls):
        return super(Camera, cls).validate() + [
            quorum.not_null("url"),
            quorum.not_empty("url")
        ]

    @classmethod
    def validate_new(cls):
        return super(Camera, cls).validate_new() + [
            quorum.not_null("camera_id"),
            quorum.not_empty("camera_id"),
            quorum.string_gt("camera_id", 2),
            quorum.string_lt("camera_id", 64),
            quorum.not_duplicate("camera_id", cls._name())
        ]

    @classmethod
    def find_a(cls, cameras = None, *args, **kwargs):
        cameras = cameras or flask.session.get("cameras", [])
        if not cameras == None:
            cls.filter_merge("camera_id", {"$in" : cameras}, kwargs)
        return cls.find(*args, **kwargs)

    @classmethod
    def get_a(cls, cameras = None, *args, **kwargs):
        cameras = cameras or flask.session.get("cameras", [])
        if not cameras == None:
            cls.filter_merge("camera_id", {"$in" : cameras}, kwargs)
        return cls.get(*args, **kwargs)

    def merge_device(self):
        self.merge(self.device, override = False)

    def filter_device(self):
        if not self.device: return
        self.device.filter_camera(self)
