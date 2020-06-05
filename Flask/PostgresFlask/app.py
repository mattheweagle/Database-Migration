from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from databases.postgres import postgres
import config

#API Calls
#from calls.review import SingleBusinessReviewsAbove, SingleBusinessReviews, AllReviews
#from calls.business import AllBusinesses, TopBusinessCity, aggregationTest, pagingTest
from calls.migrate import testInsert
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % config.POSTGRES

api = Api(app)
postgres.init_app(app)

#Define to show API docs
@app.route('/')
def index():
    return "Hello World"

#API CALLS
api.add_resource(testInsert, '/test')
#api.add_resource(AllReviews, '/review')
#api.add_resource(SingleBusinessReviews, '/review/<string:businessID>')
#api.add_resource(SingleBusinessReviewsAbove, '/review/<string:businessID>/<int:numStars>')

#api.add_resource(AllBusinesses, '/business')
#api.add_resource(TopBusinessCity, '/business/<string:city>')
#api.add_resource(aggregationTest, '/aggregate')
#api.add_resource(pagingTest, '/aggregate/<int:pageNum>')
