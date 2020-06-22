from flask_restful import Resource
from databases.mongo import mongo
from flask import jsonify
import json
import datetime
from configparser import ConfigParser
parser = ConfigParser()
parser.read('/home/ec2-user/migration/MongoFlask/calls/config.ini')






pageSize = 1000

class BusinessMigration(Resource):
	def get(self,pageNum):
		businesses = mongo.db.businesses
		output = []
		startingBusinessSize = int(parser.get('sizes','businessSize'))
		if startingBusinessSize < (pageNum-1)*pageSize:
			return "End of collection reached", 400
		#within one page of reaching the end. different limit needed so entries that
		#have been added since migration aren't added again
		if startingBusinessSize > (pageNum-1)*pageSize and startingBusinessSize < (pageNum)*pageSize:
			remainingEntries = startingBusinessSize - ((pageNum - 1) * pageSize)
			for business in businesses.find().skip((pageNum - 1) * pageSize).limit(remainingEntries):
				business['_id'] = str(business['_id'])
				output.append(business)
		else:
			for business in businesses.find().skip((pageNum - 1) * pageSize).limit(pageSize):
				business['_id'] = str(business['_id'])
				output.append(business)
		return jsonify(output)

class CheckinMigration(Resource):
	def get(self,pageNum):
		checkins = mongo.db.checkins
		output = []
		startingCheckinSize = parser.get('sizes','checkinSize')
		if checkins.count() < (pageNum-1)*pageSize:
			return "End of collection reached", 400
		if startingCheckinSize > (pageNum-1)*pageSize and startingCheckinSize < (pageNum)*pageSize:
			remainingEntries = startingCheckinSize - ((pageNum - 1) * pageSize)
			for business in businesses.find().skip((pageNum - 1) * pageSize).limit(remainingEntries):
				business['_id'] = str(business['_id'])
				output.append(business)
		else:
			for checkin in checkins.find().skip((pageNum - 1) * pageSize).limit(pageSize):
				checkin['_id'] = str(checkin['_id'])
				output.append(checkin)
		return jsonify(output)

class ReviewMigration(Resource):
	def get(self,pageNum):
		reviews = mongo.db.reviews
		output = []
		startingReviewSize = parser.get('sizes','reviewSize')
		if reviews.count() < (pageNum-1)*pageSize:
			return "End of collection reached", 400
		if startingReviewSize > (pageNum-1)*pageSize and startingReviewSize < (pageNum)*pageSize:
			remainingEntries = startingReviewSize - ((pageNum - 1) * pageSize)
			for business in businesses.find().skip((pageNum - 1) * pageSize).limit(remainingEntries):
				business['_id'] = str(business['_id'])
				output.append(business)
		else:
			for review in reviews.find().skip((pageNum - 1) * pageSize).limit(pageSize):
				review['_id'] = str(review['_id'])
				output.append(review)
		return jsonify(output)

class TipMigration(Resource):
	def get(self,pageNum):
		tips = mongo.db.tips
		output = []
		startingTipSize = parser.get('sizes','tipSize')
		if tips.count() < (pageNum-1)*pageSize:
			return "End of collection reached", 400
		if startingTipSize > (pageNum-1)*pageSize and startingTipSize < (pageNum)*pageSize:
			remainingEntries = startingTipSize - ((pageNum - 1) * pageSize)
			for business in businesses.find().skip((pageNum - 1) * pageSize).limit(remainingEntries):
				business['_id'] = str(business['_id'])
				output.append(business)
		else:
			for tip in tips.find().skip((pageNum - 1) * pageSize).limit(pageSize):
				tip['_id'] = str(tip['_id'])
				output.append(tip)
		return jsonify(output)

class UserMigration(Resource):
	def get(self,pageNum):
		users = mongo.db.users
		output = []
		startingUserSize = parser.get('sizes','userSize')
		if users.count() < (pageNum-1)*pageSize:
			return "End of collection reached", 400
		if startingUserSize > (pageNum-1)*pageSize and startingUserSize < (pageNum)*pageSize:
			remainingEntries = startingUserSize - ((pageNum - 1) * pageSize)
			for business in businesses.find().skip((pageNum - 1) * pageSize).limit(remainingEntries):
				business['_id'] = str(business['_id'])
				output.append(business)
		else:
			for user in users.find().skip((pageNum - 1) * pageSize).limit(pageSize):
				user['_id'] = str(user['_id'])
				output.append(user)
		return jsonify(output)

class addDeletedTags(Resource):
	def post(self):
		tips = mongo.db.tips
		businesses = mongo.db.businesses
		users = mongo.db.users
		reviews = mongo.db.reviews
		tips.update_many(
		    {},
            {'$set' : {  'deleted' : False}}
		)
		businesses.update_many(
		    {},
            {'$set' : {  'deleted' : False}}
		)
		users.update_many(
		    {},
            {'$set' : {  'deleted' : False}}
		)
		reviews.update_many(
		    {},
            {'$set' : {  'deleted' : False}}
		)
		return {}

class UpdateConfig(Resource):
	def post(self):
		businesses = mongo.db.businesses
		tips = mongo.db.tips
		users = mongo.db.users
		reviews = mongo.db.reviews
		checkins = mongo.db.checkins
		parser.set('sizes','businessSize',str(businesses.count()))
		parser.set('sizes','tipSize',str(tips.count()))
		parser.set('sizes','userSize',str(users.count()))
		parser.set('sizes','reviewSize',str(reviews.count()))
		parser.set('sizes','checkinSize',str(checkins.count()))
		with open('/home/ec2-user/migration/MongoFlask/calls/config.ini','w+') as configFile:
			parser.write(configFile)
		return {}
