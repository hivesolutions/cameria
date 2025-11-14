#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Cameria System
# Copyright (c) 2008-2025 Hive Solutions Lda.
#
# This file is part of Hive Cameria System.
#
# Hive Cameria System is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Cameria System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Cameria System. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2025 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import os
import datetime

import flask  # @UnusedImport

import quorum

import cameria.models

SECRET_KEY = "dzhneqksmwtuinay5dfdljec19pi765p"
""" The "secret" key to be at the internal encryption
processes handled by flask (eg: sessions) """

MONGO_DATABASE = "cameria"
""" The default database to be used for the connection with
the MongoDB database """

CURRENT_DIRECTORY = os.path.dirname(__file__)
CURRENT_DIRECTORY_ABS = os.path.abspath(CURRENT_DIRECTORY)
UPLOAD_FOLDER = os.path.join(CURRENT_DIRECTORY_ABS, "uploads")

global app

if quorum.conf("LOAD_APP", True, cast=bool):
    app = quorum.load(
        name=__name__,
        secret_key=quorum.conf("SECRET_KEY", SECRET_KEY),
        redis_session=quorum.conf("REDIS_SESSION", True, cast=bool),
        mongo_database=quorum.conf("MONGO_DATABASE", MONGO_DATABASE),
        logger=quorum.conf("LOGGER", "cameria.debug"),
        models=cameria.models,
        PERMANENT_SESSION_LIFETIME=datetime.timedelta(365),
        UPLOAD_FOLDER=UPLOAD_FOLDER,
        MAX_CONTENT_LENGTH=1024**3,
    )
else:
    app = quorum.load(name=__name__)

import cameria.views  # @UnusedImport

if __name__ == "__main__":
    quorum.run(server="netius")
else:
    __path__ = []
