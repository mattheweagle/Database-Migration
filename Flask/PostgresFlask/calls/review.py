from flask_restful import Resource
from databases.mongo import mongo
from flask import jsonify
import json

class AllReviews(Resource):
    #get all reviews
    def get(self):
        reviews = mongo.db.reviews
        output = []
        for r in reviews.find():
            r['_id'] = str(r['_id'])
            output.append(r)
        return json.dumps(output)
		
class SingleBusinessReviews(Resource):
    #get all reviews for a certain business
    def get(self, businessID):
        reviews = mongo.db.reviews
        output = []
        for r in reviews.find({'business_id': businessID}):
            r['_id'] = str(r['_id'])
            output.append(r)
        return json.dumps(output)
		
class SingleBusinessReviewsAbove(Resource):
	#get all reviews rated higher than certain number of stars
    def get(self, businessID, numStars):
        reviews = mongo.db.reviews
        output = []
        for r in reviews.find({'business_id': businessID}):
            if r['stars'] >= numStars:
                r['_id'] = str(r['_id'])
                output.append(r)
        return json.dumps(output)
