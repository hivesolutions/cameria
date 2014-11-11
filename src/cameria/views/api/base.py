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

@app.route("/api/login.json", methods = ("GET", "POST"), json = True)
@app.route("/api/signin.json", methods = ("GET", "POST"), json = True)
def login_api():
    # retrieves both the username and the password from
    # the flask request form, these are the values that
    # are going to be used in the username validation
    username = quorum.get_field("username")
    password = quorum.get_field("password")
    account = models.Account.login(username, password)

    # updates the current user (name) in session with
    # the username that has just be accepted in the login
    flask.session["username"] = account.username
    flask.session["cameras"] = account.cameras and account.cameras.list()
    flask.session["tokens"] = account.tokens

    # makes the current session permanent this will allow
    # the session to persist along multiple browser initialization
    flask.session.permanent = True

    # tries to retrieve the session identifier from the current
    # session but only in case it exists
    sid = hasattr(flask.session, "sid") and flask.session.sid or None

    return dict(
        sid = sid,
        session_id = sid,
        username = username
    )

@app.route("/api/logout.json", methods = ("GET", "POST"), json = True)
@app.route("/api/signout.json", methods = ("GET", "POST"), json = True)
def logout_api():
    # removes the various session associated values from the
    # session so that the used is no longer allowed to interact
    # with the system (at least for private operations)
    if "username" in flask.session: del flask.session["username"]
    if "cameras" in flask.session: del flask.session["cameras"]
    if "tokens" in flask.session: del flask.session["tokens"]

    return dict()

@app.route("/api/session.json", methods = ("GET",))
def session_api():
    session = flask.session
    id = hasattr(session, "sid") and session.sid or None

    return dict(id = id)
