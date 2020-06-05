from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_restful import Api
import config
from databases.mongo import mongo
#API Calls
from calls.review import SingleBusinessReviewsAbove, SingleBusinessReviews, AllReviews
from calls.business import AllBusinesses, TopBusinessCity
from calls.migrate import aggregationTest, pagingTest

app = Flask(__name__)
app.config["MONGO_URI"] = config.mongoConfig['URI']
app.config['MONGO_DBNAME'] = config.mongoConfig['DBNAME']

api = Api(app)
mongo.init_app(app)

print("MongoDB Database:",mongo.db)

#Define to show API docs
@app.route('/')
def index():
    return "Hello World"

#API CALLS
api.add_resource(AllReviews, '/review')
api.add_resource(SingleBusinessReviews, '/review/<string:businessID>')
api.add_resource(SingleBusinessReviewsAbove, '/review/<string:businessID>/<int:numStars>')

api.add_resource(AllBusinesses, '/business')
api.add_resource(TopBusinessCity, '/business/<string:city>')
api.add_resource(aggregationTest, '/aggregate')
api.add_resource(pagingTest, '/aggregate/<int:pageNum>')
