from flask import Flask, request  # makes a flask app and serves it to a specified port
import os  # can grab environment variables
import threading
import time
from datetime import datetime
import json  # make me interact with json

from flask_httpauth import HTTPBasicAuth  # protects the rest api from being publicly available
from werkzeug.security import check_password_hash, \
    generate_password_hash  # hashes the password, so it is not passed in clear

from sb_db_request import get_full_event_list
from webhook import handle_intent
import pprint

# initialize the flask app
app = Flask(__name__)

user = os.environ.get('USER')
pw = os.environ.get('PASS')

users = {
    user: generate_password_hash(pw)
}
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@app.route('/')
def index():
    """
  default route, has text, so I can see when the app is running
    :return: Hello World
    """
    return 'Hello World! This is the running Webhook for Sommerblut. ' \
           'For the API please append /webhook to the current url\r\n' \
           f'Last Modified: {datetime.fromtimestamp(os.stat("webhook.py").st_mtime)}'


# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
@auth.login_required
def update():
    """
Main listener to DF, will call handle_intent upon being activated
    :return: the response to DF
    """
    if request.method == 'POST':
        resp = request.data.decode("utf8")
        resp = json.loads(resp)
        # print("====================================== REQUEST.DATA ======================================")
        response = handle_intent(intent_name=resp['queryResult']['intent']['displayName'])
        return response
    else:
        return "Incorrect request format (/webhook) You are not deemed worthy of a response."


def update_db_cache():
    """
responsible for a multi-threaded updating of the cache.
anything in here will be executed regularly in parallel to the app
    """
    while 1:
        pre = time.perf_counter()
        get_full_event_list(entries=50)
        get_full_event_list(page=1, entries=10)
        get_full_event_list(page=2, entries=10)
        post = time.perf_counter()
        print(f'DB Refresh time: {post - pre:.5f}')
        time.sleep(30)


# run the app
if __name__ == '__main__':
    # start the thread that is keeping the cache updated
    x = threading.Thread(target=update_db_cache,
                         # daemon=True
                         )
    x.start()
    # execute and expose the backend as a flask app on a given port
    app.run(host='0.0.0.0', port=5002, debug=True)
    # only appears when app is stopped
    print("Backend restarting")
