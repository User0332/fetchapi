import inspect

method = "method"
headers = "headers"
body = "body"
mode = "mode"
credentials = "credentials"
cache = "cache"
redirect = "redirect"
referrer = "referrer"
referrerPolicy = "referrerPolicy"
integrity = "integrity"
keepalive = "keepalive"

def make_js_properties(*properties: str):
	_locals = inspect.getouterframes(
		inspect.currentframe()
	)[1].frame.f_locals
	
	for prop in properties:
		_locals[prop] = prop
