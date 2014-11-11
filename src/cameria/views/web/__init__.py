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

from . import account
from . import base
from . import camera
from . import device
from . import set

from . import settings as _settings

from .account import list_accounts, list_accounts_json, new_account, create_account,\
    show_account, show_account_s, edit_account, update_account, delete_account
from .base import index, signin, login, logout, about, handler_404, handler_413,\
    handler_exception
from .camera import list_cameras, list_cameras_json, new_camera, create_camera, show_camera,\
    edit_camera, update_camera, delete_camera, settings_camera
from .device import list_devices, list_devices_json, new_device, create_device, show_device,\
    edit_device, update_device, delete_device
from .set import list_sets, list_sets_json, new_set, create_set, show_set, edit_set,\
    update_set, delete_set
from .settings import settings, import_a, import_do, export_do, reset_do
