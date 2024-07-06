#!/usr/bin/env python3
'''Python function that inserts a new document in a collection.
'''


def insert_school(mongo_collection, **kwargs):
    '''Insert new document in a collection.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result._id
