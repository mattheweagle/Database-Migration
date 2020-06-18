from flask_restful import Resource
from databases.mongo import mongo
from flask import jsonify, request
import json

class GetUser(Resource):
    #get a single user
    def get(self,user_id):
        users = mongo.db.users

        user = users.find_one({'user_id': user_id, 'deleted':False})

        if(user):
            user['_id'] = str(user['_id'])
            return jsonify(user)
        return "User not found"

class AddUser(Resource):
    #add a user from JSON data
    def post(self):
        users = mongo.db.users
        request_text = request.get_json(force=True)
        user_json = json.loads(json.dumps(request_text))

        if('yelping_since' in user_json and 'useful' in user_json and 'compliment_photos' in user_json and 'compliment_list' in user_json
            and 'compliment_funny' in user_json and 'funny' in user_json and 'review_count' in user_json
            and 'elite' in user_json and 'fans' in user_json and 'compliment_note' in user_json and 'compliment_plain' in user_json and 'compliment_writer' in user_json
            and 'compliment_cute' in user_json and 'average_stars' in user_json and 'user_id' in user_json and 'compliment_more' in user_json
            and 'friends' in user_json and 'compliment_hot' in user_json and 'cool' in user_json and 'name' in user_json
            and 'compliment_profile' in user_json and 'compliment_cool' in user_json and 'deleted' in user_json):
            users.insert(user_json)
            return "Success"
        return "Invalid fields"

class UpdateUser(Resource):
    #update a user
    def put(self,user_id):
        users = mongo.db.users
        request_text = request.get_json(force=True)
        user_json = json.loads(json.dumps(request_text))

        user_json['user_id'] = user_id
        if('yelping_since' in user_json and 'useful' in user_json and 'compliment_photos' in user_json and 'compliment_list' in user_json
            and 'compliment_funny' in user_json and 'funny' in user_json and 'review_count' in user_json
            and 'elite' in user_json and 'fans' in user_json and 'compliment_note' in user_json and 'compliment_plain' in user_json and 'compliment_writer' in user_json
            and 'compliment_cute' in user_json and 'average_stars' in user_json and 'user_id' in user_json and 'compliment_more' in user_json
            and 'friends' in user_json and 'compliment_hot' in user_json and 'cool' in user_json and 'name' in user_json
            and 'compliment_profile' in user_json and 'compliment_cool' in user_json and 'deleted' in user_json):
            users.replace_one({'user_id': user_id}, user_json)
            return "Update Successful"
        return "Update failed"

class DeleteUser(Resource):
    #set deleted tag to true for a user
    def delete(self,user_id):
        users = mongo.db.users

        user = users.find_one({'user_id': user_id, 'deleted':False})
        if(user):
            users.update_one({'user_id': user_id},{'$set' : {'deleted' : True}})
            return "Successfully deleted"
        return "User not found"
