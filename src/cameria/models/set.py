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
from cameria.models import camera

FILTER_FUNCTION = "function() {\
    for(var index = 0; index < this.cameras.length; index++) {\
        var camera = this.cameras[index];\
        if(%s.indexOf(camera) == -1) { return false; }\
    }\
    return true;\
}"
""" Javascript based function that filters the sets that contain
the cameras that are currently defined """

class Set(spec.Spec):

    set_id = dict(
        index = True,
        immutable = True
    )

    name = dict(
        index = True,
        default = True
    )

    cameras = dict(
        type = quorum.references(
            camera.Camera,
            name = "camera_id",
            eager = True
        )
    )

    @classmethod
    def validate(cls):
        return super(Set, cls).validate() + [
            quorum.not_null("name"),
            quorum.not_empty("name")
        ]

    @classmethod
    def validate_new(cls):
        return super(Set, cls).validate_new() + [
            quorum.not_null("set_id"),
            quorum.not_empty("set_id"),
            quorum.string_gt("set_id", 1),
            quorum.string_lt("set_id", 64),
            quorum.not_duplicate("set_id", cls._name())
        ]

    @classmethod
    def find_a(cls, cameras = None, *args, **kwargs):
        cameras = cameras or flask.session.get("cameras", [])
        if not cameras == None:
            function = FILTER_FUNCTION % cameras
            cls.filter_merge("$where", function, kwargs)
        return cls.find(*args, **kwargs)

    @classmethod
    def get_a(cls, cameras = None, *args, **kwargs):
        cameras = cameras or flask.session.get("cameras", [])
        if not cameras == None:
            function = FILTER_FUNCTION % cameras
            cls.filter_merge("$where", function, kwargs)
        return cls.get(*args, **kwargs)

    def merge_cameras(self):
        for camera in self.cameras.objects:
            camera.merge_device()
            camera.merge(self)
            camera.filter_device()
