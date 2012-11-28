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
import hashlib
import tempfile
import datetime
import cStringIO

import quorum

SECRET_KEY = "dzhneqksmwtuinay5dfdljec19pi765p"
""" The "secret" key to be at the internal encryption
processes handled by flask (eg: sessions) """

PASSWORD_SALT = "cameria"
""" The salt suffix to be used during the encoding
of the password into an hash value """

MONGO_URL = "mongodb://localhost:27017"
""" The default url to be used for the connection with
the mongo database """

MONGO_DATABASE = "cameria"
""" The default database to be used for the connection with
the mongo database """

SINGLE_ENTITIES = (
    ("users", "username"),
)
""" The set of entities to be considered single file
oriented (exports to one file per complete set) """

MULTIPLE_ENTITIES = (
    ("sets", "id"),
    ("cameras", "id"),
    ("devices", "id")
)
""" The set of entities to be considered multiple file
oriented (exports to one file per entity) """

CURRENT_DIRECTORY = os.path.dirname(__file__)
CURRENT_DIRECTORY_ABS = os.path.abspath(CURRENT_DIRECTORY)
UPLOAD_FOLDER = os.path.join(CURRENT_DIRECTORY_ABS, "uploads")
SETS_FOLDER = os.path.join(CURRENT_DIRECTORY_ABS, "sets")
CAMERAS_FOLDER = os.path.join(CURRENT_DIRECTORY_ABS, "cameras")
DEVICES_FOLDER = os.path.join(CURRENT_DIRECTORY_ABS, "devices")
SETTINGS_FOLDER = os.path.join(CURRENT_DIRECTORY_ABS, "settings")

app = flask.Flask(__name__)
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(365)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 1024 ** 3

@app.route("/", methods = ("GET",))
@app.route("/index", methods = ("GET",))
@quorum.extras.ensure("index")
def index():
    return flask.render_template(
        "index.html.tpl",
        link = "home"
    )

@app.route("/signin", methods = ("GET",))
def signin():
    return flask.render_template(
        "signin.html.tpl"
    )

@app.route("/signin", methods = ("POST",))
def login():
    # retrieves both the username and the password from
    # the flask request form, these are the values that
    # are going to be used in the username validation
    username = flask.request.form.get("username", None)
    password = flask.request.form.get("password", None)

    # in case any of the mandatory arguments is not provided
    # an error is set in the current page
    if not username or not password:
        return flask.render_template(
            "signin.html.tpl",
            username = username,
            error = "Both username and password must be provided"
        )

    # retrieves the structure containing the information
    # on the currently available users and unpacks the
    # various attributes from it (defaulting to base values)
    users = get_users_m()
    user = users.get(username, {})
    _password = user.get("password", None)

    # encodes the provided password into an sha1 hash appending
    # the salt value to it before the encoding
    password_sha1 = hashlib.sha1(password + PASSWORD_SALT).hexdigest()

    # checks that both the user structure and the password values
    # are present and that the password matched, if one of these
    # values fails the login process fails and the user is redirected
    # to the signin page with an error string
    if not user or not _password or not password_sha1 == _password:
        return flask.render_template(
            "signin.html.tpl",
            username = username,
            error = "Invalid username and/or password"
        )

    # retrieves the tokens and cameras sequence from the user to set
    # them in the current session
    tokens = user.get("tokens", ())
    cameras = user.get("cameras", None)

    # updates the current user (name) in session with
    # the username that has just be accepted in the login
    flask.session["username"] = username
    flask.session["tokens"] = tokens
    flask.session["cameras"] = cameras

    # makes the current session permanent this will allow
    # the session to persist along multiple browser initialization
    flask.session.permanent = True

    return flask.redirect(
        flask.url_for("index")
    )

@app.route("/signout", methods = ("GET", "POST"))
def logout():
    if "username" in flask.session: del flask.session["username"]
    if "tokens" in flask.session: del flask.session["tokens"]
    if "cameras" in flask.session: del flask.session["cameras"]

    return flask.redirect(
        flask.url_for("signin")
    )

@app.route("/import", methods = ("GET",))
@quorum.extras.ensure("import")
def import_d():
    return flask.render_template(
        "import.html.tpl",
        link = "import"
    )

@app.route("/import", methods = ("POST",))
@quorum.extras.ensure("import")
def import_do():
    # retrieves the import file values (reference to the
    # uploaded file) and then validates if it has been
    # defined, in case it fails prints the template with
    # the appropriate error variable set
    import_file = flask.request.files.get("import_file", None)
    if import_file == None or not import_file.filename:
        return flask.render_template(
            "import.html.tpl",
            error = "No file defined"
        )

    # creates a temporary file path for the storage of the file
    # and then saves it into that directory
    fd, file_path = tempfile.mkstemp()
    import_file.save(file_path)

    db = quorum.mongo.get_db()
    manager = quorum.export.ExportManager(
        db,
        single = SINGLE_ENTITIES,
        multiple = MULTIPLE_ENTITIES
    )
    try: manager.import_data(file_path)
    finally: os.close(fd); os.remove(file_path)
    return flask.redirect(
        flask.url_for("index")
    )

@app.route("/export", methods = ("GET",))
@quorum.extras.ensure("export")
def export_do():
    db = quorum.mongo.get_db()
    file = cStringIO.StringIO()
    manager = quorum.export.ExportManager(
        db,
        single = SINGLE_ENTITIES,
        multiple = MULTIPLE_ENTITIES
    )
    manager.export_data(file)
    return flask.Response(
        file.getvalue(),
        headers = {
            "Content-Disposition" : "attachment; filename=database.dat"
        },
        mimetype = "application/octet-stream"
    )

@app.route("/about", methods = ("GET",))
@quorum.extras.ensure("about")
def about():
    return flask.render_template(
        "about.html.tpl",
        link = "about"
    )

@app.route("/sets", methods = ("GET",))
@quorum.extras.ensure("sets.list")
def list_set():
    sets = get_sets()
    sets = ensure_sets_f(sets)

    return flask.render_template(
        "sets_list.html.tpl",
        link = "sets",
        sets = sets
    )

@app.route("/sets/<id>", methods = ("GET",))
@quorum.extras.ensure("sets.show")
def show_set(id):
    set = get_set(id)
    cameras = set.get("cameras", [])
    ensure_cameras(cameras)

    return flask.render_template(
        "sets_show.html.tpl",
        link = "sets",
        sub_link = "show",
        set = set
    )

@app.route("/sets/<id>/settings", methods = ("GET",))
@quorum.extras.ensure("sets.settings")
def settings_set(id):
    set = get_set(id)

    return flask.render_template(
        "sets_settings.html.tpl",
        link = "sets",
        sub_link = "settings",
        set = set
    )

@app.route("/cameras", methods = ("GET",))
@quorum.extras.ensure("cameras.list")
def list_camera():
    cameras = get_cameras()
    cameras = ensure_cameras_f(cameras)

    return flask.render_template(
        "cameras_list.html.tpl",
        link = "cameras",
        cameras = cameras
    )

@app.route("/cameras/<id>", methods = ("GET",))
@quorum.extras.ensure("cameras.show")
def show_camera(id):
    camera = get_camera(id)
    filter(camera)
    ensure_camera(camera)

    return flask.render_template(
        "cameras_show.html.tpl",
        link = "cameras",
        sub_link = "show",
        camera = camera
    )

@app.route("/cameras/<id>/settings", methods = ("GET",))
@quorum.extras.ensure("cameras.settings")
def settings_camera(id):
    camera = get_camera(id)
    ensure_camera(camera)

    return flask.render_template(
        "cameras_settings.html.tpl",
        link = "cameras",
        sub_link = "settings",
        camera = camera
    )

@app.route("/devices", methods = ("GET",))
@quorum.extras.ensure("devices.list")
def list_device():
    devices = get_devices()

    return flask.render_template(
        "devices_list.html.tpl",
        link = "devices",
        devices = devices
    )

@app.route("/device/<id>", methods = ("GET",))
@quorum.extras.ensure("devices.show")
def show_device(id):
    device = get_device(id = id)

    return flask.render_template(
        "devices_show.html.tpl",
        link = "devices",
        sub_link = "show",
        device = device
    )

@app.route("/user/<username>", methods = ("GET",))
@quorum.extras.ensure("users.show")
def show_user(username):
    user = get_user(username = username)
    username = user["username"]
    quorum.extras.ensure_user(username)

    return flask.render_template(
        "users_show.html.tpl",
        link = "users",
        sub_link = "show",
        user = user
    )

@app.route("/login.json", methods = ("GET", "POST"))
@app.route("/signin.json", methods = ("GET", "POST"))
def login_json():
    # retrieves both the username and the password from
    # the flask request args or form, these are the values that
    # are going to be used in the username validation
    username = flask.request.args.get(
        "username",
        flask.request.form.get("username", None)
    )
    password = flask.request.args.get(
        "password",
        flask.request.form.get("password", None)
    )

    # in case any of the mandatory arguments is not provided
    # an error is set in the current page
    if not username or not password:
        return flask.Response(
            json.dumps({
                "exception" : {
                    "message" : "Both username and password must be provided"
                }
            }),
            status = 400,
            mimetype = "application/json"
        )

    # retrieves the structure containing the information
    # on the currently available users and unpacks the
    # various attributes from it (defaulting to base values)
    users = get_users()
    user = users.get(username, {})
    _password = user.get("password", None)

    # encodes the provided password into an sha1 hash appending
    # the salt value to it before the encoding
    password_sha1 = hashlib.sha1(password + PASSWORD_SALT).hexdigest()

    # checks that both the user structure and the password values
    # are present and that the password matched, if one of these
    # values fails the login process fails and an error is sent
    # to the used (client) indicating so
    if not user or not _password or not password_sha1 == _password:
        return flask.Response(
            json.dumps({
                "exception" : {
                    "message" : "Invalid user name and/or password"
                }
            }),
            status = 403,
            mimetype = "application/json"
        )

    # retrieves the tokens and cameras sequence from the user to set
    # them in the current session
    tokens = user.get("tokens", ())
    cameras = user.get("cameras", None)

    # updates the current user (name) in session with
    # the username that has just be accepted in the login
    flask.session["username"] = username
    flask.session["tokens"] = tokens
    flask.session["cameras"] = cameras

    # makes the current session permanent this will allow
    # the session to persist along multiple browser initialization
    flask.session.permanent = True

    # tries to retrieve the session identifier from the current
    # session but only in case it exists
    sid = hasattr(flask.session, "sid") and flask.session.sid or None

    return flask.Response(
        json.dumps({
            "sid" : sid,
            "session_id" : sid,
            "username" : username
        }),
        mimetype = "application/json"
    )

@app.route("/sets.json", methods = ("GET",))
@quorum.extras.ensure("sets.list", json = True)
def list_set_json():
    sets = get_sets()
    sets = ensure_sets_f(sets)

    return flask.Response(
        json.dumps({
            "sets" : sets
        }),
        mimetype = "application/json"
    )

@app.route("/cameras.json", methods = ("GET",))
@quorum.extras.ensure("cameras.list", json = True)
def list_camera_json():
    cameras = get_cameras()
    cameras = ensure_cameras_f(cameras)

    return flask.Response(
        json.dumps({
            "cameras" : cameras
        }),
        mimetype = "application/json"
    )

@app.route("/session.json", methods = ("GET",))
def session_json():
    session = flask.session
    id = hasattr(session, "sid") and session.sid or None

    return flask.Response(
        json.dumps({
            "id" : id
        }),
        mimetype = "application/json"
    )

@app.errorhandler(404)
def handler_404(error):
    return flask.Response(
        flask.render_template(
            "error.html.tpl",
            error = "404 - Page not found"
        ),
        status = 404
    )

@app.errorhandler(413)
def handler_413(error):
    return flask.Response(
        flask.render_template(
            "error.html.tpl",
            error = "412 - Precondition failed"
        ),
        status = 413
    )

@app.errorhandler(BaseException)
def handler_exception(error):
    return flask.Response(
        flask.render_template(
            "error.html.tpl",
            error = str(error)
        ),
        status = 500
    )

def get_users():
    users_path = os.path.join(SETTINGS_FOLDER, "users.json")
    if not os.path.exists(users_path): raise RuntimeError("Users file does not exist")
    users_file = open(users_path, "rb")
    try: users = json.load(users_file)
    finally: users_file.close()

    return users

def get_users_m():
    db = quorum.mongo.get_db()
    users = quorum.mongo.MongoMap(db.users, "username")
    return users

def get_user(username):
    users = get_users()
    user = users.get(username, None)
    if not user: raise RuntimeError("User '%s' not found" % username)

    return user

def get_sets():
    sets_directory = os.path.join(SETS_FOLDER)
    if not os.path.exists(sets_directory): raise RuntimeError("Sets directory does not exist")
    entries = os.listdir(sets_directory)
    entries.sort()

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
    entries.sort()

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
    entries.sort()

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

def ensure_cameras(cameras):
    for camera in cameras: ensure_camera(camera)

def ensure_cameras_f(cameras):
    _cameras = []
    for camera in cameras:
        try: ensure_camera(camera)
        except: continue
        else: _cameras.append(camera)
    return _cameras

def ensure_camera(camera):
    cameras = flask.session.get("cameras", None)
    if cameras == None or camera["id"] in cameras: return
    raise RuntimeError("Permission denied")

def ensure_sets_f(sets):
    _sets = []
    for set in sets:
        cameras = set.get("cameras", ())
        try: ensure_cameras(cameras)
        except: continue
        else: _sets.append(set)
    return _sets

def load():
    # sets the global wide application settings and
    # configures the application object according to
    # this settings
    debug = os.environ.get("DEBUG", False) and True or False
    redis_url = os.getenv("REDISTOGO_URL", None)
    not debug and quorum.extras.SSLify(app)
    app.session_interface = quorum.extras.RedisSessionInterface(url = redis_url)
    app.debug = debug
    app.secret_key = SECRET_KEY

def run():
    # sets the debug control in the application
    # then checks the current environment variable
    # for the target port for execution (external)
    # and then start running it (continuous loop)
    debug = os.environ.get("DEBUG", False) and True or False
    reloader = os.environ.get("RELOADER", False) and True or False
    redis_url = os.getenv("REDISTOGO_URL", None)
    mongo_url = os.getenv("MONGOHQ_URL", MONGO_URL)
    port = int(os.environ.get("PORT", 5000))
    quorum.mongo.url = mongo_url
    quorum.mongo.database = MONGO_DATABASE
    not debug and quorum.extras.SSLify(app)
    app.session_interface = quorum.extras.RedisSessionInterface(url = redis_url)
    app.debug = debug
    app.secret_key = SECRET_KEY
    app.run(
        use_debugger = debug,
        debug = debug,
        use_reloader = reloader,
        host = "0.0.0.0",
        port = port
    )

if __name__ == "__main__": run()
else: load()
