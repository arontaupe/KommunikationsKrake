# this document contains all helper functions that are used to calculate responses.

import random

# import the response functionality
from response_func import chip_response, chip_w_context_response, event_response
from retrieve_from_gdf import retrieve_event_index, retrieve_found_events
from sb_db_request import get_accessibility_ids


def collect_accessibility_needs(parameters, num_contexts, output_contexts, session_id):
    """
    gets the accessibility info stored in GDF and performs a database request with the accessibility codes
    :param parameters:
    :param num_contexts:
    :param output_contexts:
    :param session_id: The Unique Session ID with Google. Can be overwritten to open new Session.
    :return:
    """
    bedarf = parameters.get('bedarf')
    if len(bedarf) == 0:
        return chip_response(
            text='Brauchst Du etwas Bestimmtes? Was soll ich bei der Auswahl bedenken?',
            chips=['Ich brauche keine Barrierefreiheit',
                   'Ich suche Veranstaltungen in einfacher Sprache',
                   'Ich habe eine Sehbehinderung',
                   'Ich habe eine Hörbehinderung',
                   'Ich habe eine Gehbehinderung'],
            # dgs_videos_chips=make_video_array(['RC14', 'RC15', 'RC16', 'RC17', 'RC18'])
        )

    prev_selection_bedarf = None
    for i in range(num_contexts):
        if 'save_bedarf' in output_contexts[i]['name']:
            prev_selection_bedarf = output_contexts[i]['parameters']['prev_selection_bedarf']

    new_bedarf = [0, 0, 0, 0, 0, 0]
    if prev_selection_bedarf:
        new_bedarf = prev_selection_bedarf
    if bedarf:
        if bedarf == 'kein Bedarf':
            new_bedarf[0] = 1
            return chip_w_context_response(session_id=session_id,
                                           context='save_bedarf',
                                           variable_name='prev_selection_bedarf',
                                           variable=new_bedarf,
                                           text=f'Okay, ich habe {bedarf} abgespeichert.',
                                           chips=["Weiter: Interessen angeben",
                                                  "Zurück zum Hauptmenü"],
                                           # dgs_videos_chips=make_video_array(['E1', 'AC7']),
                                           )
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
    return chip_w_context_response(session_id=session_id,
                                   context='save_bedarf',
                                   variable_name='prev_selection_bedarf',
                                   variable=new_bedarf,
                                   text=f'Brauchst Du noch eine andere Form von Barrierefreiheit?',
                                   chips=["Ja",
                                          "Nein, weiter zum Interessen angeben",
                                          "Zurück zum Haupt-menü"],
                                   # dgs_videos_chips=make_video_array(['AC2', 'AC1', 'AC7']),
                                   # dgs_videos_bot=make_video_array(['A6'])  # TODO
                                   )


def show_full_event_list(output_contexts, session_id, random_order=False):
    """
    retrieves all stored events from GDF and displays them
    :param random_order: boolean whether mixing should happen or not
    :param output_contexts: info retrieved from gdf
    :param session_id: The Unique Session ID with Google. Can be overwritten to open new Session.
    :return:
    """
    event_count, events, titles, ids = retrieve_found_events(output_contexts)
    #print(f'{event_count=}') Was machte das??

    if events is None or event_count == 0:
        return chip_response(text='Ich habe leider keine Events gefunden',
                             chips=['Barrierefreiheit angeben'])

    event_index = int(retrieve_event_index(output_contexts))
    display_num = 1
    # Case: Wir sind am Ende der Liste
    if event_index == event_count:
        next_event_index = 0
        return chip_w_context_response(session_id=session_id,
                                       context='event_index',
                                       variable_name='event_index',
                                       variable=next_event_index,
                                       text='Ich habe dir nun alle ausgewählten Events gezeigt.\r\n'
                                            'Was möchtest du nun tun?',
                                       chips=['Zeig mir die Veranstaltungen noch einmal',
                                              'Zurück zum Hauptmenü'],
                                       # dgs_videos_bot=make_video_array(['A19b']),
                                       # dgs_videos_chips=make_video_array(['RC29b', 'AC7'])
                                       )

    next_event_index = event_index + 1

    title = titles[event_index]
    # Case: we are at the beginning of the list
    chips = ['Gib mir eine weitere Empfehlung',
             'Ich möchte mehr zur Veranstaltung wissen',
             'Schick mir Infos zur Veranstaltung per Mail']
    if event_index == 0:
        # Case: we are in the middle of the list
        pass
    else:
        chips.append('Zeig mir die letzte Empfehlung nochmal')

    # Case some random event from the list is required
    if random_order:
        event_index = random.randint(0, event_count)
    # Final Response
    return event_response(
        session_id=session_id,
        context='event_index',
        variable_name='event_index',
        variable=next_event_index,
        display_num=display_num,
        display_index=event_index,
        events=events,
        chips=chips,
        # dgs_videos_chips=dgs_videos_chips,
        # dgs_videos_bot=make_video_array([f'{title}_Kurzi'])
    )


def map_bedarf_for_db(bedarf=None):
    accessibilities = get_accessibility_ids()
    codes = None
    if bedarf:
        if bedarf == [1.0, 0.0, 0.0, 0.0, 0.0, 0.0] or \
                bedarf == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] or \
                bedarf[0] == 1.0:
            codes = None
        else:
            codes = []
            if bedarf[1] == 1.0:  # leichte Sprache
                codes.append(accessibilities['Leichte Sprache'])
            if bedarf[2] == 1.0:  # Höreinschränkung
                choice = random.choice(['Induktions·schleife [Eine Induktions·schleife ist für schwerhörige Menschen. '
                                        'Sie können den Ton der Veranstaltung dann direkt in ihrem Hör·gerät hören.]',
                                        'Übersetzung in Gebärden·sprache'])
                codes.append(accessibilities[choice])
            if bedarf[3] == 1.0:  # Mobilitätseinschränkung
                choice = random.choice(['Rollstuhl', 'Geh·behinderung/ Aufzüge'])
                codes.append(accessibilities[choice])
            if bedarf[4] == 1.0:  # Visuelle Einschränkung
                choice = random.choice(['Fühl-Tour', 'Unter·titel/ Ober·titel', 'Seh·behinderung/ Seh·schwäche'])
                codes.append(accessibilities[choice])
    return codes


def order_events_by_interest(interests, events=None, event_count=None):
    """
    bekommt einen interessenarray mit ints: [0,1,1,1,0,0,1,0,0]
    muss similarity score errechnen mit events[i]['interests'] und dann liste sortieren nach the highest score
    Names of the entities from DB: BODIES, LIFE, RITUALS, POETRY, UTOPIA, SOCIETY, NATURE, NONACTIVE, FUNNY
    :param interests: array with 9 ints
    :param events: list of events
    :param event_count: number of elements in events
    :return: events list, but sorted according to interest score
    """
    titles = ids = []

    if event_count is not None:
        user_interests = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # read out user interests
        for i in range(len(interests)):
            if interests[i] == 'Ja':
                user_interests[i] = 1
            if interests[i] == 'Ist mir egal':
                user_interests[i] = 2

        # remap the event profile to array
        for i in events:
            score = 0
            event_interests = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            if events[i]['interest'] is not None:
                for interest in events[i]['interest']:
                    if interest == 'BODIES':
                        event_interests[0] = 1
                    elif interest == 'LIFE':
                        event_interests[1] = 1
                    elif interest == 'RITUALS':
                        event_interests[2] = 1
                    elif interest == 'POETRY':
                        event_interests[3] = 1
                    elif interest == 'UTOPIA':
                        event_interests[4] = 1
                    elif interest == 'SOCIETY':
                        event_interests[5] = 1
                    elif interest == 'NATURE':
                        event_interests[6] = 1
                    elif interest == 'NONACTIVE':
                        event_interests[7] = 1
                    elif interest == 'FUNNY':
                        event_interests[8] = 1

            #for j in user_interests:
            print(user_interests)
            print(event_interests)
            for j in range(len(user_interests)):
                if user_interests[j] == event_interests[j]:
                    #print("Treffer" + str(j))
                    if j == 7:
                       score += 4
                    else:
                       score += 2
                elif user_interests[j] == 2:
                    score += 1
                else:
                    score -= 1
                    #print("Kein Treffer" + str(j))
            # store each interest ranking score in the list, for future reference
            events[i]['interest_ranking'] = score
            print(score)
        # the actual sorting, the highest ranking first
        events = dict(sorted(events.items(), key=lambda x: x[1]['interest_ranking'], reverse=True))
        # rename keys
        events = dict(zip(list(range(len(events))), list(events.values())))

        for i in events:
            titles.append(events[i].get('title'))
            ids.append(events[i].get('id'))

    return event_count, events, titles, ids
