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

import os
import datetime
import tempfile

from cameria.main import app
from cameria.main import flask
from cameria.main import quorum

NAME = "cameria"
""" The default name to be used as prefix for the database
export file in the export operation """

SINGLE_ENTITIES = (
    ("account", "username"),
)
""" The set of entities to be considered single file
oriented (exports to one file per complete set) """

MULTIPLE_ENTITIES = (
    ("set", "set_id"),
    ("camera", "camera_id"),
    ("device", "device_id")
)
""" The set of entities to be considered multiple file
oriented (exports to one file per entity) """

@app.route("/settings", methods = ("GET",))
@quorum.ensure("settings")
def settings():
    return flask.render_template(
        "settings/show.html.tpl",
        link = "settings",
        sub_link = "show"
    )

@app.route("/import", methods = ("GET",))
@quorum.ensure("import")
def import_a():
    return flask.render_template(
        "settings/import.html.tpl",
        link = "settings",
        sub_link = "import"
    )

@app.route("/import", methods = ("POST",))
@quorum.ensure("import")
def import_do():
    # retrieves the import file values (reference to the
    # uploaded file) and then validates if it has been
    # defined, in case it fails prints the template with
    # the appropriate error variable set
    import_file = quorum.get_field("import_file", None)
    if import_file == None or not import_file.filename:
        return flask.render_template(
            "settings/import.html.tpl",
            link = "settings",
            sub_link = "import",
            error = "No file defined"
        )

    # creates a temporary file path for the storage of the file
    # and then saves it into that directory
    fd, file_path = tempfile.mkstemp()
    import_file.save(file_path)

    # retrieves the database and creates a new export manager for
    # the currently defined entities then imports the data defined
    # in the current temporary path
    database = quorum.get_mongo_db()
    manager = quorum.export.ExportManager(
        database,
        single = SINGLE_ENTITIES,
        multiple = MULTIPLE_ENTITIES
    )
    try: manager.import_data(file_path)
    finally: os.close(fd); os.remove(file_path)
    return flask.redirect(
        flask.url_for(
            "import_a",
            message = "Database file imported with success"
        )
    )

@app.route("/export", methods = ("GET",))
@quorum.ensure("export")
def export_do():
    database = quorum.get_mongo_db()
    file = quorum.legacy.BytesIO()
    manager = quorum.export.ExportManager(
        database,
        single = SINGLE_ENTITIES,
        multiple = MULTIPLE_ENTITIES
    )
    manager.export_data(file)

    date_time = datetime.datetime.utcnow()
    date_time_s = date_time.strftime("%Y%m%d")
    file_name = "%s_%s.dat" % (NAME, date_time_s)

    return flask.Response(
        file.getvalue(),
        headers = {
            "Content-Disposition" : "attachment; filename=%s" % file_name
        },
        mimetype = "application/octet-stream"
    )

@app.route("/reset", methods = ("GET",))
@quorum.ensure("reset")
def reset_do():
    quorum.drop_mongo_db()
    return flask.redirect(
        flask.url_for("settings")
    )
