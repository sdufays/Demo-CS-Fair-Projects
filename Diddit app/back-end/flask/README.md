Requirements for running the mock Flask service return_jwt.py are as follows:

Server side packages:
- Flask (Flask, request, jsonify, make_response)
- uuid
- werkzeug.security (generate_password_hash, check_password_hash)
- jwt
- datetime (datetime, timedelta)
- functools (wraps)

UI Client Side:
The client side of the mock connection will use HTTP POST to send fake form data containing a username and password
to the service, which will return a JSON Web Token (JWT) to be used for future authentication. 
The terminal command to send this form is as follows:

Login Credentials:
$ curl -X POST -H "Content-type: multipart/form-data"  -F "email=admin@diddit.com" -F "password=strongpassword" "localhost:5000/login"

Wrong answer:
$ curl -X POST -H "Content-type: multipart/form-data"  -F "email=user@diddit.com" -F "password=password" "localhost:5000/login"

The terminal command to send a GET Request and pull the sample calendar data is as follows:

$ curl localhost:5000/refresh

* localhost may need to be changed to the IP address of the device running the service, in this case 127.0.0.1
