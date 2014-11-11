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

import quorum

from cameria.models import spec

class Device(spec.Spec):

    device_id = dict(
        index = True,
        immutable = True
    )

    name = dict(
        index = True,
        default = True
    )

    type = dict(
        index = True
    )

    model_d = dict(
        index = True
    )

    device = dict(
        index = True
    )

    filter_options = dict(
        type = list
    )

    @classmethod
    def validate_new(cls):
        return super(Device, cls).validate_new() + [
            quorum.not_null("device_id"),
            quorum.not_empty("device_id"),
            quorum.string_gt("device_id", 2),
            quorum.string_lt("device_id", 64),
            quorum.not_duplicate("device_id", cls._name()),

            quorum.not_null("type"),
            quorum.not_empty("type"),

            quorum.not_null("model_d"),
            quorum.not_empty("model_d")
        ]

    def pre_create(self):
        spec.Spec.pre_create(self)

        # creates the device's name from the joining of the type
        # and the model identifier of the current device
        self.name = self.get_name()

    def pre_update(self):
        spec.Spec.pre_update(self)

        # creates the device's name from the joining of the type
        # and the model identifier of the current device
        self.name = self.get_name()

    def filter_camera(self, camera):
        for filter_option in self.filter_options:
            if not hasattr(camera, filter_option): continue
            setattr(camera, filter_option, None)

    def get_name(self):
        return "%s %s" % (self.type, self.model_d)
