# import flask dependencies
import json  # make me interact with json
# use pretty printing for json responses
import os  # can grab environment variables
from pprint import pprint  # needed for nice json printouts
import random  # generates random chips for me
# server functionality
from flask import Flask, request  # makes a flask app and serves it to a specified port

# Import datetime class from datetime module
from datetime import datetime, timedelta  # used for calculation of timewindows

from flask_httpauth import HTTPBasicAuth  # protects the rest api from being publicly available
from werkzeug.security import check_password_hash, \
    generate_password_hash  # hashes the pasword, so its not passed in clear

auth = HTTPBasicAuth()

# import the response functionality
from response_func import image_response, \
    chip_response, chip_w_context_response, \
    chip_w_two_context_response, \
    event_response, text_response, \
    context_response, button_response, \
    event_schedule_response, event_detail_response
# import functionality to read out variables from gdf
from retrieve_from_gdf import retrieve_bedarf, retrieve_found_events, retrieve_event_index, retrieve_event_id, \
    retrieve_interests, whether_searched_events
# import the database functions
from sb_db_request import test_sb_db, get_accessibility_ids, get_full_event_list, get_event_schedule, get_event_title, \
    get_partial_event_list, get_upcoming_event_list, get_timeframe_event_list, get_all_titles_ids
from video_builder import make_video_array

# import all background intent_logic functionality
from intent_logic import collect_accessibility_needs, show_full_event_list, map_bedarf_for_db, order_events_by_interest

# console should say 200 meaning we have a link to the SB_DB
test_sb_db()

user = os.environ.get('USER')
pw = os.environ.get('PASS')

users = {
    user: generate_password_hash(pw)
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


# initialize the flask app
app = Flask(__name__)


@app.route('/')
def index():
    """
  default route, has text, so I can see when the app is running
    :return: Hello World
    """
    return 'Hello World! This is the running Webhook for Sommerblut. ' \
           'For the API please append /webhook to the current url'


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
    output_contexts = req.get('queryResult').get('outputContexts')
    num_contexts = len(output_contexts)
    session_id = req.get('session')
    # this is the session id given by dialogflow, it can be overridden to start a new session.
    # Then all data and variables will be lost.
    session_id_array = session_id.split("/")
    session_id = session_id_array[len(session_id_array) - 1]

    if intent_name == 'test.fulfillment':
        # several options for feature testing
        now = datetime.now()
        # return {'fulfillmentText': f'Webhook : Der Webhook funktioniert. {now}'}
        # return chip_response(chips=['Der', 'Webhook', 'funktioniert'])
        # return image_response(url = 'https://github.com/arontaupe/KommunikationsKrake/blob/262cd82afae5fac968fa1d535a87d53cd99b9048/backend/sources/fa/a.png?raw=true')

        return text_response(text='Das Backend ist ansprechbar',
                             dgs_videos_bot=make_video_array(titles=['3', '2', '1']))
        # return context_response(session_id=session_id, context='mycontext', variable_name='variable1',
        #                        variable='value1')
        # return image_response(
        #    url='https://github.com/arontaupe/KommunikationsKrake/blob/262cd82afae5fac968fa1d535a87d53cd99b9048/backend/sources/fa/a.png?raw=true')

    elif intent_name == 'script.accessibility.select':
        return chip_response(text='Viele Veranstaltungen sind barrierefrei.\r\n'
                                  'Du kannst auswählen:\r\n'
                                  'Welche Form von Barrierefreiheit brauchst Du?\r\n'
                                  'Dann zeige ich dir nur Veranstaltungen an.\r\n'
                                  'Diese Veranstaltungen sind barrierefrei für Dich.\r\n'
                                  'Welche Form von Barrierefreiheit brauchst Du?\r\n',
                             chips=['Ich brauche keine Barrierefreiheit',
                                    'Ich suche Veranstaltungen in einfacher Sprache',
                                    'Ich habe eine Sehbehinderung',
                                    'Ich habe eine Hörbehinderung',
                                    'Ich habe eine Gehbehinderung'
                                    # 'Ich suche eine Veranstaltung ohne schnelle, blinkende Lichter.
                                    # Und ohne laute, plötzliche Geräusche.'
                                    ],
                             dgs_videos_bot=make_video_array(['A5']),
                             dgs_videos_chips=make_video_array(['RC14', 'RC15', 'RC16', 'RC17', 'RC18']))

    elif intent_name == 'accessibility.select - collect':
        return collect_accessibility_needs(parameters=parameters,
                                           num_contexts=num_contexts,
                                           output_contexts=output_contexts,
                                           session_id=session_id)

    elif intent_name == 'script.interest.select.start':
        # here we are done with collecting the accessibility and have to store it for further use
        prev_selection_bedarf = None
        for i in range(num_contexts):
            if 'save_bedarf' in output_contexts[i]['name']:
                prev_selection_bedarf = output_contexts[i]['parameters']['prev_selection_bedarf']
                # print('Saving final Accessibility: ' + str(prev_selection_bedarf))
        return chip_w_context_response(
            text='Ich möchte dir Veranstaltungen empfehlen.\r\n'
                 'Veranstaltungen, die gut zu dir passen.\r\n'
                 'Dazu muss ich dich erstmal kennenlernen.\r\n'
                 'Ich befrage dich zu Deinen Interessen.\r\n'
                 'Du kannst immer mit Ja, mit Nein, oder mit Egal antworten.',
            chips=["Weiter: Frage 1"],
            session_id=session_id,
            context='final_accessibility',
            variable_name='final_accessibility',
            variable=prev_selection_bedarf,
            dgs_videos_bot=make_video_array(['A7']),
            dgs_videos_chips=make_video_array(['RC21'])
        )

    elif intent_name == 'script.interest.select.1':
        # here we are done with collecting the accessibility and have to store it for further use
        prev_selection_bedarf = None
        for i in range(num_contexts):
            if 'save_bedarf' in output_contexts[i]['name']:
                prev_selection_bedarf = output_contexts[i]['parameters']['prev_selection_bedarf']
                # print('Saving final Accessibility: ' + str(prev_selection_bedarf))
        return chip_response(
            text='Erste Aussage: \r\n'
                 'Menschliche Körper faszinieren mich.',
            chips=["Ja", "Nein", "Ist mir egal"],
            dgs_videos_bot=make_video_array(['A8']),
            dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
        )

    elif intent_name == 'script.interest.select.1 - egal' or \
            intent_name == 'script.interest.select.1 - ja' or \
            intent_name == 'script.interest.select.1 - nein':
        interest_1 = parameters.get('interest_1')
        return chip_w_context_response(text='Soso, ' + interest_1 + ' also.',
                                       chips=["Weiter: Frage 2"],
                                       session_id=session_id,
                                       context='interest_1',
                                       variable_name='interest_1',
                                       variable=interest_1,
                                       dgs_videos_bot=make_video_array(['RC20']),
                                       dgs_videos_chips=make_video_array(['RC21'])
                                       )

    elif intent_name == 'script.interest.select.2':
        # here we are asking for interest_2
        return chip_response(text='Mich interessieren Lebenswege, die nicht ganz normal verlaufen.',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             dgs_videos_bot=make_video_array(['A9']),
                             dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                             )

    elif intent_name == 'script.interest.select.2 - egal' or \
            intent_name == 'script.interest.select.2 - ja' or \
            intent_name == 'script.interest.select.2 - nein':
        interest_2 = parameters.get('interest_2')
        return chip_w_context_response(text=interest_2 + ', interessant.',
                                       chips=["Weiter: Frage 3"],
                                       session_id=session_id,
                                       context='interest_2',
                                       variable_name='interest_2',
                                       variable=interest_2,
                                       dgs_videos_bot=make_video_array(['RC20']),
                                       dgs_videos_chips=make_video_array(['RC21'])
                                       )

    elif intent_name == 'script.interest.select.3':
        # here we are asking for interest_3
        return chip_response(text='Ich beschäftige mich gerne mit Ritualen.\r\n'
                                  'Zum Beispiel: Ich zünde eine Kerze für jemanden an.',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             dgs_videos_bot=make_video_array(['A10']),
                             dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                             )

    elif intent_name == 'script.interest.select.3 - egal' or \
            intent_name == 'script.interest.select.3 - ja' or \
            intent_name == 'script.interest.select.3 - nein':
        interest_3 = parameters.get('interest_3')
        return chip_w_context_response(text='Rituale eher so: ' + interest_3,
                                       chips=["Weiter: Frage 4"],
                                       session_id=session_id,
                                       context='interest_3',
                                       variable_name='interest_3',
                                       variable=interest_3,
                                       dgs_videos_bot=make_video_array(['RC20']),
                                       dgs_videos_chips=make_video_array(['RC21'])
                                       )

    elif intent_name == 'script.interest.select.4':
        # here we are asking for interest_4
        return chip_response(text='Ich mag Poetisches. \r\n'
                                  'Zum Beispiel: Schöne Musik. Oder: Schöne Bilder.',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             dgs_videos_bot=make_video_array(['A11']),
                             dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                             )

    elif intent_name == 'script.interest.select.4 - egal' or \
            intent_name == 'script.interest.select.4 - ja' or \
            intent_name == 'script.interest.select.4 - nein':
        interest_4 = parameters.get('interest_4')
        return chip_w_context_response(text=interest_4 + '? Poesie steckt überall.',
                                       chips=["Weiter: Frage 5"],
                                       session_id=session_id,
                                       context='interest_4',
                                       variable_name='interest_4',
                                       variable=interest_4,
                                       dgs_videos_bot=make_video_array(['RC20']),
                                       dgs_videos_chips=make_video_array(['RC21'])
                                       )

    elif intent_name == 'script.interest.select.5':
        # here we are asking for interest_5
        return chip_response(text='Ich sehne mich nach einer guten Zukunft.',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             dgs_videos_bot=make_video_array(['A12']),
                             dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                             )

    elif intent_name == 'script.interest.select.5 - egal' or \
            intent_name == 'script.interest.select.5 - ja' or \
            intent_name == 'script.interest.select.5 - nein':
        interest_5 = parameters.get('interest_5')
        return chip_w_context_response(text=interest_5 + ', also ich finde UTOPIA gut.',
                                       chips=["Weiter: Frage 6"],
                                       session_id=session_id,
                                       context='interest_5',
                                       variable_name='interest_5',
                                       variable=interest_5,
                                       dgs_videos_bot=make_video_array(['RC20']),
                                       dgs_videos_chips=make_video_array(['RC21'])
                                       )

    elif intent_name == 'script.interest.select.6':
        # here we are asking for interest_6
        return chip_response(text='Ich interessiere mich für die Frage:\r\n'
                                  'Welche Themen sind in unserer Gesellschaft gerade wichtig? \r\n'
                                  'Worüber wird gerade gesprochen?',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             dgs_videos_bot=make_video_array(['A13']),
                             dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                             )

    elif intent_name == 'script.interest.select.6 - egal' or \
            intent_name == 'script.interest.select.6 - ja' or \
            intent_name == 'script.interest.select.6 - nein':
        interest_6 = parameters.get('interest_6')
        return chip_w_context_response(text=interest_6 + ', Ich merke, dass das wichtig ist.',
                                       chips=["Weiter: Frage 7"],
                                       session_id=session_id,
                                       context='interest_6',
                                       variable_name='interest_6',
                                       variable=interest_6,
                                       dgs_videos_bot=make_video_array(['RC20']),
                                       dgs_videos_chips=make_video_array(['RC21'])
                                       )

    elif intent_name == 'script.interest.select.7':
        # here we are asking for interest_7
        return chip_response(text='Ich bin gerne draußen unterwegs und mag Natur.',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             dgs_videos_bot=make_video_array(['A14']),
                             dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                             )

    elif intent_name == 'script.interest.select.7 - egal' or \
            intent_name == 'script.interest.select.7 - ja' or \
            intent_name == 'script.interest.select.7 - nein':
        interest_7 = parameters.get('interest_7')
        return chip_w_context_response(text='Dass du ' + interest_7 + ' klickst, find ich gut!',
                                       chips=["Weiter: Frage 8"],
                                       session_id=session_id,
                                       context='interest_7',
                                       variable_name='interest_7',
                                       variable=interest_7,
                                       dgs_videos_bot=make_video_array(['RC20']),
                                       dgs_videos_chips=make_video_array(['RC21'])
                                       )

    elif intent_name == 'script.interest.select.8':
        # here we are asking for interest_8
        return chip_response(text='Ich möchte nur zuhören.\r\n'
                                  'Ich möchte nicht selbst bei etwas mitmachen müssen. ',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             dgs_videos_bot=make_video_array(['A16']),
                             dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                             )

    elif intent_name == 'script.interest.select.8 - egal' or \
            intent_name == 'script.interest.select.8 - ja' or \
            intent_name == 'script.interest.select.8 - nein':
        interest_8 = parameters.get('interest_8')
        return chip_w_context_response(text='Ich habe mir gemerkt, dass du ' + interest_8 + ' geantwortet hast.',
                                       chips=["Weiter: Frage 9"],
                                       session_id=session_id,
                                       context='interest_8',
                                       variable_name='interest_8',
                                       variable=interest_8,
                                       dgs_videos_bot=make_video_array(['RC20']),
                                       dgs_videos_chips=make_video_array(['RC21'])
                                       )

    elif intent_name == 'script.interest.select.9':
        # here we are asking for interest_9
        return chip_response(text='Ich möchte nicht so viel nachdenken. \r\n'
                                  'Ich will lieber etwas Lustiges sehen.',
                             chips=["Ja", "Nein", "Ist mir egal"],
                             dgs_videos_bot=make_video_array(['A15']),
                             dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                             )

    elif intent_name == 'script.interest.select.9 - egal' or \
            intent_name == 'script.interest.select.9 - ja' or \
            intent_name == 'script.interest.select.9 - nein':
        interest_9 = parameters.get('interest_9')
        return chip_w_context_response(text=None,
                                       chips=["Weiter zu den Veranstaltungstipps", "Menü"],
                                       session_id=session_id,
                                       context='interest_9',
                                       variable_name='interest_9',
                                       variable=interest_9)

    elif intent_name == 'teach.fingeralhabet':
        try:
            fa_letter = parameters.get('FA-Zeichen')
            if fa_letter == '':
                chips = chips = random.sample(
                    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 5)
                return chip_response(text='Na klar.\r\n'
                                          'Welchen Buchstaben möchtest du denn lernen?\r\n'
                                          'Gib einen Buchstaben ein.\r\n'
                                          'Ich zeige ihn dir.\r\n',
                                     chips=chips,
                                     dgs_videos_bot=make_video_array(['Finger1'])
                                     )
            folder = 'https://github.com/arontaupe/KommunikationsKrake/blob/262cd82afae5fac968fa1d535a87d53cd99b9048/backend/sources/fa/'
            return image_response(url=str(folder) + str(fa_letter) + '.png?raw=true',
                                  chips=['Ich möchte noch einen Buchstaben lernen', 'Zurück zum Hauptmenü'],
                                  dgs_videos_bot=make_video_array(['Finger1']),
                                  dgs_videos_chips=make_video_array(['Finger2', 'AC7'])
                                  )
        except Exception as e:
            print("Exception when trying to access fa_letter: %s\n" % e)
            return text_response('Mir sind leider die Bilder ausgegangen.')

    elif intent_name == 'faq.sommerblut.team':
        return button_response(url='https://www.sommerblut.de/ls/ueber-uns/profil-team',
                               button_text='Das Team vom Sommerblut',
                               text=' Das Sommerblut hat ein ganz tolles Team. \r\n'
                                    ' Du kannst sie hier finden',
                               chips=['Ich habe eine andere Frage', 'Zurück zum Hauptmenü'],
                               dgs_videos_bot=make_video_array(['F4']),
                               dgs_videos_chips=make_video_array(['RC3', 'AC7']))

    elif intent_name == 'script.time.select':
        # here we are making the database call and see whether we need to filter further
        bedarf = retrieve_bedarf(output_contexts=output_contexts)

        interests = retrieve_interests(output_contexts=output_contexts)
        codes = map_bedarf_for_db(bedarf=bedarf)
        # print(codes)
        event_count, events, titles, ids = get_full_event_list(accessibility=codes)

        event_count, events = order_events_by_interest(interests=interests, event_count=event_count, events=events)
        if events and event_count:
            text = ''
            if event_count > 5:
                text = 'Ich habe sehr viele Veranstaltungen für dich gefunden. ' \
                       'Möchtest du ein bestimmtes Datum auswählen?',
                chips = ['Ja: Zeitraum auswählen',
                         "Nein: alle Empfehlungen anzeigen"
                         ]
                dgs_videos_bot = make_video_array(['A17'])
                dgs_videos_chips = make_video_array(['RC22', 'RC23'])
            else:
                text = 'Okay, hier kommt mein Tipp für dich! \r\n' \
                       'Ich kann dir mehr zu einer Veranstaltung erzählen oder eine andere Veranstaltung vorschlagen'
                chips = ["Zeig mir die Veranstaltungen",
                         'Zeig mir endlich die Veranstaltungen!'
                         ]
                dgs_videos_bot = make_video_array(['A19'])
                dgs_videos_chips = make_video_array(['RC27a'])
            return chip_w_context_response(text=text,
                                           chips=chips,
                                           session_id=session_id,
                                           context='events_found',
                                           variable_name='events_found',
                                           variable=events,
                                           lifespan=150,
                                           dgs_videos_bot=dgs_videos_bot,
                                           dgs_videos_chips=dgs_videos_chips
                                           )
        else:
            return chip_response(text='Ich habe leider keine Events mit deinen Barrierefreiheiten gefunden',
                                 chips=['Weiter zum Veranstaltungstipp'])

    elif intent_name == 'script.time.filter':
        return chip_response(text='Das wird spannend! Ich kann dir nun: '
                                  'alle Veranstaltungen, die noch bevorstehen oder '
                                  'Veranstaltungen in den nächsten 5 Tagen suchen',
                             chips=['Nur zukünftige Veranstaltungen',
                                    'Veranstaltungen in den nächsten 5 Tagen'],
                             dgs_videos_bot=make_video_array(['A18']),
                             dgs_videos_chips=make_video_array(['RC25', 'RC26'])
                             )

    elif intent_name == 'script.time.filter.future':
        try:
            # here we are making the database call and see whether we need to filter further
            bedarf = retrieve_bedarf(output_contexts)
            # interests = retrieve_interests()
            codes = map_bedarf_for_db(bedarf=bedarf)
            event_count, events = get_upcoming_event_list(accessibility=codes)

            text = f'Okay, hier kommt mein heißer Tipp an noch stattfindenden Veranstaltungen für dich! ',
            chips = ["Zeig mir die Veranstaltungen"]
            return chip_w_context_response(text=text,
                                           chips=chips,
                                           session_id=session_id,
                                           context='events_found',
                                           variable_name='events_found',
                                           variable=events,
                                           lifespan=150,
                                           dgs_videos_bot=make_video_array(['A19']),
                                           dgs_videos_chips=make_video_array(['RC27a'])
                                           )
        except Exception as e:
            print("Exception when trying to access upcoming events: %s\n" % e)
            return chip_response(
                text='Ich habe leider einen Fehler in meinen Berechnungen gemacht, kannst du das nochmal sagen?',
                chips=['Zeig mir alle zukünftigen Veranstaltungen', "Zeig mir alle Veranstaltungen"])



    elif intent_name == 'script.time.filter.nextdays':
        try:
            num_next_days_filter = int(parameters.get('num_next_days_filter'))

            # here we are making the database call and see whether we need to filter further
            bedarf = retrieve_bedarf(output_contexts)
            # interests = retrieve_interests()
            codes = map_bedarf_for_db(bedarf=bedarf)

            event_count, events = get_timeframe_event_list(
                to_date=datetime.now() + timedelta(days=num_next_days_filter),
                accessibility=codes)

            text = f'Okay, hier sind die Veranstaltungen in den nächsten {num_next_days_filter} Tagen für dich'
            chips = ["Zeig mir die Veranstaltungen"]
            return chip_w_context_response(text=text,
                                           chips=chips,
                                           session_id=session_id,
                                           context='events_found',
                                           variable_name='events_found',
                                           variable=events,
                                           lifespan=150,
                                           dgs_videos_chips=make_video_array(['RC27a'])
                                           )
        except Exception as e:
            print("Exception when trying to access num_event_filter: %s\n" % e)
            return chip_response(
                text='Ich habe leider nicht verstanden, wie viele Tage ich dir anzeigen soll.',
                chips=["Zeig mir alle Veranstaltungen"],
                dgs_videos_chips=make_video_array(['RC27a'])
            )

    elif intent_name == 'script.event.menu':
        return show_full_event_list(output_contexts=output_contexts, session_id=session_id)

    elif intent_name == 'script.event.details':
        try:
            event_id = retrieve_event_id(output_contexts=output_contexts)
        except Exception as e:
            print("Exception when trying to access event_id: %s\n" % e)

        if whether_searched_events(output_contexts=output_contexts) == False:
            if event_id:
                return chip_w_context_response(session_id=session_id,
                                               text='Was möchtest du mehr wissen über die Veranstaltung?\r\n'
                                                    '1. Ist die Veranstaltung barrierefrei?\r\n'
                                                    '2. Worum geht es genau in der Veranstaltung?\r\n'
                                                    '3. Wie handhabt ihr Corona?\r\n'
                                                    '4. Wo und Wann findet sie statt?\r\n',
                                               chips=['Barrierefreiheit',
                                                      'Programmtext',
                                                      'Coronasituation',
                                                      'Datum und Ort',
                                                      'Zeig mir die Veranstaltung auf Sommerblut.de'
                                                      ],
                                               variable_name='event_id',
                                               variable=event_id,
                                               context='event_id',
                                               dgs_videos_bot=make_video_array(['AC20']),
                                               dgs_videos_chips=make_video_array(
                                                   ['RC30', 'RC31', 'RC32', 'RC33', 'RC34'])
                                               )

        try:
            event_count, events = retrieve_found_events(output_contexts)
            if event_id and events is not None:
                return chip_w_context_response(session_id=session_id,
                                               text='Was möchtest du mehr wissen über die Veranstaltung?\r\n'
                                                    '1. Ist die Veranstaltung barrierefrei?\r\n'
                                                    '2. Worum geht es genau in der Veranstaltung?\r\n'
                                                    '3. Wie handhabt ihr Corona?\r\n'
                                                    '4. Wo und Wann findet sie statt?\r\n',
                                               chips=['Barrierefreiheit',
                                                      'Programmtext',
                                                      'Coronasituation',
                                                      'Datum und Ort',
                                                      'Zeig mir die Veranstaltung auf Sommerblut.de',
                                                      'Zurück: Veranstaltungs-empfehlungen'],
                                               variable_name='event_id',
                                               variable=event_id,
                                               context='event_id',
                                               dgs_videos_bot=make_video_array(['AC20']),
                                               dgs_videos_chips=make_video_array(
                                                   ['RC30', 'RC31', 'RC32', 'RC33', 'RC34', 'RC34b'])
                                               )
            elif event_id != 0 and events is None:
                return chip_w_context_response(session_id=session_id,
                                               text='Was möchtest du mehr wissen über die Veranstaltung?\r\n'
                                                    '1. Ist die Veranstaltung barrierefrei?\r\n'
                                                    '2. Worum geht es genau in der Veranstaltung?\r\n'
                                                    '3. Wie handhabt ihr Corona?\r\n'
                                                    '4. Wo und Wann findet sie statt?\r\n',
                                               chips=['Barrierefreiheit',
                                                      'Programmtext',
                                                      'Coronamaßnahmen',
                                                      'Datum und Ort',
                                                      'Zeig mir die Veranstaltung auf sommerblut.de',
                                                      'Zurück: Ich habe eine Frage'],
                                               variable_name='event_id',
                                               variable=event_id,
                                               context='event_id',
                                               dgs_videos_bot=make_video_array(['AC20']),
                                               dgs_videos_chips=make_video_array(
                                                   ['RC30', 'RC31', 'RC32', 'RC33', 'RC34', 'RC34b'])
                                               )

            elif events is not None:
                next_event_index = int(retrieve_event_index(output_contexts))
                if next_event_index == event_count:
                    event_index = event_count - 1
                else:
                    event_index = next_event_index - 1

                event_id = events[str(event_index)]['id']

                return chip_w_context_response(session_id=session_id,
                                               text='Was möchtest du mehr wissen über die Veranstaltung?\r\n'
                                                    '1. Ist die Veranstaltung barrierefrei?\r\n'
                                                    '2. Worum geht es genau in der Veranstaltung?\r\n'
                                                    '3. Wie handhabt ihr Corona?\r\n'
                                                    '4. Wo und Wann findet sie statt?\r\n',
                                               chips=['Barrierefreiheit',
                                                      'Programmtext',
                                                      'Coronamaßnahmen',
                                                      'Datum und Ort',
                                                      'Zeig mir die Veranstaltung auf sommerblut.de',
                                                      'Zurück: Veranstaltungs-empfehlungen'],
                                               variable_name='event_id',
                                               variable=event_id,
                                               context='event_id',
                                               dgs_videos_bot=make_video_array(['AC20']),
                                               dgs_videos_chips=make_video_array(
                                                   ['RC30', 'RC31', 'RC32', 'RC33', 'RC34', 'RC34b'])
                                               )
            else:
                return chip_response(
                    text='Ich habe leider keine Veranstaltungen gespeichert. '
                         'Hast du schon deinen Zugänglichkeitsbedarf angegeben?',
                    chips=['Zugänglichkeit auswählen', 'Interessen angeben'])

        except Exception as e:
            print("Exception when trying to access event details and event_id: %s\n" % e)



    elif intent_name == 'script.event.menu.previous':
        event_count, events = retrieve_found_events(output_contexts)
        if events is None:
            return chip_response(
                text='Ich habe leider keine Events gespeichert. '
                     'Hast du schon deinen Zugänglichkeitsbedarf angegeben?',
                chips=['Zugänglichkeit auswählen', 'Interessen angeben'])

        next_event_index = event_index = int(retrieve_event_index(output_contexts))
        display_num = 1
        if event_count == 1:
            return chip_w_context_response(session_id=session_id,
                                           context='event_index',
                                           variable_name='event_index',
                                           variable=next_event_index,
                                           text='Ich habe dir nun alle ausgewählten Veranstaltungen gezeigt. '
                                                'Was möchtest du nun tun?',
                                           chips=['Zeig mir die Veranstaltungen noch einmal',
                                                  'Zurück zum Hauptmenü'],
                                           dgs_videos_bot=make_video_array(['A19b']),
                                           dgs_videos_chips=make_video_array(['RC29b', 'AC7']))
        if event_index == 0:
            event_index = event_count - 2
            next_event_index = event_index + 1
        elif event_index == 1:
            event_index = event_count - 1
            next_event_index = event_index + 1
        else:
            event_index = event_index - 2
            next_event_index = event_index + 1

        # print(event_index, next_event_index, event_count)
        if event_index == 0:
            chips = ['Zeig mir das nächste Event',
                     'Mehr zur Veranstaltung']
            dgs_videos_chips = make_video_array(['RC28', 'RC29'])
        else:
            chips = ['Zeig mir die letzte Empfehlung nochmal',
                     'Gib mir eine weitere Empfehlung',
                     'Mehr zur Veranstaltung']
            dgs_videos_chips = make_video_array(['RC27', 'RC28', 'RC29'])
        return event_response(
            text='Ich empfehle dir noch einmal die letzte Veranstaltung. '
                 'Ich kann dir dir mehr erzählen oder eine andere Veranstaltung vorschlagen',
            session_id=session_id,
            context='event_index',
            variable_name='event_index',
            variable=next_event_index,
            display_num=display_num,
            display_index=event_index,
            events=events,
            chips=chips,
            dgs_videos_chips=dgs_videos_chips
        )

    elif intent_name == 'script.event.details - linkout':
        event_id = retrieve_event_id(output_contexts)
        url = 'https://www.sommerblut.de/en/event/' + str(event_id)
        button_text = 'Link zum Event'
        return button_response(url=url, button_text=button_text, chips=['Zurück: Veranstaltungsdetails'])

    elif intent_name == 'script.event.details - program':
        event_id = retrieve_event_id(output_contexts)
        event_count, events = retrieve_found_events(output_contexts=output_contexts)
        program_content = 'Ich habe leider keine Programmbeschreibung gefunden'
        title = 'der Veranstaltung'
        if event_id and events:
            for e in range(event_count):
                if events[str(e)].get('id') == event_id:
                    program_content = events[str(e)].get('program_content')
                    title = events[str(e)].get('title')
        return chip_response(
            text=f'Hier ist der Programmtext von {title}: \r\n'
                 f'{program_content}',
            chips=['Zurück zu den Einzelheiten zur Veranstaltung'],
            dgs_videos_chips=make_video_array(['RC34c']),
            dgs_videos_bot=make_video_array([f'{title}_Lang']))

    elif intent_name == 'script.event.details - corona':
        event_id = retrieve_event_id(output_contexts)
        event_count, events = retrieve_found_events(output_contexts=output_contexts)
        health_infection_notice = ' Ich konnte leider keine Infos zum Coronaschutz finden \r\n'
        title = 'der Veranstaltung'
        if event_id and events:
            for e in range(event_count):
                if events[str(e)].get('id') == event_id:
                    if events[str(e)].get('health_infection_notice') is not None:
                        health_infection_notice = events[str(e)].get('health_infection_notice')
                    title = events[str(e)].get('title')
        return chip_response(
            text=f'Diese Corona-Regeln gelten bei {title}: \r\n'
                 f'{health_infection_notice}',
            chips=['Zurück zu den Einzelheiten zur Veranstaltung'],
            dgs_videos_chips=make_video_array(['RC34c']),
            dgs_videos_bot=make_video_array([f'{title}_Corona'])
        )

    elif intent_name == 'script.event.details - accessibility':
        event_id = retrieve_event_id(output_contexts)
        event_count, events = retrieve_found_events(output_contexts=output_contexts)
        accessible_other = 'Ich konnte leider keine Infos zur Barrierefreiheit finden'
        title = 'der Veranstaltung'
        if event_id and events:
            for e in range(event_count):
                if events[str(e)].get('id') == event_id:
                    if events[str(e)].get('accessible_other') is not None:
                        accessible_other = events[str(e)].get('accessible_other')
                    title = events[str(e)].get('title')
        return chip_response(
            text=f'Das sind die Corona-Regeln bei {title}: \r\n'
                 f'{accessible_other}'
                 f'Möchtest du weitere Informationen zur Veranstaltung?',
            chips=['Zurück zu den Einzelheiten zur Veranstaltung',
                   'Ich brauche Unterstützung bei der Veranstaltung. Mit wem kann ich Kontakt aufnehmen?',
                   'Zu welchen Zeiten kann ich die Veranstaltung besuchen?'],
            dgs_videos_bot=make_video_array([f'{title}_Barri']),
            dgs_videos_chips=make_video_array(['RC34c', 'RC34d', 'RC36'])

        )

    elif intent_name == 'script.event.details - schedule':
        event_id = retrieve_event_id(output_contexts)
        event_count, events = retrieve_found_events(output_contexts=output_contexts)
        if event_id and events:
            for e in range(event_count):
                if events[str(e)].get('id') == event_id:
                    duration = int(events[str(e)].get('duration'))
                    title = events[str(e)].get('title')
                    location = events[str(e)].get('location')
                    price = int(events[str(e)].get('price_vvk'))
                    image = events[str(e)].get('event_images')
                    return event_detail_response(duration=duration,
                                                 title=title,
                                                 location=location,
                                                 price=price,
                                                 image=image,
                                                 text=f'{title} dauert {duration} Minuten. \r\n '
                                                      f'Es findet statt an diesem Ort: {location}. \r\n'
                                                      f'Er kostet {price} Euro. \r\n'
                                                      f'(Event_ID: {event_id})',
                                                 chips=['Zurück zu den Einzelheiten zur Veranstaltung',
                                                        'Hauptmenü',
                                                        'Zu welchen Zeiten kann ich die Veranstaltung besuchen?'],
                                                 # dgs_videos_bot=make_video_array(),
                                                 dgs_videos_chips=make_video_array(['RC34c', 'AC7', 'RC36'])
                                                 )
        else:
            return chip_response(
                text='Irgendwie habe ich wohl die Veranstaltungsnummer vergessen, versuch es doch noch einmal.',
                chips=['Zurück zur Übersicht der Veranstaltungen',
                       'Zurück zu den Einzelheiten zur Veranstaltung', 'Hauptmenü'],
                dgs_videos_chips=make_video_array(['AC7']),
            )

    elif intent_name == 'script.event.details.showSchedule':
        event_id = int(retrieve_event_id(output_contexts))
        play_count, plays = get_event_schedule(event_id)
        event_title = get_event_title(event_id)

        return event_schedule_response(play_count,
                                       plays,
                                       text=f'Titel der Veranstaltung: {event_title} \r\n'
                                            f'Veranstaltungs-Nummer: {event_id}',
                                       chips=['Ich möchte online ein Ticket kaufen',
                                              'Ich möchte ein Ticket am Telefon kaufen',
                                              'Ich möchte Tickets an der Theaterkasse kaufen',
                                              'Zurück zu den Einzelheiten zur Veranstaltung',
                                              'Zurück zur Übersicht der Veranstaltungen'],
                                       dgs_videos_chips=make_video_array(['RC37', 'RC38', 'RC39', 'RC34c', 'RC34b'])
                                       )

    elif intent_name == 'faq.contact.accessibility':
        return chip_response(text='Franziska hilft dir gerne bei Fragen zur Barrierefreiheit von Veranstaltungen.\r\n'
                                  'So kannst Du sie erreichen:\r\n'
                                  'franziska.lammers@sommerblut.de\r\n'
                                  'Oder per Telefon: 0221 – 29 49 91 34\r\n',
                             chips=['Zurück zu den Einzelheiten zur Veranstaltung'],
                             dgs_videos_bot=make_video_array(['A21']),
                             dgs_videos_chips=make_video_array(['RC34c'])

                             )

    elif intent_name == 'faq.event':

        event_count, events, titles, ids = get_full_event_list()

        if events:
            event_title = parameters.get('event_title')
            if event_title == '':
                chips = random.sample(titles, 5)
                # print(chips)
                return chip_response(text='Du kannst den Namen der Veranstaltung in das Textfeld unten eingeben. '
                                          'Oder eine von unten wählen:',
                                     chips=chips,
                                     dgs_videos_chips=make_video_array(['F2']),
                                     # dgs_videos_bot=make_video_array(['A23']),
                                     )
            else:
                idx = titles.index(event_title)
                event_id = ids[idx]
                # print(event_id)
                return chip_w_two_context_response(session_id=session_id,
                                                   text='Was möchtest du mehr wissen über die Veranstaltung?\r\n'
                                                        '1. Ist die Veranstaltung barrierefrei?\r\n'
                                                        '2. Worum geht es genau in der Veranstaltung? \r\n'
                                                        '3. Wie handhabt ihr Corona?\r\n'
                                                        '4. Wo und Wann findet sie statt?\r\n',
                                                   chips=['Barrierefreiheit',
                                                          'Programmtext',
                                                          'Coronamaßnahmen',
                                                          'Datum und Ort',
                                                          'Zeig mir die Veranstaltung auf Sommerblut.de',
                                                          'Zurück: Ich habe eine Frage'],
                                                   variable_name='event_id',
                                                   variable_name_2='events_found',
                                                   variable=event_id,
                                                   variable_2=events,
                                                   context='event_id',
                                                   context_2='events_found',
                                                   dgs_videos_bot=make_video_array(['AC20']),
                                                   dgs_videos_chips=make_video_array(
                                                       ['RC30', 'RC31', 'RC32', 'RC33', 'RC34'])
                                                   )


    elif intent_name == 'faq.tickets.sale_location':
        return chip_response(
            text='An folgenden Orten können Tickets gekauft werden:\r\n'
                 'Theater·kasse am Neumarkt\r\n'
                 'Die Theater·kasse ist auf der Zwischen·ebene der U-Bahn-Station Neumarkt.\r\n '
                 'Die genaue Adresse ist:\r\n'
                 'Neumarkt, U-Bahn-Passage\r\n'
                 'Laden 12\r\n'
                 '50667 Köln, \r\n',
            chips=['Zeig mir die Veranstaltung auf Sommerblut.de',
                   'Zurück zu den Einzelheiten zur Veranstaltung'],
            dgs_videos_bot=make_video_array(['A24']),
            dgs_videos_chips=make_video_array(['RC34', 'RC34c'])
        )

    elif intent_name == 'faq.tickets.sale_phone':
        return button_response(url='tel:+4922142076000',
                               button_text='Direkt anrufen',
                               text='Du kannst die Tickets auch am Telefon bestellen.\r\n'
                                    'Unter der Telefonnummer 0221 42 07 6000.\r\n'
                                    'Aber Achtung:\r\n'
                                    'Am Telefon kann man die Tickets mit Kreditkarte bezahlen.\r\n',
                               chips=['Zeig mir die Veranstaltung auf Sommerblut.de',
                                      'Zurück zu den Einzelheiten zur Veranstaltung'],
                               dgs_videos_chips=make_video_array(['RC34', 'RC34c']),
                               dgs_videos_bot=make_video_array(['A23']),
                               )

    elif intent_name == 'script.tickets.sale':
        return button_response(url='https://t.rausgegangen.de/tickets/shop/sommerblut-2022',
                               button_text='Rausgegangen Ticketshop',
                               text='Hier geht es zum Ticketshop von Sommerblut.',
                               chips=['Zeig mir die Veranstaltung auf Sommerblut.de',
                                      'Zurück zu den Einzelheiten zur Veranstaltung'])

    elif 'smalltalk' in intent_name or intent_name == 'fallback.default':
        return chip_response(text='Vielleicht habe ich Dich nicht richtig verstanden.\r\n'
                                  'Kannst du das noch einmal anders sagen?',
                             chips=['Zurück zum Hauptmenü',
                                    'Ich habe eine Frage',
                                    'Team von Ällei kontaktieren'],
                             dgs_videos_bot=make_video_array(['E2']),
                             dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                             )


    elif intent_name == 'faq.bot.cando':
        return chip_response(
            text='Ich bin noch am lernen. Ich kann dir Veranstaltungen empfehlen und Fragen beantworten. '
                 'Hoffentlich bin ich bald so fit im Internet wie du.',
            chips=['Hauptmenü', 'Ich habe eine Frage', 'Team von Ällei kontaktieren'],
            dgs_videos_chips=make_video_array(['AC7']),
        )

    elif intent_name == 'faq.knowledge.chatbot':
        return chip_response(
            text='Ein Chatbot Ist eine Maschine, die sich mit dir unterhalten kann wie ein Mensch.',
            chips=['Zurück zum Hauptmenü', 'Ich habe eine andere Frage'],
            dgs_videos_chips=make_video_array(['AC7']),
        )

    elif intent_name == 'faq.knowledge.whoami':
        return chip_response(
            text='Ich bin Ällei, ein Chatbot. '
                 'Ich lebe auf der Website des Sommerblut Festivals. '
                 'Komm mich gern besuchen!',
            chips=['Zurück zum  Hauptmenü', 'Ich habe eine andere Frage'],
            dgs_videos_chips=make_video_array(['AC7', 'RC3']),
        )

    elif intent_name == 'script.welcome':
        return chip_response(
            text='Hi! \r\n'
                 'Mein Name ist Ällei! \r\n'
                 'Schön, dass du hier bist. \r\n'
                 'Suchst Du nach Informationen über das Sommerblut Festival? \r\n'
                 'Ich kann Dir helfen. \r\n'
                 'Bist du das erste mal hier? \r\n'
                 'Dann schau dir gern das Einführungs-Video an.\r\n',
            chips=['Einführungsvideo', 'Einführungsvideo in leichter Sprache', 'Kenne ich schon: Hauptmenü',
                   'Ich habe eine Frage'],
            dgs_videos_bot=make_video_array(['A1']),
            dgs_videos_chips=make_video_array(['RC1a', 'RC1b', 'RC2', 'RC3']))

    elif intent_name == 'script.bot.introvideo':
        ls_video = parameters.get('ls_video')
        if ls_video == 'JA':
            return chip_response(
                text='Video: Wie funktioniert der Chatbot und was kann er alles:',
                chips=['Weiter zum Hauptmenü'],
                # dgs_videos_bot=None,
                dgs_videos_chips=make_video_array(['RC4', 'AC7']),
                content_videos=make_video_array(['Intro_Video_LS']))

        return chip_response(
            text='Video: Wie funktioniert der Chatbot und was kann er alles:',
            chips=['Weiter zum Hauptmenü'],
            # dgs_videos_bot=None,
            dgs_videos_chips=make_video_array(['RC4', 'AC7']),
            content_videos=make_video_array(['Intro_Video']))

    elif intent_name == 'script.main_menu':
        return chip_response(
            text='Okay, worauf hast du jetzt Lust?\r\n'
                 'Ich kann dir zum Beispiel noch mehr über mich erzählen.\r\n'
                 'Und über künstliche Intelligenz.\r\n'
                 'Oder ich berate dich, welche Veranstaltung dir gefallen wird.\r\n',
            chips=['Video: Ällei und KI', 'Video: Ällei und KI in Leichter Sprache', 'Veranstaltungsberatung',
                   'Mehr über Sommerblut erfahren', 'Team von Ällei kontaktieren'],
            dgs_videos_bot=make_video_array(['A2']),
            dgs_videos_chips=make_video_array(['RC5a', 'RC5b', 'RC6', 'RC7', 'Feedback1']))

    elif intent_name == 'script.bot_theme_input':
        ls_video = parameters.get('ls_video')
        if ls_video == 'JA':
            return chip_response(text='Hier wird ein Video gezeigt:\r\n'
                                      ' "Barrierefreiheit im digitalen Raum"\r\n'
                                      'Dieses Video ist leider noch nicht verfügbar.',
                                 chips=['Mehr über Sommerblut erfahren',
                                        'Ich habe eine Frage',
                                        'Veranstaltungsberatung'],
                                 dgs_videos_bot=make_video_array(['E1']),
                                 # content_videos=make_video_array(['E1']),
                                 dgs_videos_chips=make_video_array(['RC7', 'RC3', 'RC6'])
                                 )

        return chip_response(
            text='Hier wird ein Video gezeigt:\r\n '
                 '"Barrierefreiheit im digitalen Raum"\r\n'
                 'Dieses Video ist leider noch nicht verfügbar.',
            chips=['Mehr über Sommerblut erfahren',
                   'Ich habe eine Frage',
                   'Veranstaltungsberatung'],
            # dgs_videos_bot=make_video_array(['A2']),
            content_videos=make_video_array(['E1']),
            dgs_videos_chips=make_video_array(['RC7', 'RC3', 'RC6'])
        )

    elif intent_name == 'faq.sommerblut':
        return chip_response(
            text='Okay, was willst du über das Sommerblut wissen?',
            chips=['Ich möchte mehr über das Motto 2022 wissen.',
                   'Womit beschäftigt sich das Sommerblut?',
                   # 'Frage zur Barrierefreiheit',
                   'Wer steckt hinter dem Sommerblut?'],
            dgs_videos_bot=make_video_array(['F3']),
            dgs_videos_chips=make_video_array(['FA9', 'FA10', 'FA11'])
        )

    elif intent_name == 'faq.start':
        return chip_response(
            text='Alles klar. Du kannst die Frage unten in das Textfeld schreiben. '
                 'Oder du kannst aus einem Bereich auswählen:',
            chips=['Frage zu einer konkreten Veranstaltung',
                   'Frage zum Sommerblut allgemein',
                   # 'Frage zur Barrierefreiheit',
                   'Frage zu Ällei, dem Chatbot',
                   'Das Fingeralphabet kennen lernen'],
            dgs_videos_bot=make_video_array(['F1']),
            dgs_videos_chips=make_video_array(['FA1', 'FA2', 'FA4', 'FA5'])
        )

    elif intent_name == 'script.play_sb_video':
        return chip_response(
            text='Video: Was ist Sommerblut?',
            chips=['weiter: Themenvorstellung'],
            content_videos=make_video_array(['SB_Intro']),
            dgs_videos_chips=make_video_array(['AC6'])
        )

    elif intent_name == 'script.sb_theme.play_video':
        return chip_response(
            text='Hier ist ein Video zum Thema "Mach mal neu". ',
            chips=['Weiter: Bedarfsfilter'],
            content_videos=make_video_array(['SB_Theme']),
            dgs_videos_chips=make_video_array(['RC13'])
        )


    elif intent_name == 'script.sb_intro':
        return chip_response(
            text='Das Sommerblut gibt es nun schon seit mehr als 20 Jahren. Hier ist ein Video. '
                 'Es erzählt dir mehr über das Festival.',
            chips=['Video anschauen: Was ist Sommerblut',
                   'Vorstellung überspringen'],
            dgs_videos_bot=make_video_array(['A3a']),
            dgs_videos_chips=make_video_array(['RC8', 'AC6'])
        )

    elif intent_name == 'script.sb_theme_intro':
        return chip_response(
            text='Alles klar.\r\n '
                 'Beim Sommerblut gibt es ganz unterschiedliche Veranstaltungen.\r\n'
                 'Dieses Jahr ist unser Motto "Mach mal neu".\r\n'
                 'Soll ich dir dazu mehr erzählen?',
            chips=['Video: Mehr zum Thema "Mach mal Neu"',
                   'Nein, weiter zur Veranstaltungsberatung'],
            dgs_videos_bot=make_video_array(['A4']),
            dgs_videos_chips=make_video_array(['RC11', 'RC12'])
        )

    elif intent_name == 'mail.feedback':
        return button_response(
            text='Du kannst uns eine Email schreiben: ',
            button_text='Email an Ällei',
            url='mailto:chatbot@sommerblut.de',
            chips=['Tschüss', 'Hauptmenü'],
            dgs_videos_bot=make_video_array(['Feedback2']),
            dgs_videos_chips=make_video_array(['AC7'])
        )


# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
@auth.login_required
def update():
    """
Main listener to DF, will call handle_intent upon being activated
    :return: the response to DF
    """
    if request.method == 'POST':
        update = request.data.decode("utf8")
        update = json.loads(update)
        # print("====================================== REQUEST.DATA ======================================")
        # pprint(update)
        response = handle_intent(update['queryResult']['intent']['displayName'], update)

        # if response:
        # print("====================================== RESPONSE.DATA ======================================")
        # pprint(response)

        return response
    else:
        return "Incorrect request format (/)"


# run the app 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

print("Backend started without error")
