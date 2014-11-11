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

import os
import datetime

import flask #@UnusedImport

import quorum

import cameria.models

SECRET_KEY = "dzhneqksmwtuinay5dfdljec19pi765p"
""" The "secret" key to be at the internal encryption
processes handled by flask (eg: sessions) """

MONGO_DATABASE = "cameria"
""" The default database to be used for the connection with
the mongo database """

CURRENT_DIRECTORY = os.path.dirname(__file__)
CURRENT_DIRECTORY_ABS = os.path.abspath(CURRENT_DIRECTORY)
UPLOAD_FOLDER = os.path.join(CURRENT_DIRECTORY_ABS, "uploads")

app = quorum.load(
    name = __name__,
    secret_key = SECRET_KEY,
    redis_session = True,
    mongo_database = MONGO_DATABASE,
    logger = "cameria.debug",
    models = cameria.models,
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(365),
    UPLOAD_FOLDER = UPLOAD_FOLDER,
    MAX_CONTENT_LENGTH = 1024 ** 3
)

import cameria.views #@UnusedImport

if __name__ == "__main__":
    quorum.run(server = "netius")
