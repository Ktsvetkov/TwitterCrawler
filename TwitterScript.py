from GetTweetCount import getTweetCount
from pymongo import MongoClient
import os

env_var_DB_HOST = os.environ['OPENSHIFT_MONGODB_DB_HOST']
env_var_DB_PORT = os.environ['OPENSHIFT_MONGODB_DB_PORT']
env_var_DB_URL = os.environ['OPENSHIFT_MONGODB_DB_URL']
client = MongoClient(env_var_DB_URL)
#client = MongoClient('localhost', 27017)
db = client['Events-database']
eventbriteDB = db.eventbriteEvents
ticketmasterDB = db.ticketmasterEvents
yelpDB = db.yelpEvents

def main():
    #Check Eventbrite
    for event in eventbriteDB.find():
        print event["name"]
        event["twitterCount"] = getTweetCount(event["name"])
        eventbriteDB.update_one(
            {"_id":  event["_id"]},
            {
                "$set": {
                    "twitterCount": event["twitterCount"]
                }
            }
        )

    #Check Ticketmaster
    for event in ticketmasterDB.find():
        print event["name"]
        event["twitterCount"] = getTweetCount(event["name"])
        ticketmasterDB.update_one(
            {"_id": event["_id"]},
            {
                "$set": {
                    "twitterCount": event["twitterCount"]
                }
            }
        )


    #Check Yelp
    for business in yelpDB.find():
        print business["name"]
        business["twitterCount"] = getTweetCount(business["name"])
        yelpDB.update_one(
            {"_id": business["_id"]},
            {
                "$set": {
                    "twitterCount": business["twitterCount"]
                }
            }
        )



main()