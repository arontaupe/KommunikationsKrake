# import flask dependencies
import json  # make me interact with json
from pprint import pprint

from flask import Flask, request  # makes the thing ngrokable

pprint('keep pprint')

# import code generated from openapi
# import the response functionality
from response_func import image_response, chip_response, chip_w_context_response, event_response, text_response
from retrieve_from_gdf import retrieve_bedarf, retrieve_found_events, retrieve_event_index, retrieve_event_id
# import the database functions
from sb_db_request import test_sb_db, get_accessibility_ids, get_full_event_list

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
    # action = req.get('queryResult').get('action')
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

        new_bedarf = [0, 0, 0, 0, 0, 0]
        if prev_selection_bedarf:
            new_bedarf = prev_selection_bedarf
            print('Stored on DF: ' + str(new_bedarf))
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
        print('Now Modified Bedarf: ' + str(new_bedarf))
        return chip_w_context_response(session_id='fixedID',
                                       context='save_bedarf',
                                       variable_name='prev_selection_bedarf',
                                       variable=new_bedarf,
                                       text='Okay, ich habe deinen Bedarf ' + bedarf +
                                            ' abgespeichert.'' Willst du weitere Bedarfe angeben?',
                                       chips=["Ja", "Nein, weiter: Interessenselektor", "Menü"])

    elif intent_name == 'script.interest.select.1':
        # here we are done with collecting the accessibility and have to store it for further use
        prev_selection_bedarf = None
        for i in range(num_contexts):
            if 'save_bedarf' in output_contexts[i]['name']:
                prev_selection_bedarf = output_contexts[i]['parameters']['prev_selection_bedarf']
                print('Saving final Accessibility: ' + str(prev_selection_bedarf))
                # print(prev_selection_bedarf)
        return chip_w_context_response(
            text='Hier kannst du nun 9 Aussagen bewerten und ich suche dir danach eine passende Veranstaltung heraus. \n'
                 'Du kannst sie immer mit Ja, Nein, oder Ist mir Egal bewerten. \n'
                 'Erste Frage: \n'
                 'Ich finde menschliche Körper interessant.',
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
        bedarf = retrieve_bedarf(output_contexts)
        if bedarf:
            print('Fetched Bedarf: ' + str(bedarf))
        # interests = retrieve_interests()
        accessibilities = get_accessibility_ids()
        codes = []
        if bedarf:
            if bedarf == [1.0, 0.0, 0.0, 0.0, 0.0, 0.0] or bedarf == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:
                codes = None
                print('No special accessibility need detected ')
            else:
                # if bedarf[0] == 1: # kein Bedarf
                #    events = get_event_names_w_access()
                if bedarf[1] == 1.0:  # leichte Sprache
                    codes.append(accessibilities['Leichte Sprache'])
                if bedarf[2] == 1.0:  # Höreinschränkung
                    codes.append(accessibilities['Induktive Höranlage'])
                    codes.append(accessibilities['Audiodeskription'])
                    codes.append(accessibilities['Deutsche Gebärdensprache'])
                if bedarf[3] == 1.0:  # Mobilitätseinschränkung
                    codes.append(accessibilities['Rollstuhl'])
                    codes.append(accessibilities['Gehbehinderung'])
                if bedarf[4] == 1.0:  # Visuelle Einschränkung
                    codes.append(accessibilities['Touch-Tour'])
                    codes.append(accessibilities['Übertitel/Untertitel'])
                # if bedarf[5] == 1.0:  # begrenzte Reize
                # codes.append(accessibilities['Leichte Sprache'])
            # print('Asking for Accessibilities: ' + str(codes))
            event_count, events = get_full_event_list(codes)
            # print(event_count)
        if events and event_count:
            text = ''
            if event_count > 5:
                text = 'Ich habe mehr als 5 (' + str(
                    event_count) + ') Veranstaltungen gefunden, möchtest du nach Veranstaltungsdatum filtern?'
                chips = ["Zeig mir die Veranstaltungen", 'Nach Datum filtern']
            else:
                text = 'Ich habe ' + str(event_count) + ' Veranstaltungen gefunden.'
                chips = ["Zeig mir die Veranstaltungen"]
            return chip_w_context_response(text=text,
                                           chips=chips,
                                           session_id='fixedID',
                                           context='events_found',
                                           variable_name='events_found',
                                           variable=events
                                           )
        else:
            return text_response(text='Ich habe leider keine Events mit deinen Zugänglichkeitsanforderungen gefunden')

    elif intent_name == 'script.event.menu':

        event_count, events = retrieve_found_events(output_contexts)
        # print(event_count, type(event_count))
        # pprint(events)
        if events is None:
            print('no events')
            return text_response(text='Ich habe leider keine Events gespeichert')

        event_index = int(retrieve_event_index(output_contexts))
        print(event_index, type(event_index))

        display_num = 1
        next_event_index = event_index
        print(event_index, next_event_index, event_count)

        if event_index == event_count:
            next_event_index = 0
            return chip_w_context_response(session_id='fixedID',
                                           context='event_index',
                                           variable_name='event_index',
                                           variable=next_event_index,
                                           text='Ich habe dir nun alle ausgewählten Events gezeigt. '
                                                'Was möchtest du nun tun?',
                                           chips=['Zurück: Hauptmenü', 'Zeig mir die Veranstaltungen noch einmal'])

        next_event_index = event_index + 1
        print(event_index, next_event_index, event_count)
        if event_index == 0:
            chips = ['Zeig mir das nächste Event', 'Mehr zur Veranstaltung']
        else:
            chips = ['Zeig mir das letzte Event', 'Zeig mir das nächste Event', 'Mehr zur Veranstaltung']

        return event_response(
            text='Ich empfehle dir die folgende Veranstaltung. '
                 'Ich kann dir dir mehr erzählen oder eine andere Veranstaltung vorschlagen',
            session_id='fixedID',
            context='event_index',
            variable_name='event_index',
            variable=next_event_index,
            display_num=display_num,
            display_index=event_index,
            event_count=event_count,
            events=events,
            chips=chips
        )

    elif intent_name == 'script.event.details':

        event_count, events = retrieve_found_events(output_contexts)
        if events is None or event_count is None:
            print('no events')
            return text_response(text='Ich habe leider keine Events gespeichert')

        event_index = next_event_index = int(retrieve_event_index(output_contexts))
        if next_event_index == event_count:
            event_index = event_count - 1
        else:
            event_index = next_event_index - 1

        event_id = events[event_index]['id']

        return chip_w_context_response(session_id='fixedID',
                                       text='Was möchtest du mehr wissen über die Veranstaltung?'
                                            '1. Ist die Veranstaltung barrierefrei?'
                                            '2. Worum geht es genau in der Veranstaltung'
                                            '3. Wie handhabt ihr Corona?'
                                            '4. Wo und Wann findet sie statt?',
                                       chips=['Barrierefreiheit', 'Programmtext', 'Coronamaßnahmen', 'Datum und Ort',
                                              'Zurück: Veranstaltungsübersicht'],
                                       variable_name='event_id',
                                       variable=event_id,
                                       context='event_id')

    elif intent_name == 'script.event.menu.previous':
        event_count, events = retrieve_found_events(output_contexts)
        if events is None:
            print('no events')
            return text_response(text='Ich habe leider keine Events gespeichert')

        next_event_index = event_index = int(retrieve_event_index(output_contexts))
        display_num = 1
        if event_count == 1:
            return chip_w_context_response(session_id='fixedID',
                                           context='event_index',
                                           variable_name='event_index',
                                           variable=next_event_index,
                                           text='Ich habe dir nun alle ausgewählten Events gezeigt. '
                                                'Was möchtest du nun tun?',
                                           chips=['Zurück: Hauptmenü', 'Zeig mir die Veranstaltungen noch einmal'])
        print(event_index, next_event_index, event_count)
        if event_index == 0:
            event_index = event_count - 2
            next_event_index = event_index + 1
        elif event_index == 1:
            event_index = event_count - 1
            next_event_index = event_index + 1
        else:
            event_index = event_index - 2
            next_event_index = event_index + 1

        print(event_index, next_event_index, event_count)
        if event_index == 0:
            chips = ['Zeig mir das nächste Event', 'Mehr zur Veranstaltung']
        else:
            chips = ['Zeig mir das letzte Event', 'Zeig mir das nächste Event', 'Mehr zur Veranstaltung']
        return event_response(
            text='Ich empfehle dir noch einmal die letzte Veranstaltung. '
                 'Ich kann dir dir mehr erzählen oder eine andere Veranstaltung vorschlagen',
            session_id='fixedID',
            context='event_index',
            variable_name='event_index',
            variable=next_event_index,
            display_num=display_num,
            display_index=event_index,
            event_count=event_count,
            events=events,
            chips=chips
        )
    elif intent_name == 'script.event.details - program':
        event_id = retrieve_event_id(output_contexts)
        return chip_response(
            text='Du hast nach dem Programmtext der Veranstaltung gefragt.  TODO Event ID = ' + str(event_id),
            chips=['Zurück: Veranstaltungsübersicht', 'Hauptmenü'])

    elif intent_name == 'script.event.details - corona':
        event_id = retrieve_event_id(output_contexts)
        return chip_response(
            text='Du hast nach dem Coronainfos der Veranstaltung gefragt.  TODO Event ID = ' + str(event_id),
            chips=['Zurück: Veranstaltungsübersicht', 'Hauptmenü'])
    elif intent_name == 'script.event.details - accessibility':
        event_id = retrieve_event_id(output_contexts)
        return chip_response(
            text='Du hast nach den Barrierefreiheitsinfos der Veranstaltung gefragt. TODO Event ID = ' + str(event_id),
            chips=['Zurück: Veranstaltungsübersicht', 'Hauptmenü'])
    elif intent_name == 'script.event.details - schedule':
        event_id = retrieve_event_id(output_contexts)
        return chip_response(
            text='Du hast nach den Spielzeiten der Veranstaltung gefragt. TODO Event ID = ' + str(event_id),
            chips=['Zurück: Veranstaltungsübersicht', 'Hauptmenü'])


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
        # pprint(update)
        response = handle_intent(update['queryResult']['intent']['displayName'], update)

        if response:
            print("====================================== RESPONSE.DATA ======================================")
            # pprint(response)

        return response
    else:
        return "Incorrect request format (/)"


# run the app 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

print("botserver started")
