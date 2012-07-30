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

YEAR_IN_SECS = 31536000

class SSLify(object):
    """
    Secures your flask app by enabling the forcing
    of the protocol in the http connection.
    """

    def __init__(self, app, age=YEAR_IN_SECS, subdomains=False):
        if app is not None:
            self.app = app
            self.hsts_age = age
            self.hsts_include_subdomains = subdomains

            self.init_app(self.app)
        else:
            self.app = None

    def init_app(self, app):
        """
        Configures the configured Flask app to enforce ssl.
        """

        app.before_request(self.redirect_to_ssl)
        app.after_request(self.set_hsts_header)

    @property
    def hsts_header(self):
        """
        Returns the proper hsts policy.
        """
        
        hsts_policy = "max-age={0}".format(self.hsts_age)

        if self.hsts_include_subdomains:
            hsts_policy += "; includeSubDomains"

        return hsts_policy

    def redirect_to_ssl(self):
        """
        Redirect incoming requests to https.
        """
        
        criteria = [
            flask.request.is_secure,
            self.app.debug,
            flask.request.headers.get("X-Forwarded-Proto", "http") == "https"
        ]

        if not any(criteria):
            if flask.request.url.startswith("http://"):
                url = flask.request.url.replace("http://", "https://", 1)
                r = flask.redirect(url)

                return r

    def set_hsts_header(self, response):
        """
        Adds HSTS header to each response.
        """

        response.headers.setdefault("Strict-Transport-Security", self.hsts_header)
        return response
