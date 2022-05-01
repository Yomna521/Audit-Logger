""""
    A MongoDB instance to save and query the audit logs
"""
import json

from pymongo import MongoClient
from service import logger


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
    print(record)
    return


# find all matches of the query in the collection
def findAll(query: dict, db=collection) -> list:
    results = []
    for result in db.find(query):
        results.append(result)
    return results
