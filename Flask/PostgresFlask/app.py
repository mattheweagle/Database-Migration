from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from databases.postgres import postgres
import config

#import API functions for routing
from calls.review import BusinessReviewsAbove, BusinessReviews, GetReview, AddReview, UpdateReview, DeleteReview
from calls.business import GetBusiness,AddBusiness,UpdateBusiness,TopBusinessCity, DeleteBusiness
from calls.user import GetUser,AddUser,UpdateUser,DeleteUser
from calls.checkin import GetCheckin, AddCheckin
from calls.tip import GetTips
from calls.migrate import BusinessMigration, CheckinMigration, ReviewMigration, TipMigration, UserMigration

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % config.POSTGRES

api = Api(app)
postgres.init_app(app)

#Define to show API docs
@app.route('/')
def index():
    return "Hello World"

#reviews
api.add_resource(GetReview, '/review/<string:review_id>')
api.add_resource(AddReview, '/review/add')
api.add_resource(UpdateReview, '/review/update/<string:review_id>')
api.add_resource(DeleteReview, '/review/delete/<string:review_id>')
api.add_resource(BusinessReviews, '/review/business/<string:business_id>')
api.add_resource(BusinessReviewsAbove, '/review/business/<string:business_id>/<int:numStars>')

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

#API CALLS
api.add_resource(BusinessMigration, '/migration/business')
api.add_resource(CheckinMigration, '/migration/checkin')
api.add_resource(ReviewMigration, '/migration/review')
api.add_resource(TipMigration, '/migration/tip')
api.add_resource(UserMigration, '/migration/user')
