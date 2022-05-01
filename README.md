# Audit Logger
## _Audit Logging Microservice_

Audit Logger serves client systems as an HTTP endpoint, and saves logs in a MongoDB. <br>
Audit Logger is fully coded in python without any frameworks.

Logs are saved as dictionaries consistining of two keys with dictionary values:
- <b>_http_request_:</b>
        <ul><ul>HTTP command </ul></ul>
        <ul><ul>Client address </ul></ul>
        <ul><ul>Query [for GET requests]</ul></ul>
- <b>_event_:</b> 
        <ul><ul>Event sent by client [for POST requests] </ul></ul> 

### Block Diagram
An abstract view of the system.
![image](https://user-images.githubusercontent.com/59218287/165890295-dbbfdde6-c87d-427e-b6ef-12cd267d6139.png) <br>
Clients can make HTTP requests to the system's API. The Handler handles these requests:
  - POST requests: 
    <ul><ul>Authenticate client request </ul></ul>
    <ul><ul>Call a logger instance to construct the log </ul></ul>
    <ul><ul>Send the constructed log to database </ul></ul>
    <ul><ul>Send response to client</ul></ul>
  - GET requests:
    <ul><ul>Authenticate client request </ul></ul>
    <ul><ul>Send query to database </ul></ul>
    <ul><ul>Call a logger instance to construct the log </ul></ul>
    <ul><ul>Send the constructed log to database </ul></ul>
    <ul><ul>Send response to client with results</ul></ul>
  
### Deployment
To deploy the microservice, run the following command on terminal:<br>
<b> sudo python3.8 <./run.py </b><br>
Now, the server should be running on your local host using port 8000.<br>
<img width="431" src="https://user-images.githubusercontent.com/59218287/166134702-1e0e8dc7-520a-4fe7-a965-7b279dfd5c2a.png"><br>
        
### Testing
Open another terminal to act as the client side.<br><br>
To test the POST requests, run the curl commands saved in post_requests.sh on terminal:<br>
<img width="431" src="https://user-images.githubusercontent.com/59218287/166139384-0116be14-3f14-4811-8ec1-36a97a2e856b.png"><br><br>

The server side after excuting the commands:<br>
<img width="431" src="https://user-images.githubusercontent.com/59218287/166139495-e058172b-67ba-48b9-a1fa-219891911c50.png"><br><br>       

To test the GET query requests, run the curl commands in get_requests.sh on terminal:<br>
<img width="431" src="https://user-images.githubusercontent.com/59218287/166139762-5dc80613-a5b4-4bb5-ba38-fa61f4e43794.png"><br>
<img width="431" src="https://user-images.githubusercontent.com/59218287/166139892-04d46f66-267a-4314-ad22-ae7c93e6a676.png"><br><br>         

To test the authentication:<br>
<img width="431" src="https://user-images.githubusercontent.com/59218287/166136702-e664819f-00ab-4604-a16a-d5ce3cea339e.png"><br>
  
        
### Database
As the service is write-intensive, and the events are open-ended. NoSQL offers the best solution to save the logs.<br>  
The object view in MongoDB:<br>
<img width="431" src="https://user-images.githubusercontent.com/59218287/166140012-a9f3c839-6804-4e45-97c4-6e3552fc8398.png"><br>   



### Enviroment
- Ubuntu 18.04.06 (VMware Workstation 16)
- Python 3.8
- MongoDB (pymongo)

### Possible Improvement
- Deploying on a remote host instead of the local host
- Containerizing the microservice as a docker container
- Upgrading from the basic HTTP authentication       
       
