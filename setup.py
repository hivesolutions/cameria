#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Cameria System
# Copyright (c) 2008-2016 Hive Solutions Lda.
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

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2016 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import os
import setuptools

setuptools.setup(
    name = "cameria",
    version = "0.1.0",
    author = "Hive Solutions Lda.",
    author_email = "development@hive.pt",
    description = "Cameria Web Interface",
    license = "Apache License, Version 2.0",
    keywords = "cameria cameras iptv control",
    url = "http://cameria.hive.pt",
    zip_safe = False,
    packages = [
        "cameria",
        "cameria.models",
        "cameria.views",
        "cameria.views.api",
        "cameria.views.web"
    ],
    package_dir = {
        "" : os.path.normpath("src")
    },
    package_data = {
        "cameria" : [
            "static/css/*",
            "static/images/*",
            "static/js/*",
            "templates/*.tpl",
            "templates/account/*.tpl",
            "templates/camera/*.tpl",
            "templates/device/*.tpl",
            "templates/partials/*.tpl",
            "templates/set/*.tpl",
            "templates/settings/*.tpl"
        ]
    },
    install_requires = [
        "flask",
        "quorum"
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ]
)
