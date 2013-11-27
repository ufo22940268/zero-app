#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 garlic <garlic@localhost.localdomain>
#
# Distributed under terms of the MIT license.

"""

"""

from zero import client
import pytest
import json

raw_app = client.create_app()
app = raw_app.test_client()

def test_index():
    rv = app.get('/')
    assert rv.data.find('error') == -1

def test_add():
    rv = app.get('/add')
    assert rv.data.find('error') == -1

    rv = app.post('/add',
            data = {'field1': 'aaaaa', 'field2': 'b', 'radio_field': 'a'})
    assert rv.data
    assert rv.data.find('submit') == -1
