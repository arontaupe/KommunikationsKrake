# responsible for defining what kind of responses can get sent by the backend

from copy import deepcopy  # needed for the copying of the sample jsons
from sample_jsons import SAMPLE_IMAGE_JSON, SAMPLE_CHIP_JSON, SAMPLE_TEXT_JSON, SAMPLE_CONTEXT_JSON, SAMPLE_CHIP_W_CONTEXT_JSON  # load in the prototype jsons


# sends a text response, takes an optional array of suggestion chips
def chip_response(text = None, chips = None):
    resp = deepcopy(SAMPLE_CHIP_JSON)
    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text
    if chips:
        resp['fulfillmentMessages'][1]['payload']['richContent'][0][0]['options'] = [{'text': i} for i in chips]
    return resp


def text_response(text = None):
    resp = deepcopy(SAMPLE_TEXT_JSON)
    if text:
        resp['fulfillmentText'] = text
    return resp

def context_response(session_id, context, variable_name = None, variable = None):
    resp = deepcopy(SAMPLE_CONTEXT_JSON)
    if session_id:
        resp['outputContexts'][0]['name'] = 'projects/kommkrake-pcsi/locations/global/agent/sessions/' + str(session_id) + '/contexts/' + str(context)
        if variable_name:
            resp['outputContexts'][0]['parameters'][variable_name] = variable
    return resp

def chip_w_context_response(session_id, context, text = None, chips = None, variable_name = None, variable = None):
    resp = deepcopy(SAMPLE_CHIP_W_CONTEXT_JSON)
    if text:
        resp['fulfillmentMessages'][0]['text']['text'][0] = text
    if chips:
        resp['fulfillmentMessages'][1]['payload']['richContent'][0][0]['options'] = [{'text': i} for i in chips]
    if session_id:
        resp['outputContexts'][0]['name'] = 'projects/kommkrake-pcsi/locations/global/agent/sessions/' + str(session_id) + '/contexts/' + str(context)
        if variable_name:
            resp['outputContexts'][0]['parameters'][variable_name] = variable
    return resp


# sends a single image, along with optional text, a title, alt text and some chips
def image_response(url, text = None, title = '', subtitle = '', chips = None):
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