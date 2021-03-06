import random  # generates random chips for me
from flask import request  # makes a flask app and serves it to a specified port

# import all background intent_logic functionality
from intent_logic import collect_accessibility_needs, map_bedarf_for_db, order_events_by_interest, show_full_event_list
# import the response functionality
from response_func import button_response, chip_response, chip_w_context_response, chip_w_two_context_response, \
    event_detail_response, event_response, event_schedule_response, image_response, text_response
# import functionality to read out variables from gdf
from retrieve_from_gdf import retrieve_bedarf, retrieve_event_id, retrieve_event_index, \
    retrieve_found_events, \
    retrieve_interests, whether_searched_events
# import the database functions
from sb_db_request import get_event_schedule, get_event_title, get_full_event_list, get_timeframe_event_list
from video_builder import make_video_array
from smalltalk import give_smalltalk
from glossary import give_glossary


def handle_intent(intent_name):
    """
    Handle the webhook request.
this is the main intent switch function. All intents that use the backend must be routed here.
    :param intent_name: the name given in the dialogflow interface
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
        # return {'fulfillmentText': f'Webhook : Der Webhook funktioniert. {datetime.now()}'}
        # return chip_response(chips=['Der', 'Webhook', 'funktioniert'])
        # return image_response(url = 'https://github.com/arontaupe/KommunikationsKrake/blob/'
        #                            '262cd82afae5fac968fa1d535a87d53cd99b9048/backend/sources/fa/a.png?raw=true')

        return text_response(text='Das Backend ist ansprechbar',
                             dgs_videos_bot=make_video_array(titles=['3', '2', '1']))
        # return context_response(session_id=session_id, context='mycontext', variable_name='variable1',
        #                        variable='value1')
        # return image_response(
        #    url='https://github.com/arontaupe/KommunikationsKrake/blob/262cd82afae5fac968fa1d535a87d53cd99b9048/backend/sources/fa/a.png?raw=true')

    elif intent_name == 'script.accessibility.select':
        return chip_response(text='Viele Veranstaltungen sind barrierefrei.\r\n'
                                  'Du kannst ausw??hlen:\r\n'
                                  'Welche Form von Barrierefreiheit brauchst Du?\r\n'
                                  'Dann zeige ich dir nur Veranstaltungen an.\r\n'
                                  'Diese Veranstaltungen sind barrierefrei f??r Dich.\r\n'
                                  'Welche Form von Barrierefreiheit brauchst Du?\r\n',
                             chips=['Ich brauche keine Barrierefreiheit',
                                    'Ich suche Veranstaltungen in einfacher Sprache',
                                    'Ich habe eine Sehbehinderung',
                                    'Ich habe eine H??rbehinderung',
                                    'Ich habe eine Gehbehinderung'
                                    # 'Ich suche eine Veranstaltung ohne schnelle, blinkende Lichter.
                                    # Und ohne laute, pl??tzliche Ger??usche.'
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
            text='Ich m??chte dir Veranstaltungen empfehlen.\r\n'
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

    elif intent_name == 'script.interest.collect':
        try:
            interest_1 = parameters.get('interest_1')
            interest_2 = parameters.get('interest_2')
            interest_3 = parameters.get('interest_3')
            interest_4 = parameters.get('interest_4')
            interest_5 = parameters.get('interest_5')
            interest_6 = parameters.get('interest_6')
            interest_7 = parameters.get('interest_7')
            interest_8 = parameters.get('interest_8')
            interest_9 = parameters.get('interest_9')
        except Exception as e:
            print("Exception when trying to access the interests:script.interest.collect %s\n" % e)
            return text_response('Ich bekomme keine Interessen gesagt')

        while interest_1 == '':
            return chip_response(text='1. Aussage: \r\n'
                                      'Menschliche K??rper faszinieren mich.',
                                 chips=["Ja", "Nein", "Ist mir egal"],
                                 dgs_videos_bot=make_video_array(['A8']),
                                 dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4']))
        while interest_2 == '':
            return chip_w_context_response(text='2. Aussage: \r\n'
                                                'Mich interessieren Lebenswege, die nicht ganz normal verlaufen.',
                                           chips=["Ja", "Nein", "Ist mir egal"],
                                           session_id=session_id,
                                           context='interest_1',
                                           variable_name='interest_1',
                                           variable=interest_1,
                                           dgs_videos_bot=make_video_array(['A9']),
                                           dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                                           )
        while interest_3 == '':
            return chip_w_context_response(text='3. Aussage: \r\n'
                                                'Ich besch??ftige mich gerne mit Ritualen.\r\n'
                                                'Zum Beispiel: Ich z??nde eine Kerze f??r jemanden an.',
                                           chips=["Ja", "Nein", "Ist mir egal"],
                                           session_id=session_id,
                                           context='interest_2',
                                           variable_name='interest_2',
                                           variable=interest_2,
                                           dgs_videos_bot=make_video_array(['A10']),
                                           dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                                           )
        while interest_4 == '':
            return chip_w_context_response(text='4. Aussage: \r\n'
                                                'Ich mag Poetisches. \r\n'
                                                'Zum Beispiel: Sch??ne Musik. '
                                                'Oder: Sch??ne Bilder.',
                                           chips=["Ja", "Nein", "Ist mir egal"],
                                           session_id=session_id,
                                           context='interest_3',
                                           variable_name='interest_3',
                                           variable=interest_3,
                                           dgs_videos_bot=make_video_array(['A11']),
                                           dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                                           )
        while interest_5 == '':
            return chip_w_context_response(text='5. Aussage: \r\n'
                                                'Ich sehne mich nach einer guten Zukunft.',
                                           chips=["Ja", "Nein", "Ist mir egal"],
                                           session_id=session_id,
                                           context='interest_4',
                                           variable_name='interest_4',
                                           variable=interest_4,
                                           dgs_videos_bot=make_video_array(['A12']),
                                           dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                                           )
        while interest_6 == '':
            return chip_w_context_response(text='6. Aussage: \r\n'
                                                'Ich interessiere mich f??r die Frage:\r\n'
                                                'Welche Themen sind in unserer Gesellschaft gerade wichtig? \r\n'
                                                'Wor??ber wird gerade gesprochen?',
                                           chips=["Ja", "Nein", "Ist mir egal"],
                                           session_id=session_id,
                                           context='interest_5',
                                           variable_name='interest_5',
                                           variable=interest_5,
                                           dgs_videos_bot=make_video_array(['A13']),
                                           dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                                           )
        while interest_7 == '':
            return chip_w_context_response(text='7. Aussage: \r\n'
                                                'Ich bin gerne drau??en unterwegs und mag Natur.',
                                           chips=["Ja", "Nein", "Ist mir egal"],
                                           session_id=session_id,
                                           context='interest_6',
                                           variable_name='interest_6',
                                           variable=interest_6,
                                           dgs_videos_bot=make_video_array(['A14']),
                                           dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                                           )
        while interest_8 == '':
            return chip_w_context_response(text='8. Aussage: \r\n'
                                                'Ich m??chte nur zuh??ren.\r\n'
                                                'Ich m??chte nicht selbst bei etwas mitmachen m??ssen.',
                                           chips=["Ja", "Nein", "Ist mir egal"],
                                           session_id=session_id,
                                           context='interest_7',
                                           variable_name='interest_7',
                                           variable=interest_7,
                                           dgs_videos_bot=make_video_array(['A16']),
                                           dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                                           )
        while interest_9 == '':
            return chip_w_context_response(text='9. Aussage: \r\n'
                                                'Ich m??chte nicht so viel nachdenken. \r\n'
                                                'Ich will lieber etwas Lustiges sehen.',
                                           chips=["Ja", "Nein", "Ist mir egal"],
                                           session_id=session_id,
                                           context='interest_8',
                                           variable_name='interest_8',
                                           variable=interest_8,
                                           dgs_videos_bot=make_video_array(['A15']),
                                           dgs_videos_chips=make_video_array(['AC1', 'AC2', 'AC4'])
                                           )
        else:
            return chip_w_context_response(text='Danke f??r deine Antworten.',
                                           session_id=session_id,
                                           context='interest_9',
                                           variable_name='interest_9',
                                           variable=interest_9,
                                           dgs_videos_bot=make_video_array(['RC20']),
                                           dgs_videos_chips=make_video_array(['RC21b']),
                                           chips=['Weiter zu den Veranstaltungstipps']
                                           )

    elif intent_name == 'teach.fingeralhabet':
        try:
            fa_letter = parameters.get('FA-Zeichen')
            if fa_letter == '':
                chips = random.sample(
                    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 5)
                chips.append('Mehr Buchstaben vorschlagen')
                return chip_response(text='Na klar.\r\n'
                                          'Welchen Buchstaben m??chtest du denn lernen?\r\n'
                                          'Gib einen Buchstaben ein.\r\n'
                                          'Ich zeige ihn dir.\r\n',
                                     chips=chips,
                                     dgs_videos_bot=make_video_array(['Finger1'])
                                     )
            folder = 'https://github.com/arontaupe/KommunikationsKrake/blob/' \
                     '262cd82afae5fac968fa1d535a87d53cd99b9048/backend/sources/fa/'
            return image_response(url=str(folder) + str(fa_letter) + '.png?raw=true',
                                  chips=['Ich m??chte noch einen Buchstaben lernen',
                                         'Zur??ck zum Hauptmen??'],
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
                               chips=['Ich habe eine andere Frage', 'Zur??ck zum Hauptmen??'],
                               dgs_videos_bot=make_video_array(['F4']),
                               dgs_videos_chips=make_video_array(['RC3', 'AC7']))

    elif intent_name == 'script.time.select':
        # here we are making the database call and see whether we need to filter further
        bedarf = None
        codes = None
        try:
            bedarf = retrieve_bedarf(output_contexts=output_contexts)
            codes = map_bedarf_for_db(bedarf=bedarf)
        except Exception as e:
            print("Exception when trying to access Accessibilities: %s\n" % e)
        if bedarf:
            print(f'Accessibilites: {bedarf}')
        if codes:
            print(f'Accessibility Codes: {codes}')

        entries = 50  # the number that decides how many events get called per round
        # page = retrieve_page_cache(output_contexts=output_contexts)  # page = index of the call batch
        page = 1
        # print(f'Page: {page}')
        # call the database, if no page number exists yet, the first page will return
        event_count, events, titles, ids = get_full_event_list(accessibility=codes, page=page, entries=entries)
        print(f'Event_count: {event_count}')
        # print(f'Titles: {titles}')

        # obsolete, only used when chunking instead of caching
        # while less events than stated in event_count are present, make another call
        # if page var is lost, the second clause catches it
        while entries * page < event_count and len(events) <= event_count:
            _, events_cache, _, ids_cache = retrieve_found_events(output_contexts=output_contexts)
            # print(f'IDs Cache: {ids_cache}')
            if events_cache is None:
                pass  # do nothing when no cache is present, just hand over the caught events
            else:
                event_list = list(events.values())
                event_list.extend(list(events_cache.values()))
                # pprint(f'Joined Values: {event_list}')
                # rename keys
                events = dict(zip(list(range(len(event_list))), event_list))
                # pprint(f'New Events: {events.keys()}')
            page += 1
            return chip_w_two_context_response(text='Das sind viele Vorschl??ge. \r\n Ich muss nochmal suchen.',
                                               chips=['Finde mehr Veranstaltungstipps'],
                                               session_id=session_id,
                                               context='events_found',
                                               variable_name='events_found',
                                               variable=events,
                                               lifespan=5,
                                               context_2='page_cache',
                                               variable_name_2='page_cache',
                                               variable_2=page,
                                               dgs_videos_bot=make_video_array(['E1']),
                                               dgs_videos_chips=make_video_array(['RC21b']),
                                               )
        # get final list of events
        # event_count, events, titles, ids = retrieve_found_events(output_contexts=output_contexts)
        # print(f'IDs: {ids}')

        if events:
            try:
                interests = retrieve_interests(output_contexts=output_contexts)
            except Exception as e:
                print("Exception when trying to access Interests: %s\n" % e)
            # print(f'Interests: {interests}')
            event_count, events, titles, ids = order_events_by_interest(interests=interests,
                                                                        event_count=event_count,
                                                                        events=events)
        # print(f'IDs: {ids}')
        if events and event_count:
            if event_count > 5:
                text = 'Ich habe sehr viele Veranstaltungen f??r dich gefunden. ' \
                       'M??chtest du ein bestimmtes Datum ausw??hlen?',
                chips = ['Ja: Zeitraum ausw??hlen',
                         "Nein: alle Empfehlungen anzeigen"
                         ]
                dgs_videos_bot = make_video_array(['A17'])
                dgs_videos_chips = make_video_array(['RC22', 'RC23'])
            else:
                text = 'Okay, hier kommt mein Tipp f??r dich! \r\n' \
                       'Ich kann dir mehr zu einer Veranstaltung erz??hlen oder eine andere Veranstaltung vorschlagen'
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
            return chip_response(text='Ich habe leider keine Veranstaltungen mit deinen Barrierefreiheiten gefunden',
                                 chips=['Barrierefreiheit angeben', 'Zur??ck zum Hauptmen??'],
                                 dgs_videos_bot=make_video_array(['A18b']),
                                 dgs_videos_chips=make_video_array(['RC13', 'AC7'])
                                 )

    elif intent_name == 'script.time.filter':
        return chip_response(text='Das wird spannend! Ich kann dir nun: '
                                  'alle Veranstaltungen, die noch bevorstehen oder '
                                  'Veranstaltungen in den n??chsten 5 Tagen suchen',
                             chips=['Nur zuk??nftige Veranstaltungen',
                                    'Veranstaltungen in den n??chsten 5 Tagen'],
                             dgs_videos_bot=make_video_array(['A18']),
                             dgs_videos_chips=make_video_array(['RC25', 'RC26'])
                             )

    elif intent_name == 'script.time.filter.future':
        try:
            # here we are making the database call and see whether we need to filter further
            bedarf = retrieve_bedarf(output_contexts)
            interests = retrieve_interests(output_contexts=output_contexts)
            codes = map_bedarf_for_db(bedarf=bedarf)
            event_count, events, titles, ids = get_timeframe_event_list(accessibility=codes)
            event_count, events, titles, ids = order_events_by_interest(interests=interests, event_count=event_count,
                                                                        events=events)

            text = f'Okay, hier kommt mein hei??er Tipp an noch stattfindenden Veranstaltungen f??r dich! ',
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
                chips=['Zeig mir alle zuk??nftigen Veranstaltungen', "Zeig mir alle Veranstaltungen"])

    elif intent_name == 'script.time.filter.nextdays':
        try:
            num_next_days_filter = int(parameters.get('num_next_days_filter'))
            bedarf = retrieve_bedarf(output_contexts=output_contexts)
            interests = retrieve_interests(output_contexts=output_contexts)
            codes = map_bedarf_for_db(bedarf=bedarf)
            event_count, events, titles, ids = get_timeframe_event_list(num_days=num_next_days_filter,
                                                                        accessibility=codes)
            event_count, events, titles, ids = order_events_by_interest(interests=interests, event_count=event_count,
                                                                        events=events)
            # here we are making the database call and see whether we need to filter further

            text = f'Okay, hier sind die Veranstaltungen in den n??chsten {num_next_days_filter} Tagen f??r dich'
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
        event_id = None
        try:
            event_id = retrieve_event_id(output_contexts=output_contexts)
        except Exception as e:
            print("Exception when trying to access event_id: %s\n" % e)

        if not whether_searched_events(output_contexts=output_contexts):
            if event_id:
                return chip_w_context_response(session_id=session_id,
                                               text='Was m??chtest du mehr wissen ??ber die Veranstaltung?\r\n'
                                                    '1. Ist die Veranstaltung barrierefrei?\r\n'
                                                    '2. Worum geht es genau in der Veranstaltung?\r\n'
                                                    '3. Wie handhabt ihr Corona?\r\n'
                                                    '4. Wo und Wann findet sie statt?\r\n',
                                               chips=['Barrierefreiheit',
                                                      'Programmtext',
                                                      'Coronasituation',
                                                      'Datum und Ort',
                                                      'Zeig mir die Veranstaltung auf Sommerblut.de',
                                                      'Zur??ck: Ich habe eine andere Frage'],
                                               variable_name='event_id',
                                               variable=event_id,
                                               context='event_id',
                                               dgs_videos_bot=make_video_array(['AC20']),
                                               dgs_videos_chips=make_video_array(
                                                   ['RC30', 'RC31', 'RC32', 'RC33', 'RC34', 'RC3'])
                                               )

        try:
            event_count, events, titles, ids = retrieve_found_events(output_contexts)
            if event_id and events is not None:
                return chip_w_context_response(session_id=session_id,
                                               text='Was m??chtest du mehr wissen ??ber die Veranstaltung?\r\n'
                                                    '1. Ist die Veranstaltung barrierefrei?\r\n'
                                                    '2. Worum geht es genau in der Veranstaltung?\r\n'
                                                    '3. Wie handhabt ihr Corona?\r\n'
                                                    '4. Wo und Wann findet sie statt?\r\n',
                                               chips=['Barrierefreiheit',
                                                      'Programmtext',
                                                      'Coronasituation',
                                                      'Datum und Ort',
                                                      'Zeig mir die Veranstaltung auf Sommerblut.de',
                                                      'Zur??ck: Veranstaltungs-empfehlungen'],
                                               variable_name='event_id',
                                               variable=event_id,
                                               context='event_id',
                                               dgs_videos_bot=make_video_array(['AC20']),
                                               dgs_videos_chips=make_video_array(
                                                   ['RC30', 'RC31', 'RC32', 'RC33', 'RC34', 'RC34b'])
                                               )
            elif event_id != 0 and events is None:
                return chip_w_context_response(session_id=session_id,
                                               text='Was m??chtest du mehr wissen ??ber die Veranstaltung?\r\n'
                                                    '1. Ist die Veranstaltung barrierefrei?\r\n'
                                                    '2. Worum geht es genau in der Veranstaltung?\r\n'
                                                    '3. Wie handhabt ihr Corona?\r\n'
                                                    '4. Wo und Wann findet sie statt?\r\n',
                                               chips=['Barrierefreiheit',
                                                      'Programmtext',
                                                      'Coronama??nahmen',
                                                      'Datum und Ort',
                                                      'Zeig mir die Veranstaltung auf sommerblut.de',
                                                      'Zur??ck: Ich habe eine Frage'],
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
                                               text='Was m??chtest du mehr wissen ??ber die Veranstaltung?\r\n'
                                                    '1. Ist die Veranstaltung barrierefrei?\r\n'
                                                    '2. Worum geht es genau in der Veranstaltung?\r\n'
                                                    '3. Wie handhabt ihr Corona?\r\n'
                                                    '4. Wo und Wann findet sie statt?\r\n',
                                               chips=['Barrierefreiheit',
                                                      'Programmtext',
                                                      'Coronama??nahmen',
                                                      'Datum und Ort',
                                                      'Zeig mir die Veranstaltung auf sommerblut.de',
                                                      'Zur??ck: Veranstaltungs-empfehlungen'],
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
                         'Hast du schon deinen Zug??nglichkeitsbedarf angegeben?',
                    chips=['Zug??nglichkeit ausw??hlen', 'Interessen angeben'])

        except Exception as e:
            print("Exception when trying to access event details and event_id: %s\n" % e)

    elif intent_name == 'script.event.menu.previous':
        event_count, events, titles, ids = retrieve_found_events(output_contexts)
        if events is None:
            return chip_response(
                text='Ich habe leider keine Events gespeichert. '
                     'Hast du schon deinen Zug??nglichkeitsbedarf angegeben?',
                chips=['Zug??nglichkeit ausw??hlen', 'Interessen angeben'])

        next_event_index = event_index = int(retrieve_event_index(output_contexts))
        display_num = 1
        if event_count == 1:
            return chip_w_context_response(session_id=session_id,
                                           context='event_index',
                                           variable_name='event_index',
                                           variable=next_event_index,
                                           text='Ich habe dir nun alle ausgew??hlten Veranstaltungen gezeigt. '
                                                'Was m??chtest du nun tun?',
                                           chips=['Zeig mir die Veranstaltungen noch einmal',
                                                  'Zur??ck zum Hauptmen??'],
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
            chips = ['Zeig mir das n??chste Event',
                     'Mehr zur Veranstaltung']
            dgs_videos_chips = make_video_array(['RC28', 'RC29'])
        else:
            chips = ['Zeig mir die letzte Empfehlung nochmal',
                     'Gib mir eine weitere Empfehlung',
                     'Mehr zur Veranstaltung']
            dgs_videos_chips = make_video_array(['RC27', 'RC28', 'RC29'])
        return event_response(
            text='Ich empfehle dir noch einmal die letzte Veranstaltung. '
                 'Ich kann dir dir mehr erz??hlen oder eine andere Veranstaltung vorschlagen',
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
        return button_response(url=url, button_text=button_text, chips=['Zur??ck: Veranstaltungsdetails'])

    elif intent_name == 'script.event.details - program':
        event_id = retrieve_event_id(output_contexts)
        event_count, events, titles, ids = retrieve_found_events(output_contexts=output_contexts)
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
            chips=['Zur??ck zu den Einzelheiten zur Veranstaltung'],
            dgs_videos_chips=make_video_array(['RC34c']),
            dgs_videos_bot=make_video_array([f'{title}_Lang']))

    elif intent_name == 'script.event.details - corona':
        event_id = retrieve_event_id(output_contexts)
        event_count, events, tittles, ids = retrieve_found_events(output_contexts=output_contexts)
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
                 f'{health_infection_notice}\r\n'
                 f'M??chtest du weitere Informationen zur Veranstaltung?',
            chips=['Zur??ck zu den Einzelheiten zur Veranstaltung'],
            dgs_videos_chips=make_video_array(['RC34c']),
            dgs_videos_bot=make_video_array([f'{title}_Corona'])
        )

    elif intent_name == 'script.event.details - accessibility':
        event_id = retrieve_event_id(output_contexts)
        event_count, events, titles, ids = retrieve_found_events(output_contexts=output_contexts)
        accessible_other = 'Ich konnte leider keine Infos zur Barrierefreiheit finden\r\n'
        title = 'der Veranstaltung'
        if event_id and events:
            for e in range(event_count):
                if events[str(e)].get('id') == event_id:
                    if events[str(e)].get('accessible_other') is not None:
                        accessible_other = events[str(e)].get('accessible_other')
                    title = events[str(e)].get('title')
        return chip_response(
            text=f'Das sind die Barriere-Informationen bei {title}: \r\n'
                 f'{accessible_other}\r\n'
                 f'M??chtest du weitere Informationen zur Veranstaltung?',
            chips=['Zur??ck zu den Einzelheiten zur Veranstaltung',
                   'Ich brauche Unterst??tzung bei der Veranstaltung. Mit wem kann ich Kontakt aufnehmen?',
                   'Zu welchen Zeiten kann ich die Veranstaltung besuchen?'],
            dgs_videos_bot=make_video_array([f'{title}_Barri']),
            dgs_videos_chips=make_video_array(['RC34c', 'RC34d', 'RC36'])

        )

    elif intent_name == 'script.event.details - schedule':
        event_id = retrieve_event_id(output_contexts)
        event_count, events, titles, ids = retrieve_found_events(output_contexts=output_contexts)
        if event_id and events:
            for e in range(event_count):
                e_idx = str(e)
                text = ''
                if events[e_idx].get('id') == event_id:
                    duration = title = location = price = image = None
                    if events[e_idx].get('title'):
                        title = events[e_idx].get('title')
                        text += f'{title} \r\n \r\n'
                    if events[e_idx].get('duration'):
                        duration = int(events[e_idx].get('duration'))
                        text += f' Dauer: {duration} Minuten. \r\n '
                    if events[e_idx].get('location'):
                        location = events[e_idx].get('location')
                        text += f'Ort: {location}. \r\n'
                    if events[e_idx].get('price_vvk'):
                        price = int(events[e_idx].get('price_vvk'))
                        text += f'Preis: {price} Euro. \r\n'
                    if events[e_idx].get('event_images'):
                        image = events[e_idx].get('event_images')

                    return event_detail_response(duration=duration,
                                                 title=title,
                                                 location=location,
                                                 price=price,
                                                 image=image,
                                                 text=text,
                                                 chips=['Zur??ck zu den Einzelheiten zur Veranstaltung',
                                                        'Hauptmen??',
                                                        'Zu welchen Zeiten kann ich die Veranstaltung besuchen?'],
                                                 # dgs_videos_bot=make_video_array(),
                                                 dgs_videos_chips=make_video_array(['RC34c', 'AC7', 'RC36'])
                                                 )
        else:
            return chip_response(
                text='Irgendwie habe ich wohl die Veranstaltungsnummer vergessen, versuch es doch noch einmal.',
                chips=['Zur??ck zur ??bersicht der Veranstaltungen',
                       'Zur??ck zu den Einzelheiten zur Veranstaltung', 'Hauptmen??'],
                dgs_videos_chips=make_video_array(['AC7']),
            )

    elif intent_name == 'script.event.details.showSchedule':
        event_id = int(retrieve_event_id(output_contexts))
        play_count, plays = get_event_schedule(event_id)
        event_title = get_event_title(event_id)
        # print(f'{play_count=}')
        if play_count == 0:
            return chip_response(text=f'Titel der Veranstaltung: {event_title} \r\n'
                                      f'Die Veranstaltung ist bereits vor??ber.',
                                 chips=['Zur??ck zu den Einzelheiten zur Veranstaltung',
                                        'Zur??ck zur ??bersicht der Veranstaltungen'],
                                 dgs_videos_chips=make_video_array(['RC34c', 'RC34b'])
                                 )
        return event_schedule_response(play_count,
                                       plays,
                                       text=f'Titel der Veranstaltung: {event_title} \r\n',
                                       chips=['Ich m??chte online ein Ticket kaufen',
                                              'Ich m??chte ein Ticket am Telefon kaufen',
                                              'Ich m??chte Tickets an der Theaterkasse kaufen',
                                              'Zur??ck zu den Einzelheiten zur Veranstaltung',
                                              'Zur??ck zur ??bersicht der Veranstaltungen'],
                                       dgs_videos_chips=make_video_array(['RC37', 'RC38', 'RC39', 'RC34c', 'RC34b'])
                                       )

    elif intent_name == 'faq.contact.accessibility':
        return chip_response(text='Franziska hilft dir gerne bei Fragen zur Barrierefreiheit von Veranstaltungen.\r\n'
                                  'So kannst Du sie erreichen:\r\n'
                                  'franziska.lammers@sommerblut.de\r\n'
                                  'Oder per Telefon: 0221 ??? 29 49 91 34\r\n',
                             chips=['Zur??ck zu den Einzelheiten zur Veranstaltung'],
                             dgs_videos_bot=make_video_array(['A21']),
                             dgs_videos_chips=make_video_array(['RC34c'])

                             )
    elif intent_name == 'faq.finance.how':
        return button_response(url='https://www.sommerblut.de/de/ueber-uns/foerderer-und-sponsoren',
                               button_text='Unsere Sponsoren',
                               text='Zu unseren Sponsoren geh??ren das "Hostel K??ln", '
                                    'das "Maritim Hotel K??ln" und die "REWE Group". '
                                    'Alle aktuellen Sponsoren und F??rderer findest du hier auf unserer Website:  '
                                    'https://www.sommerblut.de/de/ueber-uns/foerderer-und-sponsoren',
                               chips=['Ich habe eine andere Frage'],
                               dgs_videos_bot=make_video_array(['A21']),
                               dgs_videos_chips=make_video_array(['RC34c'])
                               )

    elif intent_name == 'faq.event':
        entries = 50
        # page = retrieve_page_cache(output_contexts=output_contexts)
        page = 1
        event_count, events, titles, ids = get_full_event_list(page=page, entries=entries)
        # print(f'Titles: {titles}')

        # obsolete, only necessary for chunked and not cached responses
        while entries * page < event_count:
            _, events_cache, _, ids_cache = retrieve_found_events(output_contexts=output_contexts)
            # print(f'IDs Cache: {ids_cache}')
            if events_cache is None:
                pass
            else:
                event_list = list(events.values())
                event_list.extend(list(events_cache.values()))
                # pprint(f'Joined Values: {event_list}')
                # rename keys
                events = dict(zip(list(range(len(event_list))), event_list))
                # pprint(f'New Events: {events.keys()}')

            page += 1
            return chip_w_two_context_response(text='Das sind viele Veranstaltungen. \r\n'
                                                    'Ich muss nochmal suchen.',
                                               chips=['Finde mehr Veranstaltungen'],
                                               session_id=session_id,
                                               context='events_found',
                                               variable_name='events_found',
                                               variable=events,
                                               lifespan=3,
                                               context_2='page_cache',
                                               variable_name_2='page_cache',
                                               variable_2=page
                                               )
        # print(f'Event Count: {event_count}')
        # print(f'Titles: {titles}')
        # get final list of events
        # event_count, events, titles, ids = retrieve_found_events(output_contexts=output_contexts)

        if events:
            event_title = parameters.get('event_title')
            if event_title == '':
                chips = random.sample(titles, 5)
                chips.append('Mehr Veranstaltungen vorschlagen')
                # print(chips)
                return chip_response(text='Du kannst den Namen der Veranstaltung in das Textfeld unten eingeben. '
                                          'Oder eine von unten w??hlen:',
                                     chips=chips,
                                     dgs_videos_chips=make_video_array(['F2']),
                                     # dgs_videos_bot=make_video_array(['A23']),
                                     )
            else:
                idx = titles.index(event_title)
                event_id = ids[idx]
                # print(event_id)
                return chip_w_two_context_response(session_id=session_id,
                                                   text='Was m??chtest du mehr wissen ??ber die Veranstaltung?\r\n'
                                                        '1. Ist die Veranstaltung barrierefrei?\r\n'
                                                        '2. Worum geht es genau in der Veranstaltung? \r\n'
                                                        '3. Wie handhabt ihr Corona?\r\n'
                                                        '4. Wo und Wann findet sie statt?\r\n',
                                                   chips=['Barrierefreiheit',
                                                          'Programmtext',
                                                          'Coronama??nahmen',
                                                          'Datum und Ort',
                                                          'Zeig mir die Veranstaltung auf Sommerblut.de',
                                                          'Zur??ck: Ich habe eine Frage'],
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
            text='An folgenden Orten k??nnen Tickets gekauft werden:\r\n'
                 'Theater??kasse am Neumarkt\r\n'
                 'Die Theater??kasse ist auf der Zwischen??ebene der U-Bahn-Station Neumarkt.\r\n '
                 'Die genaue Adresse ist:\r\n'
                 'Neumarkt, U-Bahn-Passage\r\n'
                 'Laden 12\r\n'
                 '50667 K??ln, \r\n',
            chips=['Zeig mir die Veranstaltung auf Sommerblut.de',
                   'Zur??ck zu den Einzelheiten zur Veranstaltung'],
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
                                      'Zur??ck zu den Einzelheiten zur Veranstaltung'],
                               dgs_videos_chips=make_video_array(['RC34', 'RC34c']),
                               dgs_videos_bot=make_video_array(['A23']),
                               )

    elif intent_name == 'script.tickets.sale':
        return button_response(url='https://t.rausgegangen.de/tickets/shop/sommerblut-2022',
                               button_text='Rausgegangen Ticketshop',
                               text='Hier geht es zum Ticketshop von Sommerblut.',
                               chips=['Zeig mir die Veranstaltung auf Sommerblut.de',
                                      'Zur??ck zu den Einzelheiten zur Veranstaltung'])

    elif intent_name == 'fallback.default':
        return chip_response(text='Vielleicht habe ich Dich nicht richtig verstanden.\r\n'
                                  'Kannst du das noch einmal anders sagen?',
                             chips=['Zur??ck zum Hauptmen??',
                                    'Ich habe eine Frage',
                                    'Team von ??llei kontaktieren'],
                             dgs_videos_bot=make_video_array(['E2']),
                             dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                             )
    elif 'smalltalk' in intent_name:
        return give_smalltalk(intent_name)

    elif 'glossary' in intent_name:
        return give_glossary(intent_name, parameters, output_contexts)

    elif intent_name == 'faq.bot.cando':
        return chip_response(
            text='Ich bin noch am lernen. Ich kann dir Veranstaltungen empfehlen und Fragen beantworten. '
                 'Hoffentlich bin ich bald so fit im Internet wie du.',
            chips=['Hauptmen??', 'Ich habe eine Frage', 'Team von ??llei kontaktieren'],
            dgs_videos_chips=make_video_array(['AC7']),
        )

    elif intent_name == 'faq.sommerblut.for-who':
        return chip_response(
            text='Das Sommerblut ist f??r alle da.',
            chips=['Hauptmen??', 'Ich habe eine Frage', 'Team von ??llei kontaktieren'],
            dgs_videos_chips=make_video_array(['AC7']),
        )

    elif intent_name == 'faq.sommerblut.how-many-visitors':
        return chip_response(
            text='2022 kamen im Mai ??ber 7000 Besucher*innen zum Sommerblut Festival.',
            chips=['Hauptmen??', 'Ich habe eine Frage', 'Team von ??llei kontaktieren'],
            dgs_videos_chips=make_video_array(['AC7']),
        )


    elif intent_name == 'faq.knowledge.chatbot':
        return chip_response(
            text='Ein Chatbot Ist eine Maschine, die sich mit dir unterhalten kann wie ein Mensch.',
            chips=['Zur??ck zum Hauptmen??', 'Ich habe eine andere Frage'],
            dgs_videos_chips=make_video_array(['AC7']),
        )

    elif intent_name == 'faq.knowledge.whoami':
        return chip_response(
            text='Ich bin ??llei, ein Chatbot. \r\n'
                 'Ich lebe auf der Website des Sommerblut Festivals. \r\n'
                 'Komm mich gern besuchen!',
            chips=['Zur??ck zum  Hauptmen??', 'Ich habe eine andere Frage'],
            dgs_videos_chips=make_video_array(['AC7', 'RC3']),
        )

    elif intent_name == 'faq.sommerblut.donate':
        return button_response(url='https://www.sommerblut.de/de/ueber-uns/unterstuetzen',
                               button_text='Spenden an Sommerblut',
                               text='Gro??artig. \r\n'
                                    'Das h??re ich gern. \r\n'
                                    'Hier findest du alle Infos dazu: ',
                               chips=['Zur??ck zum  Hauptmen??',
                                      'Ich habe eine andere Frage'],
                               dgs_videos_chips=make_video_array(['AC7', 'RC3']),
                               )

    elif intent_name == 'faq.sommerblut.cooperation':
        return chip_response(
            text='Ja, oft sogar. \r\n'
                 'Wir freuen uns immer, wenn wir andere arbeiten lassen k??nnen.',
            chips=['Zur??ck zum  Hauptmen??',
                   'Ich habe eine andere Frage'],
            dgs_videos_chips=make_video_array(['AC7', 'RC3']),
        )

    elif intent_name == 'faq.sommerblut.discount':
        return chip_response(
            text='Wir bieten erm????igte Tickets f??r viele unterschiedliche Gruppen und Menschen:\r\n '
                 'Sch??ler:innen, Studierende, Azubis und Freiwilligendienstleistende.\r\n'
                 'Menschen mit Nachweis ??ber eine Behinderung.\r\n'
                 'Menschen, die Hartz IV oder andere Bez??ge und soziale Hilfen erhalten. \r\n'
                 'Solltest Du dir unsicher sein, ob Du in eine dieser Kategorien f??llst, \r\n'
                 'schicke uns einfach eine E-Mail und frag nach. \r\n'
                 'Wir m??chten Sommerblut f??r alle Menschen so zug??nglich wie m??glich gestalten.',
            chips=['Zur??ck zum  Hauptmen??',
                   'Ich habe eine andere Frage'],
            dgs_videos_chips=make_video_array(['AC7', 'RC3']),
        )

    elif intent_name == 'faq.sommerblut.career':
        return button_response(url='mailto:info@sommerblut.de',
                               button_text='Schreib uns eine Mail',
                               text='Wir freuen uns immer, wenn das Sommerblut Team w??chst. '
                                    'Schau doch einmal bei den Ausschreibungen vorbei. '
                                    'Oder du kannst meine Kolleg*innen fragen. '
                                    'Hier ist die Email Adresse:  info@sommerblut.de',
                               chips=['Zur??ck zum  Hauptmen??',
                                      'Ich habe eine andere Frage'],
                               dgs_videos_chips=make_video_array(['AC7', 'RC3']),
                               )

    elif intent_name == 'script.welcome':
        return chip_response(
            text='Hi! \r\n'
                 'Mein Name ist ??llei! \r\n'
                 'Sch??n, dass du hier bist. \r\n'
                 'Suchst Du nach Informationen ??ber das Sommerblut Festival? \r\n'
                 'Ich kann Dir helfen. \r\n'
                 'Bist du das erste mal hier? \r\n'
                 'Dann schau dir gern das Einf??hrungs-Video an.\r\n',
            chips=['Einf??hrungsvideo', 'Einf??hrungsvideo in leichter Sprache', 'Kenne ich schon: Hauptmen??',
                   'Ich habe eine Frage'],
            dgs_videos_bot=make_video_array(['A1']),
            dgs_videos_chips=make_video_array(['RC1a', 'RC1b', 'RC2', 'RC3']))

    elif intent_name == 'script.bot.introvideo':
        ls_video = parameters.get('ls_video')
        if ls_video == 'JA':
            return chip_response(
                text='Video: Wie funktioniert der Chatbot und was kann er alles:',
                chips=['Weiter zum Hauptmen??'],
                # dgs_videos_bot=None,
                dgs_videos_chips=make_video_array(['RC4', 'AC7']),
                content_videos=make_video_array(['Intro_Video_LS']))

        return chip_response(
            text='Video: Wie funktioniert der Chatbot und was kann er alles:',
            chips=['Weiter zum Hauptmen??'],
            # dgs_videos_bot=None,
            dgs_videos_chips=make_video_array(['RC4', 'AC7']),
            content_videos=make_video_array(['Intro_Video']))

    elif intent_name == 'script.main_menu':
        return chip_response(
            text='Okay, worauf hast du jetzt Lust?\r\n'
                 'Ich kann dir zum Beispiel noch mehr ??ber mich erz??hlen.\r\n'
                 'Und ??ber k??nstliche Intelligenz.\r\n'
                 'Oder ich berate dich, welche Veranstaltung dir gefallen wird.\r\n',
            chips=['Video: ??llei und KI',
                   'Video: ??llei und KI in Leichter Sprache',
                   'Veranstaltungsberatung',
                   'Mehr ??ber Sommerblut erfahren',
                   'Team von ??llei kontaktieren',
                   'Ich habe eine Frage'],
            dgs_videos_bot=make_video_array(['A2']),
            dgs_videos_chips=make_video_array(['RC5a', 'RC5b', 'RC6', 'RC7', 'Feedback1']))

    elif intent_name == 'script.bot_theme_input':
        ls_video = parameters.get('ls_video')
        if ls_video == 'JA':
            return chip_response(text='Hier wird ein Video gezeigt:\r\n'
                                      ' "Barrierefreiheit im digitalen Raum"\r\n'
                                      'Dieses Video ist leider noch nicht verf??gbar.',
                                 chips=['Mehr ??ber Sommerblut erfahren',
                                        'Ich habe eine Frage',
                                        'Veranstaltungsberatung'],
                                 dgs_videos_bot=make_video_array(['E1']),
                                 # content_videos=make_video_array(['E1']),
                                 dgs_videos_chips=make_video_array(['RC7', 'RC3', 'RC6'])
                                 )

        return chip_response(
            text='Hier wird ein Video gezeigt:\r\n '
                 '"Barrierefreiheit im digitalen Raum"\r\n'
                 'Dieses Video ist leider noch nicht verf??gbar.',
            chips=['Mehr ??ber Sommerblut erfahren',
                   'Ich habe eine Frage',
                   'Veranstaltungsberatung'],
            # dgs_videos_bot=make_video_array(['A2']),
            content_videos=make_video_array(['E1']),
            dgs_videos_chips=make_video_array(['RC7', 'RC3', 'RC6'])
        )

    elif intent_name == 'faq.sommerblut':
        return chip_response(
            text='Okay, was willst du ??ber das Sommerblut wissen?',
            chips=['Ich m??chte mehr ??ber das Motto 2022 wissen.',
                   'Womit besch??ftigt sich das Sommerblut?',
                   # 'Frage zur Barrierefreiheit',
                   'Wer steckt hinter dem Sommerblut?'],
            dgs_videos_bot=make_video_array(['F3']),
            dgs_videos_chips=make_video_array(['FA9', 'FA10', 'FA11'])
        )

    elif intent_name == 'faq.start':
        return chip_response(
            text='Alles klar. Du kannst die Frage unten in das Textfeld schreiben. '
                 'Oder du kannst aus einem Bereich ausw??hlen:',
            chips=['Ich habe eine Frage zu einer bestimmten Veranstaltung',
                   'Frage zum Sommerblut allgemein',
                   # 'Frage zur Barrierefreiheit',
                   'Frage zu ??llei, dem Chatbot',
                   'Das Fingeralphabet kennen lernen',
                   'Begriff erkl??ren'],
            dgs_videos_bot=make_video_array(['F1']),
            dgs_videos_chips=make_video_array(['FA1', 'FA2', 'FA4', 'FA5'])
        )

    elif intent_name == 'script.play_sb_video':
        return chip_response(
            text='Video: Was ist Sommerblut?',
            chips=['Weiter zur Themenvorstellung'],
            content_videos=make_video_array(['SB_Intro']),
            dgs_videos_chips=make_video_array(['AC6'])
        )

    elif intent_name == 'script.sb_theme.play_video':
        return chip_response(
            text='Hier ist ein Video zum Thema "Mach mal neu". ',
            chips=['Weiter zum Bedarfsfilter'],
            content_videos=make_video_array(['SB_Theme']),
            dgs_videos_chips=make_video_array(['RC13'])
        )

    elif intent_name == 'script.sb_intro':
        return chip_response(
            text='Das Sommerblut gibt es nun schon seit mehr als 20 Jahren. Hier ist ein Video. '
                 'Es erz??hlt dir mehr ??ber das Festival.',
            chips=['Video anschauen: Was ist Sommerblut',
                   'Vorstellung ??berspringen'],
            dgs_videos_bot=make_video_array(['A3a']),
            dgs_videos_chips=make_video_array(['RC8', 'AC6'])
        )

    elif intent_name == 'script.sb_theme_intro':
        return chip_response(
            text='Alles klar.\r\n '
                 'Beim Sommerblut gibt es ganz unterschiedliche Veranstaltungen.\r\n'
                 'Dieses Jahr ist unser Motto "Mach mal neu".\r\n'
                 'Soll ich dir dazu mehr erz??hlen?',
            chips=['Video: Mehr zum Thema "Mach mal Neu"',
                   'Nein, weiter zur Veranstaltungsberatung'],
            dgs_videos_bot=make_video_array(['A4']),
            dgs_videos_chips=make_video_array(['RC11', 'RC12'])
        )

    elif intent_name == 'mail.feedback':
        return button_response(
            text='Du kannst uns eine Email schreiben: ',
            button_text='Email an ??llei',
            url='mailto:chatbot@sommerblut.de',
            chips=['Tsch??ss', 'Hauptmen??'],
            dgs_videos_bot=make_video_array(['Feedback2']),
            dgs_videos_chips=make_video_array(['E1', 'AC7'])
        )
