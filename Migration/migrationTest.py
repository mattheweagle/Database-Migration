#test updates and deletes consistent across databases
#test random sampling of entries
import random, string
import requests
import config

with open ('review_ids.csv', 'r') as review_ids, open ('user_ids.csv', 'r') as user_ids, open ('business_ids.csv', 'r') as business_ids, open ('requestUpdatesDeletes.txt', 'r') as requestList:
	mongoHost = config.mongo['HOST']
	postgresHost = config.postgres['HOST']


	for line in requestList:
		line = line.split(', ')
		mongoResponse = requests.get(mongoHost + line[2].strip() + '/' + line[1])
		postgresResponse = requests.get(postgresHost + line[2].strip() + '/' + line[1])
		#if mongoResponse.text != postgresResponse.text:
			#responseDifferences.write(randReview + ',' + mongoResponse.text + postgresResponse.text)
	reviewLines = review_ids.readlines()
	userLines = user_ids.readlines()
	businessLines = business_ids.readlines()

	responseDifferences = open('responseDifferences.txt','a')
	for i in range(10000):
		randReview = random.choice(reviewLines).strip().split(',')[1]
		mongoResponse = requests.get(mongoHost + '/business/' + '-000aQFeK6tqVLndf7xORg')
		postgresResponse = requests.get(postgresHost + '/business/' + '-000aQFeK6tqVLndf7xORg')
		if mongoResponse.text != postgresResponse.text:
			responseDifferences.write(randReview + ',' + mongoResponse.text + postgresResponse.text)
	responseDifferences.close()
