from flask import Flask
from flask import request
import json
import logging
from flask import jsonify
from time import strftime


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")
log = logging.getLogger("application")

app = Flask(__name__)

g_user = {
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "5d48a0a8e9f04aa38008",
    "externalId": "58342554-38d6-4ec8-948c-50044d0a33fd",
    "meta": {
        "resourceType": "User",
        "created": "2018-03-27T19:59:26.000Z",
        "lastModified": "2018-03-27T19:59:26.000Z"
    },
    "userName": "Test_User_feed3ace-693c-4e5a-82e2-694be1b39934",
    "name": {
        "formatted": "givenName familyName",
        "familyName": "familyName",
        "givenName": "givenName",
    },
    "active": True,
    "emails": [{
        "value": "Test_User_22370c1a-9012-42b2-bf64-86099c2a1c22@testuser.com",
        "type": "work",
        "primary": True
    }]
}



@app.route("/")
def hello():
    return "Hello World!"

@app.route("/Users/<user_id>", methods=['GET'])
def get_user_by_id(user_id):
    global g_user
    log.info("get user %s" % user_id)
    return jsonify(g_user)

@app.route("/Users", methods=['GET'])
def get_user():
    global g_user
    filter = request.args.get('filter')
    log.info("get user by filter %s" % filter)
    return jsonify(g_user)



@app.route("/Users/<user_id>", methods=['PUT'])
def put_user(user_id):
    log.info("put user %s" % user_id)
    jsonify(success=True)

@app.route("/Users", methods=['POST'])
def post_user():
    if not request.json:
        abort(400)

    log.info("post user %s" % request.json)
    jsonify(success=True)


@app.before_request
def log_request_info():
    log.debug('incoming request')
    log.debug('%s %s',request.method, request.url)
    # log.debug('Headers: %s', request.headers)
    # log.debug('Body: %s', request.get_data())

# @app.after_request
# def after_request(response):
#     timestamp = strftime('[%Y-%b-%d %H:%M]')
#     #log.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
#     log.debug(request.__dict__)
#     log.debug(response.__dict__)
#     return response


