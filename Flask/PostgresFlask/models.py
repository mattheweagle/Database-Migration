from app import postgres

class Business(postgres.Model):
	__tablename__ = 'Businesses'

	_id = postgres.Column(postgres.String(), primary_key=True)
	city = postgres.Column(postgres.String())
	review_count = postgres.Column(postgres.Integer())
	business_name = postgres.Column(postgres.String())
	business_id = postgres.Column(postgres.String())
	longitude = postgres.Column(postgres.Numeric())
	hours = postgres.Column(postgres.JSON())
	business_state = postgres.Column(postgres.String())
	postal_code = postgres.Column(postgres.String())
	stars = postgres.Column(postgres.Numeric())
	address = postgres.Column(postgres.String())
	latitude = postgres.Column(postgres.Numeric())
	is_open = postgres.Column(postgres.Boolean())
	business_attributes = postgres.Column(postgres.JSON())
	categories = postgres.Column(postgres.String())
	deleted = postgres.Column(postgres.Boolean())

	def __init__(self, _id, city, review_count, business_name, business_id, longitude, hours, business_state, postal_code, stars, address, latitude, is_open, business_attributes, categories, deleted):
		self._id = _id
		self.city = city
		self.review_count = review_count
		self.business_name = business_name
		self.business_id = business_id
		self.longitude = longitude
		self.hours = hours
		self.business_state = business_state
		self.postal_code = postal_code
		self.stars = stars
		self.address = address
		self.latitude = latitude
		self.is_open = is_open
		self.business_attributes = business_attributes
		self.categories = categories
		self.deleted = deleted

	def __repr__(self):
		return '<_id {}>'.format(self._id)

	def serialize(self):
		return {
			'_id': self._id,
			'business_name': self.business_name,
			'stars': self.stars,
			'business_attributes':self.business_attributes
		}

class Checkin(postgres.Model):
	__tablename__ = 'Checkins'

	_id = postgres.Column(postgres.String(), primary_key=True)
	date = postgres.Column(postgres.String())
	business_id = postgres.Column(postgres.String())

	def __init__(self, _id, date, business_id):
		self._id = _id
		self.date = date
		self.business_id = business_id


	def __repr__(self):
		return '<_id {}>'.format(self._id)

	def serialize(self):
		return {
			'_id': self._id,
		}

class Review(postgres.Model):
	__tablename__ = 'Reviews'

	_id = postgres.Column(postgres.String(), primary_key=True)
	funny = postgres.Column(postgres.Integer())
	useful = postgres.Column(postgres.Integer())
	review_id = postgres.Column(postgres.String())
	text = postgres.Column(postgres.String())
	business_id = postgres.Column(postgres.String())
	stars = postgres.Column(postgres.Integer())
	date = postgres.Column(postgres.String())
	user_id = postgres.Column(postgres.String())
	cool = postgres.Column(postgres.Integer())
	deleted = postgres.Column(postgres.Boolean())

	def __init__(self, _id, funny, useful, review_id, text, business_id, stars, date, user_id, cool, deleted):
		self._id = _id
		self.funny = funny
		self.useful = useful
		self.review_id = review_id
		self.text = text
		self.business_id = business_id
		self.stars = stars
		self.date = date
		self.user_id = user_id
		self.cool = cool
		self.deleted = deleted

	def __repr__(self):
		return '<_id {}>'.format(self._id)

	def serialize(self):
		return {
			'_id': self._id,
		}

class Tip(postgres.Model):
	__tablename__ = 'Tips'

	_id = postgres.Column(postgres.String(), primary_key=True)
	user_id = postgres.Column(postgres.String())
	text = postgres.Column(postgres.String())
	business_id = postgres.Column(postgres.String())
	compliment_count = postgres.Column(postgres.Integer())
	date = postgres.Column(postgres.String())
	deleted = postgres.Column(postgres.Boolean())

	def __init__(self, _id, user_id, text, business_id, compliment_count, date, deleted):
		self._id = _id
		self.user_id = user_id
		self.text = text
		self.business_id = business_id
		self.compliment_count = compliment_count
		self.date = date
		self.deleted = deleted

	def __repr__(self):
		return '<_id {}>'.format(self._id)

	def serialize(self):
		return {
			'_id': self._id,
		}

class User(postgres.Model):
	__tablename__ = 'Users'

	_id = postgres.Column(postgres.String(), primary_key=True)
	yelping_since = postgres.Column(postgres.String())
	useful = postgres.Column(postgres.Integer())
	compliment_photos = postgres.Column(postgres.Integer())
	compliment_list = postgres.Column(postgres.Integer())
	compliment_funny = postgres.Column(postgres.Integer())
	funny = postgres.Column(postgres.Integer())
	review_count = postgres.Column(postgres.Integer())
	elite = postgres.Column(postgres.String())
	fans = postgres.Column(postgres.Integer())
	compliment_note = postgres.Column(postgres.Integer())
	compliment_plain = postgres.Column(postgres.Integer())
	compliment_writer = postgres.Column(postgres.Integer())
	compliment_cute = postgres.Column(postgres.Integer())
	average_stars = postgres.Column(postgres.Numeric())
	user_id = postgres.Column(postgres.String())
	compliment_more = postgres.Column(postgres.Integer())
	friends = postgres.Column(postgres.String())
	compliment_hot = postgres.Column(postgres.Integer())
	cool = postgres.Column(postgres.Integer())
	name = postgres.Column(postgres.String())
	compliment_profile = postgres.Column(postgres.Integer())
	compliment_cool = postgres.Column(postgres.Integer())
	deleted = postgres.Column(postgres.Boolean())

	def __init__(self, _id, yelping_since, useful, compliment_photos,compliment_list, compliment_funny, funny, review_count, elite, fans, compliment_note,compliment_plain,compliment_writer,compliment_cute,average_stars,user_id,compliment_more,friends,compliment_hot,cool,name,compliment_profile,compliment_cool,deleted):
		self._id = _id
		self.yelping_since = yelping_since
		self.useful = useful
		self.compliment_photos = compliment_photos
		self.compliment_list = compliment_list
		self.compliment_funny = compliment_funny
		self.funny = funny
		self.review_count = review_count
		self.elite = elite
		self.fans = fans
		self.compliment_note = compliment_note
		self.compliment_plain = compliment_plain
		self.compliment_writer = compliment_writer
		self.compliment_cute = compliment_cute
		self.average_stars = average_stars
		self.user_id = user_id
		self.compliment_more = compliment_more
		self.friends = friends
		self.compliment_hot = compliment_hot
		self.cool = cool
		self.name = name
		self.compliment_profile = compliment_profile
		self.compliment_cool = compliment_cool
		self.deleted = deleted

	def __repr__(self):
		return '<_id {}>'.format(self._id)

	def serialize(self):
		return {
			'_id': self._id,
		}
