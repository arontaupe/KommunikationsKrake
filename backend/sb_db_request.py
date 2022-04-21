# import dependencies for database request
import requests
from requests.auth import HTTPBasicAuth  # die datenbank läuft über basic auth
import json  # make me interact with json

# import the response functionality
from response_func import chip_response, image_response
import os

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
    response = requests.get(url, auth=HTTPBasicAuth(DB_USER,DB_PASS))
    print('Request: ' + str(response.url))
    print('Status Code: ' + str(response.status_code))  # response 200 := success. all 400eds:= really bad
    accessibilities = {}
    resp = response.json()
    num_categories = len(resp)
    for i in range(num_categories):
        accessibilities[resp[i]['name']] = resp[i]['id']
    print(accessibilities)
    return accessibilities


def get_event_names_w_access(accessibility = None):
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

