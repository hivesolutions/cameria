#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Cameria System
# Copyright (c) 2008-2022 Hive Solutions Lda.
#
# This file is part of Hive Cameria System.
#
# Hive Cameria System is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Cameria System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Cameria System. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2022 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

from cameria import models

from cameria.main import app
from cameria.main import quorum

@app.route("/api/sets.json", methods = ("GET",), json = True)
@quorum.ensure("sets.list", json = True)
def list_sets_api():
    object = quorum.get_object(
        alias = True,
        find = True,
        limit = 0,
        sort = [("name", 1)]
    )
    sets = models.Set.find_a(map = True, **object)
    return dict(sets = sets)

@app.route("/api/sets/<set_id>.json", methods = ("GET",), json = True)
@quorum.ensure("sets.show", json = True)
def show_set_api(set_id):
    set = models.Set.get_a(map = True, set_id = set_id)
    return set

@app.route("/api/sets_m.json", methods = ("GET",), json = True)
@quorum.ensure("sets.list", json = True)
def list_sets_m_api():
    object = quorum.get_object(
        alias = True,
        find = True,
        limit = 0,
        sort = [("name", 1)]
    )
    sets = models.Set.find_a(**object)
    for set in sets: set.merge_cameras()
    return dict(sets = sets)
