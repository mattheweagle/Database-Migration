from flask_restful import Resource
from databases.mongo import mongo
from flask import jsonify
import json
import datetime

class AllBusinesses(Resource):
    #get all reviews
    def get(self):
        Businesses = mongo.db.businesses
        output = []
        for b in Businesses.find():
            b['_id'] = str(b['_id'])
            output.append(b)
        return json.dumps(output)
		
class TopBusinessCity(Resource):
    #get all reviews for a certain business
    def get(self, city):
        Businesses = mongo.db.businesses
        output = []
        highestStars = 0
        for b in Businesses.find({'city': city}):
            b['_id'] = str(b['_id'])
            if b['stars'] > highestStars:
                highestStars = b['stars']
                output = [b]
        return json.dumps(output)
	
class aggregationTest(Resource):
	def post(self):
		tips = mongo.db.tips
		tips.update_many(
		    {},
            {'$set' : {  'TimeAdded' : datetime.datetime.now()}}
		)
		return {}
		
class pagingTest(Resource):
	def post(self,pageNum):
		tips = mongo.db.tips
		output = []
		for t in tips.find().skip((pageNum - 1) * 15).limit(15):
			t['_id'] = str(t['_id'])
			t['TimeAdded'] = str(t['TimeAdded'])
			output.append(t)
		return json.dumps(output)