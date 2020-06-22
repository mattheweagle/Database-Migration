import requests
import json
import time

#migrate businesses
def MigrateBusinesses(pageNum):
	response = ''
	First = True
	while 1:
		if not First:
			with open ('migrationLog.txt', 'a') as migrationLog:
				migrationLog.write('business,' + str(pageNum) + '\n')
		First = False

		url = 'http://localhost:5000/migration/business/' + str((int(pageNum)+1))
		t0 = time.time()
		g = requests.get(url)
		t1 = time.time()
		if g.status_code == 200:
			print(t1 - t0)
			p = requests.post('http://localhost:80/migration/business',data=json.dumps(g.text))
			print(time.time() - t1)
			pageNum = pageNum + 1
		elif g.status_code == 400:
			break;
		else:
			return

	MigrateCheckins(0)

#migrate checkins
def MigrateCheckins(pageNum):
	response = ''
	First = True
	while 1:
		if not First:
			with open ('migrationLog.txt', 'a') as migrationLog:
				migrationLog.write('checkin,' + str(pageNum) + '\n')
		First = False

		url = 'http://localhost:5000/migration/checkin/' + str((int(pageNum)+1))
		t0 = time.time()
		g = requests.get(url)
		t1 = time.time()
		if g.status_code == 400:
			break;
		print(t1 - t0)
		p = requests.post('http://localhost:80/migration/checkin',data=json.dumps(g.text))
		print(time.time() - t1)
		pageNum = pageNum + 1
	MigrateReviews(0)

#migrate reviews
def MigrateReviews(pageNum):
	response = ''
	First = True
	while 1:
		if not First:
			with open ('migrationLog.txt', 'a') as migrationLog:
				migrationLog.write('review,' + str(pageNum) + '\n')
		First = False

		url = 'http://localhost:5000/migration/review/' + str((int(pageNum)+1))
		t0 = time.time()
		g = requests.get(url)
		t1 = time.time()
		if g.status_code == 400:
			break;
		print(t1 - t0)
		p = requests.post('http://localhost:80/migration/review',data=json.dumps(g.text))
		print(time.time() - t1)
		pageNum = pageNum + 1
	MigrateUsers(0)

#migrate users
def MigrateUsers(pageNum):
	response = ''
	First = True
	while 1:
		if not First:
			with open ('migrationLog.txt', 'a') as migrationLog:
				migrationLog.write('user,' + str(pageNum) + '\n')
		First = False

		url = 'http://localhost:5000/migration/user/' + str((int(pageNum)+1))
		t0 = time.time()
		g = requests.get(url)
		t1 = time.time()
		if g.status_code == 400:
			break;
		print(t1 - t0)
		p = requests.post('http://localhost:80/migration/user',data=json.dumps(g.text))
		print(time.time() - t1)
		pageNum = pageNum + 1
	MigrateTips(0)

#migrate tips
def MigrateTips(pageNum):
	response = ''
	First = True
	while 1:
		if not First:
			with open ('migrationLog.txt', 'a') as migrationLog:
				migrationLog.write('tip,' + str(pageNum) + '\n')
		First = False

		url = 'http://localhost:5000/migration/tip/' + str((int(pageNum)+1))
		t0 = time.time()
		g = requests.get(url)
		t1 = time.time()
		if g.status_code == 400:
			break;
		print(t1 - t0)
		p = requests.post('http://localhost:80/migration/tip',data=json.dumps(g.text))
		print(time.time() - t1)
		pageNum = pageNum + 1

with open ('migrationLog.txt', 'rw') as migrationLog:
	timeStart = time.time()
	#check the last line in the migration log to see what collection and page the script left off at
	#restart script from the correct page
	lastStep = []
	for line in migrationLog:
		line = line.strip()
		lastStep = line.split(',')

	lastStep[1] = int(lastStep[1])

	#start of script. update Mongo config file with how many documents are in each collection
	if lastStep[0] == 'business' and lastStep[1] == 0:
		requests.post('http://localhost:5000/migration/config')

	if lastStep[0] == 'business':
		MigrateBusinesses(lastStep[1])
	elif lastStep[0] == 'checkin':
		MigrateCheckins(lastStep[1])
	elif lastStep[0] == 'review':
		MigrateReviews(lastStep[1])
	elif lastStep[0] == 'tip':
		MigrateTips(lastStep[1])
	elif lastStep[0] == 'user':
		MigrateUsers(lastStep[1])
	print('Total migration time: ')
	print(time.time() - timeStart)
