# import flask dependencies
from flask import Flask, request  # makes the thing ngrokable
import json  # make me interact with json

# import the response functionality
from response_func import image_response, chip_response, text_response

# import the database functions
from sb_db_request import test_sb_db, get_event_names_w_access

# import library to send rich responses from webhook
from dialogflow_fulfillment import WebhookClient

# console should say 200 and the chatbot should send a message
test_sb_db()

# initialize the flask app
app = Flask(__name__)


@app.route('/')
def index():
    """
  default route, has text so I can see when the app is running
    :return: Hello World
    """
    return 'Hello World! This is the running Webhook for Sommerblut.'


BEDARF = [0, 0, 0, 0, 0, 0]


def handle_intent(intent_name, agent: WebhookClient, req_json) -> None:
    """
    Handle the webhook request.
this is the main intent switch function. All intents that use the backend must be routed here.
    :param intent_name:
    :param req_json: the raw format from DF
    :return: None
    """
    # build a request object
    req = request.get_json(force=True)
    # fetch action from json
    action = req.get('queryResult').get('action')
    # fetch param from json
    parameters = req.get('queryResult').get('parameters')
    session_name = req.get('sessionInfo').get('session')

    if intent_name == 'test.fulfillment':
        #return {'fulfillmentText': 'Webhook : Der Webhook funktioniert.'}
        #return chip_response(chips = ['Der','Webhook','funktioniert'])
        return image_response(url = 'https://github.com/arontaupe/KommunikationsKrake/blob/262cd82afae5fac968fa1d535a87d53cd99b9048/backend/sources/fa/a.png?raw=true')
        #return text_response('Hallo')

    elif intent_name == 'accessibility.select - collect':
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
        return chip_response(text = 'Webhook : Okay, ich habe deinen Bedarf ' + bedarf +
                                 ' abgespeichert.'' Willst du weitere Bedarfe angeben?'
                                 '(Was der Webhook weiss: ' + str(BEDARF),
                                 chips=["Ja", "Nein", "Menü"])

    elif intent_name == 'teach.fingeralhabet':
        fa_letter = parameters.get('FA-Zeichen')
        if fa_letter:
            folder = 'https://github.com/arontaupe/KommunikationsKrake/blob/262cd82afae5fac968fa1d535a87d53cd99b9048/backend/sources/fa/'
            return image_response(url = str(folder) + str(fa_letter) + '.png?raw=true', chips = ['Noch ein Buchstabe','Menü'])

    elif intent_name == 'test.webhook.image':
        return image_response(url = 'https://github.com/arontaupe/KommunikationsKrake/blob/262cd82afae5fac968fa1d535a87d53cd99b9048/backend/sources/fa/a.png?raw=true')


# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def update():
    """
Main listener to DF, will call handle_intent upon being activated
    :return: the response to DF
    """
    if request.method == 'POST':
        answer = request.data.decode("utf8")
        answer = json.loads(answer)
        print("====================================== REQUEST.DATA ======================================")
        # print(request.data)
        response = handle_intent(answer['queryResult']['intent']['displayName'], answer)

        if response:
            print("responding: ", response)
        return response
    else:
        return "Incorrect request format (/)"


# run the app 
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

print("botserver started")
