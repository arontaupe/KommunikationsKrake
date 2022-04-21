# import flask dependencies
import json  # make me interact with json

from flask import Flask, request  # makes the thing ngrokable

# import code generated from openapi
# import the response functionality
from response_func import image_response, chip_response, chip_w_context_response
# import the database functions
from sb_db_request import test_sb_db, get_accessibility_ids, get_event_names_w_access

# import library to send rich responses from webhook

# console should say 200 and the chatbot should send a message
test_sb_db()

# initialize the flask app
app = Flask(__name__)


@app.route('/')
def index():
    """
  default route, has text, so I can see when the app is running
    :return: Hello World
    """
    return 'Hello World! This is the running Webhook for Sommerblut.'


def retrieve_bedarf():
    # build a request object
    req = request.get_json(force=True)
    output_contexts = req.get('queryResult').get('outputContexts')
    num_contexts = len(output_contexts)

    for i in range(num_contexts):
        accessibilities = None
        if 'final_accessibility' in output_contexts[i]['name']:
            accessibilities = output_contexts[i]['parameters']['final_accessibility']
            print('Accessibilities: ' + accessibilities)
    return accessibilities


retrieve_bedarf()


def retrieve_interests():
    # build a request object
    req = request.get_json(force=True)
    output_contexts = req.get('queryResult').get('outputContexts')
    num_contexts = len(output_contexts)
    interest_1 = interest_2 = interest_3 = interest_4 = interest_5 = interest_6 = interest_7 = interest_8 = interest_9 = None

    for i in range(num_contexts):
        if 'interest_1' in output_contexts[i]['name']:
            interest_1 = output_contexts[i]['parameters']['interest_1']
        if 'interest_2' in output_contexts[i]['name']:
            interest_2 = output_contexts[i]['parameters']['interest_2']
        if 'interest_3' in output_contexts[i]['name']:
            interest_3 = output_contexts[i]['parameters']['interest_3']
        if 'interest_4' in output_contexts[i]['name']:
            interest_4 = output_contexts[i]['parameters']['interest_4']
        if 'interest_5' in output_contexts[i]['name']:
            interest_5 = output_contexts[i]['parameters']['interest_5']
        if 'interest_6' in output_contexts[i]['name']:
            interest_6 = output_contexts[i]['parameters']['interest_6']
        if 'interest_7' in output_contexts[i]['name']:
            interest_7 = output_contexts[i]['parameters']['interest_7']
        if 'interest_8' in output_contexts[i]['name']:
            interest_8 = output_contexts[i]['parameters']['interest_8']
        if 'interest_9' in output_contexts[i]['name']:
            interest_9 = output_contexts[i]['parameters']['interest_9']

    return [interest_1, interest_2, interest_3, interest_4, interest_5, interest_6, interest_7, interest_8, interest_9]


def handle_intent(intent_name, req_json):
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
    # print('Parameters: ' + str(parameters))
    output_contexts = req.get('queryResult').get('outputContexts')
    # print('Contexts: ' + str(output_contexts))
    num_contexts = len(output_contexts)
    # print(num_contexts)

    # session_name = req.get('sessionInfo').get('session')

    if intent_name == 'test.fulfillment':
        # return {'fulfillmentText': 'Webhook : Der Webhook funktioniert.'}
        return chip_response(chips=['Der', 'Webhook', 'funktioniert'])
        # return image_response(url = 'https://github.com/arontaupe/KommunikationsKrake/blob/262cd82afae5fac968fa1d535a87d53cd99b9048/backend/sources/fa/a.png?raw=true')
        # return text_response('Hallo')
        # return context_response(session_id='abc',context='mycontext',variable_name = 'variable1', variable= 'value1')

    elif intent_name == 'accessibility.select - collect':
        bedarf = parameters.get('bedarf')

        prev_selection_bedarf = None
        for i in range(num_contexts):
            if 'save_bedarf' in output_contexts[i]['name']:
                prev_selection_bedarf = output_contexts[i]['parameters']['prev_selection_bedarf']
                print(prev_selection_bedarf)

        # print('Old Bedarf: ' + str(prev_selection_bedarf))

        new_bedarf = [0, 0, 0, 0, 0, 0]
        if prev_selection_bedarf:
            new_bedarf = prev_selection_bedarf.split(",")
            # print('Stored on DF: ' + str(new_bedarf))
        if bedarf:
            if bedarf == 'kein Bedarf':
                new_bedarf[0] = 1
            elif bedarf == 'leichte Sprache':
                new_bedarf[1] = 1
            elif bedarf == 'Höreinschränkung':
                new_bedarf[2] = 1
            elif bedarf == 'Mobilitätseinschränkung':
                new_bedarf[3] = 1
            elif bedarf == 'Visuelle Einschränkung':
                new_bedarf[4] = 1
            elif bedarf == 'begrenzte Reize':
                new_bedarf[5] = 1

        return chip_w_context_response(session_id='fixedID',
                                       context='save_bedarf',
                                       variable_name='prev_selection_bedarf',
                                       variable=str(new_bedarf),
                                       text='Webhook : Okay, ich habe deinen Bedarf ' + bedarf +
                                            ' abgespeichert.'' Willst du weitere Bedarfe angeben?',
                                       chips=["Ja", "Nein, weiter: Interessenselektor", "Menü"])

    elif intent_name == 'script.interest.select.1':
        # here we are done with collecting the accessibility and have to store it for further use
        prev_selection_bedarf = None
        for i in range(num_contexts):
            if 'save_bedarf' in output_contexts[i]['name']:
                prev_selection_bedarf = output_contexts[i]['parameters']['prev_selection_bedarf']
                # print(prev_selection_bedarf)
        return chip_w_context_response(text='Ich finde menschliche Körper interessant.',
                                       chips=["Ja", "Nein", "Ist mir egal"],
                                       session_id='fixedID',
                                       context='final_accessibility',
                                       variable_name='final_accessibility',
                                       variable=prev_selection_bedarf)

    elif intent_name == 'script.interest.select.1 - egal' or \
            intent_name == 'script.interest.select.1 - ja' or \
            intent_name == 'script.interest.select.1 - nein':
        interest_1 = parameters.get('interest_1')
        return chip_w_context_response(text='Soso, ' + interest_1 + ' also.',
                                       chips=["Weiter: Frage 2", "Menü"],
                                       session_id='fixedID',
                                       context='interest_1',
                                       variable_name='interest_1',
                                       variable=interest_1)

    elif intent_name == 'script.interest.select.2':
        # here we are asking for interest_2
        return chip_response(text='Ich mag Biografien und Lebensgeschichten.',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             )

    elif intent_name == 'script.interest.select.2 - egal' or intent_name == 'script.interest.select.2 - ja' or intent_name == 'script.interest.select.2 - nein':
        interest_2 = parameters.get('interest_2')
        return chip_w_context_response(text=interest_2 + ', interessant.',
                                       chips=["Weiter: Frage 3", "Menü"],
                                       session_id='fixedID',
                                       context='interest_2',
                                       variable_name='interest_2',
                                       variable=interest_2)

    elif intent_name == 'script.interest.select.3':
        # here we are asking for interest_3
        return chip_response(text='Mich faszinieren Rituale',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             )

    elif intent_name == 'script.interest.select.3 - egal' or intent_name == 'script.interest.select.3 - ja' or intent_name == 'script.interest.select.3 - nein':
        interest_3 = parameters.get('interest_3')
        return chip_w_context_response(text='Rituale eher so: ' + interest_3,
                                       chips=["Weiter: Frage 4", "Menü"],
                                       session_id='fixedID',
                                       context='interest_3',
                                       variable_name='interest_3',
                                       variable=interest_3)

    elif intent_name == 'script.interest.select.4':
        # here we are asking for interest_4
        return chip_response(text='Poesie begeistert mich',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             )

    elif intent_name == 'script.interest.select.4 - egal' or intent_name == 'script.interest.select.4 - ja' or intent_name == 'script.interest.select.4 - nein':
        interest_4 = parameters.get('interest_4')
        return chip_w_context_response(text=interest_4 + '? Poesie steckt überall.',
                                       chips=["Weiter: Frage 5", "Menü"],
                                       session_id='fixedID',
                                       context='interest_4',
                                       variable_name='interest_4',
                                       variable=interest_4)

    elif intent_name == 'script.interest.select.5':
        # here we are asking for interest_5
        return chip_response(text='Ich verfolge aktuelles Zeitgeschehen und aktuelle Diskurse',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             )

    elif intent_name == 'script.interest.select.5 - egal' or intent_name == 'script.interest.select.5 - ja' or intent_name == 'script.interest.select.5 - nein':
        interest_5 = parameters.get('interest_5')
        return chip_w_context_response(text=interest_5 + ', also ich finde Aktuelles wichtig',
                                       chips=["Weiter: Frage 6", "Menü"],
                                       session_id='fixedID',
                                       context='interest_5',
                                       variable_name='interest_5',
                                       variable=interest_5)


    elif intent_name == 'script.interest.select.6':
        # here we are asking for interest_6
        return chip_response(text='Ich bin gerne Draußen unterwegs und mag Pflanzen.',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             )

    elif intent_name == 'script.interest.select.6 - egal' or intent_name == 'script.interest.select.6 - ja' or intent_name == 'script.interest.select.6 - nein':
        interest_6 = parameters.get('interest_6')
        return chip_w_context_response(text=interest_6 + ', Ich merke, dass das wichtig ist.',
                                       chips=["Weiter: Frage 7", "Menü"],
                                       session_id='fixedID',
                                       context='interest_6',
                                       variable_name='interest_6',
                                       variable=interest_6)

    elif intent_name == 'script.interest.select.7':
        # here we are asking for interest_7
        return chip_response(text='Ich lasse mich lieber berieseln als selber aktiv mitmachen zu müssen',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             )

    elif intent_name == 'script.interest.select.7 - egal' or intent_name == 'script.interest.select.7 - ja' or intent_name == 'script.interest.select.7 - nein':
        interest_7 = parameters.get('interest_7')
        return chip_w_context_response(text='Dass du ' + interest_7 + ' klickst, sag ich deiner Mutter!',
                                       chips=["Weiter: Frage 8", "Menü"],
                                       session_id='fixedID',
                                       context='interest_7',
                                       variable_name='interest_7',
                                       variable=interest_7)

    elif intent_name == 'script.interest.select.8':
        # here we are asking for interest_8
        return chip_response(text='Ich finde Utopien und Zukunftsvisionen interessant.',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             )

    elif intent_name == 'script.interest.select.8 - egal' or intent_name == 'script.interest.select.8 - ja' or intent_name == 'script.interest.select.8 - nein':
        interest_8 = parameters.get('interest_8')
        return chip_w_context_response(text='Ich habe mir gemerkt, dass du ' + interest_8 + ' geantwortet hast.',
                                       chips=["Weiter: Frage 9", "Menü"],
                                       session_id='fixedID',
                                       context='interest_8',
                                       variable_name='interest_8',
                                       variable=interest_8)

    elif intent_name == 'script.interest.select.9':
        # here we are asking for interest_9
        return chip_response(text='Ich möchte lieber etwas lustiges sehen, als nachdenklich gestimmt zu werden',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             )

    elif intent_name == 'script.interest.select.9 - egal' or intent_name == 'script.interest.select.9 - ja' or intent_name == 'script.interest.select.9 - nein':
        interest_9 = parameters.get('interest_9')
        return chip_w_context_response(text=None,
                                       chips=["Weiter: Zeitselektor", "Menü"],
                                       session_id='fixedID',
                                       context='interest_9',
                                       variable_name='interest_9',
                                       variable=interest_9)

    elif intent_name == 'teach.fingeralhabet':
        fa_letter = parameters.get('FA-Zeichen')
        if fa_letter:
            folder = 'https://github.com/arontaupe/KommunikationsKrake/blob/262cd82afae5fac968fa1d535a87d53cd99b9048/backend/sources/fa/'
            return image_response(url=str(folder) + str(fa_letter) + '.png?raw=true',
                                  chips=['Noch ein Buchstabe', 'Menü'])

    elif intent_name == 'test.webhook.image':
        return image_response(
            url='https://github.com/arontaupe/KommunikationsKrake/blob/262cd82afae5fac968fa1d535a87d53cd99b9048/backend/sources/fa/a.png?raw=true')

    elif intent_name == 'script.time.select':
        # here we are making the database call and see whether we need to filter further
        bedarf = retrieve_bedarf()
        # interests = retrieve_interests()
        accessibilities = get_accessibility_ids()
        codes = []
        if bedarf:
            if bedarf == [1, 0, 0, 0, 0, 0] or bedarf == [0, 0, 0, 0, 0, 0]:
                codes = None
            else:
                # if bedarf[0] == 1: # kein Bedarf
                #    events = get_event_names_w_access()
                if bedarf[1] == 1:  # leichte Sprache
                    codes.append(accessibilities['Leichte Sprache'])
                if bedarf[2] == 1:  # Höreinschränkung
                    codes.append(accessibilities['Induktive Höranlage'])
                    codes.append(accessibilities['Audiodeskription'])
                    codes.append(accessibilities['Deutsche Gebärdensprache'])
                if bedarf[3] == 1:  # Mobilitätseinschränkung
                    codes.append(accessibilities['Rollstuhl'])
                    codes.append(accessibilities['Gehbehinderung'])
                if bedarf[4] == 1:  # Visuelle Einschränkung
                    codes.append(accessibilities['Touch-Tour'])
                    codes.append(accessibilities['Übertitel/Untertitel'])
                # if bedarf[5] == 1:  # begrenzte Reize
                # codes.append(accessibilities['Leichte Sprache'])
            print(codes)
            event_count, events = get_event_names_w_access(codes)
            print(event_count)

        return chip_w_context_response(text='Ich habe ' + event_count + ' Veranstaltungen gefunden',
                                       chips=["Zeig mir die Veranstaltungen"],
                                       session_id='fixedID',
                                       context='events_found',
                                       variable_name='events_found',
                                       variable=events
                                       )


# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def update():
    """
Main listener to DF, will call handle_intent upon being activated
    :return: the response to DF
    """
    if request.method == 'POST':
        update = request.data.decode("utf8")
        update = json.loads(update)
        print("====================================== REQUEST.DATA ======================================")
        # print(update)
        response = handle_intent(update['queryResult']['intent']['displayName'], update)

        if response:
            print("====================================== RESPONSE.DATA ======================================")
            print(response)

        return response
    else:
        return "Incorrect request format (/)"


# run the app 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

print("botserver started")