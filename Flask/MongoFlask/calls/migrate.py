from flask_restful import Resource
from databases.mongo import mongo
from flask import jsonify
import json
import datetime

pageSize = 1000

class BusinessMigration(Resource):
	def get(self,pageNum):
		businesses = mongo.db.businesses
		output = []
		for business in businesses.find().skip((pageNum - 1) * pageSize).limit(pageSize):
			business['_id'] = str(business['_id'])
			output.append(business)
		return jsonify(output)

class CheckinMigration(Resource):
	def get(self,pageNum):
		checkins = mongo.db.checkins
		output = []
		for checkin in checkins.find().skip((pageNum - 1) * pageSize).limit(pageSize):
			checkin['_id'] = str(checkin['_id'])
			output.append(checkin)
		return jsonify(output)

class ReviewMigration(Resource):
	def get(self,pageNum):
		reviews = mongo.db.reviews
		output = []
		for review in reviews.find().skip((pageNum - 1) * pageSize).limit(pageSize):
			review['_id'] = str(review['_id'])
			output.append(review)
		return jsonify(output)

class TipMigration(Resource):
	def get(self,pageNum):
		tips = mongo.db.tips
		output = []
		for tip in tips.find().skip((pageNum - 1) * pageSize).limit(pageSize):
			tip['_id'] = str(tip['_id'])
			output.append(tip)
		return jsonify(output)

class UserMigration(Resource):
	def get(self,pageNum):
		users = mongo.db.users
		output = []
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
