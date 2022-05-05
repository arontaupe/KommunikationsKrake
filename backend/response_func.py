# responsible for defining what kind of responses can get sent by the backend

from copy import deepcopy  # needed for the copying of the sample jsons
# load in the prototype jsons
from sample_jsons import SAMPLE_IMAGE_JSON, \
    SAMPLE_CHIP_JSON, \
    SAMPLE_TEXT_JSON, \
    SAMPLE_CONTEXT_JSON, \
    SAMPLE_CHIP_W_CONTEXT_JSON, \
    SAMPLE_EVENT_JSON_1, \
    SAMPLE_BUTTON_JSON, \
    SAMPLE_EVENT_SCHEDULE_JSON, \
    SAMPLE_EVENT_DETAILS_JSON
import datetime

def chip_response(text=None,
                  chips=None,
                  dgs_videos_bot=None,
                  dgs_videos_chips=None):
    """
sends a text response, takes an optional array of suggestion chips
    :param text: the text that will be sent as message
    :param chips: the suggestion buttons: array of strings
    :param dgs_videos_bot:  the DGS videos displayed alongside the messages of the bot,
    has to be in format{str(title):str(url)}
    :param dgs_videos_chips: the DGS videos displayed alongside the response options from the user,
    has to be in format{str(title):str(url)}
    :return: json response object
    """
    resp = deepcopy(SAMPLE_CHIP_JSON)
    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text
    if chips:
        resp['fulfillmentMessages'][1]['payload']['richContent'][0][0]['options'] = [{'text': i} for i in chips]
    if dgs_videos_bot:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_bot'] = [{title: url} for title, url in
                                                                       dgs_videos_bot.items()]
    if dgs_videos_chips:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_chips'] = [{title: url} for title, url in
                                                                         dgs_videos_chips.items()]
    return resp


def text_response(text=None, dgs_videos_bot=None):
    """
this method sends a standard text response to the bot and can transport a dict of dgs_videos
    :param text: the text that will be sent as message
    :param dgs_videos_bot:  dict: for each text, there should be a youtube url with a title and equivalent content
has to be in format{str(title):str(url)}
    :return:  json response object
    """
    resp = deepcopy(SAMPLE_TEXT_JSON)
    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text
    if dgs_videos_bot:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos'] = [{title: url} for title, url in
                                                                   dgs_videos_bot.items()]
    return resp


def context_response(session_id, context, lifespan=50, variable_name=None, variable=None):
    """
sends no visible message, just saves variables in GDF, mostly used for testing
    :param session_id: the unique identifier for the agent. str
    :param context: name of the context where the variable is saved in GDF. str
    :param lifespan: int, the amount of interactions that a context variable will be preserved. defaults to 50
    :param variable_name: the key of the variable to be saved
    :param variable: the value of the variable to be saved
    :return: json response object
    """
    resp = deepcopy(SAMPLE_CONTEXT_JSON)
    if session_id:
        resp['outputContexts'][0]['name'] = 'projects/kommkrake-pcsi/locations/global/agent/sessions/' + str(
            session_id) + '/contexts/' + str(context)
        if variable_name:
            resp['outputContexts'][0]['parameters'][variable_name] = variable
        if lifespan:
            resp['outputContexts'][0]['lifespanCount'] = lifespan
    return resp


def chip_w_context_response(session_id,
                            context,
                            lifespan=50,
                            text=None,
                            chips=None,
                            variable_name=None,
                            variable=None,
                            dgs_videos_bot=None,
                            dgs_videos_chips=None):
    """
can send optional text, some chips and save a context variable
    :param session_id: the unique identifier for the agent. str
    :param context: name of the context where the variable is saved in GDF. str
    :param lifespan: int, the amount of interactions that a context variable will be preserved. defaults to 50
    :param variable_name: the key of the variable to be saved
    :param variable: the value of the variable to be saved
    :param text: the text that will be sent as message
    :param chips: the suggestion buttons: array of strings
    :param dgs_videos_bot:  the DGS videos displayed alongside the messages of the bot,
    has to be in format{str(title):str(url)}
    :param dgs_videos_chips: the DGS videos displayed alongside the response options from the user,
    has to be in format{str(title):str(url)}
    :return: json response object
    :return:
    """
    resp = deepcopy(SAMPLE_CHIP_W_CONTEXT_JSON)
    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text
    if chips:
        resp['fulfillmentMessages'][1]['payload']['richContent'][0][0]['options'] = [{'text': i} for i in chips]
    if session_id:
        resp['outputContexts'][0]['name'] = 'projects/kommkrake-pcsi/locations/global/agent/sessions/' + str(
            session_id) + '/contexts/' + str(context)
        if variable_name:
            resp['outputContexts'][0]['parameters'][variable_name] = variable
        if lifespan:
            resp['outputContexts'][0]['lifespanCount'] = lifespan
    if dgs_videos_bot:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_bot'] = [{title: url} for title, url in
                                                                       dgs_videos_bot.items()]
    if dgs_videos_chips:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_chips'] = [{title: url} for title, url in
                                                                         dgs_videos_chips.items()]
    return resp


# sends a single image, along with optional text, a title, alt text and some chips
def image_response(url,
                   text=None,
                   title='',
                   subtitle='',
                   chips=None,
                   dgs_videos_bot=None,
                   dgs_videos_chips=None):
    """
sends an image along with text and chips to the user
    :param url: string, is hopefully a valid image url
    :param title: displayed as title in response, string
    :param subtitle: displayed as subtitle in response, string
    :param text: the text that will be sent as message
    :param chips: the suggestion buttons: array of strings
    :param dgs_videos_bot:  the DGS videos displayed alongside the messages of the bot,
    has to be in format{str(title):str(url)}
    :param dgs_videos_chips: the DGS videos displayed alongside the response options from the user,
    has to be in format{str(title):str(url)}
    :return: json response object
    """
    resp = deepcopy(SAMPLE_IMAGE_JSON)
    resp['fulfillmentMessages'][1]['payload']['richContent'][0][0]['rawUrl'] = url
    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text
    if title:
        resp['fulfillmentMessages'][1]['payload']['richContent'][0][1]['title'] = title
    if subtitle:
        resp['fulfillmentMessages'][1]['payload']['richContent'][0][1]['subtitle'] = subtitle
    if chips:
        resp['fulfillmentMessages'][1]['payload']['richContent'][0][2]['options'] = [{'text': i} for i in chips]
    if dgs_videos_bot:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_bot'] = [{title: url} for title, url in
                                                                       dgs_videos_bot.items()]
    if dgs_videos_chips:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_chips'] = [{title: url} for title, url in
                                                                         dgs_videos_chips.items()]
    return resp


def event_response(session_id,
                   context,
                   display_num,
                   events,
                   display_index,
                   lifespan=50,
                   chips=None,
                   text=None,
                   variable_name=None,
                   variable=None,
                   dgs_videos_bot=None,
                   dgs_videos_chips=None):
    """
sends a response card displaying one event from the array of events according to the display index param
    :param session_id: the unique identifier for the agent. str
    :param display_num: Number of events to show. currently modified to only support one event
    :param events: array of found_events
    :param display_index:
    :param context: name of the context where the variable is saved in GDF. str
    :param lifespan: int, the amount of interactions that a context variable will be preserved. defaults to 50
    :param variable_name: the key of the variable to be saved
    :param variable: the value of the variable to be saved
    :param text: the text that will be sent as message
    :param chips: the suggestion buttons: array of strings
    :param dgs_videos_bot:  the DGS videos displayed alongside the messages of the bot,
    has to be in format{str(title):str(url)}
    :param dgs_videos_chips: the DGS videos displayed alongside the response options from the user,
    has to be in format{str(title):str(url)}
    :return: json response object
    """
    resp = deepcopy(SAMPLE_EVENT_JSON_1)
    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text
    if events:
        i = 0
        e = display_index
        # send out entire event to be visible in frontend
        resp['fulfillmentMessages'][1]['payload']['event'] = events.get(str(e))

        # fill my card
        resp['fulfillmentMessages'][1]['payload']['richContent'][i][1]['title'] = events.get(str(e))['title']
        subline = ''
        if events.get(str(e))['subtitle']:
            subline = subline + events.get(str(e))['subtitle'] + '\r\n'
        if events.get(str(e))['next_date']:
            next_date = events.get(str(e))['next_date']
            subline = subline + f' Nächstes Datum: {next_date}\r\n'
            # print(next_date)
            # date = datetime.datetime.strptime(next_date, '%Y-%m-%dT%X')
            # print(date)
        if events.get(str(e))['duration']:
            subline = subline + 'Spieldauer: ' + str(events.get(str(e))['duration']) + ' Minuten' + '\r\n'
        if events.get(str(e))['location']:
            subline = subline + 'Spielort: ' + str(events.get(str(e))['location']) + '\r\n'
        if events.get(str(e))['artist_name']:
            subline = subline + 'Künstler: ' + str(events.get(str(e))['artist_name']) + '\r\n'
        if events.get(str(e))['max_capacity']:
            subline = subline + 'Maximale Platzanzahl: ' + str(
                events.get(str(e))['max_capacity']) + '\r\n'
        resp['fulfillmentMessages'][1]['payload']['richContent'][i][1]['subtitle'] = subline
        if events.get(str(e))['event_images']:
            resp['fulfillmentMessages'][1]['payload']['richContent'][i][0]['rawUrl'] = events.get(str(e))[
                'event_images']

        description = ''
        if events.get(str(e))['short_description']:
            description = description + str(events.get(str(e))['short_description'])
        if events.get(str(e))['accessibility']:
            resp['fulfillmentMessages'][1]['payload']['richContent'][i][3]['title'] = 'Barrierefreiheit'
            accessibility = ''
            for j in range(len(events.get(str(e))['accessibility'])):
                access_name = events.get(str(e))['accessibility'][j]['name']
                accessibility += f'{access_name} \r\n '
            resp['fulfillmentMessages'][1]['payload']['richContent'][i][3]['text'] = accessibility

        if description:
            resp['fulfillmentMessages'][1]['payload']['richContent'][i][2]['text'] = description
        sale_msg = 'Tickets hier kaufen \r\n'
        if events.get(str(e))['price_vvk']:
            sale_msg = sale_msg + 'Preis: ' + str(int(events.get(str(e))['price_vvk'])) + ' Euro ' + '\r\n'

        resp['fulfillmentMessages'][1]['payload']['richContent'][i][4]['text'] = sale_msg + '\r\n'
        resp['fulfillmentMessages'][1]['payload']['richContent'][i][4]['link'] = events.get(str(e))[
            'ticket_link']
        resp['fulfillmentMessages'][1]['payload']['richContent'][i][2]['title'] = 'Kurzbeschreibung'

    if chips:
        resp['fulfillmentMessages'][1]['payload']['richContent'][display_num][0]['options'] = [{'text': i} for i in
                                                                                               chips]
    if session_id:
        resp['outputContexts'][0]['name'] = 'projects/kommkrake-pcsi/locations/global/agent/sessions/' + str(
            session_id) + '/contexts/' + str(context)
        if variable_name:
            resp['outputContexts'][0]['parameters'][variable_name] = variable
        if lifespan:
            resp['outputContexts'][0]['lifespanCount'] = lifespan
    if dgs_videos_bot:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_bot'] = [{title: url} for title, url in
                                                                       dgs_videos_bot.items()]
    if dgs_videos_chips:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_chips'] = [{title: url} for title, url in
                                                                         dgs_videos_chips.items()]
    return resp


def button_response(url,
                    button_text,
                    text=None,
                    chips=None,
                    dgs_videos_bot=None,
                    dgs_videos_chips=None):
    """
sends a clickable button that can link out
    :param url:
    :param button_text:
    :param text: the text that will be sent as message
    :param chips: the suggestion buttons: array of strings
    :param dgs_videos_bot:  the DGS videos displayed alongside the messages of the bot,
    has to be in format{str(title):str(url)}
    :param dgs_videos_chips: the DGS videos displayed alongside the response options from the user,
    has to be in format{str(title):str(url)}
    :return: json response object
    """
    resp = deepcopy(SAMPLE_BUTTON_JSON)
    resp['fulfillmentMessages'][1]['payload']['richContent'][0][0]['link'] = url
    resp['fulfillmentMessages'][1]['payload']['richContent'][0][0]['text'] = button_text
    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text
    if chips:
        resp['fulfillmentMessages'][1]['payload']['richContent'][0][1]['options'] = [{'text': i} for i in chips]
    if dgs_videos_bot:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_bot'] = [{title: url} for title, url in
                                                                       dgs_videos_bot.items()]
    if dgs_videos_chips:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_chips'] = [{title: url} for title, url in
                                                                         dgs_videos_chips.items()]
    return resp


def event_detail_response(title,
                          duration,
                          location,
                          price,
                          image,
                          text=None,
                          chips=None,
                          dgs_videos_bot=None,
                          dgs_videos_chips=None):
    """
sends out a card with more info on a specific event
    :param title:
    :param duration:
    :param location:
    :param price:
    :param image:
    :param text: the text that will be sent as message
    :param chips: the suggestion buttons: array of strings
    :param dgs_videos_bot:  the DGS videos displayed alongside the messages of the bot,
    has to be in format{str(title):str(url)}
    :param dgs_videos_chips: the DGS videos displayed alongside the response options from the user,
    has to be in format{str(title):str(url)}
    :return: json response object
    """
    event_details = {'title': title, 'duration': duration, 'location': location, 'price': price, 'image': image}

    resp = deepcopy(SAMPLE_EVENT_DETAILS_JSON)

    resp['fulfillmentMessages'][1]['payload']['event_details'] = event_details
    resp['fulfillmentMessages'][1]['payload']['richContent'].append([{
        "type": "info",
        "title": title,
        "subtitle": location + '\r\n € ' + str(price),  # accessible_request,
        "image": {"src": {"rawUrl": image}},
        "actionLink": ""}], )

    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text
    if chips:
        resp['fulfillmentMessages'][1]['payload']['richContent'].append([{"type": "chips",
                                                                          "options": [{'text': i} for i in chips]
                                                                          }])
    if dgs_videos_bot:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_bot'] = [{title: url} for title, url in
                                                                       dgs_videos_bot.items()]
    if dgs_videos_chips:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_chips'] = [{title: url} for title, url in
                                                                         dgs_videos_chips.items()]
    return resp


def event_schedule_response(play_count,
                            plays,
                            text=None,
                            chips=None,
                            dgs_videos_bot=None,
                            dgs_videos_chips=None):
    """
sends out a card for each scheduled play the currently selected event has
    :param play_count:
    :param plays:
    :param text: the text that will be sent as message
    :param chips: the suggestion buttons: array of strings
    :param dgs_videos_bot:  the DGS videos displayed alongside the messages of the bot,
    has to be in format{str(title):str(url)}
    :param dgs_videos_chips: the DGS videos displayed alongside the response options from the user,
    has to be in format{str(title):str(url)}
    :return: json response object
    """
    resp = deepcopy(SAMPLE_EVENT_SCHEDULE_JSON)
    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text

    # send out entire play schedule to be visible in frontend
    resp['fulfillmentMessages'][1]['payload']['plays'] = plays

    for i in range(play_count):
        accessible_request = plays[i]['accessible_request']
        accessible_for = ''
        for j in range(len(accessible_request)):
            accessible_for = accessible_for + str(accessible_request[j].get('name')) + '\r\n'
        date = plays[i]['date']
        end_date = plays[i]['end_date']
        play_id = plays[i]['id']
        location = plays[i]['location']
        opening_time = plays[i]['opening_time']
        ticket_link = plays[i]['ticket_link']
        additional_title = plays[i]['additional_title']

        resp['fulfillmentMessages'][1]['payload']['richContent'].append([{
            "type": "info",
            "title": f'Datum: {date}, \r\n Uhrzeit: {opening_time}',
            "subtitle": f'Barrierefreiheitsinfo: {accessible_for}',  # accessible_request,
            "image": {"src": {"rawUrl": "https://example.com/images/logo.png"}},
            "actionLink": ticket_link}], )
    if chips:
        resp['fulfillmentMessages'][1]['payload']['richContent'].append([{"type": "chips",
                                                                          "options": [{'text': i} for i in chips]
                                                                          }])
    if dgs_videos_bot:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_bot'] = [{title: url} for title, url in
                                                                       dgs_videos_bot.items()]
    if dgs_videos_chips:
        resp['fulfillmentMessages'][1]['payload']['dgs_videos_chips'] = [{title: url} for title, url in
                                                                         dgs_videos_chips.items()]
    return resp
