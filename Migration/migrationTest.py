import requests
import json
import time

for i in range(20):
	url = 'http://localhost:5000/aggregate/' + str((i+1))
	t0 = time.time()
	g = requests.get(url)
	t1 = time.time()
	print(t1 - t0)
	p = requests.post('http://localhost:80/test',data=g.text)
	print(time.time() - t1)
