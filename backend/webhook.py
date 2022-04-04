import sys

print("botserver started")

# import flask dependencies
from flask import Flask, request, make_response, jsonify
from copy import deepcopy
from sample_jsons import SAMPLE_PAYLOAD_JSON, SAMPLE_RESPONSE_JSON, SAMPLE_IMAGE_JSON, SAMPLE_LIST_JSON, \
    SAMPLE_LISTITEM_JSON_SHORT
import json

# initialize the flask app
app = Flask(__name__)


# default route 
@app.route('/')
def index():
    return 'Hello World! This is the running Webhook for Sommerblut.'


@app.route("/helloworld")
def hello():
    return """
        Hello World!<br /><br />
        <a href="/">Back to index</a>
    """


# this is the main intent switch function. All intents that use the backend must be routed here.
def handle_intent(intent_name, req_json):
    if intent_name == 'backend.test':
        return standard_response(req_json)
    # elif intent_name == 'session.login':
    #  return login(req_json)


def standard_response(text, suggestions=None):
    resp = deepcopy(SAMPLE_RESPONSE_JSON)
    resp['payload']['google']['richResponse']['items'][0]['simpleResponse']['textToSpeech'] = text
    if suggestions:
        resp['payload']['google']['richResponse']['suggestions'] = [{'title': i} for i in suggestions]
    return resp


def image_response(imgpath, textresponse='Here is your image', title='', accessibilitytext='', suggestions=None):
    resp = SAMPLE_IMAGE_JSON
    resp['payload']['google']['richResponse']['items'][1]['basicCard']['image']['url'] = imgpath
    if textresponse:
        resp['payload']['google']['richResponse']['items'][0]['simpleResponse']['textToSpeech'] = textresponse
    if title:
        resp['payload']['google']['richResponse']['items'][1]['basicCard']['title'] = title
    if accessibilitytext:
        resp['payload']['google']['richResponse']['items'][1]['basicCard']['accessibilityText'] = accessibilitytext
    if suggestions:
        resp['payload']['google']['richResponse']['suggestions'] = [{'title': i} for i in suggestions]
    return resp


# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')

    # return a fulfillment response
    return {'fulfillmentText': 'This is a response from webhook.'}


# create a route for webhook 
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))


# run the app 
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
