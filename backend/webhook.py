print("botserver started")

# import flask dependencies
from flask import Flask, request, make_response, jsonify # makes the thing ngrokable
import json # make me interact with json

# import the response functionality
from response_func import standard_response, image_response, img_resp

# import the database functions
from sb_db_request import test_sb_db, get_events_w_access

# import library to send rich responses from webhook
from dialogflow_fulfillment import WebhookClient

# console should say 200 and the chatbot should send a message
test_sb_db()

# TODO should get a list of all events with a determined accessibility id (0-9)
#get_events_w_access(1)

# initialize the flask app
app = Flask(__name__)

def handler(agent: WebhookClient) -> None:
    """Handle the webhook request."""

# default route 
@app.route('/')
def index():
    return 'Hello World! This is the running Webhook for Sommerblut.'

BEDARF = [0,0,0,0,0,0]

# this is the main intent switch function. All intents that use the backend must be routed here.
def handle_intent(intent_name, req_json):
    # build a request object
    req = request.get_json(force=True)
    # fetch action from json
    action = req.get('queryResult').get('action')
    # fetch param from json
    parameters = req.get('queryResult').get('parameters')

    if intent_name == 'test.fulfillment':
        return {'fulfillmentText': 'Webhook : Der Webhook funktioniert.'};

    elif intent_name == 'bedarf.select - collect':
        bedarf = parameters.get('bedarf')
        if bedarf:
            if bedarf == 'kein Bedarf':
                BEDARF[0] = 1
            elif bedarf == 'leichte Sprache':
                BEDARF[1] = 1
            elif bedarf == 'Höreinschränkung':
                BEDARF[2] = 1
            elif bedarf == 'Mobilitätseinschränkung':
                BEDARF[3] = 1
            elif bedarf == 'Visuelle Einschränkung':
                BEDARF[4] = 1
            elif bedarf == 'begrenzte Reize':
                BEDARF[5] = 1
        return standard_response('Webhook : Okay, ich habe deinen Bedarf ' + bedarf +
                                   ' abgespeichert.'' Willst du weitere Bedarfe angeben?'
                '(Was der Webhook weiss: ' + str(BEDARF),
                                 suggestions= ["Ja", "Nein", "Menü"])

    elif intent_name == 'teach.fingeralhabet':
        fa_letter = parameters.get('fa_letter')
        if fa_letter:
            folder = 'https://github.com/arontaupe/KommunikationsKrake/blob/262cd82afae5fac968fa1d535a87d53cd99b9048/backend/sources/fa/'
            return image_response(folder + fa_letter + '.png?raw=true')

    elif intent_name == 'test.webhook.image':
        return img_resp()


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
    #return make_response(jsonify(results()))


# run the app 
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
