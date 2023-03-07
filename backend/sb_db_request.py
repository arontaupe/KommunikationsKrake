from __future__ import print_function
import json
import os
from datetime import datetime, timedelta
import requests
# used for caching the api responses from the db
from cachetools import TTLCache, cached
from requests.auth import HTTPBasicAuth  # die datenbank läuft über basic auth
import time

# import dependencies for database request# import dependencies for database request
import sb_db  # sommerblut datenbank openapi
# import the response functionality
from response_func import chip_response
from retrieve_from_gdf import retrieve_found_events
from sb_db.rest import ApiException

BASEURL = os.environ.get('BASEURL')
BASEURL_DEV = os.environ.get('BASEURL_DEV')

# Configure HTTP basic authorization: basicAuth
configuration = sb_db.Configuration()
configuration.username = DB_USER = os.environ.get('DB_USER')
configuration.password = DB_PASS = os.environ.get('DB_PASS')
# here it can be switched between production Database and development database
configuration.host = BASEURL  # = BASEURL_DEV

# create an instance of the API class
accessibilities_api = sb_db.AccessibilitiesApi(sb_db.ApiClient(configuration))
event_api = sb_db.EventsApi(sb_db.ApiClient(configuration))
running_events_api = sb_db.RunningEventsApi(sb_db.ApiClient(configuration))

accept_language = 'ls'  # str | options: ('ls', 'de', 'en')


def test_sb_db():
	"""
	Used for testing whether the SB DB is reachable
	:return: Response to DF and the Response Code
	"""
	url = BASEURL + "/api/accessibilities.json"
	response = requests.get(url, auth=HTTPBasicAuth(DB_USER, DB_PASS))
	print('Database Status Code: ' + str(response.status_code))  # response 200 := success. all 400eds:= really bad
	return chip_response('Status der Datenbank: ' + str(response.status_code), ['Menü', 'Exit'])


def get_accessibility_ids():
	"""
	:return: all accessibility classes and their ID as a dict
	"""
	try:
		resp = accessibilities_api.get_all_accessibilities(accept_language=accept_language)
	except ApiException as e:
		print("Exception when calling AccessibilitiesApi->get_all_accessibilities: %s\n" % e)

	accessibilities = {}
	num_categories = len(resp)
	for i in range(num_categories):
		accessibilities[resp[i]['name']] = resp[i]['id']
	return accessibilities


def get_accessibility_ids_clean():
	"""
	:return: all accessibility classes and their ID as a dict
	"""
	try:
		# get all accessibilities
		resp = accessibilities_api.get_all_accessibilities(accept_language=accept_language)
	except ApiException as e:
		print("Exception when calling AccessibilitiesApi->get_all_accessibilities: %s\n" % e)
	return resp


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


def get_single_event_by_id(event_id):
	"""
	only works for old events somehow
	:param event_id: int
	:return: json response
	"""
	try:
		# get a specific event by name
		api_response = event_api.get_event_by_id(event_id, accept_language=accept_language)
	except ApiException as e:
		print("Exception when calling EventApi->get_single_event_by_id: %s\n" % e)
	# TODO
	return api_response


@cached(cache=TTLCache(maxsize=1024, ttl=timedelta(hours=24), timer=datetime.today))
def get_full_event_list(accessibility=None, page=1, entries=10):
	"""
	should get the full info to display on the cards later
	:param entries:
	:param page:
	:param accessibility: numeric id 0-9
	:return: json with list of all events fulfilling the accessibility
	"""
	if accessibility:
		try:
			resp = event_api.get_all_events(accessible=[accessibility],
			                                accept_language=accept_language,
			                                entries=entries,
			                                page=page,
			                                conjunction_accessible='and'
			                                )
		except ApiException as e:
			print("Exception when calling EventsApi->get all events: %s\n" % e)
	else:
		try:
			resp = event_api.get_all_events(accept_language=accept_language,
			                                entries=entries,
			                                page=page
			                                )
		except ApiException as e:
			print("Exception when calling EventsApi->get all events: %s\n" % e)

	titles = []
	ids = []
	for i in resp.get('items'):
		titles.append(i.get('title'))
		ids.append(i.get('id'))

	event_count = resp['count']
	if event_count <= entries:
		call_count = event_count
	elif event_count >= entries * page:
		call_count = entries
	else:
		call_count = len(resp['items'])

	events = {}
	for i in range(call_count):
		events[i] = {}
		event = resp['items'][i]
		events[i]['id'] = event['id']
		events[i]['title'] = event['title']
		next_date = 'Die Veranstaltung ist schon vorbei.'
		if event['next_date']:
			next_date = event['next_date']['isdate']
		events[i]['next_date'] = next_date
		events[i]['duration'] = event['duration_minutes']
		location = address = None
		if event['location']:
			location = event['location']['name']
			address = ''
			address += event['location']['street'] if event['location']['street'] else ''
			address += event['location']['number'] if event['location']['number'] else ''
			address += ', ' if address != '' else ''
			address += event['location']['postal'] if event['location']['postal'] else ''
			address += event['location']['city'] if event['location']['city'] else ''

		events[i]['location'] = location
		events[i]['address'] = address
		events[i]['artist_name'] = event['artist_name']
		events[i]['info_text'] = event['info_text']
		events[i]['subtitle'] = event['subtitle']
		events[i]['ticket_link'] = event['ticket_link']
		events[i]['price_vvk'] = event['price_vvk']
		events[i]['price_ak'] = event['price_ak']
		events[i]['max_capacity'] = event['max_capacity']
		events[i]['accessible_request_sommerblut'] = event['accessible_request_sommerblut']
		events[i]['category'] = event['category']
		# somehow the DB response is broken here, therefore some steps to fix that.
		image = None
		if event['event_images']:
			image_json = event['event_images']
			parsed = json.loads(image_json)
			image = parsed['mainimage']['name']
		events[i]['event_images'] = 'https://datenbank.sommerblut.de/media/images/normal/' + str(image)
		events[i]['accessibility'] = event['accessible_request_sommerblut']
		events[i]['program_content'] = event['program_content']
		events[i]['short_description'] = event['short_description']
		events[i]['health_infection_notice'] = event['health_infection_notice']
		events[i]['interest'] = event['interest']
		events[i]['accessible_other'] = event['accessible_other']
		events[i]['ensembles'] = event['ensembles']
		events[i]['interest_ranking'] = None
	return event_count, events, titles, ids

def test_DB_response_time():
	pre = time.perf_counter()
	get_full_event_list(page=1, entries=50)

	post = time.perf_counter()

	print(f'DB Call time: {post - pre:.5f}')


def get_partial_event_list(num_events=int, accessibility=None):
	"""
	should get the full info to display on the cards later, but for a set amount of events
	:param num_events:
	:param accessibility: numeric id 0-9
	:return: json with list of all events fulfilling the accessibility
	"""
	if accessibility:
		try:
			resp = event_api.get_all_events(accessible=[accessibility],
			                                accept_language=accept_language,
			                                entries=num_events,
			                                conjunction_accessible='and'
			                                )
		except ApiException as e:
			print("Exception when calling EventsApi->get all events: %s\n" % e)
	else:
		try:
			resp = event_api.get_all_events(accept_language=accept_language,
			                                entries=num_events
			                                )
		except ApiException as e:
			print("Exception when calling EventsApi->get all events: %s\n" % e)
	if num_events <= resp['count']:
		event_count = num_events
	else:
		event_count = resp['count']

	events = {}

	for i in range(event_count):
		events[i] = {}
		events[i]['id'] = resp['items'][i]['id']
		events[i]['title'] = resp['items'][i]['title']
		next_date = 'Die Veranstaltung ist schon vorbei.'
		if resp['items'][i]['next_date']:
			next_date = resp['items'][i]['next_date']['isdate']
		events[i]['next_date'] = next_date
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
		events[i]['health_infection_notice'] = resp['items'][i]['health_infection_notice']
		events[i]['interest'] = resp['items'][i]['interest']
		events[i]['accessible_other'] = resp['items'][i]['accessible_other']
		events[i]['interest_ranking'] = None
	return event_count, events


def get_timeframe_event_list(from_date=datetime.now(),
                             num_days=None,
                             accessibility=None
                             ):
	"""
	get all events within a specified timeframe with accessibility
	:param from_date:
	:param num_days:
	:param accessibility: numeric id 0-9
	:return: json with list of all events fulfilling the accessibility
	"""
	if num_days:
		until_date = from_date + timedelta(days=num_days)
		if accessibility:
			try:
				resp = event_api.get_all_events(accept_language=accept_language,
				                                entries=30,
				                                to_date=[f'["{until_date}"]'],
				                                from_date=[f'["{from_date}"]'],
				                                accessible=[accessibility],
				                                conjunction_accessible='and'
				                                )
			except ApiException as e:
				print("Exception when calling EventsApi->get all events: %s\n" % e)
		else:
			try:
				resp = event_api.get_all_events(accept_language=accept_language,
				                                entries=30,
				                                to_date=[f'["{until_date}"]'],
				                                from_date=[f'["{from_date}"]']
				                                )
			except ApiException as e:
				print("Exception when calling EventsApi->get all events: %s\n" % e)
	else:
		if accessibility:
			try:
				resp = event_api.get_all_events(accept_language=accept_language,
				                                entries=30,
				                                from_date=[f'["{from_date}"]'],
				                                accessible=[accessibility],
				                                conjunction_accessible='and'
				                                )
			except ApiException as e:
				print("Exception when calling EventsApi->get all events: %s\n" % e)
		else:
			try:
				resp = event_api.get_all_events(accept_language=accept_language,
				                                entries=30,
				                                from_date=[f'["{from_date}"]']
				                                )
			except ApiException as e:
				print("Exception when calling EventsApi->get all events: %s\n" % e)

	titles = []
	ids = []
	for i in resp.get('items'):
		titles.append(i.get('title'))
		ids.append(i.get('id'))

	event_count = resp['count']

	events = {}
	for i in range(event_count):
		events[i] = {}
		events[i]['id'] = resp['items'][i]['id']
		events[i]['title'] = resp['items'][i]['title']
		next_date = 'Die Veranstaltung ist schon vorbei.'
		if resp['items'][i]['next_date']:
			next_date = resp['items'][i]['next_date']['isdate']
		events[i]['next_date'] = next_date
		events[i]['duration'] = resp['items'][i]['duration_minutes']
		location = None
		if resp['items'][i]['location']:
			location = resp['items'][i]['location']['name']
		events[i]['location'] = location
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
		image = None
		if resp['items'][i]['event_images']:
			image_json = resp['items'][i]['event_images']
			parsed = json.loads(image_json)
			image = parsed['mainimage']['name']
		events[i]['event_images'] = 'https://datenbank.sommerblut.de/media/images/normal/' + str(image)
		events[i]['accessibility'] = resp['items'][i]['accessible_request_sommerblut']
		events[i]['program_content'] = resp['items'][i]['program_content']
		events[i]['short_description'] = resp['items'][i]['short_description']
		events[i]['health_infection_notice'] = resp['items'][i]['health_infection_notice']
		events[i]['interest'] = resp['items'][i]['interest']
		events[i]['accessible_other'] = resp['items'][i]['accessible_other']
		events[i]['interest_ranking'] = None
	return event_count, events, titles, ids


def get_event_schedule(event_id):
	"""
	gets the entire upcoming play
	:param event_id: the event id for which you need the plays
	:return:
	"""
	try:
		# returns all upcoming eventDates for the given eventId
		resp = running_events_api.get_all_next_event_dates_by_event_id(event_id,
		                                                               accept_language=accept_language
		                                                               )
	except ApiException as e:
		print("Exception when calling EventsApi->get_all_next_event_dates_by_event_id: %s\n" % e)

	plays = {}
	play_count = len(resp)
	print(f'{play_count=}')

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

	return play_count, plays


def get_all_titles_ids():
	try:
		resp = event_api.get_all_events(accept_language=accept_language,
		                                entries=30
		                                )
		titles = []
		ids = []
		for i in resp.get('items'):
			titles.append(i.get('title'))
			ids.append(i.get('id'))

		return titles, ids
	except ApiException as e:
		print("Exception when calling EventsApi->get all titles: %s\n" % e)


def get_event_title(event_id):
	"""
	gets an event title by supplying the numeric id
	:param event_id: event id, int
	:return: the event and important variables
	"""
	suburl = '/api/events/' + str(event_id) + '.json'
	url = BASEURL + suburl
	response = requests.get(url, auth=HTTPBasicAuth(DB_USER, DB_PASS))
	resp = response.json()
	title = resp['title']
	return title


def get_next_event():
	try:
		# returns all upcoming events
		resp = running_events_api.get_all_next_event_dates(accept_language=accept_language)
		play = resp[0]
		title = play['event']['title']
		id = play['event']['id']
		next_date = play['event']['next_date']['isdate']
	except ApiException as e:
		print("Exception when calling RunningEventsApi->get_all_next_event_dates: %s\n" % e)

	return title, id, next_date
