#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import time,uuid
import orm
import asyncio
import logging
import aiomysql
from orm import Model,StringField,BooleanField,FloatField,TextField

def next_id():
	return '%015d%s000' % (int(time.time()*1000),uuid.uuid4().hex)

class User(Model):
	__table__ = 'users'

	id = StringField(primary_key = True,default = next_id,ddl='varchar(50)')
	email = StringField(ddl = 'varchar(50)')
	passwd = StringField(ddl = 'varchar(50)')
	admin = BooleanField()
	name = StringField(ddl = 'varchar(50)')
	image = StringField(ddl = 'varcahr(50)')
	created_at = FloatField(default = time.time)

class Blog(Model):
	__table__ = 'blogs'

	id = StringField(primary_key = True,default = next_id,ddl='varchar(50)')
	email = StringField(ddl = 'varchar(50)')
	passwd = StringField(ddl = 'varchar(50)')
	admin = BooleanField()
	name = StringField(ddl = 'varchar(50)')
	image = StringField(ddl = 'varcahr(50)')
	created_at = FloatField(default = time.time)

class Comment(Model):
	__table__ = 'comment'

	id = StringField(primary_key = True,default = next_id,ddl='varchar(50)')
	email = StringField(ddl = 'varchar(50)')
	passwd = StringField(ddl = 'varchar(50)')
	admin = BooleanField()
	name = StringField(ddl = 'varchar(50)')
	image = StringField(ddl = 'varcahr(50)')
	created_at = FloatField(default = time.time)
'''
async def test():
	re = await create_pool(None,user = 'root',password = '12345678',db = 'awesome')
	u = User(name = 'test',email = 'xxx@gmail.com',passwd = '123124',image = 'sdsd')
	u.save
	print(next_id())
'''

async def test():
	await orm.create_pool(loop=loop,user = 'root',password = '12345678',db = 'awesome')
	print('222222')
	u = User(name = 'test',email = 'xxx@gmail.com',passwd = '123124',image = 'sdsd')
	print('333333')
	await u.save()
	print('444444')
	print(next_id())

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
print('6666')