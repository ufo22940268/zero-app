#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 garlic <garlic@localhost.localdomain>
#
# Distributed under terms of the MIT license.

"""

"""

from zero import sample_app

app = sample_app.create_app().test_client()

def test_index():
    rv = app.get('/')
    assert rv.data == 'ok'
