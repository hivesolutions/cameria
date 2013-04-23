#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Cameria System
# Copyright (C) 2008-2012 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import models

from cameria import app
from cameria import flask
from cameria import quorum

@app.route("/cameras", methods = ("GET",))
@quorum.ensure("cameras.list")
def list_cameras():
    return flask.render_template(
        "camera/list.html.tpl",
        link = "cameras",
        sub_link = "list"
    )

@app.route("/cameras.json", methods = ("GET",))
@quorum.ensure("cameras.list")
def list_cameras_json():
    object = quorum.get_object(alias = True, find = True)
    builds = models.Camera.find(map = True, sort = [("id", -1)], **object)
    return flask.Response(
        quorum.dumps_mongo(builds),
        mimetype = "application/json"
    )

@app.route("/camera/new", methods = ("GET",))
@quorum.ensure("cameras.new")
def new_camera():
    return flask.render_template(
        "camera/new.html.tpl",
        link = "cameras",
        sub_link = "create",
        camera = {},
        errors = {}
    )

@app.route("/cameras", methods = ("POST",))
@quorum.ensure("cameras.new")
def create_camera():
    # creates the new camera, using the provided arguments and
    # then saves it into the data source, all the validations
    # should be ran upon the save operation
    camera = models.Camera.new()
    try: camera.save()
    except quorum.ValidationError, error:
        return flask.render_template(
            "camera/new.html.tpl",
            link = "cameras",
            sub_link = "create",
            camera = error.model,
            errors = error.errors
        )

    # redirects the user to the pending page, indicating that
    # the camera is not yet activated and is pending the email
    # confirmation action
    return flask.redirect(
        flask.url_for("show_camera", camera_id = camera.camera_id)
    )

@app.route("/cameras/<camera_id>", methods = ("GET",))
@quorum.ensure("cameras.show")
def show_camera(camera_id):
    camera = models.Camera.get(camera_id = camera_id)
    return flask.render_template(
        "camera/show.html.tpl",
        link = "cameras",
        sub_link = "show",
        camera = camera
    )

@app.route("/cameras/<camera_id>/delete", methods = ("GET",))
@quorum.ensure("cameras.delete")
def delete_camera(camera_id):
    camera = models.Camera.get(camera_id = camera_id)
    camera.delete()
    return flask.redirect(
        flask.url_for("list_cameras")
    )

@app.route("/cameras/<camera_id>/settings", methods = ("GET",))
@quorum.ensure("cameras.show")
def settings_camera(camera_id):
    camera = models.Camera.get(camera_id = camera_id)
    return flask.render_template(
        "camera/settings.html.tpl",
        link = "cameras",
        sub_link = "settings",
        camera = camera
    )
