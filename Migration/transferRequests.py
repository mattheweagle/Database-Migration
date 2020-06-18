import requests
import json
import time
import random, string
import datetime
from configparser import ConfigParser

parser = ConfigParser()
parser.read('/home/ec2-user/migration/Migration/config.ini')

#apply all updates and deletes to Postgres that have happened since migration started
#generateRequests opens and closes this file after every write to ensure the most
#up to date version is read here
with open ('requestUpdatesDeletes.txt', 'r') as requestList:
	for request in requestList:
		request = request.strip('\n').split(', ')
		url = 'http://localhost:80' + request[2]
		if request[0] == 'update':
			requests.put(url,data=request[3])
		elif request[0] == 'delete':
			requests.delete(url)

	#update proxy setting to now send updates and deletes to postgres
	#as well as Mongo once all requests are sent to postgres
	parser.set('migration','complete','True')
	with open('/home/ec2-user/migration/Migration/config.ini','w+') as configFile:
		parser.write(configFile)
