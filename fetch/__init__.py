"""
Like the JavaScript fetch() function - just for fun!
"""

import httpx
import asyncio
from promiseapi import Promise
from contextlib import contextmanager, asynccontextmanager
from types import FunctionType
from ._classes import Options

TASKS: list[asyncio.Task] = []

async def _clean():
	"""Await all async tasks"""
	await asyncio.gather(*TASKS)

@asynccontextmanager
async def fetch_ctx(): # call to cleanup if using _fetch() async
	try: yield
	finally: await _clean()

async def _fetch(resource: str, options: Options={}) -> httpx.Response:
	"""Async utility"""
	
	async with httpx.AsyncClient() as client:
			return await client.request(
				options.get("method", "GET"),
				resource,
				data=options.get("body", {}),
				headers=options.get("headers", {}),
			)
		
def _sync_fetch(resolve: FunctionType, reject: FunctionType, resource: str, options: Options={}) -> httpx.Response:
	"""Inner synchronous fetch utility"""

	try:
		res = httpx.request(
			options.get("method", "GET"),
			resource,
			data=options.get("body", {}),
			headers=options.get("headers", {}),
		)
		resolve(res)
	except Exception as e:
		reject(e)

def fetch(resource: str, options: Options={}):
	"""Like the JavaScript fetch() function - just for fun!"""

	return Promise(
		lambda resolve, reject: 
		_sync_fetch(
			resolve, reject, 
			resource, options
		)
	)