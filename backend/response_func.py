# responsible for defining what kind of responses can get sent by the backend

from copy import deepcopy  # needed for the copying of the sample jsons

from sample_jsons import SAMPLE_IMAGE_JSON, \
    SAMPLE_CHIP_JSON, \
    SAMPLE_TEXT_JSON, \
    SAMPLE_CONTEXT_JSON, \
    SAMPLE_CHIP_W_CONTEXT_JSON, \
    SAMPLE_EVENT_JSON_1, SAMPLE_EVENT_JSON_2, SAMPLE_EVENT_JSON_3  # load in the prototype jsons


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


def context_response(session_id, context, variable_name=None, variable=None):
    resp = deepcopy(SAMPLE_CONTEXT_JSON)
    if session_id:
        resp['outputContexts'][0]['name'] = 'projects/kommkrake-pcsi/locations/global/agent/sessions/' + str(
            session_id) + '/contexts/' + str(context)
        if variable_name:
            resp['outputContexts'][0]['parameters'][variable_name] = variable
    return resp


def chip_w_context_response(session_id, context, text=None, chips=None, variable_name=None, variable=None):
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
                   chips=None,
                   text=None,
                   variable_name=None,
                   variable=None):
    if display_num == 3:
        resp = deepcopy(SAMPLE_EVENT_JSON_3)
    elif display_num == 2:
        resp = deepcopy(SAMPLE_EVENT_JSON_2)
    elif display_num == 1:
        resp = deepcopy(SAMPLE_EVENT_JSON_1)
    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text
    if events:
        for i in range(display_num):
            if display_index:
                e = i + display_index
            else:
                e = i
            resp['fulfillmentMessages'][1]['payload']['richContent'][i][1]['title'] = events.get(str(e))['title']
            subline = ''
            if events.get(str(e))['subtitle']:
                subline = subline + events.get(str(e))['subtitle']
            if events.get(str(e))['next_date']:
                subline = subline + ' Nächstes Datum: ' + events.get(str(e))['next_date']
            if subline:
                resp['fulfillmentMessages'][1]['payload']['richContent'][i][1]['subtitle'] = subline
            if events.get(str(e))['event_images']:
                resp['fulfillmentMessages'][1]['payload']['richContent'][i][0]['rawUrl'] = events.get(str(e))[
                    'event_images']
            description = ''
            if events.get(str(e))['duration']:
                description = description + 'Spieldauer: ' + str(events.get(str(e))['duration']) + ' Minuten' + '\n'
            if events.get(str(e))['location']:
                description = description + 'Spielort: ' + str(events.get(str(e))['location']) + '\n'
            if events.get(str(e))['artist_name']:
                description = description + 'Künstler: ' + str(events.get(str(e))['artist_name']) + '\n'
            if events.get(str(e))['max_capacity']:
                description = description + 'Maximale Platzanzahl: ' + str(
                    events.get(str(e))['max_capacity']) + '\n'
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
            sale_msg = 'Tickets hier kaufen'
            if events.get(str(e))['price_vvk']:
                sale_msg = sale_msg + 'Preis: ' + str(events.get(str(e))['price_vvk']) + 'Euro \n'

            resp['fulfillmentMessages'][1]['payload']['richContent'][i][4]['text'] = sale_msg
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
    # else return ful
    return resp
