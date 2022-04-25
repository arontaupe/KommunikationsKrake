# import dependencies for database request
import json
import os

import requests
from requests.auth import HTTPBasicAuth  # die datenbank läuft über basic auth

# import the response functionality
from response_func import chip_response

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
BASEURL = os.environ.get('BASEURL')


# makes sure the webhook is online and working
def test_sb_db():
    """
    Used for testing whether the SB DB is reachable
    :return: Response to DF and the Response Code
    """
    url = BASEURL + "/api/accessibilities.json"
    response = requests.get(url, auth=HTTPBasicAuth(DB_USER, DB_PASS))
    print('Request: ' + str(response.url))
    print('Status Code: ' + str(response.status_code))  # response 200 := success. all 400eds:= really bad
    # print('Headers')
    # print(response.headers)
    # print(response.json())
    return chip_response('Status der Datenbank: ' + str(response.status_code), ['Menü', 'Exit'])


def get_accessibility_ids():
    """
    :return: all accessibility classes and their ID as a dict
    """
    url = BASEURL + "/api/accessibilities.json"
    response = requests.get(url, auth=HTTPBasicAuth(DB_USER, DB_PASS))
    print('Request: ' + str(response.url))
    print('Status Code: ' + str(response.status_code))  # response 200 := success. all 400eds:= really bad
    accessibilities = {}
    resp = response.json()
    num_categories = len(resp)
    for i in range(num_categories):
        accessibilities[resp[i]['name']] = resp[i]['id']
    print(accessibilities)
    return accessibilities


def get_event_names_w_access(accessibility=None):
    """
    gets an accesibility code and returns all event names fulfilling the accessibility in an array.
    :param accessibility: numeric id 0-9
    :return: json with list of all events fulfilling the accessibility
    """
    query = '?entries=30'
    if accessibility:
        query = query + '?accessible=' + str(accessibility)
    suburl = "/api/events.json"
    url = BASEURL + suburl + query
    response = requests.get(url, auth=HTTPBasicAuth(DB_USER, DB_PASS))
    print('Query: ' + str(url))
    print('Response from: ' + str(response.url))
    print('Status Code: ' + str(response.status_code))
    # print(response.json())
    resp = response.json()
    event_count = resp['count']
    print('Number of Events Found: ' + str(event_count))
    events = {}

    for i in range(event_count):
        events[resp['items'][i]['title']] = resp['items'][i]['id']
    print(events)
    return event_count, events


def get_full_event_list(accessibility=None):
    """
    should get the full info to display on the cards later
    :param accessibility: numeric id 0-9
    :return: json with list of all events fulfilling the accessibility
    """
    query = '?entries=30'
    if accessibility:
        query = query + '?accessible=' + str(accessibility)
    suburl = "/api/events.json"
    url = BASEURL + suburl + query
    response = requests.get(url, auth=HTTPBasicAuth(DB_USER, DB_PASS))
    print('Query: ' + str(url))
    print('Response from: ' + str(response.url))
    print('Status Code: ' + str(response.status_code))
    resp = response.json()
    event_count = resp['count']
    print('Number of Events Found: ' + str(event_count))
    events = {}

    for i in range(event_count):
        events[i] = {}
        events[i]['id'] = resp['items'][i]['id']
        events[i]['title'] = resp['items'][i]['title']
        events[i]['next_date'] = resp['items'][i]['next_date']['isdate']
        events[i]['duration'] = resp['items'][i]['duration_minutes']
        events[i]['location'] = resp['items'][i]['location']['name']
        events[i]['artist_name'] = resp['items'][i]['artist_name']
        events[i]['info_text'] = resp['items'][i]['info_text']
        events[i]['subtitle'] = resp['items'][i]['subtitle']
        events[i]['ticket_link'] = resp['items'][i]['ticket_link']
        events[i]['price_vvk'] = resp['items'][i]['price_vvk']
        events[i]['price_ak'] = resp['items'][i]['price_ak']
        events[i]['max_capacity'] = resp['items'][i]['max_capacity']
        # somehow the DB response is broken here, therefore some steps to fix that.
        image_json = resp['items'][i]['event_images']
        # print(image_json)
        parsed = json.loads(image_json)
        image = parsed['mainimage']['name']
        events[i]['event_images'] = 'https://datenbank.sommerblut.de/media/images/normal/' + str(image)
        events[i]['accessibility'] = resp['items'][i]['accessible_request_sommerblut']

    # print(events)

    return event_count, events


def get_event_w_id(id):
    """
gets an event and all attached info by supplying the numeric id
    :param id: event id, int
    :return: the event and important variables
    """
    suburl = '/api/events/' + str(id) + '.json'
    url = BASEURL + suburl
    response = requests.get(url, auth=HTTPBasicAuth(DB_USER, DB_PASS))
    print('Status Code: ' + str(response.status_code))
    print('Response from: ' + str(response.url))
    title = response.json()['title']
    subtitle = response.json()['subtitle']
    duration = response.json()['duration_minutes']
    print('Title: ' + title)
    return response, title, subtitle, duration
