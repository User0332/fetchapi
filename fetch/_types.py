from typing import Union, Literal

Method = Union[
	Literal["GET"],
	Literal["POST"],
	Literal["DELETE"],
	Literal["HEAD"],
	Literal["PUT"],
	Literal["CONNECT"],
	Literal["OPTIONS"],
	Literal["TRACE"],
	Literal["PATCH"],
	str
]

Headers = Union[dict[str, str], None]
Body = Union[str, None]
Mode = Union[
	Literal["cors"],
	Literal["no-cors"],
	Literal["same-origin"],
	str,
	None
]

Credentials = Union[
	Literal["omit"],
	Literal["same-origin"],
	Literal["include"],
	None
]

Cache = Union[
	Literal["default"], 
	Literal["no-store"], 
	Literal["reload"], 
	Literal["no-cache"], 
	Literal["force-cache"], 
	Literal["only-if-cached"],
	None
]

Redirect = Union[
	Literal["follow"],
	Literal["error"],
	Literal["manual"],
	None
]

Referrer = Union[str, None]
ReferrerPolicy = Union[
	Literal["no-referrer"], 
	Literal["no-referrer-when-downgrade"], 
	Literal["same-origin"], 
	Literal["origin"], 
	Literal["strict-origin"], 
	Literal["origin-when-cross-origin"],
	Literal["strict-origin-when-cross-origin"],
	Literal["unsafe-url"],
	None
]

Integrity = Union[str, None]
KeepAlive = Union[bool, None]