from flask_restful import Resource
from databases.postgres import postgres
from flask import jsonify, request
from models import Checkin
import json
import datetime

class GetCheckin(Resource):
    #get list of checkins for a business
    def get(self,business_id):
        checkin = Checkin.query.filter_by(business_id=business_id).first()

        if(checkin):
            result = {
                "_id": checkin._id,
                "business_id": checkin.business_id,
                "date": checkin.date
            }
            return result
        return "Business not found"

class AddCheckin(Resource):
    #add a checkin time to a business
    def put(self,business_id,time):
        checkin = Checkin.query.filter_by(business_id=business_id).first()

        if(checkin):
            checkin.date = checkin.date + ', ' + time
            postgres.session.add(checkin)
            postgres.session.commit()
            return "Success"
        return "Business not found"
