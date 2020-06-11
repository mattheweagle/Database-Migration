from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_restful import Api
from databases.mongo import mongo
import config

#import API functions for routing
from calls.review import BusinessReviewsAbove, BusinessReviews, GetReview, AddReview, UpdateReview, DeleteReview
from calls.business import GetBusiness,AddBusiness,UpdateBusiness,TopBusinessCity, DeleteBusiness
from calls.user import GetUser,AddUser,UpdateUser,DeleteUser
from calls.checkin import GetCheckin, AddCheckin
from calls.tip import GetTips
from calls.migrate import addDeletedTags, BusinessMigration, CheckinMigration, ReviewMigration, TipMigration, UserMigration, UpdateConfig

app = Flask(__name__)
app.config["MONGO_URI"] = config.mongoConfig['URI']
app.config['MONGO_DBNAME'] = config.mongoConfig['DBNAME']

api = Api(app)
mongo.init_app(app)

print("MongoDB Database:",mongo.db)

@app.route('/')
def index():
    return "Hello World"


#API CALLS

#reviews
api.add_resource(GetReview, '/review/<string:review_id>')
api.add_resource(AddReview, '/review')
api.add_resource(UpdateReview, '/review/update/<string:review_id>')
api.add_resource(DeleteReview, '/review/delete/<string:review_id>')
api.add_resource(BusinessReviews, '/review/business/<string:businessID>')
api.add_resource(BusinessReviewsAbove, '/review/business/<string:businessID>/<int:numStars>')

#businesses
api.add_resource(GetBusiness, '/business/<string:business_id>')
api.add_resource(AddBusiness, '/business/add')
api.add_resource(UpdateBusiness, '/business/update/<string:business_id>')
api.add_resource(DeleteBusiness, '/business/delete/<string:business_id>')
api.add_resource(TopBusinessCity, '/business/top/<string:city>')

#users
api.add_resource(GetUser, '/user/<string:user_id>')
api.add_resource(AddUser, '/user/add')
api.add_resource(UpdateUser, '/user/update/<string:user_id>')
api.add_resource(DeleteUser, '/user/delete/<string:user_id>')

#checkins
api.add_resource(GetCheckin, '/checkin/<string:business_id>')
api.add_resource(AddCheckin, '/checkin/add/<string:business_id>/<string:time>')

#tips
api.add_resource(GetTips, '/tip/<string:business_id>')

#migration APIs
api.add_resource(BusinessMigration, '/migration/business/<int:pageNum>')
api.add_resource(CheckinMigration, '/migration/checkin/<int:pageNum>')
api.add_resource(ReviewMigration, '/migration/review/<int:pageNum>')
api.add_resource(TipMigration, '/migration/tip/<int:pageNum>')
api.add_resource(UserMigration, '/migration/user/<int:pageNum>')
api.add_resource(UpdateConfig, '/migration/config')
