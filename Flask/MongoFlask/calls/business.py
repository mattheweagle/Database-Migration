from flask_restful import Resource
from databases.mongo import mongo
from flask import jsonify, request
import json
import datetime

class GetBusiness(Resource):
    #get a single business
    def get(self,business_id):
        businesses = mongo.db.businesses
        business = businesses.find_one({'business_id': business_id, 'deleted':False})

        if(business):
            business['_id'] = str(business['_id'])
            return jsonify(business)
        return "Business not found"

class AddBusiness(Resource):
    #add a business from JSON data
    def post(self):
        businesses = mongo.db.businesses
        request_text = request.get_json(force=True)
        business_json = json.loads(json.dumps(request_text))

        if('city' in business_json and 'review_count' in business_json and 'name' in business_json and 'business_id' in business_json
            and 'longitude' in business_json and 'hours' in business_json and 'state' in business_json
            and 'postal_code' in business_json and 'stars' in business_json and 'address' in business_json and 'latitude' in business_json
            and 'is_open' in business_json and 'attributes' in business_json and 'categories' in business_json and 'deleted' in business_json):
            businesses.insert(business_json)
            return "Success"
        return "Invalid fields"

class UpdateBusiness(Resource):
    #update a business
    def put(self,business_id):
        businesses = mongo.db.businesses
        request_text = request.get_json(force=True)
        business_json = json.loads(json.dumps(request_text))

        if('city' in business_json and 'review_count' in business_json and 'name' in business_json and 'business_id' in business_json
            and 'longitude' in business_json and 'hours' in business_json and 'state' in business_json
            and 'postal_code' in business_json and 'stars' in business_json and 'address' in business_json and 'latitude' in business_json
            and 'is_open' in business_json and 'attributes' in business_json and 'categories' in business_json and 'deleted' in business_json):
            businesses.replace_one({'business_id': business_id}, business_json)
            return "Update Successful"
        return "Update failed"

class DeleteBusiness(Resource):
    #set deleted tag to true for a business
    def delete(self,business_id):
        businesses = mongo.db.businesses
        business = businesses.find_one({'business_id': business_id, 'deleted':False})

        if(business):
            businesses.update_one({'business_id': business_id},{'$set' : {'deleted' : True}})
            return "Successfully deleted"
        return "Business not found"

class TopBusinessCity(Resource):
    #get the top rated business for a city
    def get(self, city):
        Businesses = mongo.db.businesses
        output = {}
        highestStars = 0
        businessesCity = Businesses.find({'city': city, 'deleted':False})
        if(int(businessesCity.count()) > 0):
            for business in businessesCity:
                business['_id'] = str(business['_id'])
                if business['stars'] > highestStars:
                    highestStars = business['stars']
                    output = business
            return jsonify(output)
        return "No businesses found for that city"
