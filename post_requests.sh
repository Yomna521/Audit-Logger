#!/bin/bash


# POST requests to log events

curl -v -X POST -u yomna:auditlogger -H 'Content-Type: application/json' -d '{"level":"DEBUG","user_ip":"1.2.3.4","user_name":"John Doe","event_type":"logging in","outcome":"successful"}'  http://localhost:8000/log/

sleep 5

curl -v -X POST -u yomna:auditlogger -H 'Content-Type: application/json' -d '{"level":"DEBUG","user_ip":"1.2.3.4","user_name":"John Doe","event_type":"created new customer account","new_user_name":"Jane Doe","outcome":"successful"}'  http://localhost:8000/log/

sleep 5 

curl -v -X POST -u yomna:auditlogger -H 'Content-Type: application/json' -d '{"level":"DEBUG","user_ip":"1.2.3.4","user_name":"John Doe","event_type":"deactivation","reason":"subscription fees are too expensive","outcome":"successful"}'  http://localhost:8000/log/

sleep 5

curl -v -X POST -u yomna:auditlogger -H 'Content-Type: application/json' -d '{"level":"DEBUG","user_ip":"1.2.3.4","user_name":"John Doe","event_type":"read","resource":"file.txt","outcome":"unauthorized"}'  http://localhost:8000/log/

sleep 5

curl -v -X POST -u yomna:auditlogger -H 'Content-Type: application/json' -d '{"level":"DEBUG","user_ip":"1.2.3.4","user_name":"John Doe","event_type":"billing","billing_amount":100,"outcome":"successful"}'  http://localhost:8000/log/


 
