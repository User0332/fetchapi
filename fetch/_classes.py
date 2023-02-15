from typing import Literal, Union, TypedDict

class Options(TypedDict):
	method: Union[
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

	headers: Union[dict[str, str], None]
	body: Union[dict, None]
	
	mode: Union[
		Literal["cors"],
		Literal["no-cors"],
		Literal["same-origin"],
		str,
		None
	]

	credentials: Union[
		Literal["omit"],
		Literal["same-origin"],
		Literal["include"],
		None
	]

	cache: Union[
		Literal["default"], 
		Literal["no-store"], 
		Literal["reload"], 
		Literal["no-cache"], 
		Literal["force-cache"], 
		Literal["only-if-cached"],
		None
	]

	redirect: Union[
		Literal["follow"],
		Literal["error"],
		Literal["manual"],
		None
	]

	referrrer: Union[str, None]

	referrerPolicy: Union[
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

	integrity: Union[str, None]
	keepalive: Union[bool, None]



