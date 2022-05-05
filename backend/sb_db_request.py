from __future__ import print_function

import json
import os
from pprint import pprint

from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth  # die datenbank läuft über basic auth

from retrieve_from_gdf import retrieve_bedarf

# import dependencies for database request# import dependencies for database request
import sb_db  # sommerblut datenbank openapi
# import the response functionality
from response_func import chip_response
from sb_db.rest import ApiException

# Configure HTTP basic authorization: basicAuth
configuration = sb_db.Configuration()
configuration.username = DB_USER = os.environ.get('DB_USER')
configuration.password = DB_PASS = os.environ.get('DB_PASS')
BASEURL = os.environ.get('BASEURL')

# create an instance of the API class
accessibilities_api = sb_db.AccessibilitiesApi(sb_db.ApiClient(configuration))
event_api = sb_db.EventsApi(sb_db.ApiClient(configuration))
running_events_api = sb_db.RunningEventsApi(sb_db.ApiClient(configuration))

accept_language = 'ls'  # str | request specific language (optional)


# makes sure the webhook is online and working
def test_sb_db():
    """
    Used for testing whether the SB DB is reachable
    :return: Response to DF and the Response Code
    """
    url = BASEURL + "/api/accessibilities.json"
    response = requests.get(url, auth=HTTPBasicAuth(DB_USER, DB_PASS))
    print('Status Code: ' + str(response.status_code))  # response 200 := success. all 400eds:= really bad

    return chip_response('Status der Datenbank: ' + str(response.status_code), ['Menü', 'Exit'])


def get_accessibility_ids():
    """
    :return: all accessibility classes and their ID as a dict
    """
    try:
        # get all accessibilities
        api_response = accessibilities_api.get_all_accessibilities(accept_language=accept_language)
    except ApiException as e:
        print("Exception when calling AccessibilitiesApi->get_all_accessibilities: %s\n" % e)

    accessibilities = {}
    # TODO clean up here, give back the original dict
    num_categories = len(api_response)
    for i in range(num_categories):
        accessibilities[api_response[i]['name']] = api_response[i]['id']
    # print(accessibilities)
    return accessibilities



def get_accessibility_ids_clean():
    """
    :return: all accessibility classes and their ID as a dict
    """
    try:
        # get all accessibilities
        api_response = accessibilities_api.get_all_accessibilities(accept_language=accept_language)
    except ApiException as e:
        print("Exception when calling AccessibilitiesApi->get_all_accessibilities: %s\n" % e)
    # print(api_response)
    return api_response


def get_events_by_name(event_name):
    """
seems to be broken on database side. would be cool if it worked tho
    :param event_name:
    :return:
    """
    try:
        # get a specific event by name
        api_response = event_api.get_events_by_name(event_name, accept_language=accept_language)
        # pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventApi->get_events_by_name: %s\n" % e)
    # TODO
    return api_response



def get_event_names_w_access(accessibility=None):
    """
    gets an accesibility code and returns all event names fulfilling the accessibility in an array.
    :param accessibility: numeric id 0-9
    :return: json with list of all events fulfilling the accessibility
    """

    query = '?entries=30'
    if accessibility:
        query = query + '&accessible=' + str(accessibility)
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
        events[resp['items'][i]['title']] = resp['items'][i]['id']
    return event_count, events


def get_full_event_list(accessibility=None):
    """
    should get the full info to display on the cards later
    :param accessibility: numeric id 0-9
    :return: json with list of all events fulfilling the accessibility
    """
    if accessibility:
        try:
            # get all events
            api_response = event_api.get_all_events(accessible=[accessibility],
                                                    accept_language=accept_language,
                                                    entries=30)
        except ApiException as e:
            print("Exception when calling EventsApi->get all events: %s\n" % e)
    else:
        try:
            # get all events
            api_response = event_api.get_all_events(accept_language=accept_language,
                                                    entries=30)
        except ApiException as e:
            print("Exception when calling EventsApi->get all events: %s\n" % e)

    resp = api_response
    event_count = resp['count']

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
        events[i]['accessible_request_sommerblut'] = resp['items'][i]['accessible_request_sommerblut']
        events[i]['category'] = resp['items'][i]['category']
        # somehow the DB response is broken here, therefore some steps to fix that.
        image_json = resp['items'][i]['event_images']
        parsed = json.loads(image_json)
        image = parsed['mainimage']['name']
        events[i]['event_images'] = 'https://datenbank.sommerblut.de/media/images/normal/' + str(image)
        events[i]['accessibility'] = resp['items'][i]['accessible_request_sommerblut']
        events[i]['program_content'] = resp['items'][i]['program_content']
        events[i]['short_description'] = resp['items'][i]['short_description']
        events[i]['health_infection_notice'] = None  # resp['items'][i]['health_infection_notice']
        events[i]['interest'] = None  # resp['items'][i]['interest']
        events[i]['accessible_other'] = None  # resp['items'][i]['accessible_other']
        events[i]['interest_ranking'] = None
    return event_count, events



def get_full_event_list_filtered(accessibility=None):
    """
    should get the full info to display on the cards later
    :param accessibility: numeric id 0-9
    :return: json with list of all events fulfilling the accessibility
    """

    if accessibility:
        try:
            # get all events
            api_response = event_api.get_all_events(accessible=[accessibility],
                                                    accept_language=accept_language,
                                                    entries=30)
        except ApiException as e:
            print("Exception when calling EventsApi->get all events: %s\n" % e)
    else:
        try:
            # get all events
            api_response = event_api.get_all_events(accept_language=accept_language,
                                                    entries=30)
        except ApiException as e:
            print("Exception when calling EventsApi->get all events: %s\n" % e)

    resp = api_response
    event_count = resp['count']

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
        events[i]['accessible_request_sommerblut'] = resp['items'][i]['accessible_request_sommerblut']
        events[i]['category'] = resp['items'][i]['category']
        # somehow the DB response is broken here, therefore some steps to fix that.
        image_json = resp['items'][i]['event_images']
        parsed = json.loads(image_json)
        image = parsed['mainimage']['name']
        events[i]['event_images'] = 'https://datenbank.sommerblut.de/media/images/normal/' + str(image)
        events[i]['accessibility'] = resp['items'][i]['accessible_request_sommerblut']
        events[i]['interests'] = None
        events[i]['interest_ranking'] = None
    return event_count, events


def get_partial_event_list(num_events=int, accessibility=None):
    """
    should get the full info to display on the cards later, but for a set amount of events
    :param accessibility: numeric id 0-9
    :return: json with list of all events fulfilling the accessibility
    """
    if accessibility:
        try:
            # get all events
            resp = event_api.get_all_events(accessible=[accessibility],
                                            accept_language=accept_language,
                                            entries=num_events)
        except ApiException as e:
            print("Exception when calling EventsApi->get all events: %s\n" % e)
    else:
        try:
            # get all events
            resp = event_api.get_all_events(accept_language=accept_language,
                                            entries=num_events)

        except ApiException as e:
            print("Exception when calling EventsApi->get all events: %s\n" % e)
    event_count = 0
    if num_events <= resp['count']:
        event_count = num_events
    else:
        event_count = resp['count']

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
        events[i]['accessible_request_sommerblut'] = resp['items'][i]['accessible_request_sommerblut']
        events[i]['category'] = resp['items'][i]['category']
        # somehow the DB response is broken here, therefore some steps to fix that.
        image_json = resp['items'][i]['event_images']
        parsed = json.loads(image_json)
        image = parsed['mainimage']['name']
        events[i]['event_images'] = 'https://datenbank.sommerblut.de/media/images/normal/' + str(image)
        events[i]['accessibility'] = resp['items'][i]['accessible_request_sommerblut']
        events[i]['program_content'] = resp['items'][i]['program_content']
        events[i]['short_description'] = resp['items'][i]['short_description']
        events[i]['health_infection_notice'] = None  # resp['items'][i]['health_infection_notice']
        events[i]['interest'] = None  # resp['items'][i]['interest']
        events[i]['accessible_other'] = None  # resp['items'][i]['accessible_other']
        events[i]['interest_ranking'] = None
    return event_count, events


def get_upcoming_event_list(accessibility=None):
    """
    get all upcoming events with accessibility
    :param accessibility: numeric id 0-9
    :return: json with list of all events fulfilling the accessibility
    """
    if accessibility:
        try:
            # get all events
            api_response = event_api.get_all_events(accessible=[accessibility],
                                                    accept_language=accept_language,
                                                    entries=30,
                                                    time=['upcoming'])
        except ApiException as e:
            print("Exception when calling EventsApi->get all upcoming events: %s\n" % e)
    else:
        try:
            # get all events
            api_response = event_api.get_all_events(accept_language=accept_language,
                                                    entries=30,
                                                    time=['upcoming'])
        except ApiException as e:
            print("Exception when calling EventsApi->get all upcoming events: %s\n" % e)

    resp = api_response
    event_count = resp['count']

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
        events[i]['accessible_request_sommerblut'] = resp['items'][i]['accessible_request_sommerblut']
        events[i]['category'] = resp['items'][i]['category']
        # somehow the DB response is broken here, therefore some steps to fix that.
        image_json = resp['items'][i]['event_images']
        parsed = json.loads(image_json)
        image = parsed['mainimage']['name']
        events[i]['event_images'] = 'https://datenbank.sommerblut.de/media/images/normal/' + str(image)
        events[i]['accessibility'] = resp['items'][i]['accessible_request_sommerblut']
        events[i]['program_content'] = resp['items'][i]['program_content']
        events[i]['short_description'] = resp['items'][i]['short_description']
        events[i]['health_infection_notice'] = None  # resp['items'][i]['health_infection_notice']
        events[i]['interest'] = None  # resp['items'][i]['interest']
        events[i]['accessible_other'] = None  # resp['items'][i]['accessible_other']
        events[i]['interest_ranking'] = None
    return event_count, events


def get_timeframe_event_list(to_date,
                             from_date=datetime.now(),
                             accessibility=None):
    """
    get all events within a specified timeframe with accessibility
    :param accessibility: numeric id 0-9
    :return: json with list of all events fulfilling the accessibility
    """
    try:
        # get all events
        query = '?entries=30&toDate=[\"' + str(to_date) + '\"]'
        if accessibility:
            query = query + '&accessible=' + str(accessibility)

        suburl = '/api/events.json'
        url = BASEURL + suburl + query
        print('Request to:' + url)
        response = requests.get(url, auth=HTTPBasicAuth(DB_USER, DB_PASS))
        print('Status Code: ' + str(response.status_code))
        print('Response from: ' + str(response.url))
        resp = response.json()
    except ApiException as e:
        print("Exception when calling EventsApi->get all timeframe events: %s\n" % e)

    event_count = resp['count']
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
        events[i]['accessible_request_sommerblut'] = resp['items'][i]['accessible_request_sommerblut']
        events[i]['category'] = resp['items'][i]['category']
        # somehow the DB response is broken here, therefore some steps to fix that.
        image_json = resp['items'][i]['event_images']
        parsed = json.loads(image_json)
        image = parsed['mainimage']['name']
        events[i]['event_images'] = 'https://datenbank.sommerblut.de/media/images/normal/' + str(image)
        events[i]['accessibility'] = resp['items'][i]['accessible_request_sommerblut']
        events[i]['program_content'] = resp['items'][i]['program_content']
        events[i]['short_description'] = resp['items'][i]['short_description']
        events[i]['health_infection_notice'] = None  # resp['items'][i]['health_infection_notice']
        events[i]['interest'] = None  # resp['items'][i]['interest']
        events[i]['accessible_other'] = None  # resp['items'][i]['accessible_other']
        events[i]['interest_ranking'] = None
    return event_count, events


def get_event_schedule(event_id):
    """
    gets the entire upcoming play
    :param event_id: the event id for which you need the plays
    :return:
    """
    try:
        # returns all upcoming eventDates for the given eventId
        resp = running_events_api.get_all_next_event_dates_by_event_id(event_id,
                                                                       accept_language=accept_language)
        print('getting event schedule')
        # pprint(resp)
    except ApiException as e:
        print("Exception when calling RunningEventsApi->get_all_next_event_dates_by_event_id: %s\n" % e)

    plays = {}
    play_count = len(resp)
    print(play_count)

    for i in range(play_count):
        plays[i] = {}
        plays[i]['accessible_request'] = resp[i]['accessible_request']
        plays[i]['date'] = resp[i]['date']
        plays[i]['end_date'] = resp[i]['end_date']
        plays[i]['id'] = resp[i]['id']
        plays[i]['location'] = resp[i]['location']
        plays[i]['opening_time'] = resp[i]['opening_time']
        plays[i]['ticket_link'] = resp[i]['ticket_link']
        plays[i]['additional_title'] = resp[i]['additional_title']
        # pprint(resp[i])
    # print(play_count)
    # pprint(plays)
    return play_count, plays


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


def get_all_titles_ids():
    try:
        # get all events
        resp = event_api.get_all_events(accept_language=accept_language,
                                        entries=30)
        titles = []
        ids = []
        for i in resp.get('items'):
            titles.append(i.get('title'))
            ids.append(i.get('id'))

        return titles, ids
    except ApiException as e:
        print("Exception when calling EventsApi->get all titles: %s\n" % e)


def get_event_title(id):
    """
gets an event title by supplying the numeric id
    :param id: event id, int
    :return: the event and important variables
    """
    suburl = '/api/events/' + str(id) + '.json'
    url = BASEURL + suburl
    response = requests.get(url, auth=HTTPBasicAuth(DB_USER, DB_PASS))
    print('Status Code: ' + str(response.status_code))
    print('Response from: ' + str(response.url))
    resp = response.json()
    title = resp['title']
    return title


def get_event_accessibility_info(id):
    """
gets the events accessibility text by supplying the numeric id
    :param id: event id, int
    :return: the event and important variables
    """
    suburl = '/api/events/' + str(id) + '.json'
    url = BASEURL + suburl
    response = requests.get(url, auth=HTTPBasicAuth(DB_USER, DB_PASS))
    print('Status Code: ' + str(response.status_code))
    print('Response from: ' + str(response.url))
    resp = response.json()
    accessibility = resp['title']
    # TODO
    return accessibility


def get_event_corona_info(id):
    """
gets the events corona info by supplying the numeric id
    :param id: event id, int
    :return: the event and important variables
    """
    suburl = '/api/events/' + str(id) + '.json'
    url = BASEURL + suburl
    response = requests.get(url, auth=HTTPBasicAuth(DB_USER, DB_PASS))
    print('Status Code: ' + str(response.status_code))
    print('Response from: ' + str(response.url))
    resp = response.json()
    corona_info = resp['title']
    # TODO
    return corona_info
