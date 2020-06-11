from flask_restful import Resource
from databases.postgres import postgres
from flask import jsonify, request
from models import User
import json

class GetUser(Resource):
	#get a single user
	def get(self,user_id):
		user = User.query.filter_by(user_id=user_id,deleted=False).first()

		if(user):
			result = {
				"average_stars": float(user.average_stars),
				"compliment_cool": user.compliment_cool,
				"compliment_cute": user.compliment_cute,
				"compliment_funny": user.compliment_funny,
				"compliment_hot": user.compliment_hot,
				"compliment_list": user.compliment_list,
				"compliment_more": user.compliment_more,
				"compliment_note": user.compliment_note,
				"compliment_photos": user.compliment_photos,
				"compliment_plain": user.compliment_plain,
				"compliment_profile": user.compliment_profile,
				"compliment_writer": user.compliment_writer,
				"cool": user.cool,
				"deleted": user.deleted,
				"elite": user.elite,
				"fans": user.fans,
				"friends": user.friends,
				"funny": user.funny,
				"name": user.name,
				"review_count": user.review_count,
				"useful": user.useful,
				"user_id": user.user_id,
				"yelping_since": user.yelping_since
			}
			return result
		return "User not found"

class AddUser(Resource):
	#add a user from JSON data
	def post(self):
		request_text = request.get_json(force=True)
		user_json = json.loads(json.dumps(request_text))

		if('yelping_since' in user_json and 'useful' in user_json and 'compliment_photos' in user_json and 'compliment_list' in user_json
			and 'compliment_funny' in user_json and 'funny' in user_json and 'review_count' in user_json
			and 'elite' in user_json and 'fans' in user_json and 'compliment_note' in user_json and 'compliment_plain' in user_json and 'compliment_writer' in user_json
			and 'compliment_cute' in user_json and 'average_stars' in user_json and 'user_id' in user_json and 'compliment_more' in user_json
			and 'friends' in user_json and 'compliment_hot' in user_json and 'cool' in user_json and 'name' in user_json
			and 'compliment_profile' in user_json and 'compliment_cool' in user_json and 'deleted' in user_json):
			new_user = User(
				yelping_since = user_json['yelping_since'],
				useful = user_json['useful'],
				compliment_photos = user_json['compliment_photos'],
				compliment_list = user_json['compliment_list'],
				compliment_funny = user_json['compliment_funny'],
				funny = user_json['funny'],
				review_count = user_json['review_count'],
				elite = user_json['elite'],
				fans = user_json['fans'],
				compliment_note = user_json['compliment_note'],
				compliment_plain = user_json['compliment_plain'],
				compliment_writer = user_json['compliment_writer'],
				compliment_cute = user_json['compliment_cute'],
				average_stars = user_json['average_stars'],
				user_id = user_json['user_id'],
				compliment_more = user_json['compliment_more'],
				friends = user_json['friends'],
				compliment_hot = user_json['compliment_hot'],
				cool = user_json['cool'],
				name = user_json['name'],
				compliment_profile = user_json['compliment_profile'],
				compliment_cool = user_json['compliment_cool'],
				deleted = user_json['deleted']
			)
			postgres.session.add(new_user)
			postgres.session.commit()
			return "Success"
		return "Invalid fields"

class UpdateUser(Resource):
	#update a user
	def put(self,user_id):
		request_text = request.get_json(force=True)
		user_json = json.loads(json.dumps(request_text))

		if('yelping_since' in user_json and 'useful' in user_json and 'compliment_photos' in user_json and 'compliment_list' in user_json
			and 'compliment_funny' in user_json and 'funny' in user_json and 'review_count' in user_json
			and 'elite' in user_json and 'fans' in user_json and 'compliment_note' in user_json and 'compliment_plain' in user_json and 'compliment_writer' in user_json
			and 'compliment_cute' in user_json and 'average_stars' in user_json and 'user_id' in user_json and 'compliment_more' in user_json
			and 'friends' in user_json and 'compliment_hot' in user_json and 'cool' in user_json and 'name' in user_json
			and 'compliment_profile' in user_json and 'compliment_cool' in user_json and 'deleted' in user_json):
			user = User.query.filter_by(user_id=user_id,deleted=False).first()

			if(user):
				user.yelping_since = user_json['yelping_since']
				user.useful = user_json['useful']
				user.compliment_photos = user_json['compliment_photos']
				user.compliment_list = user_json['compliment_list']
				user.compliment_funny = user_json['compliment_funny']
				user.funny = user_json['funny']
				user.review_count = user_json['review_count']
				user.elite = user_json['elite']
				user.fans = user_json['fans']
				user.compliment_note = user_json['compliment_note']
				user.compliment_plain = user_json['compliment_plain']
				user.compliment_writer = user_json['compliment_writer']
				user.compliment_cute = user_json['compliment_cute']
				user.average_stars = user_json['average_stars']
				user.user_id = user_json['user_id']
				user.compliment_more = user_json['compliment_more']
				user.friends = user_json['friends']
				user.compliment_hot = user_json['compliment_hot']
				user.cool = user_json['cool']
				user.name = user_json['name']
				user.compliment_profile = user_json['compliment_profile']
				user.compliment_cool = user_json['compliment_cool']
				user.deleted = user_json['deleted']

				postgres.session.add(user)
				postgres.session.commit()
				return "Success"
			return "User not found"
		return "Update failed"

class DeleteUser(Resource):
	#set deleted tag to true for a user
	def delete(self,user_id):
		user = User.query.filter_by(user_id=user_id,deleted=False).first()

		if(user):
			user.deleted = True
			postgres.session.add(user)
			postgres.session.commit()
			return "Successfully deleted"
		return "User not found"
