from __future__ import print_function

import os
from pprint import pprint

import sb_db
from sb_db.rest import ApiException

# Configure HTTP basic authorization: basicAuth
configuration = sb_db.Configuration()
configuration.username = os.environ.get('DB_USER')
configuration.password = os.environ.get('DB_PASS')
BASEURL = os.environ.get('BASEURL')

# create an instance of the API class
api_instance = sb_db.AccessibilitiesApi(sb_db.ApiClient(configuration))

event_api = sb_db.EventsApi(sb_db.ApiClient(configuration))

events = event_api.get_all_events(accessible=[[5, 6]])
accept_language = 'de'  # str | request specific language (optional)
try:
    # get all events
    api_response = events = event_api.get_all_events(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get all events: %s\n" % e)

try:
    # get all accessibilities
    api_response = api_instance.get_all_accessibilities(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessibilitiesApi->get_all_accessibilities: %s\n" % e)