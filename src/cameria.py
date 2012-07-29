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

import os
import json
import flask

CURRENT_DIRECTORY = os.path.dirname(__file__)
CURRENT_DIRECTORY_ABS = os.path.abspath(CURRENT_DIRECTORY)
SETS_FOLDER = os.path.join(CURRENT_DIRECTORY_ABS, "sets")
CAMERAS_FOLDER = os.path.join(CURRENT_DIRECTORY_ABS, "cameras")
DEVICES_FOLDER = os.path.join(CURRENT_DIRECTORY_ABS, "devices")

app = flask.Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template(
        "index.html.tpl",
        link = "home"
    )

@app.route("/")
@app.route("/about")
def about():
    return flask.render_template(
        "about.html.tpl",
        link = "about"
    )

@app.route("/sets")
def list_set():
    sets = get_sets()

    return flask.render_template(
        "sets_list.html.tpl",
        link = "sets",
        sets = sets
    )

@app.route("/sets/<id>")
def show_set(id):
    set = get_set(id)

    return flask.render_template(
        "sets_show.html.tpl",
        link = "sets",
        sub_link = "show",
        set = set
    )

@app.route("/sets/<id>/settings")
def settings_set(id):
    pass

@app.route("/cameras")
def list_camera():
    cameras = get_cameras()

    return flask.render_template(
        "cameras_list.html.tpl",
        link = "cameras",
        cameras = cameras
    )

@app.route("/cameras/<id>")
def show_camera(id):
    camera = get_camera(id)
    filter(camera)

    return flask.render_template(
        "cameras_show.html.tpl",
        link = "cameras",
        sub_link = "show",
        camera = camera
    )

@app.route("/cameras/<id>/settings")
def settings_camera(id):
    camera = get_camera(id)

    return flask.render_template(
        "cameras_settings.html.tpl",
        link = "cameras",
        camera = camera
    )

@app.route("/devices")
def list_device():
    devices = get_devices()

    return flask.render_template(
        "devices_list.html.tpl",
        link = "devices",
        devices = devices
    )

@app.route("/device/<id>")
def show_device(id):
    device = get_device(id = id)

    return flask.render_template(
        "devices_show.html.tpl",
        link = "devices",
        sub_link = "show",
        device = device
    )

@app.errorhandler(404)
def handler_404(error):
    return str(error)

@app.errorhandler(413)
def handler_413(error):
    return str(error)

@app.errorhandler(BaseException)
def handler_exception(error):
    return str(error)

def get_sets():
    sets_directory = os.path.join(SETS_FOLDER)
    if not os.path.exists(sets_directory): raise RuntimeError("Sets directory does not exist")
    entries = os.listdir(sets_directory)

    sets = []

    for entry in entries:
        base, extension = os.path.splitext(entry)
        if not extension == ".json": continue

        set = get_set(base)
        sets.append(set)

    return sets

def get_set(id):
    # retrieves the path to the (target) set (configuration) file and
    # check if it exists then opens it and loads the json configuration
    # contained in it to set it in the template
    set_path = os.path.join(SETS_FOLDER, "%s.json" % id)
    if not os.path.exists(set_path): raise RuntimeError("Set file does not exist")
    set_file = open(set_path, "rb")
    try: set = json.load(set_file)
    finally: set_file.close()

    cameras = set.get("cameras", [])
    _camera = set.get("camera", {})

    for camera in cameras:
        id = camera["id"]
        __camera = get_camera(id)

        merge(camera, __camera)
        merge(camera, _camera)

        filter(camera)

    return set

def get_cameras():
    cameras_directory = os.path.join(CAMERAS_FOLDER)
    if not os.path.exists(cameras_directory): raise RuntimeError("Cameras directory does not exist")
    entries = os.listdir(cameras_directory)

    cameras = []

    for camera in entries:
        base, extension = os.path.splitext(camera)
        if not extension == ".json": continue

        camera = get_camera(base)
        cameras.append(camera)

    return cameras

def get_camera(id):
    camera_path = os.path.join(CAMERAS_FOLDER, "%s.json" % id)
    if not os.path.exists(camera_path): raise RuntimeError("Camera file does not exist")
    camera_file = open(camera_path, "rb")
    try: camera = json.load(camera_file)
    finally: camera_file.close()

    return camera

def get_devices():
    devices_directory = os.path.join(DEVICES_FOLDER)
    if not os.path.exists(devices_directory): raise RuntimeError("Devices directory does not exist")
    entries = os.listdir(devices_directory)

    devices = []

    for device in entries:
        base, extension = os.path.splitext(device)
        if not extension == ".json": continue

        type, model = base.split("_", 1)

        device = get_device(type, model)
        devices.append(device)

    return devices

def get_device(type = None, model = None, id = None):
    id = id or "%s_%s" % (type, model)
    device_path = os.path.join(DEVICES_FOLDER, "%s.json" % id)
    if not os.path.exists(device_path): raise RuntimeError("Device file does not exist")
    device_file = open(device_path, "rb")
    try: device = json.load(device_file)
    finally: device_file.close()

    return device

def merge(first, second, override = True):
    for key, value in second.items():
        if key in first and not override: continue
        first[key] = value

def filter(camera):
    type = camera.get("type", "axis")
    model = camera.get("model", "211")

    device = get_device(type, model)
    _camera = device.get("camera", {})
    settings = device.get("settings", {})

    merge(camera, _camera, override = False)

    for key, value in settings.items():
        if value: continue
        if not key in camera: continue
        del camera[key]

def run():
    # sets the debug control in the application
    # then checks the current environment variable
    # for the target port for execution (external)
    # and then start running it (continuous loop)
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(use_debugger = True, debug = True, use_reloader = False, host = "0.0.0.0", port = port)

if __name__ == "__main__":
    run()
