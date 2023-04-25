"""
Like the JavaScript fetch() function - just for fun!
"""

import httpx
import httpx._client
import asyncio
from promiseapi import Promise
from contextlib import asynccontextmanager
from types import FunctionType
from ._classes import Options, Response
from . import cache

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

	headers = options.get("headers", {})
	cache_option: str = options.get("cache", "no-cache")

	headers["Referer"] = options.get("referer")
	headers["Referrer-Policy"] = options.get("referrerPolicy")
	headers["Keep-Alive"] = options.get("keepalive")
	headers["Sec-Fetch-Mode"] = options.get("mode")
	if cache_option in ("no-cache", "no-store"):
		headers["Cache-Control"] = cache_option

	headers = { header: value for header, value in headers.items() if value is not None }

	if cache_option in ("only-if-cached", "force-cache", "default"):
		val = cache.CACHE.get(resource+str(options))

		if val: resolve(val)
		if cache_option == "only-if-cached":
			reject( 
				httpx.RequestError(
					"There was no request in the cache!"
				)
			)

	try:
		with httpx.Client(
			max_redirects=(0 if options.get("redirect") == "error" else httpx._client.DEFAULT_MAX_REDIRECTS),
			headers=headers,
			follow_redirects=(
				True if options.get("redirect") == "follow" else False
			),
		) as client:
			res = client.request(
				options.get("method", "GET"),
				resource,
				content=options.get("body", "")
			)

		obj = Response(res)

		if cache_option in ("force-cache", "no-cache"): cache.CACHE[resource+str(options)] = obj

		resolve(obj)
	except Exception as e:
		reject(e)

def fetch(resource: str, options: Options={}) -> Promise[Response]:
	"""Like the JavaScript fetch() function - just for fun!"""

	return Promise(
		lambda resolve, reject: 
		_sync_fetch(
			resolve, reject, 
			resource, options
		)
	)