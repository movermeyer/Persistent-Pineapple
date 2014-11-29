[![travis ci build state](https://travis-ci.org/JasonAUnrein/Persistent-Pineapple.svg?branch=master)](https://travis-ci.org/JasonAUnrein/Persistent-Pineapple)

[![rtd state](https://readthedocs.org/projects/persistent-pineapple/badge/?version=latest)](https://readthedocs.org/projects/persistent-pineapple/?badge=latest)

[![Coverage Status](https://img.shields.io/coveralls/JasonAUnrein/Persistent-Pineapple.svg)](https://coveralls.io/r/JasonAUnrein/Persistent-Pineapple)

## Introduction
Persistent Pineapple provides a simple interface to save settings for
applications or other modules.  The settings file is in the JSON format for
simplicty.  A slightly modified JSON format is used to allow for comments and
other creature features.  Please read the _json.py file for more details.

## Documentation
Documentation is hosted on [persistetpineapple.readthedocs.org](http://persistetpineapple.readthedocs.org/en/latest/)

## Install
Download the tarball and install with `pip install <package>`.

## Usage
See the unit tests for more in-depth examples. Here are the basics:

### Example code

```
    settings = PersistentPineapple('/etc/myapp.json')
    print settings.program_name
    if settings.debug:
        print "we're in debug mode"
    settings.debug = False
```

### Example settings file (/etc/myapp.json)

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
