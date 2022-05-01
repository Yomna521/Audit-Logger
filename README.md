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
<img width="431" alt="1" src="https://user-images.githubusercontent.com/59218287/166134702-1e0e8dc7-520a-4fe7-a965-7b279dfd5c2a.png">
        
### Testing
To test the microservice, open another terminal to act as the client side.<br>
To test the POST requests, run the curl commands saved in post_requests.sh on terminal:<br>
 <img width="450" alt="2" src="https://user-images.githubusercontent.com/59218287/166134784-f56c8083-8436-4103-8d19-2765e49f78d6.png"> <br>
The server side after excuting the commands:
        <img width="432" alt="3" src="https://user-images.githubusercontent.com/59218287/166134822-74fdd582-d08d-404a-9b8b-f3b67686ba0f.png"><br>
        
To test the GET query requests, run the get_request.sh script from the client on terminal:<br>
       <b> ./get_request.sh</b><br>
""""ADD THE RESULTS""""" 
        
        
To test the authentication:<br>
<b>$ curl -u yomna:wrongpassword http://localhost:8000/log/ </b><br>
        
        
### Database
As the service is write-intensive, and the events are open-ended. NoSQL offers the best solution to save the logs.<br>
After the requests logs are saved as follows:<br>
        
        
The object view:<br>
<img width="349" alt="aaaaa" src="https://user-images.githubusercontent.com/59218287/166134867-51e0b601-05f2-43c1-8b67-e9d798d653c4.png">
<img width="413" alt="idk" src="https://user-images.githubusercontent.com/59218287/166134870-14bf77b3-00ff-48e1-9205-55321c207a35.png">

### Enviroment
- Ubuntu 18.04.06 (VMware Workstation 16)
- Python 3.8
- MongoDB (pymongo)

### Possible Improvement
- Deploying on a remote host instead of the local host
- Containerizing the microservice as a docker container
- Upgrading from the basic HTTP authentication       
       
