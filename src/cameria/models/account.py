#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Cameria System
# Copyright (c) 2008-2022 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2022 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import uuid
import time
import hashlib
import datetime

import quorum

from . import base
from . import camera

PASSWORD_SALT = "cameria"
""" The salt suffix to be used during the encoding
of the password into an hash value """

USER_TYPE = 1
""" The identifier (integer) to be used to represent an user
of type (normal) user """

SUPER_USER_TYPE = 2
""" The identifier (integer) to be used to represent a user
of type (super) user """

ADMIN_TYPE = 3
""" The identifier (integer) to be used to represent an user
of type admin (administrator) """

TYPE_NAMES = {
    USER_TYPE : "user",
    SUPER_USER_TYPE : "super user",
    ADMIN_TYPE : "admin"
}
""" The map associating the various values for the user types
with the appropriate string values that represent them """

USER_ACL = {
    USER_TYPE : (
        "index",
        "about",
        "sets.list",
        "sets.show",
        "cameras.list",
        "cameras.show",
        "accounts.show_s"
    ),
    SUPER_USER_TYPE : (
        "index",
        "about",
        "sets.list",
        "sets.show",
        "cameras.list",
        "cameras.show",
        "accounts.show_s"
    ),
    ADMIN_TYPE : (
        "*",
    )
}
""" The map associating the user type with the corresponding
list (sequence) of access control tokens """

class Account(base.Base):

    username = dict(
        index = True,
        immutable = True,
        default = True
    )

    password = dict(
        private = True
    )

    confirmation = dict(
        private = True
    )

    email = dict(
        index = True,
        immutable = True
    )

    login_count = dict(
        type = int
    )

    last_login = dict(
        type = float
    )

    type = dict(
        type = int
    )

    tokens = dict(
        type = list
    )

    cameras = dict(
        type = quorum.references(
            camera.Camera,
            name = "camera_id"
        )
    )

    @classmethod
    def setup(cls):
        super(Account, cls).setup()

        # tries to find the root account (default) in case it's not
        # found returns immediately nothing to be done
        root = cls.find(username = "root")
        if root: return

        # creates the various accounts that are going to be used for
        # the default initial access to the data source
        cls.create_account_d("root", "root", ADMIN_TYPE)

    @classmethod
    def validate(cls):
        return super(Account, cls).validate() + [
            quorum.equals("password_confirm", "password")
        ]

    @classmethod
    def validate_new(cls):
        return super(Account, cls).validate_new() + [
            quorum.not_null("username"),
            quorum.not_empty("username"),
            quorum.string_gt("username", 1),
            quorum.string_lt("username", 64),
            quorum.not_duplicate("username", cls._name()),

            quorum.not_null("password"),
            quorum.not_empty("password"),

            quorum.not_null("password_confirm"),
            quorum.not_empty("password_confirm"),

            quorum.not_null("email"),
            quorum.not_empty("email"),
            quorum.is_email("email"),
            quorum.not_duplicate("email", cls._name()),

            quorum.not_null("type"),

            quorum.not_null("cameras")
        ]

    @classmethod
    def login(cls, username, password):
        # verifies that both the username and the password are
        # correctly set in the current instance
        if not username or not password:
            raise quorum.OperationalError(
                "Both username and password must be provided",
                code = 400
            )

        # retrieves the account associated with the provided username
        # in case none is found raises an operational error indicating
        # the problem with the account retrieval
        account = cls.get(
            username = username,
            rules = False,
            build = False,
            raise_e = False
        )
        if not account:
            raise quorum.OperationalError(
                "No valid account found",
                code = 403
            )

        # creates the SHA1 hash value for the password and verifies that
        # the provided password is the expected
        password = password + PASSWORD_SALT
        password = quorum.legacy.bytes(password)
        password_sha1 = hashlib.sha1(password).hexdigest()
        _password = account.password
        if not password_sha1 == _password:
            raise quorum.OperationalError(
                "Invalid or mismatch password",
                code = 403
            )

        # sets the login count and last login values in the account as the
        # current time and then saves it in the data store
        login_count = account.val("login_count", 0)
        account.login_count = login_count + 1
        account.last_login = time.time()
        account.save()

        # returns the account representing the user that has just been logged
        # in into the system to the caller method
        return account

    @classmethod
    def create_account_d(cls, username, password, type, cameras = None):
        # creates the structure to be used as the root account description
        # using the default value and then stores the account as it's going
        # to be used as the default root entity (for administration)
        account = cls(
            enabled = True,
            username = username,
            password = password,
            email = "%s@cameria.com" % username,
            type = type,
            cameras = cameras
        )
        account.save(validate = False)
        account.enabled = True
        account.save()

    @classmethod
    def confirmed(cls, confirmation):
        # tries to retrieves the account for the provided confirmation
        # code and in case it fails produces an error
        account = cls.get(confirmation = confirmation)
        if not account: raise quorum.OperationalError("Account not found or invalid confirmation")
        if account.enabled: raise quorum.OperationalError("Account is already active")

        # sets the account model as enabled and then saves it in the
        # current data source
        account.enabled = True
        account.save()

    @classmethod
    def _build(cls, model, map):
        super(Account, cls)._build(model, map)
        enabled = model.get("enabled", False)
        email = model.get("email", None)
        last_login = model.get("last_login", None)
        last_login_date = last_login and datetime.datetime.utcfromtimestamp(last_login)
        last_login_string = last_login_date and last_login_date.strftime("%d/%m/%Y %H:%M:%S")
        model["enabled_l"] = enabled and "enabled" or "disabled"
        model["email_s"] = email and email.replace("@", " at ").replace(".", " dot ")
        model["last_login_l"] = last_login_string

    def pre_create(self):
        base.Base.pre_create(self)

        # in case the type of the account to be created is admin
        # the camera attribute should be set as invalid, indicating
        # that all the cameras should be displayed
        if self.type in (SUPER_USER_TYPE, ADMIN_TYPE): self.cameras = None

        # "encrypts" the password into the target format defined
        # by the salt and the SHA1 hash function and then creates
        # the API key for the current account
        self.password = hashlib.sha1(quorum.legacy.bytes(self.password + PASSWORD_SALT)).hexdigest()
        self.api_key = hashlib.sha1(quorum.legacy.bytes(str(uuid.uuid4()))).hexdigest()
        self.confirmation = hashlib.sha1(quorum.legacy.bytes(str(uuid.uuid4()))).hexdigest()

        # updates the various default values for the current account
        # user to be created
        self.enabled = False
        self.login_count = 0
        self.last_login = None
        if not hasattr(self, "type") or not self.type: self.type = USER_TYPE
        self.tokens = USER_ACL.get(self.type, ())

    def pre_update(self):
        base.Base.pre_update(self)

        # in case the type of the account to be created is admin
        # the camera attribute should be set as invalid, indicating
        # that all the cameras should be displayed
        if self.type in (SUPER_USER_TYPE, ADMIN_TYPE): self.cameras = None

        # in case the currently set password is empty it must
        # be removed (not meant to be updated), otherwise it
        # must be correctly encrypted using the current approach
        has_password = hasattr(self, "password")
        has_password_confirm = hasattr(self, "password_confirm")
        if has_password and self.password == "": del self.password
        elif has_password_confirm:
            self.password = hashlib.sha1(quorum.legacy.bytes(self.password + PASSWORD_SALT)).hexdigest()

    def post_create(self):
        base.Base.post_create(self)

        # runs the post operation for the preparation of the confirm
        # of the account (must send appropriate documents: email, etc.)
        self.confirm()

    def confirm(self):
        # creates a new account in order to obtain the new build
        # values (include obfuscated email value) restores the
        # confirmation values that has been removed (private value)
        account = self.copy(build = True)
        account.confirmation = self.confirmation

        # sends a mail about the confirmation of the email to the
        # the email address associated with the current account
        quorum.send_mail_a(
            subject = "Welcome to Cameria, please confirm you email",
            sender = "Cameria Mailer <mailer@cameria.com>",
            receivers = ["%s <%s>" % (self.username, self.email)],
            plain = "email/confirm.txt.tpl",
            rich = "email/confirm.html.tpl",
            context = dict(
                account = account
            )
        )

    def type_s(self):
        return TYPE_NAMES.get(self.type, None)
