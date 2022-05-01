""""
    A MongoDB instance to save and query the audit logs
"""
import json

from pymongo import MongoClient


# Credentials
URL = "mongodb://yomna:auditlogger@logs-shard-00-00.5bidw.mongodb.net:27017,logs-shard-00-01.5bidw.mongodb.net:27017,logs-shard-00-02.5bidw.mongodb.net:27017/audit_logs?ssl=true&replicaSet=atlas-kcgm46-shard-0&authSource=admin&retryWrites=true&w=majority"
log_database = "logs"
audit_log_collection = "audit_logs"

# Establishing a connection
client = MongoClient(URL)
database = client["logs"]
collection = database["audit_logs"]


# save a log to collection
def save_log(log: json, db=collection):
    record = db.insert_one(log)
    return


# Assuming the client systems only have access to query over events
def findAll(query: dict, db=collection) -> list:
    # 'event.' is appended before the keys in the query dict to enable mongodb to query events (nested dictionaries)
    e = 'event.'
    corrected_query = {e+k : v for k, v in query.items()}
    # append results into a list
    results = []
    for result in db.find(corrected_query):
        results.append(result)
    return results
