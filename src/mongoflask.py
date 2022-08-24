from curses.ascii import isdigit
from datetime import date, datetime

import isodate as iso
from bson import ObjectId
from flask.json import JSONEncoder
from werkzeug.routing import BaseConverter
import re
try: 
    import urllib.parse as urlparse
except ImportError:
    from urlparse import urlparse as urlparse


class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return iso.datetime_isoformat(o)
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)


class ObjectIdConverter(BaseConverter):
    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return str(value)

def find_restaurants(mongo, field=None, search=None):
    query = {}
    if field:
        if type(search) == str: ##?## if search is not a string then we will assume it is an ObjectId()
            search = urlparse.unquote(search) ##?## Convert %20's into spaces
            if re.match('^[0-9.]+$',search): ##?## Check if search is just a number (float or int)
                if search.isdigit(): ##?## check if the search is just an int()
                    search = int(search)
                else:
                    search = float(search)
            else:
                search = re.compile(search+'.*', re.IGNORECASE)
        query[urlparse.unquote(field)] = search 
    result = mongo.db.restaurant.find(query)
    result_count = len(list(result.clone())) ##?## Check length of listed curser clone
    if result_count > 1: 
        return list(result)
    else:
        return next(result, {})