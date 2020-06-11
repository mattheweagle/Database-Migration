from flask_restful import Resource
from databases.postgres import postgres
from flask import jsonify, request
import json
from models import Business,Checkin,Review,Tip,User

class BusinessMigration(Resource):
    def post(self):
        r = request.get_json(force=True)
        businessBatch = r[10:len(r)-6].strip().replace("\n", "").split('},   {')
        for singleBusiness in businessBatch:
            json_data = json.loads('{' + singleBusiness + '}')
            try:
                business=Business(
                    city = json_data['city'],
                    review_count = json_data['review_count'],
                    business_name = json_data['name'],
                    business_id = json_data['business_id'],
                    longitude = json_data['longitude'],
                    hours = json_data['hours'],
                    business_state = json_data['state'],
                    postal_code = json_data['postal_code'],
                    stars = json_data['stars'],
                    address = json_data['address'],
                    latitude = json_data['latitude'],
                    is_open = json_data['is_open'],
                    business_attributes = json_data['attributes'],
                    categories = json_data['categories'],
                    deleted = json_data['deleted']
                )
            except Exception as e:
                return(str(e))
            postgres.session.add(business)
        postgres.session.commit()
        return {}

class CheckinMigration(Resource):
    def post(self):
        r = request.get_json(force=True)
        checkinBatch = r[10:len(r)-6].strip().replace("\n", "").split('},   {')
        for singleCheckin in checkinBatch:
            json_data = json.loads('{' + singleCheckin + '}')
            try:
                checkin=Checkin(
                    date = json_data['date'],
                    business_id = json_data['business_id']
                )
            except Exception as e:
                return(str(e))
            postgres.session.add(checkin)
        postgres.session.commit()
        return {}

class ReviewMigration(Resource):
    def post(self):
        r = request.get_json(force=True)
        reviewBatch = r[10:len(r)-6].strip().replace("\n", "").split('},   {')
        for singleReview in reviewBatch:
            json_data = json.loads('{' + singleReview + '}')
            try:
                review=Review(
                    funny = json_data['funny'],
                    useful = json_data['useful'],
                    review_id = json_data['review_id'],
                    text = json_data['text'],
                    business_id = json_data['business_id'],
                    stars = json_data['stars'],
                    date = json_data['date'],
                    user_id = json_data['user_id'],
                    cool = json_data['cool'],
                    deleted = json_data['deleted']

                )
            except Exception as e:
                return(str(e))
            postgres.session.add(review)
        postgres.session.commit()
        return {}

class TipMigration(Resource):
    def post(self):
        r = request.get_json(force=True)
        tipBatch = r[10:len(r)-6].strip().replace("\n", "").split('},   {')
        for singleTip in tipBatch:
            json_data = json.loads('{' + singleTip + '}')
            try:
                tip=Tip(
                    user_id = json_data['user_id'],
                    text = json_data['text'],
                    business_id = json_data['business_id'],
                    compliment_count = json_data['compliment_count'],
                    date = json_data['date'],
                    deleted = json_data['deleted']
                )
            except Exception as e:
                return(str(e))
            postgres.session.add(tip)
        postgres.session.commit()
        return {}

class UserMigration(Resource):
    def post(self):
        r = request.get_json(force=True)
        userBatch = r[10:len(r)-6].strip().replace("\n", "").split('},   {')
        for singleUser in userBatch:
            json_data = json.loads('{' + singleUser + '}')
            try:
                user=User(
                    yelping_since = json_data['yelping_since'],
                    useful = json_data['useful'],
                    compliment_photos = json_data['compliment_photos'],
                    compliment_list = json_data['compliment_list'],
                    compliment_funny = json_data['compliment_funny'],
                    funny = json_data['funny'],
                    review_count = json_data['review_count'],
                    elite = json_data['elite'],
                    fans = json_data['fans'],
                    compliment_note = json_data['compliment_note'],
                    compliment_plain = json_data['compliment_plain'],
                    compliment_writer = json_data['compliment_writer'],
                    compliment_cute = json_data['compliment_cute'],
                    average_stars = json_data['average_stars'],
                    user_id = json_data['user_id'],
                    compliment_more = json_data['compliment_more'],
                    friends = json_data['friends'],
                    compliment_hot = json_data['compliment_hot'],
                    cool = json_data['cool'],
                    name = json_data['name'],
                    compliment_profile = json_data['compliment_profile'],
                    compliment_cool = json_data['compliment_cool'],
                    deleted = json_data['deleted']
                )
            except Exception as e:
                return(str(e))
            postgres.session.add(user)
        postgres.session.commit()
        return {}
