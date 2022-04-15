# responsible for defining what kind of responses can get sent by the backend

from copy import deepcopy  # needed for the copying of the sample jsons
from sample_jsons import SAMPLE_RESPONSE_JSON, SAMPLE_IMAGE_JSON, SAMPLE_CHIP_JSON  # load in the prototype jsons


# sends a text response, takes an optional array of suggestion chips
def standard_response(text, suggestions=None):
    resp = deepcopy(SAMPLE_RESPONSE_JSON)
    resp['payload']['google']['richResponse']['items'][0]['simpleResponse']['textToSpeech'] = text
    if suggestions:
        resp['payload']['google']['richResponse']['suggestions'] = [{'title': i} for i in suggestions]
    return resp


# sends a single image, along with optional text, a title, alt text and some chips
def image_response(imgpath, textresponse='Here is your image', title='', accessibilitytext='', suggestions=None):
    resp = deepcopy(SAMPLE_IMAGE_JSON)
    resp['richContent']['PLATFORM_UNSPECIFIED']['richResponse']['items'][1]['basicCard']['image']['url'] = imgpath
    if textresponse:
        resp['payload']['PLATFORM_UNSPECIFIED']['richResponse']['items'][0]['simpleResponse'][
            'textToSpeech'] = textresponse
    if title:
        resp['payload']['PLATFORM_UNSPECIFIED']['richResponse']['items'][1]['basicCard']['title'] = title
    if accessibilitytext:
        resp['payload']['PLATFORM_UNSPECIFIED']['richResponse']['items'][1]['basicCard'][
            'accessibilityText'] = accessibilitytext
    if suggestions:
        resp['payload']['google']['richResponse']['suggestions'] = [{'title': i} for i in suggestions]
    return resp


def chip_response(text = None, chips = None):
    resp = deepcopy(SAMPLE_CHIP_JSON)
    if text:
        resp['fulfillmentText'] = text
    if chips:
        resp['fulfillmentMessages'][0]['payload']['richContent'][0][0]['options'] = [{'text': i} for i in chips]
    return resp


def img_resp():
    resp = deepcopy(SAMPLE_IMAGE_JSON)
    return resp
