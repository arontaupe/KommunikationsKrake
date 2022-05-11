from __future__ import print_function

import os
from pprint import pprint

import sb_db
from sb_db.rest import ApiException

from datetime import datetime

# Configure HTTP basic authorization: basicAuth
configuration = sb_db.Configuration()
configuration.username = os.environ.get('DB_USER')
configuration.password = os.environ.get('DB_PASS')
BASEURL = os.environ.get('BASEURL')

# create an instance of the API class
api_instance = sb_db.AccessibilitiesApi(sb_db.ApiClient(configuration))

event_api = sb_db.EventsApi(sb_db.ApiClient(configuration))

accept_language = 'ls'  # str | request specific language (optional)

# events = event_api.get_all_events(accessible=[[5, 6]])
print(datetime.now())
try:
    # get all events
    api_response = event_api.get_all_events(accept_language=accept_language,
                                            entries=30,
                                            # from_date=datetime.now(),
                                            # to_date=[f'["{datetime.now()}"]'],
                                            accessible=[[4, 8]],
                                            conjunction_category="accessible",
                                            conjunction_accessible="and",
                                            )
    # print(api_response)
    pprint(api_response['count'])
except ApiException as e:
    print("Exception when calling EventsApi->get all events: %s\n" % e)
print(list(range(10)))
'''
try:
    # get all accessibilities
    api_response = api_instance.get_all_accessibilities(accept_language='ls')
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessibilitiesApi->get_all_accessibilities: %s\n" % e)
'''
'''
try:
    # get event by id
    api_response = event_api.get_event_by_id(event_id=854,
                                             accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessibilitiesApi->get_all_accessibilities: %s\n" % e)
'''
