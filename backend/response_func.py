# responsible for defining what kind of responses can get sent by the backend

from copy import deepcopy # needed for the copying of the sample jsons
from sample_jsons import SAMPLE_PAYLOAD_JSON, SAMPLE_RESPONSE_JSON, SAMPLE_IMAGE_JSON, SAMPLE_LIST_JSON, \
    SAMPLE_LISTITEM_JSON_SHORT # load in the prototype jsons

# sends a text response, takes an optional array of suggestion chips
def standard_response(text, suggestions=None):
    resp = deepcopy(SAMPLE_RESPONSE_JSON)
    resp['payload']['google']['richResponse']['items'][0]['simpleResponse']['textToSpeech'] = text
    if suggestions:
        resp['payload']['google']['richResponse']['suggestions'] = [{'title': i} for i in suggestions]
    return resp

# sends a single image, along with optional text, a title, alt text and some chips
def image_response(imgpath, textresponse='Here is your image', title='', accessibilitytext='', suggestions=None):
    resp = SAMPLE_IMAGE_JSON
    resp['payload']['google']['richResponse']['items'][1]['basicCard']['image']['url'] = imgpath
    if textresponse:
        resp['payload']['google']['richResponse']['items'][0]['simpleResponse']['textToSpeech'] = textresponse
    if title:
        resp['payload']['google']['richResponse']['items'][1]['basicCard']['title'] = title
    if accessibilitytext:
        resp['payload']['google']['richResponse']['items'][1]['basicCard']['accessibilityText'] = accessibilitytext
    if suggestions:
        resp['payload']['google']['richResponse']['suggestions'] = [{'title': i} for i in suggestions]
    return resp