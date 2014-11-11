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

import traceback

from cameria import models

from cameria.main import app
from cameria.main import flask
from cameria.main import quorum

@app.route("/", methods = ("GET",))
@app.route("/index", methods = ("GET",))
@quorum.ensure("index")
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
    username = quorum.get_field("username")
    password = quorum.get_field("password")
    try: account = models.Account.login(username, password)
    except quorum.OperationalError as error:
        return flask.render_template(
            "signin.html.tpl",
            username = username,
            error = error.message
        )

    # updates the current user (name) in session with
    # the username that has just be accepted in the login
    flask.session["username"] = account.username
    flask.session["cameras"] = account.cameras and account.cameras.list()
    flask.session["tokens"] = account.tokens

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

@app.route("/about", methods = ("GET",))
@quorum.ensure("about")
def about():
    return flask.render_template(
        "about.html.tpl",
        link = "about"
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
    formatted = traceback.format_exc()
    lines = formatted.splitlines()
    status = error.code if hasattr(error, "code") else 500

    return flask.Response(
        flask.render_template(
            "error.html.tpl",
            error = str(error),
            traceback = lines
        ),
        status = status
    )
