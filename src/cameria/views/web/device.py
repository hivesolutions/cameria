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
from cameria.main import flask
from cameria.main import quorum

@app.route("/devices", methods = ("GET",))
@quorum.ensure("devices.list")
def list_devices():
    return flask.render_template(
        "device/list.html.tpl",
        link = "devices",
        sub_link = "list"
    )

@app.route("/devices.json", methods = ("GET",), json = True)
@quorum.ensure("devices.list", json = True)
def list_devices_json():
    object = quorum.get_object(alias = True, find = True)
    object["sort"] = object.get("sort", [("name", 1)])
    devices = models.Device.find(map = True, **object)
    return devices

@app.route("/device/new", methods = ("GET",))
@quorum.ensure("devices.new")
def new_device():
    return flask.render_template(
        "device/new.html.tpl",
        link = "devices",
        sub_link = "create",
        device = {},
        errors = {}
    )

@app.route("/devices", methods = ("POST",))
@quorum.ensure("devices.new")
def create_device():
    # creates the new device, using the provided arguments and
    # then saves it into the data source, all the validations
    # should be ran upon the save operation
    device = models.Device.new()
    try: device.save()
    except quorum.ValidationError as error:
        return flask.render_template(
            "device/new.html.tpl",
            link = "devices",
            sub_link = "create",
            device = error.model,
            errors = error.errors
        )

    # redirects the user to the show page of the set that
    # was just created (normal workflow)
    return flask.redirect(
        flask.url_for("show_device", device_id = device.device_id)
    )

@app.route("/devices/<device_id>", methods = ("GET",))
@quorum.ensure("devices.show")
def show_device(device_id):
    device = models.Device.get(device_id = device_id)
    return flask.render_template(
        "device/show.html.tpl",
        link = "devices",
        sub_link = "show",
        device = device
    )

@app.route("/devices/<device_id>/edit", methods = ("GET",))
@quorum.ensure("devices.edit")
def edit_device(device_id):
    device = models.Device.get(device_id = device_id)
    return flask.render_template(
        "device/edit.html.tpl",
        link = "devices",
        sub_link = "edit",
        device = device,
        errors = {}
    )

@app.route("/devices/<device_id>/edit", methods = ("POST",))
@quorum.ensure("devices.edit")
def update_device(device_id):
    # finds the current device and applies the provided
    # arguments and then saves it into the data source,
    # all the validations should be ran upon the save operation
    device = models.Device.get(device_id = device_id)
    device.apply()
    try: device.save()
    except quorum.ValidationError as error:
        return flask.render_template(
            "device/edit.html.tpl",
            link = "devices",
            sub_link = "edit",
            device = error.model,
            errors = error.errors
        )

    # redirects the user to the show page of the device that
    # was just updated
    return flask.redirect(
        flask.url_for("show_device", device_id = device_id)
    )

@app.route("/devices/<device_id>/delete", methods = ("GET",))
@quorum.ensure("devices.delete")
def delete_device(device_id):
    device = models.Device.get(device_id = device_id)
    device.delete()
    return flask.redirect(
        flask.url_for("list_devices")
    )
