import requests
import json
import time
import random, string
import datetime
letters = string.ascii_lowercase

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
	return json.dumps(newUser)

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
	return json.dumps(newReview)

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
	return json.dumps(newBusiness)

def generateTip():
	newTip = {
		"business_id": ''.join(random.choice(letters) for i in range(20)),
		"compliment_count": 0,
		"date": str(datetime.datetime.now().time()),
		"deleted": False,
		"text": ''.join(random.choice(letters) for i in range(100)),
		"user_id": ''.join(random.choice(letters) for i in range(20))
	}
	return json.dumps(newTip)

with open ('requestList.txt', 'w') as requestList:
	numBusinesses = 0
	numUsers = 0
	numTips = 0
	numReviews = 0
	for i in range(1000):
		#generate inserts based on size of respective tables
		randomNum = random.random()
		if randomNum < 0.6:
			numReviews = numReviews + 1
			json_entry = generateReview()
			requestList.write('/review/add, ' + json_entry + '\n')
		elif randomNum < 0.75:
			numUsers = numUsers + 1
			json_entry = generateUser()
			requestList.write('/user/add, ' + json_entry + '\n')
		elif randomNum < 0.90:
			numTips = numTips + 1
			json_entry = generateTip()
			requestList.write('/tip/add, ' + json_entry + '\n')
		else:
			numBusinesses = numBusinesses + 1
			json_entry = generateBusiness()
			requestList.write('/business/add, ' + json_entry + '\n')
			p = requests.post('http://localhost:80/business/add',data=json_entry)
			p = requests.post('http://localhost:5000/business/add',data=json_entry)
	print("new businesses: ", numBusinesses)
	print("new Reviews: ", numReviews)
	print("new Users: ", numUsers)
	print("new Tips: ", numTips)
