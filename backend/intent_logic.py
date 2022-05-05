# use pretty printing for json responses
from pprint import pprint

pprint('intent_logic')
# import the response functionality
from response_func import image_response, chip_response, chip_w_context_response, event_response, text_response, \
    context_response, button_response, event_schedule_response

from retrieve_from_gdf import retrieve_found_events, retrieve_event_index
from sb_db_request import get_accessibility_ids


def collect_accessibility_needs(parameters, num_contexts, output_contexts, session_id):
    """
gets the accessibility info stored in GDF and performs a database request with the accessibility codes
    :param parameters:
    :param num_contexts:
    :param output_contexts:
    :param session_id:
    :return:
    """
    bedarf = parameters.get('bedarf')
    if len(bedarf) == 0:
        return chip_response(
            text='Du kannst jetzt eine Zugänglichkeit eingeben, die bei meinen Empfehlungen beachtet werden soll.',
            chips=['Keinen Bedarf angeben',
                   'Zugänglich in einfacher Sprache',
                   'Zugänglich mit Seheinschränkung',
                   'Zugänglich mit Höreinschränkungen',
                   'Zugänglich mit Mobilitätseinschränkungen',
                   'Zugänglich ohne intensive sensorische Reizungen'])

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
            return chip_w_context_response(session_id=session_id,
                                           context='save_bedarf',
                                           variable_name='prev_selection_bedarf',
                                           variable=new_bedarf,
                                           text=f'Okay, ich habe {bedarf} abgespeichert.',
                                           chips=["Weiter: Interessenselektor", "Menü"])
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
                                   text=f'Okay, ich habe deinen Bedarf {bedarf} abgespeichert.'
                                        f'Willst du weitere Bedarfe angeben?',
                                   chips=["Ja", "Nein, weiter: Interessenselektor", "Menü"])


def show_full_event_list(output_contexts, session_id):
    event_count, events = retrieve_found_events(output_contexts)
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
        return chip_w_context_response(session_id=session_id,
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
        session_id=session_id,
        context='event_index',
        variable_name='event_index',
        variable=next_event_index,
        display_num=display_num,
        display_index=event_index,
        events=events,
        chips=chips
    )

def map_bedarf_for_db(bedarf=None):
    accessibilities = get_accessibility_ids()
    codes = []
    if bedarf:
        if bedarf == [1.0, 0.0, 0.0, 0.0, 0.0, 0.0] or \
                bedarf == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:
            codes = None
            print('No special accessibility need detected ')
        else:
            # if bedarf[0] == 1: # kein Bedarf
            #    events = get_event_names_w_access()
            if bedarf[1] == 1.0:  # leichte Sprache
                codes.append(accessibilities['Leichte Sprache'])
            if bedarf[2] == 1.0:  # Höreinschränkung
                codes.append(accessibilities[
                                 'Induktions·schleife [Eine Induktions·schleife ist für schwerhörige Menschen. '
                                 'Sie können den Ton der Veranstaltung dann direkt in ihrem Hör·gerät hören.]'])
                codes.append(accessibilities['Audiodeskription'])
                codes.append(accessibilities['Übersetzung in Gebärden·sprache'])
            if bedarf[3] == 1.0:  # Mobilitätseinschränkung
                codes.append(accessibilities['Rollstuhl'])
                codes.append(accessibilities['Geh·behinderung/ Aufzüge'])
            if bedarf[4] == 1.0:  # Visuelle Einschränkung
                codes.append(accessibilities['Fühl-Tour'])
                codes.append(accessibilities['Unter·titel/ Ober·titel'])
                codes.append(accessibilities['Seh·behinderung/ Seh·schwäche'])
            # if bedarf[5] == 1.0:  # begrenzte Reize
            # codes.append(accessibilities['Leichte Sprache'])
    return codes


def order_events_by_interest(interests, events=None, event_count=None):
    """
    bekommt einen interessenarray mit ints: [0,1,1,1,0,0,1,0,0]
    muss similarity score errechnen mit events[i]['interests'] und dann liste sortieren nach highest score

    Names of the entities from DB: BODIES, LIFE, RITUALS, POETRY, UTOPIA, SOCIETY, NATURE, NONACTIVE, FUNNY
    :param interests: array with 9 ints
    :param events: list of events
    :param event_count: number of elements in events
    :return: events list, but sorted according to interest
    """
    # TODO:

    ordered_events = []

    for event in events:
        # if event['interests'] ==
        print(event)

    return event_count, ordered_events
