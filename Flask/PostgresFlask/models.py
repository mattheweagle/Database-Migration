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

	def __init__(self, _id, city, review_count, business_name, business_id, longitude, hours, business_state, postal_code, stars, address, latitude, is_open, business_attributes, categories):
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

	def __repr__(self):
		return '<_id {}>'.format(self._id)
    
	def serialize(self):
		return {
			'_id': self._id, 
			'business_name': self.business_name,
			'stars': self.stars,
			'business_attributes':self.business_attributes
		}	
