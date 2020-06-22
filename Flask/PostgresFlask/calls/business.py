from flask_restful import Resource
from databases.postgres import postgres
from flask import jsonify, request
from models import Business
import json
import datetime

class GetBusiness(Resource):
	#get a single business
	def get(self,business_id):
		business = Business.query.filter_by(business_id=business_id,deleted=False).first()

		if(business):
			result = {
				"address": business.address,
				"attributes": business.business_attributes,
				"business_id": business.business_id,
				"categories": business.categories,
				"city": business.city,
				"deleted": business.deleted,
				"hours": business.hours,
				"is_open": int(business.is_open),
				"latitude": float(business.latitude),
				"longitude": float(business.longitude),
				"name": business.business_name,
				"postal_code": business.postal_code,
				"review_count": business.review_count,
				"stars": float(business.stars),
				"state": business.business_state
			}
			return result
		return "Business not found"

class AddBusiness(Resource):
	#add a business from JSON data
	def post(self):
		request_text = request.get_json(force=True)
		business_json = json.loads(json.dumps(request_text))

		if('city' in business_json and 'review_count' in business_json and 'name' in business_json and 'business_id' in business_json
			and 'longitude' in business_json and 'hours' in business_json and 'state' in business_json
			and 'postal_code' in business_json and 'stars' in business_json and 'address' in business_json and 'latitude' in business_json
			and 'is_open' in business_json and 'attributes' in business_json and 'categories' in business_json and 'deleted' in business_json):
			new_business = Business(
				address = business_json['address'],
				business_attributes = business_json['attributes'],
				business_id = business_json['business_id'],
				categories = business_json['categories'],
				city = business_json['city'],
				deleted = business_json['deleted'],
				hours = business_json['hours'],
				is_open = business_json['is_open'],
				latitude = business_json['latitude'],
				longitude = business_json['longitude'],
				business_name = business_json['name'],
				postal_code = business_json['postal_code'],
				review_count = business_json['review_count'],
				stars = business_json['stars'],
				business_state = business_json['state']
			)
			postgres.session.add(new_business)
			postgres.session.commit()
			return "Success"
		return "Invalid fields"

class UpdateBusiness(Resource):
	#update a business
	def put(self,business_id):
		request_text = request.get_json(force=True)
		business_json = json.loads(json.dumps(request_text))

		if('city' in business_json and 'review_count' in business_json and 'name' in business_json and 'business_id' in business_json
			and 'longitude' in business_json and 'hours' in business_json and 'state' in business_json
			and 'postal_code' in business_json and 'stars' in business_json and 'address' in business_json and 'latitude' in business_json
			and 'is_open' in business_json and 'attributes' in business_json and 'categories' in business_json and 'deleted' in business_json):
			business = Business.query.filter_by(business_id=business_id,deleted=False).first()

			if(business):
				business.address = business_json['address']
				business.business_attributes = business_json['attributes']
				business.categories = business_json['categories']
				business.city = business_json['city']
				business.deleted = business_json['deleted']
				business.hours = business_json['hours']
				business.is_open = business_json['is_open']
				business.latitude = business_json['latitude']
				business.longitude = business_json['longitude']
				business.postal_code = business_json['postal_code']
				business.review_count = business_json['review_count']
				business.stars = business_json['stars']
				business.business_state = business_json['state']

				postgres.session.add(business)
				postgres.session.commit()
				return "Success"
			return "Business not found"
		return "Update failed"

class DeleteBusiness(Resource):
	#set deleted tag to true for a business
	def delete(self,business_id):
		business = Business.query.filter_by(business_id=business_id,deleted=False).first()

		if(business):
			business.deleted = True
			postgres.session.add(business)
			postgres.session.commit()
			return "Successfully deleted"
		return "Business not found"

class TopBusinessCity(Resource):
	#get the top rated business for a city
	def get(self, city):
		businesses = Business.query.filter_by(city=city,deleted=False).all()
		highestStars = 0
		if(len(businesses) > 0):
			bestBusiness = businesses[0]
			for business in businesses:
				if business.stars > highestStars:
					highestStars = business.stars
					bestBusiness = business

			result = {
				"address": bestBusiness.address,
				"attributes": bestBusiness.business_attributes,
				"business_id": bestBusiness.business_id,
				"categories": bestBusiness.categories,
				"city": bestBusiness.city,
				"deleted": bestBusiness.deleted,
				"hours": bestBusiness.hours,
				"is_open": bestBusiness.is_open,
				"latitude": float(bestBusiness.latitude),
				"longitude": float(bestBusiness.longitude),
				"name": bestBusiness.business_name,
				"postal_code": bestBusiness.postal_code,
				"review_count": bestBusiness.review_count,
				"stars": float(bestBusiness.stars),
				"state": bestBusiness.business_state
			}
			return result
		return "No businesses found for that city"
