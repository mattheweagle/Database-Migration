from flask_restful import Resource
from databases.postgres import postgres
from flask import jsonify, request
from models import Review
import json

class GetReview(Resource):
	#get a single review
	def get(self,review_id):
		review = Review.query.filter_by(review_id=review_id,deleted=False).first()

		if(review):
			result = {
				  "_id": review._id,
				  "business_id": review.business_id,
				  "cool": review.cool,
				  "date": review.date,
				  "deleted": review.deleted,
				  "funny": review.funny,
				  "review_id": review.review_id,
				  "stars": review.stars,
				  "text": review.text,
				  "useful": review.useful,
				  "user_id": review.user_id
			}
			return result
		return "Review not found"

class AddReview(Resource):
	#add a review from JSON data
	def post(self):
		request_text = request.get_json(force=True)
		review_json = json.loads(json.dumps(request_text))

		if('review_id' in review_json and 'funny' in review_json and 'useful' in review_json and 'text' in review_json
			and 'business_id' in review_json and 'stars' in review_json and 'date' in review_json
			and 'user_id' in review_json and 'cool' in review_json and 'deleted' in review_json):
			new_review = Review(
				_id = review_json['_id'],
				business_id = review_json['business_id'],
				cool = review_json['cool'],
				deleted = review_json['deleted'],
				date = review_json['date'],
				funny = review_json['funny'],
				review_id = review_json['review_id'],
				stars = review_json['stars'],
				text = review_json['text'],
				useful = review_json['useful'],
				user_id = review_json['user_id']
			)
			postgres.session.add(new_review)
			postgres.session.commit()
			return "Success"
		return "Invalid fields"

class UpdateReview(Resource):
	#update a review
	def put(self,review_id):
		request_text = request.get_json(force=True)
		review_json = json.loads(json.dumps(request_text))

		if('review_id' in review_json and 'funny' in review_json and 'useful' in review_json and 'text' in review_json
			and 'business_id' in review_json and 'stars' in review_json and 'date' in review_json
			and 'user_id' in review_json and 'cool' in review_json and 'deleted' in review_json):
			review = Review.query.filter_by(review_id=review_id,deleted=False).first()

			if(review):
				review._id = review_json['_id']
				review.business_id = review_json['business_id']
				review.cool = review_json['cool']
				review.deleted = review_json['deleted']
				review.date = review_json['date']
				review.funny = review_json['funny']
				review.review_id = review_json['review_id']
				review.stars = review_json['stars']
				review.text = review_json['text']
				review.useful = review_json['useful']
				review.user_id = review_json['user_id']

				postgres.session.add(review)
				postgres.session.commit()
				return "Success"
			return "Review not found"
		return "Update failed"

class DeleteReview(Resource):
	#set deleted tag to true for a review
	def delete(self,review_id):
		review = Review.query.filter_by(review_id=review_id,deleted=False).first()

		if(review):
			review.deleted = True
			postgres.session.add(review)
			postgres.session.commit()
			return "Successfully deleted"
		return "Review not found"

class BusinessReviews(Resource):
	#get all reviews for a certain business
	def get(self, business_id):
		reviews = Review.query.filter_by(business_id=business_id,deleted=False).all()
		if(len(reviews) > 0):
			results = [
				{
					  "_id": review._id,
					  "business_id": review.business_id,
					  "cool": review.cool,
					  "date": review.date,
					  "deleted": review.deleted,
					  "funny": review.funny,
					  "review_id": review.review_id,
					  "stars": review.stars,
					  "text": review.text,
					  "useful": review.useful,
					  "user_id": review.user_id
				} for review in reviews]
			return results
		return "No reviews found for business"

class BusinessReviewsAbove(Resource):
	#get all reviews rated higher than certain number of stars for a business
	def get(self, business_id, numStars):
		reviews = Review.query.filter_by(business_id=business_id,deleted=False).all()
		if(len(reviews) > 0):
			results = [
				{
					  "_id": review._id,
					  "business_id": review.business_id,
					  "cool": review.cool,
					  "date": review.date,
					  "deleted": review.deleted,
					  "funny": review.funny,
					  "review_id": review.review_id,
					  "stars": review.stars,
					  "text": review.text,
					  "useful": review.useful,
					  "user_id": review.user_id
				} for review in reviews if review.stars >= numStars]
			return results
		return "No reviews found for business"
