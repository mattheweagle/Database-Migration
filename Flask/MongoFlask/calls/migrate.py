from flask_restful import Resource
from databases.mongo import mongo
from flask import jsonify
import json
import datetime
		
class pagingTest(Resource):
	def get(self,pageNum):
		businesses = mongo.db.businesses
		output = []
		for b in businesses.find().skip((pageNum - 1) * 10000).limit(10000):
			b['_id'] = str(b['_id'])
			output.append(b)
		return jsonify(output)
		
class aggregationTest(Resource):
	def post(self):
		tips = mongo.db.tips
		tips.update_many(
		    {},
            {'$set' : {  'Deleted' : False}}
		)
		return {}