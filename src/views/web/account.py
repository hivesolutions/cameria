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

@app.route("/accounts", methods = ("GET",))
@quorum.ensure("accounts.list")
def list_accounts():
    return flask.render_template(
        "account/list.html.tpl",
        link = "accounts",
        sub_link = "list"
    )

@app.route("/accounts.json", methods = ("GET",), json = True)
@quorum.ensure("accounts.list", json = True)
def list_accounts_json():
    object = quorum.get_object(alias = True, find = True)
    accounts = models.Account.find(map = True, sort = [("username", 1)], **object)
    return accounts

@app.route("/account/new", methods = ("GET",))
@quorum.ensure("accounts.new")
def new_account():
    return flask.render_template(
        "account/new.html.tpl",
        link = "accounts",
        sub_link = "create",
        account = {
            "device" : {}
        },
        errors = {}
    )

@app.route("/accounts/<username>", methods = ("GET",))
@quorum.ensure("accounts.show")
def show_account(username):
    account = models.Account.get(username = username)
    return flask.render_template(
        "account/show.html.tpl",
        link = "accounts",
        sub_link = "show",
        account = account
    )

@app.route("/account", methods = ("GET",))
@quorum.ensure("accounts.show_s")
def show_account_s():
    username = flask.session["username"]
    account = models.Account.get(username = username)
    return flask.render_template(
        "account/show.html.tpl",
        link = "accounts",
        sub_link = "show",
        account = account
    )
