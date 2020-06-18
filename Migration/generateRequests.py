import requests
import json
import time
import random, string
import datetime
from configparser import ConfigParser
letters = string.ascii_lowercase
parser = ConfigParser()

#generate random entries for both additions and updates
#for updates, the id is replaced with the id of the entry it is updating
#and the rest of the attributes are random
#this makes it easier to check if updates are actually being applied
def generateUser():
	newUser = {
		"average_stars": 0,
		"compliment_cool": 0,
		"compliment_cute": 0,
		"compliment_funny": 0,
		"compliment_hot": 0,
		"compliment_list": 0,
		"compliment_more": 0,
		"compliment_note": 0,
		"compliment_photos": 0,
		"compliment_plain": 0,
		"compliment_profile": 0,
		"compliment_writer": 0,
		"cool": 0,
		"deleted": False,
		"elite": "",
		"fans": 0,
		"friends": "",
		"funny": 0,
		"name": ''.join(random.choice(letters) for i in range(10)),
		"review_count": 0,
		"useful": 0,
		"user_id": ''.join(random.choice(letters) for i in range(20)),
		"yelping_since": str(datetime.datetime.now().time())
	}
	return json.dumps(newUser,separators=(',', ':'))

def generateReview():
	newReview = {
		  "business_id": ''.join(random.choice(letters) for i in range(20)),
		  "cool": 0,
		  "date": str(datetime.datetime.now().time()),
		  "deleted": False,
		  "funny": 0,
		  "review_id": ''.join(random.choice(letters) for i in range(20)),
		  "stars": random.randint(1,5),
		  "text": ''.join(random.choice(letters) for i in range(100)),
		  "useful": 0,
		  "user_id": ''.join(random.choice(letters) for i in range(20))
	}
	return json.dumps(newReview,separators=(',', ':'))

def generateBusiness():
	newBusiness = {
		"address": ''.join(random.choice(letters) for i in range(15)),
		"attributes": {},
		"business_id": ''.join(random.choice(letters) for i in range(20)),
		"categories": "",
		"city": ''.join(random.choice(letters) for i in range(10)),
		"deleted": False,
		"hours": None,
		"is_open": True,
		"latitude": float(random.random()),
		"longitude": float(random.random()),
		"name": ''.join(random.choice(letters) for i in range(10)),
		"postal_code": random.randint(10000,99999),
		"review_count": 0,
		"stars": float(0),
		"state": ''.join(random.choice(letters) for i in range(10))
	}
	return json.dumps(newBusiness,separators=(',', ':'))

def generateTip():
	newTip = {
		"business_id": ''.join(random.choice(letters) for i in range(20)),
		"compliment_count": 0,
		"date": str(datetime.datetime.now().time()),
		"deleted": False,
		"text": ''.join(random.choice(letters) for i in range(100)),
		"user_id": ''.join(random.choice(letters) for i in range(20))
	}
	return json.dumps(newTip,separators=(',', ':'))

with open ('requestAdds.txt', 'a') as requestAdds, open ('review_ids.csv', 'r') as review_ids, open ('user_ids.csv', 'r') as user_ids, open ('business_ids.csv', 'r') as business_ids:

	#keep track of how many additions to each collection for verification after migration
	numBusinessAdds = 0
	numUserAdds = 0
	numTipAdds = 0
	numReviewAdds = 0

	#load list of ids for random updates and deletions
	#loading into memory is faster, although a different solution would be needed
	#if there were 10x the number of ids
	reviewLines = review_ids.readlines()
	userLines = user_ids.readlines()
	businessLines = business_ids.readlines()


	for i in range(10000):
		requestUpdatesDeletes = open('requestUpdatesDeletes.txt', 'a')
		parser.read('/home/ec2-user/migration/Migration/config.ini')
		migrationComplete = parser.get('migration','complete')
		print(migrationComplete)

		#randomly choose to make a creation/read/update/deletion request
		randRequest = random.random()

		#creation
		if randRequest < 0.5:
			#generate inserts based on size of respective tables
			randInsert = random.random()

			#insert a review
			if randInsert < 0.7:
				numReviews = numReviews + 1
				json_entry = generateReview()
				requestAdds.write('/review/add, ' + json_entry + '\n')
				requests.post('http://localhost:80/review/add',data=json_entry)
				requests.post('http://localhost:5000/review/add',data=json_entry)

			#insert a user
			elif randInsert < 0.9:
				numUsers = numUsers + 1
				json_entry = generateUser()
				requestAdds.write('/user/add, ' + json_entry + '\n')
				requests.post('http://localhost:80/user/add',data=json_entry)
				requests.post('http://localhost:5000/user/add',data=json_entry)

			#insert a business
			else:
				numBusinesses = numBusinesses + 1
				json_entry = generateBusiness()
				requestAdds.write('/business/add, ' + json_entry + '\n')
				requests.post('http://localhost:80/business/add',data=json_entry)
				requests.post('http://localhost:5000/business/add',data=json_entry)

		#update
		elif randRequest < 0.7:
			#update from random table
			randUpdate = random.random()

			#update a review
			if randUpdate < 0.3:
				json_entry = generateReview()
				randReview = random.choice(reviewLines).strip().split(',')[1]
				updateLog = 'update, ' + randReview + ', /review/update/' + randReview + ', ' + json_entry + '\n'
				requestUpdatesDeletes.write(updateLog)
				requests.put('http://localhost:5000/review/update/' + randReview,data=json_entry)
				if migrationComplete == 'True':
					requests.put('http://localhost:80/review/update/' + randReview,data=json_entry)

			#update a user
			elif randUpdate < 0.7:
				json_entry = generateUser()
				randUser = random.choice(userLines).strip().split(',')[1]
				updateLog = 'update, ' + randUser + ', /user/update/' + randUser + ', ' + json_entry + '\n'
				requestUpdatesDeletes.write(updateLog)
				requests.put('http://localhost:5000/user/update/' + randUser,data=json_entry)
				if migrationComplete == 'True':
					requests.put('http://localhost:80/user/update/' + randUser,data=json_entry)

			#update a business
			else:
				json_entry = generateBusiness()
				randBusiness = random.choice(businessLines).strip()
				updateLog = 'update, ' + randBusiness + ', /business/update/' + randBusiness + ', ' + json_entry + '\n'
				requestUpdatesDeletes.write(updateLog)
				requests.put('http://localhost:5000/business/update/' + randBusiness,data=json_entry)
				if migrationComplete == 'True':
					requests.put('http://localhost:80/business/update/' + randBusiness,data=json_entry)
		#delete
		elif randRequest < 1:
			#delete from random table
			randDelete = random.random()

			#delete a review
			if randDelete < 0.3:
				randReview = random.choice(reviewLines).strip().split(',')[1]
				deleteLog = 'delete, ' + randReview + ', /review/delete/' + randReview + ', ' + '\n'
				requestUpdatesDeletes.write(deleteLog)
				requests.delete('http://localhost:5000/review/delete/' + randReview)
				if migrationComplete == 'True':
					requests.delete('http://localhost:80/review/delete/' + randReview)

			#delete a user
			elif randDelete < 0.7:
				randUser = random.choice(userLines).strip().split(',')[1]
				deleteLog = 'delete, ' + randUser + ', /user/delete/' + randUser + ', ' + '\n'
				requestUpdatesDeletes.write(deleteLog)
				requests.delete('http://localhost:5000/user/delete/' + randUser)
				if migrationComplete == 'True':
					requests.delete('http://localhost:80/user/delete/' + randUser)

			#delete a business
			else:
				randBusiness = random.choice(businessLines).strip()
				deleteLog = 'delete, ' + randBusiness + ', /business/delete/' + randBusiness + ', ' + '\n'
				requestUpdatesDeletes.write(deleteLog)
				requests.delete('http://localhost:5000/business/delete/' + randBusiness)
				if migrationComplete == 'True':
					requests.delete('http://localhost:80/business/delete/' + randBusiness)
		requestUpdatesDeletes.close()

	print("new businesses: ", numBusinessAdds)
	print("new Reviews: ", numReviewAdds)
	print("new Users: ", numUserAdds)
	print("new Tips: ", numTipAdds)
