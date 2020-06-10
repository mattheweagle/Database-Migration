from flask_restful import Resource
from databases.mongo import mongo
from flask import jsonify, request
import json
import datetime

class GetTips(Resource):
    #get list of tips for a business
    def get(self, business_id):
        tips = mongo.db.tips
        output = []
        for tip in tips.find({'business_id': business_id, 'deleted':False}, {'TimeAdded':False}):
            tip['_id'] = str(tip['_id'])
            output.append(tip)
        return jsonify(output)
