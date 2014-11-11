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

@app.route("/sets", methods = ("GET",))
@quorum.ensure("sets.list")
def list_sets():
    return flask.render_template(
        "set/list.html.tpl",
        link = "sets",
        sub_link = "list"
    )

@app.route("/sets.json", methods = ("GET",), json = True)
@quorum.ensure("sets.list", json = True)
def list_sets_json():
    object = quorum.get_object(alias = True, find = True)
    object["sort"] = object.get("sort", [("name", 1)])
    sets = models.Set.find_a(map = True, **object)
    return sets

@app.route("/set/new", methods = ("GET",))
@quorum.ensure("sets.new")
def new_set():
    return flask.render_template(
        "set/new.html.tpl",
        link = "sets",
        sub_link = "create",
        set = {
            "cameras" : {}
        },
        errors = {}
    )

@app.route("/sets", methods = ("POST",))
@quorum.ensure("sets.new")
def create_set():
    # creates the new set, using the provided arguments and
    # then saves it into the data source, all the validations
    # should be ran upon the save operation
    set = models.Set.new()
    try: set.save()
    except quorum.ValidationError as error:
        return flask.render_template(
            "set/new.html.tpl",
            link = "sets",
            sub_link = "create",
            set = error.model,
            errors = error.errors
        )

    # redirects the user to the show page of the set that
    # was just created (normal workflow)
    return flask.redirect(
        flask.url_for("show_set", set_id = set.set_id)
    )

@app.route("/sets/<set_id>", methods = ("GET",))
@quorum.ensure("sets.show")
def show_set(set_id):
    set = models.Set.get_a(set_id = set_id)
    set.merge_cameras()
    return flask.render_template(
        "set/show.html.tpl",
        link = "sets",
        sub_link = "show",
        set = set
    )

@app.route("/sets/<set_id>/edit", methods = ("GET",))
@quorum.ensure("sets.edit")
def edit_set(set_id):
    set = models.Set.get_a(set_id = set_id)
    return flask.render_template(
        "set/edit.html.tpl",
        link = "sets",
        sub_link = "edit",
        set = set,
        errors = {}
    )

@app.route("/sets/<set_id>/edit", methods = ("POST",))
@quorum.ensure("sets.edit")
def update_set(set_id):
    # finds the current set and applies the provided
    # arguments and then saves it into the data source,
    # all the validations should be ran upon the save operation
    set = models.Set.get_a(set_id = set_id)
    set.apply()
    try: set.save()
    except quorum.ValidationError as error:
        return flask.render_template(
            "set/edit.html.tpl",
            link = "sets",
            sub_link = "edit",
            set = error.model,
            errors = error.errors
        )

    # redirects the user to the show page of the set that
    # was just updated
    return flask.redirect(
        flask.url_for("show_set", set_id = set_id)
    )

@app.route("/sets/<set_id>/delete", methods = ("GET",))
@quorum.ensure("sets.delete")
def delete_set(set_id):
    set = models.Set.get_a(set_id = set_id)
    set.delete()
    return flask.redirect(
        flask.url_for("list_sets")
    )

@app.route("/sets/<set_id>/settings", methods = ("GET",))
@quorum.ensure("sets.settings")
def settings_set(set_id):
    set = models.Set.get_a(set_id = set_id)
    return flask.render_template(
        "set/settings.html.tpl",
        link = "sets",
        sub_link = "settings",
        set = set
    )
