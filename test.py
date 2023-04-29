from fetch import fetch
from fetch.autocomplete import *

def main():
	fetch(
		"https://google.com",
		{
			method: GET,
			headers: {
				ContentType: "application/json"
			},
			body: {
				"hello": "world",
				"obj": {
					'x': 15,
					"list": ['a', 'b', 'c']
				}
			},
		}
	) \
	.then(
		lambda res: print(res.body),
		lambda err: print(f"An error occurred: {type(err).__name__}: {err}")
	)

if __name__ == "__main__":
	main()