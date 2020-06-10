from flask_restful import Resource
from databases.mongo import mongo
from flask import jsonify, request
import json
import datetime

class GetCheckin(Resource):
    #get list of checkins for a business
    def get(self,business_id):
        checkins = mongo.db.checkins
        checkin = checkins.find_one({'business_id': business_id})

        if(checkin):
            checkin['_id'] = str(checkin['_id'])
            return jsonify(checkin)
        return "Business not found"

class AddCheckin(Resource):
    #add a checkin time to a business
    def put(self,business_id,time):
        checkins = mongo.db.checkins
        checkin = checkins.find_one({'business_id': business_id})

        if(checkin):
            dateString = checkin['date'] + ', ' + time
            checkins.update_one({'business_id': business_id},{'$set' : {'date' : dateString}})
            return "Success"
        return "Business not found"
