from flask import Flask, request  # makes a flask app and serves it to a specified port
import os  # can grab environment variables
import threading
import time
from datetime import datetime
import json  # make me interact with json

from flask_httpauth import HTTPBasicAuth  # protects the rest api from being publicly available
from werkzeug.security import check_password_hash, generate_password_hash
# hashes the password, so it is not passed in clear

from sb_db_request import get_full_event_list
from webhook import handle_intent

# initialize the flask app
app = Flask(__name__)
# get variables from outside the container
user = os.environ.get('USER')
pw = os.environ.get('PASS')
# hash the password
users = {
    user: generate_password_hash(pw)
}
auth = HTTPBasicAuth()


def get_port():
    """
finds out if the environment has a predefined port, otherwise use 5002
    :return: port number
    """
    return int(os.environ.get("PORT", 5002))


@auth.verify_password
def verify_password(username, password):
    """
Checks if http user is in user list and checks for correctness of password
    :param username:
    :param password:
    :return: boolean verified or not
    """
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@app.route('/')
def index():
    """
  default route, has text, so I can see when the app is running, indicates the Last date of update
    :return: Hello World
    """
    return 'Hello World! \r\n' \
           'This is the running Webhook for Sommerblut. \r\n' \
           'For the API please append /webhook to the current url\r\n' \
           f'Last Modified: {datetime.fromtimestamp(os.stat("app.py").st_mtime)}'


# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
@auth.login_required
def update():
    """
Main listener to google-DF, will call handle_intent upon being activated.
Ignores anything that is not a POST-Request.
    :return: the response to google-DF
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
responsible for a multithreaded updating of the cache.
anything in here will be executed regularly in parallel to the main app
    """
    while 1:
        pre = time.perf_counter()
        get_full_event_list(entries=50)
        get_full_event_list(page=1, entries=10)
        get_full_event_list(page=2, entries=10)
        post = time.perf_counter()
        print(f'DB Refresh time: {post - pre:.5f}')
        time.sleep(180)


# run the app
if __name__ == '__main__':
    # start the thread that is keeping the cache updated
    x = threading.Thread(target=update_db_cache,
                         # daemon=True
                         )
    x.start()
    # execute and expose the backend as a flask app on a given port
    app.run(host='0.0.0.0', port=get_port(), debug=True)
    # only appears when app is stopped
    print("Backend stopped")
