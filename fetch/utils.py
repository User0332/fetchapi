import json as __json_util

class _JSONGlobal:
	def stringify(self, obj: dict):
		return __json_util.dumps(obj)
	
	def parse(self, obj: str) -> dict:
			return __json_util.loads(obj)

JSON = _JSONGlobal()

del __json_util, _JSONGlobal

JSON