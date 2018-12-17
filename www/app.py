#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
	# 如果不添加content_type，某些严谨的浏览器会把网页当成文件下载，而不是直接显示
    resp = web.Response(body = b'<h1>Awesome</h1>')
    resp.content_type = 'text/html;charset=utf-8'
	return resp 

async def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('GET','/',index)
	srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
	logging.info('server started at http://127.0.0.1:9000...') #输出日志
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()