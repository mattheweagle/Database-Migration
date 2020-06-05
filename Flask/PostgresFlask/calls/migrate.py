from flask_restful import Resource
from databases.postgres import postgres
from flask import jsonify, request
import json
from models import Business

class testInsert(Resource):
	def post(self):
		r = request.get_json(force=True)
		businessBatch = r[10:len(r)-6].strip().replace("\n", "").split('},   {')
		for singleBusiness in businessBatch:
			json_data = json.loads('{' + singleBusiness + '}')
			try:
				business=Business(
					_id = json_data['_id'],
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
					categories = json_data['categories']
				)
			except Exception as e:
				return(str(e))
			postgres.session.add(business)
		postgres.session.commit()
		return json_data
