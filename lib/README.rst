|travis ci build state|

|rtd state|

Introduction
============

Persistent Pineapple provides a simple interface to save settings for
applications or other modules.  The settings file is in the JSON format for
simplicty.  A slightly modified JSON format is used to allow for comments and
other creature features.  Please read the _json.py file for more details.

Documentation
=============

Documentation is hosted on readthedocs:
`persistetpineapple.readthedocs.org <http://persistetpineapple.readthedocs.org/en/latest/>`__

Install
=======

Download the tarball and install with ``pip install <package>``.

Usage
=====

See the unit tests for more in-depth examples. Here are the basics:


Example settings file (/etc/myapp.json)::
    {
        // App settings ///////////////////////////////////////////////////////////

        // Name of the program
        "program_name": "myapp",

        // HTTP POST listener port
        "port": 8009,

        // Debugging stuff
        "debug": true,

        // Logging settings
        "console_log_level": "INFO",
    }


Example code:
.. code:: python

    >>> settings = PersistentPineapple('/etc/myapp.json')
    >>> print settings.program_name
    myapp
    >>> if settings.debug:
    ...     print "we're in debug mode"
    we're in debug mode
    >>> settings.debug = False

.. |travis ci build state| image:: https://travis-ci.org/JasonAUnrein/Persistent-Pineapple.svg?branch=master
   :target: https://travis-ci.org/JasonAUnrein/Persistent-Pineapple

.. |rtd state| image:: https://readthedocs.org/projects/persistent-pineapple/badge/?version=latest
    :target: https://readthedocs.org/projects/persistent-pineapple/?badge=latest
    :alt: Documentation Status