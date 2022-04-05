import sys

print("botserver started")

# import flask dependencies
from flask import Flask, request, make_response, jsonify
from copy import deepcopy
from sample_jsons import SAMPLE_PAYLOAD_JSON, SAMPLE_RESPONSE_JSON, SAMPLE_IMAGE_JSON, SAMPLE_LIST_JSON, \
    SAMPLE_LISTITEM_JSON_SHORT
import json

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

BEDARF = [0,0,0,0,0,0,0,0,0]

# this is the main intent switch function. All intents that use the backend must be routed here.
def handle_intent(intent_name, req_json):
    # build a request object
    req = request.get_json(force=True)
    # fetch action from json
    action = req.get('queryResult').get('action')
    # fetch param from json
    parameters = req.get('queryResult').get('parameters')

    if intent_name == 'fulfillment.test':
        return {'fulfillmentText': 'Webhook : Der Webhook funktioniert.'};
    elif intent_name == 'bedarf.select - collect':
        bedarf = parameters.get('bedarf')
        if bedarf:
            if bedarf == 'kein':
                BEDARF[0] = 1
            elif bedarf == 'leichte Sprache':
                BEDARF[1] = 1
            elif bedarf == 'blind':
                BEDARF[2] = 1
            elif bedarf == 'gehörlos':
                BEDARF[3] = 1
            elif bedarf == 'eingeschränkte Mobilität':
                BEDARF[4] = 1
            elif bedarf == 'Rollstuhl':
                BEDARF[5] = 1
            elif bedarf == 'Untertitel':
                BEDARF[6] = 1
            elif bedarf == 'Sehschwäche':
                BEDARF[7] = 1
            elif bedarf == 'Hörschwäche':
                BEDARF[8] = 1
        return standard_response('Webhook : Okay, ich habe deinen Bedarf ' + bedarf +
                                   ' abgespeichert.'' Willst du weitere Bedarfe angeben?'
                '(Was der Webhook weiss: ' + str(BEDARF),
                                 suggestions= ["Ja", "Nein", "Menü"])









# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')

    # return a fulfillment response
    return {'fulfillmentText': 'This is a response from the webhook.'}

@app.route('/webhook', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        update = request.data.decode("utf8")
        update = json.loads(update)
        print("====================================== REQUEST.DATA ======================================")
        #print(request.data)
        response = handle_intent(update['queryResult']['intent']['displayName'], update)
        # post_command('http://'+remote_addr, requestHeaders, response)
        if response:
            print("responding: ", response)
        return response
        # handle_update(update)
        return "" #"" = 200 responsee
    else:
        return "Incorrect request format (/)"

# create a route for webhook 
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return handle_intent()
    return make_response(jsonify(results()))


# run the app 
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
