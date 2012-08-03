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

import flask
import functools

YEAR_IN_SECS = 31536000
""" The number of seconds that exist in a
complete year (365 days) """

class SSLify(object):
    """
    Secures your flask app by enabling the forcing
    of the protocol in the http connection.
    """

    def __init__(self, app, age = YEAR_IN_SECS, subdomains = False):
        """
        Constructor of the class.

        @type app: App
        @param app: The application object to be used in the
        in ssl operation for the forcing of the protocol.
        @type age: int
        @param age: The maximum age of the hsts operation.
        @type subdomains: bool
        @param subdomains: If subdomain should be allows as part
        of the security policy.
        """

        if app is not None:
            self.app = app
            self.hsts_age = age
            self.hsts_include_subdomains = subdomains

            self.init_app(self.app)
        else:
            self.app = None

    def init_app(self, app):
        """
        Configures the configured flask app to enforce ssl.

        @type app: App
        @param app: The application to be configured to enforce
        the ssl redirection support.
        """

        app.before_request(self.redirect_to_ssl)
        app.after_request(self.set_hsts_header)

    @property
    def hsts_header(self):
        """
        Returns the proper hsts policy.

        @rtype: String
        @return: The proper hsts policy string value.
        """

        hsts_policy = "max-age={0}".format(self.hsts_age)
        if self.hsts_include_subdomains: hsts_policy += "; includeSubDomains"

        return hsts_policy

    def redirect_to_ssl(self):
        """
        Redirect incoming requests to https.

        @rtype: Request
        @return: The changed request containing the redirect
        instruction in case it's required.
        """

        criteria = [
            flask.request.is_secure,
            self.app.debug,
            flask.request.headers.get("X-Forwarded-Proto", "http") == "https"
        ]

        if not any(criteria):
            if flask.request.url.startswith("http://"):
                url = flask.request.url.replace("http://", "https://", 1)
                request = flask.redirect(url)

                return request

    def set_hsts_header(self, response):
        """
        Adds hsts header to each response.
        This header should enable extra security options to be
        interpreted at the client side.

        @type response: Response
        @param response: The response to be used to set the hsts
        policy header.
        @rtype: Response
        @return: The changed response object, containing the strict
        transport security (hsts) header.
        """

        response.headers.setdefault("Strict-Transport-Security", self.hsts_header)
        return response

def ensure_login(token = None):
    if "username" in flask.session and not token: return None
    if token in flask.session.get("tokens", []): return None
    return flask.redirect(
        flask.url_for("login")
    )

def ensure_user(username):
    _username = flask.session.get("username", None)
    if not _username == None and username == _username: return
    raise RuntimeError("Permission denied")

def ensure_camera(camera):
    cameras = flask.session.get("cameras", None)
    if cameras == None or camera["id"] in cameras: return
    raise RuntimeError("Permission denied")

def ensure_cameras(cameras):
    for camera in cameras: ensure_camera(camera)

def ensure_cameras_f(cameras):
    _cameras = []
    for camera in cameras:
        try: ensure_camera(camera)
        except: continue
        else: _cameras.append(camera)
    return _cameras

def ensure_sets_f(sets):
    _sets = []
    for set in sets:
        cameras = set.get("cameras", ())
        try: ensure_cameras(cameras)
        except: continue
        else: _sets.append(set)
    return _sets

def ensure(token = None):

    def decorator(function):

        @functools.wraps(function)
        def interceptor(*args, **kwargs):
            ensure = ensure_login(token)
            if ensure: return ensure
            return function(*args, **kwargs)

        return interceptor

    return decorator
