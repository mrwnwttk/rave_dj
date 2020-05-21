import sys
import json
import requests

if len(sys.argv) == 2:
	r = requests.get(sys.argv[1])
	r = r.text
	r = r.split("Env.dataStore = ")
	r = r[1].split(" // Raw JSON")
	r = r[0]
	j = json.loads(r)
	for i, j in j["content"][0]["urls"].items():
		print(f"{i}: {j}")
else:
	print("Usage: python3 rave_dj.py <URL>")
