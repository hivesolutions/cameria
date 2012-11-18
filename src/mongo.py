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

try: import pymongo
except: pymongo = None

connection = None
""" The global connection object that should persist
the connection relation with the database service """

class MongoMap(object):
    """
    Encapsulates a mongo collection to provide an interface
    that is compatible with the "normal" key value access
    offered by the python dictionary (map).
    """

    collection = None
    """ The collection to be used as the underlying structure
    for the data access """

    key = None
    """ The name of the key to be used for the "default" search
    for value providing """

    def __init__(self, collection, key = "id"):
        self.collection = collection
        self.key = key

    def get(self, value, default = None):
        return self.collection.find_one({self.key : value}) or default

def get_connection():
    global connection
    if pymongo == None: return None
    if not connection: connection = pymongo.Connection("localhost", 27017)
    return connection

def get_db():
    connection = get_connection()
    if not connection: return None
    db = connection.cameria
    return db