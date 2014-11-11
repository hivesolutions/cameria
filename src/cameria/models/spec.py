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

from cameria.models import base

class Spec(base.Base):

    resolution = dict(
        index = True
    )

    width = dict(
        type = int
    )

    height = dict(
        type = int
    )

    compression = dict(
        type = int
    )

    fps = dict(
        type = int
    )

    clock = dict(
        type = int
    )

    @classmethod
    def get_spec(cls):
        return (
            "resolution",
            "width",
            "height",
            "compression",
            "fps",
            "clock"
        )

    def merge(self, spec, override = True):
        # verifies that the current instance contains an origin reference
        # and in case it does not creates a new one and then retrieves the
        # reference to it so that it may be used latter for setting
        has_origin = hasattr(self, "origin")
        origin = getattr(self, "origin") if has_origin else dict()
        setattr(self, "origin", origin)

        # retrieves the complete set of names that are considered
        # to belong to the spec and then iterates over them to try
        # to merge the current spec with the provided one
        names = Spec.get_spec()
        for name in names:
            # in case the spec object does not contain the current
            # spec name must continue the loop (not possible to
            # merge a non existent value)
            if not hasattr(spec, name): continue

            # verifies if the current instance already contains a set
            # and valid value and in case the override flag is not
            # set overrides the current loop (already set value)
            is_set = hasattr(self, name) and not getattr(self, name) == None
            if is_set and not override: continue

            # retrieves the current value (considered to be the original) and in
            # case the value already exists and is going to be replaced saves it
            # under the map of original values (as defined by spec)
            value = getattr(self, name) if is_set else None
            if is_set and override: origin[name] = value

            # retrieves the value for the current name in the spec
            # object and then sets it in the current instance
            value = getattr(spec, name)
            setattr(self, name, value)
