#!/bin/bash

# GET query requests

curl -v -G -d "user_ip=1.2.3.4" -u yomna:auditlogger http://localhost:8000/log/

sleep 5

curl -v -G -d "resource=file.txt" -d "outcome=unauthorized" -u yomna:auditlogger http://localhost:8000/log/

