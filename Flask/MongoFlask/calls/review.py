from flask_restful import Resource
from databases.mongo import mongo
from flask import jsonify, request
import json

class GetReview(Resource):
    #get a single review
    def get(self,review_id):
        reviews = mongo.db.reviews

        review = reviews.find_one({'review_id': review_id, 'deleted':False})

        if(review):
            review['_id'] = str(review['_id'])
            return jsonify(review)
        return "Review not found"

class AddReview(Resource):
    #add a review from JSON data
    def post(self):
        reviews = mongo.db.reviews
        request_text = request.get_json(force=True)
        review_json = json.loads(json.dumps(request_text))

        if('review_id' in review_json and 'funny' in review_json and 'useful' in review_json and 'text' in review_json
            and 'business_id' in review_json and 'stars' in review_json and 'date' in review_json
            and 'user_id' in review_json and 'cool' in review_json and 'deleted' in review_json):
            reviews.insert(review_json)
            return "Success"
        return "Invalid fields"

class UpdateReview(Resource):
    #update a review
    def put(self,review_id):
        reviews = mongo.db.reviews
        request_text = request.get_json(force=True)
        review_json = json.loads(json.dumps(request_text))

        if('review_id' in review_json and 'funny' in review_json and 'useful' in review_json and 'text' in review_json
            and 'business_id' in review_json and 'stars' in review_json and 'date' in review_json
            and 'user_id' in review_json and 'cool' in review_json and 'deleted' in review_json):
            reviews.replace_one({'review_id': review_id}, review_json)
            return "Update Successful"
        return "Update failed"

class DeleteReview(Resource):
    #set deleted tag to true for a review
    def delete(self,review_id):
        reviews = mongo.db.reviews

        review = reviews.find_one({'review_id': review_id, 'deleted':False})
        if(review):
            reviews.update_one({'review_id': review_id},{'$set' : {'deleted' : True}})
            return "Successfully deleted"
        return "Review not found"

class BusinessReviews(Resource):
    #get all reviews for a certain business
    def get(self, businessID):
        reviews = mongo.db.reviews
        output = []
        for r in reviews.find({'business_id': businessID, 'deleted':False}):
            r['_id'] = str(r['_id'])
            output.append(r)
        return jsonify(output)

class BusinessReviewsAbove(Resource):
	#get all reviews rated higher than certain number of stars for a business
    def get(self, businessID, numStars):
        reviews = mongo.db.reviews
        output = []
        for r in reviews.find({'business_id': businessID, 'deleted':False}):
            if r['stars'] >= numStars:
                r['_id'] = str(r['_id'])
                output.append(r)
        return jsonify(output)
