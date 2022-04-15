# import dependencies for database request
import requests
from requests.auth import HTTPBasicAuth   # die datenbank läuft über basic auth
import json # make me interact with json

# import the response functionality
from response_func import chip_response, image_response
import db_auth

BASEURL = 'https://datenbank.sommerblut.de'


# makes sure the webhook is online and working
def test_sb_db():
    url = BASEURL + "/api/accessibilities.json"
    response = requests.get(url, auth = HTTPBasicAuth(db_auth.DB_USER, db_auth.DB_PASS))
    print('Request: ' + str(response.url))
    print('Status Code: ' + str(response.status_code)) # response 200 := success. all 400eds:= really bad
    #print('Headers')
    #print(response.headers)
    #print(response.json())
    return chip_response('Status der Datenbank: ' + str(response.status_code), ['Menü','Exit'])


def get_events_w_access(accessibility):
    query = '?accessible=['+ str(accessibility) + ']' + '?entries=30'
    suburl = "/api/events.json"
    url = BASEURL + suburl + query
    response = requests.get(url, auth=HTTPBasicAuth(db_auth.DB_USER, db_auth.DB_PASS))
    print('Request: ' + str(response.url))
    print('Status Code: ' + str(response.status_code))

    print(response.json())
    event_count = response.json()['count']
    print('Number of Events Found: ' + str(event_count))
    display_count = event_count if event_count <= 10 else 10
    titles = []
    for i in range(display_count):
        titles.append(response.json()['items'][i]['title'])
    print(titles)
    #return response
    #print("====================================== Begin JSON ======================================")
    #print(response.json())