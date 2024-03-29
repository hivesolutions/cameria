# [![Cameria](res/logo.png)](http://cameria.hive.pt)

Simplified web based camera visualization system, developed using both [Quorum](https://github.com/hivesolutions/flask_quorum)
and [UXF](https://github.com/hivesolutions/uxf).

## Configuration

Simply configure a WSGI server pointing to [cameria.wsgi](src/cameria.wsgi).

Example configuration for [Viriatum](http://viriatum.hive.pt):

    [location:cameria]
    path = /cameria
    handler = wsgi
    script_reload = Off
    script_path = $location/mantium.wsgi

## iOS

Please refer to the proper [Cameria for iOS](https://github.com/hivesolutions/cameria_ios) page.

## License

Cameria is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://app.travis-ci.com/hivesolutions/cameria.svg?branch=master)](https://travis-ci.com/github/hivesolutions/cameria)
[![Coverage Status](https://coveralls.io/repos/hivesolutions/cameria/badge.svg?branch=master)](https://coveralls.io/r/hivesolutions/cameria?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/cameria.svg)](https://pypi.python.org/pypi/cameria)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/)
