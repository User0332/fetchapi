from ._types import *
from httpx import Response as HTTPXResponse, Headers as HTTPXHeaders
from typing import TypedDict

class Response:
	def __init__(self, response: HTTPXResponse):
		self._response = response

	@property
	def body(self) -> bytes:
		self._body_used = None
		return self._response.content

	@property
	def bodyUsed(self) -> bool:
		return hasattr(self, "_body_used")

	@property
	def headers(self) -> HTTPXHeaders:
		return self._response.headers

	@property
	def ok(self) -> bool:
		return (200 <= self._response.status_code <= 299
)
	@property
	def status(self) -> int:
		return self._response.status_code

	@property
	def statusText(self) -> str:
		return # FIX

class Options(TypedDict):
	method: Method # done
	headers: Headers # done
	body: Body # done
	mode: Mode # done
	credentials: Credentials
	cache: Cache # done
	redirect: Redirect # done
	referrer: Referrer # done
	referrerPolicy: ReferrerPolicy # done
	integrity: Integrity
	keepalive: KeepAlive # done


