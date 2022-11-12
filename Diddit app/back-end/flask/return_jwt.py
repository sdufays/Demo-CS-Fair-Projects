# flask imports
from flask import Flask, request, jsonify, make_response
import uuid  # for public id
from werkzeug.security import generate_password_hash, check_password_hash
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta
from functools import wraps


# creates Flask object
app = Flask(__name__)
# configuration
# # NEVER HARDCODE YOUR CONFIGURATION IN YOUR CODE
# # INSTEAD CREATE A .env FILE AND STORE IN IT
app.config['SECRET_KEY'] = 'your secret key'
# # database name
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# # creates SQLALCHEMY object
# db = SQLAlchemy(app)

queue = []
quid = 0 # queue id

dictionary = {
    "3330701211516000": {
        "ID": "3330701211516000",
        "Type": 1,
        "Class": "Biology",
        "Name": "HW - Atwoods Machine Lab",
        "Description Teacher": "Academic and College Advising College Knowledge Part 2, Colleg e Scholarships  Math best practices Vertical Teaming - Link: http://ahschool.schoology.com/event/6040886539/profile",
        "Description Student": "",
        "Due Date": "2022-10-13",
        "Due Time": "11:59pm",
        "Last Edit": "2022-10-09T19:23:59.000Z",
        "Marked Done": False
    },
    "3330701211516001": {
        "ID": "3330701211516001",
        "Type": 1,
        "Class": "Spanish",
        "Name": "HW - Spanish Assignment",
        "Description Teacher": "Haz la tarea.  Math best practices Vertical Teaming - Link: http://ahschool.schoology.com/event/6040886539/profile",
        "Description Student": "",
        "Due Date": "2022-10-15",
        "Due Time": "8:00am",
        "Last Edit": "2022-10-06T16:23:59.000Z",
        "Marked Done": False
    },
    "3330701211516002": {
        "ID": "3330701211516002",
        "Type": 1,
        "Class": "English",
        "Name": "Read Macbeth Chapter 1",
        "Description Teacher": "You will be reading this book over the course of two weeks  Math best practices Vertical Teaming - Link: http://ahschool.schoology.com/event/6040886539/profile",
        "Description Student": "",
        "Due Date": "2022-10-15",
        "Due Time": "8:00am",
        "Last Edit": "2022-10-06T16:23:59.000Z",
        "Marked Done": False
    },
    "3330701211516004": {
        "ID": "3330701211516002",
        "Type": 1,
        "Class": "History",
        "Name": "Watch History Video",
        "Description Teacher": "Be prepared for in-class discussion. - Link: http://ahschool.schoology.com/event/6040886539/profile",
        "Description Student": "",
        "Due Date": "2022-10-15",
        "Due Time": "11:59pm",
        "Last Edit": "2022-10-06T16:23:59.000Z",
        "Marked Done": True
    },
    "3330701211516003": {
        "ID": "3330701211516002",
        "Type": 1,
        "Class": "Computer Science Essentials",
        "Name": "Python Project #2",
        "Description Teacher": "We will be presenting in class. - Link: http://ahschool.schoology.com/event/6040886539/profile",
        "Description Student": "",
        "Due Date": "2022-10-15",
        "Due Time": "11:59pm",
        "Last Edit": "2022-10-06T16:23:59.000Z",
        "Marked Done": True
    }
}

id = 178738
public_id = "public_id"
name = "DidditUser"
email = "user@diddit.com"
password = "password"

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])

        except:
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        # return f(current_user, *args, **kwargs)

    return decorated


# User Database Route
# this route sends back list of users
# @app.route('/user', methods=['GET'])
# @token_required
# def get_all_users(current_user):
#     # querying the database
#     # for all the entries in it
#     users = User.query.all()
#     # converting the query objects
#     # to list of jsons
#     output = []
#     for user in users:
#         # appending the user data json
#         # to the response list
#         output.append({
#             'public_id': user.public_id,
#             'name': user.name,
#             'email': user.email
#         })
#
#     return jsonify({'users': output})


# route for logging user in
@app.route('/login', methods=['POST'])
def login():
    # creates dictionary of form data
    auth = request.form
    print(auth.get('email'))
    print(auth.get('password'))
    # if not auth or not auth.get('email') or not auth.get('password'):
    #     # returns 401 if any email or / and password is missing
    #     return make_response(
    #         'Could not verify',
    #         401,
    #         {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
    #     )
    # if check_password_hash(password, auth.get('password')):
    #     # generates the JWT Token
    if auth.get('email')=="admin@diddit.com" and auth.get('password')=="strongpassword":
        print("generating")
        token = jwt.encode({
            'public_id': public_id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
    else:
        print("Wrong answer")
        token = "null"
    # return make_response(jsonify({'token': token.decode('UTF-8')}), 201)
    return token
    # returns 403 if password is wrong



# signup route
# @app.route('/signup', methods=['POST'])
# def signup():
#     # creates a dictionary of the form data
#     data = request.form
#
#     # gets name, email and password
#     name, email = data.get('name'), data.get('email')
#     password = data.get('password')
#
#     # checking for existing user
#     user = User.query \
#         .filter_by(email=email) \
#         .first()
#     if not user:
#         # database ORM object
#         user = User(
#             public_id=str(uuid.uuid4()),
#             name=name,
#             email=email,
#             password=generate_password_hash(password)
#         )
#         # insert user
#         db.session.add(user)
#         db.session.commit()
#
#         return make_response('Successfully registered.', 201)
#     else:
#         # returns 202 if user already exists
#         return make_response('User already exists. Please Log in.', 202)
@app.route('/refresh', methods=['GET'])
def refresh():
    return jsonify(dictionary)

@app.route('/data', methods=['GET'])
def data():
    global quid
    queue.append(quid)
    print(queue)
    quid = quid + 1
    return str(quid-1) + " ==> at ==> " + datetime.now().__str__()

if __name__ == "__main__":
    # setting debug to True enables hot reload
    # and also provides a debugger shell
    # if you hit an error while running the server
    # app.run()
    app.run(host='0.0.0.0', debug=True)
