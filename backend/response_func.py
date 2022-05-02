# responsible for defining what kind of responses can get sent by the backend

from copy import deepcopy  # needed for the copying of the sample jsons

from sample_jsons import SAMPLE_IMAGE_JSON, \
    SAMPLE_CHIP_JSON, \
    SAMPLE_TEXT_JSON, \
    SAMPLE_CONTEXT_JSON, \
    SAMPLE_CHIP_W_CONTEXT_JSON, \
    SAMPLE_EVENT_JSON_1, \
    SAMPLE_BUTTON_JSON, \
    SAMPLE_EVENT_SCHEDULE_JSON, \
    SAMPLE_EVENT_DETAILS_JSON


# load in the prototype jsons


# sends a text response, takes an optional array of suggestion chips
def chip_response(text=None, chips=None):
    resp = deepcopy(SAMPLE_CHIP_JSON)
    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text
    if chips:
        resp['fulfillmentMessages'][1]['payload']['richContent'][0][0]['options'] = [{'text': i} for i in chips]
    return resp


def text_response(text=None):
    resp = deepcopy(SAMPLE_TEXT_JSON)
    if text:
        resp['fulfillmentText'] = text
    return resp


def context_response(session_id, context, lifespan=50, variable_name=None, variable=None):
    resp = deepcopy(SAMPLE_CONTEXT_JSON)
    if session_id:
        resp['outputContexts'][0]['name'] = 'projects/kommkrake-pcsi/locations/global/agent/sessions/' + str(
            session_id) + '/contexts/' + str(context)
        if variable_name:
            resp['outputContexts'][0]['parameters'][variable_name] = variable
        if lifespan:
            resp['outputContexts'][0]['lifespanCount'] = lifespan
    return resp


def chip_w_context_response(session_id, context, lifespan=50, text=None, chips=None, variable_name=None, variable=None):
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
    return resp


# sends a single image, along with optional text, a title, alt text and some chips
def image_response(url, text=None, title='', subtitle='', chips=None):
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
    return resp


def event_response(session_id,
                   context,
                   display_num,
                   event_count,
                   events,
                   display_index,
                   lifespan=50,
                   chips=None,
                   text=None,
                   variable_name=None,
                   variable=None):
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
            subline = subline + ' Nächstes Datum: ' + events.get(str(e))['next_date'] + '\r\n'
        if subline:
            resp['fulfillmentMessages'][1]['payload']['richContent'][i][1]['subtitle'] = subline
        if events.get(str(e))['event_images']:
            resp['fulfillmentMessages'][1]['payload']['richContent'][i][0]['rawUrl'] = events.get(str(e))[
                'event_images']
        description = ''
        if events.get(str(e))['duration']:
            description = description + 'Spieldauer: ' + str(events.get(str(e))['duration']) + ' Minuten' + '\r\n'
        if events.get(str(e))['location']:
            description = description + 'Spielort: ' + str(events.get(str(e))['location']) + '\r\n'
        if events.get(str(e))['artist_name']:
            description = description + 'Künstler: ' + str(events.get(str(e))['artist_name']) + '\r\n'
        if events.get(str(e))['max_capacity']:
            description = description + 'Maximale Platzanzahl: ' + str(
                events.get(str(e))['max_capacity']) + '\r\n'
        if events.get(str(e))['info_text']:
            description = description + str(events.get(str(e))['info_text'])
        if events.get(str(e))['accessibility']:
            resp['fulfillmentMessages'][1]['payload']['richContent'][i][3]['title'] = 'Barrierefreiheit'
            accessibility = ''
            for j in range(len(events.get(str(e))['accessibility'])):
                accessibility = accessibility + str(events.get(str(e))['accessibility'][j]['name']) + '\r\n'
            resp['fulfillmentMessages'][1]['payload']['richContent'][i][3]['text'] = accessibility
        if description:
            resp['fulfillmentMessages'][1]['payload']['richContent'][i][2]['text'] = description
        sale_msg = 'Tickets hier kaufen' + '\r\n'
        if events.get(str(e))['price_vvk']:
            sale_msg = sale_msg + 'Preis: ' + str(events.get(str(e))['price_vvk']) + 'Euro ' + '\r\n'

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
    return resp


# sends a single Button, along with optional text and some chips
def button_response(url, button_text, text=None, chips=None):
    resp = deepcopy(SAMPLE_BUTTON_JSON)
    resp['fulfillmentMessages'][1]['payload']['richContent'][0][0]['link'] = url
    resp['fulfillmentMessages'][1]['payload']['richContent'][0][0]['text'] = button_text
    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text
    if chips:
        resp['fulfillmentMessages'][1]['payload']['richContent'][0][1]['options'] = [{'text': i} for i in chips]
    return resp


# sends a single Button, along with optional text and some chips
def event_detail_response(title, duration, location, price, image, text=None, chips=None):
    event_details = {}
    event_details['title'] = title
    event_details['duration'] = duration
    event_details['location'] = location
    event_details['price'] = price
    event_details['image'] = image

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
    return resp


# sends a single Button, along with optional text and some chips
def event_schedule_response(play_count, plays, text=None, chips=None):
    resp = deepcopy(SAMPLE_EVENT_SCHEDULE_JSON)
    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text

    # send out entire play schedule to be visible in frontend
    resp['fulfillmentMessages'][1]['payload']['plays'] = plays

    for i in range(play_count):
        accessible_request = plays[i]['accessible_request']
        # print(accessible_request)
        accessible_for = ''
        for j in range(len(accessible_request)):
            accessible_for = accessible_for + str(accessible_request[j].get('name')) + '\r\n'
        # print(accessible_for)

        date = plays[i]['date']
        end_date = plays[i]['end_date']
        play_id = plays[i]['id']
        location = plays[i]['location']
        opening_time = plays[i]['opening_time']
        ticket_link = plays[i]['ticket_link']
        additional_title = plays[i]['additional_title']

        resp['fulfillmentMessages'][1]['payload']['richContent'].append([{
            "type": "info",
            "title": date,
            "subtitle": accessible_for,  # accessible_request,
            "image": {"src": {"rawUrl": "https://example.com/images/logo.png"}},
            "actionLink": ticket_link}], )

    if chips:
        resp['fulfillmentMessages'][1]['payload']['richContent'].append([{"type": "chips",
                                                                          "options": [{'text': i} for i in chips]
                                                                          }])
    return resp
