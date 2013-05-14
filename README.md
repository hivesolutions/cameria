# Cameria, web cameras infra-structure

Simplified web based camera visualization system, developed using both [quorum](https://github.com/hivesolutions/flask_quorum)
and [uxf](https://github.com/hivesolutions/uxf).

## Configuration

Simply configure a WSGI server pointing to [cameria.wsgi](src/cameria.wsgi).

Example configuration for viriatum:

    [location:cameria]
    path = /cameria
    handler = wsgi
    script_reload = Off
    script_path = $location/mantium.wsgi

## iOS

Please refer to the proper [cameria for ios](https://github.com/hivesolutions/cameria_ios) page.
