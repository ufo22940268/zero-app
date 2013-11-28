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
from pymongo import MongoClient
import random

raw_app = client.create_app()
app = raw_app.test_client()

def test_index():
    rv = app.get('/')
    assert rv.data.find('error') == -1

def test_add():
    rv = app.get('/add')
    assert rv.data.find('error') == -1

    rv = app.post('/add',
            data = {'field1': 'hongbosb', 'field2': 'shijiesb', 'radio_field': 'a'})
    assert rv.data
    assert rv.data.find('submit') == -1

    rv = app.get('index')
    assert rv.data.find('hongbosb') != -1
    assert rv.data.find('shijiesb') != -1

def get_db():
    client = MongoClient('mongodb://root:aa@127.0.0.1/zero')
    return client.zero

def test_init_data():
    shop_c = get_db()['shop']
    shop_c.drop()
    types = [u'优惠', u'活动', u'分期']
    urls = [u'https://pbs.twimg.com/profile_images/378800000401561807/4f288416a4ff51d49f892ad103c8308b.jpeg']
    for i in range(10):
        t = types[random.randint(0, 2)]
        u = urls[0]
        shop_c.insert({
            'name': 'shop %d' % i,
            'type': t,
            'image': u,
        })

    assert len(list(shop_c.find())) > 5
