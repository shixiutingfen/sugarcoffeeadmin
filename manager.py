#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
    manager.py
    ~~~~~~~~~~~

    flask manager script

    :copyright: (c) 2013.
    :license: BSD, see LICENSE for more details.
"""
from flask.ext.script import Server, Manager, prompt_bool
from myapp import app


manager = Manager(app)
manager.add_command("runserver", Server('0.0.0.0', port=6000))




if __name__ == "__main__":
    manager.run()
