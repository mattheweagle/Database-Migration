from flask_restful import Resource
from databases.postgres import postgres
from flask import jsonify, request
from models import Tip
import json
import datetime

class GetTips(Resource):
    #get list of tips for a business
    def get(self, business_id):
        tips = Tip.query.filter_by(business_id=business_id,deleted=False).all()
        results = [
            {
                "_id": tip._id,
                "business_id": tip.business_id,
                "compliment_count": tip.compliment_count,
                "date": tip.date,
                "deleted": tip.deleted,
                "text": tip.text,
                "user_id": tip.user_id
            } for tip in tips]
        return results
