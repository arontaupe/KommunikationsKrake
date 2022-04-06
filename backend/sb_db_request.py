# import dependencies for database request
import requests
from requests.auth import HTTPBasicAuth   # die datenbank läuft über basic auth
import json # make me interact with json
# die logindaten für die sommerblut datenbank. besser base64 encoden? unsafe. TODO
DB_USER = 'api_ticketing'
DB_PASS = '[T!ck28O1api'
BASEURL = 'https://datenbank.sommerblut.de'


# makes sure the webhook is online and working
def test_sb_db():
    url = BASEURL + "/api/accessibilities.json"
    response = requests.get(url, auth = HTTPBasicAuth(DB_USER, DB_PASS))
    print('Request: ' + str(response.url))
    print('Status Code: ' + str(response.status_code)) # response 200 := success. all 400eds:= really bad
    print('Headers')
    print(response.headers)
    print(response.json())
    return standard_response('the Webhook is online', ['Menü','Exit'])


def get_events_w_access(accessibility):
    query = '?accessible=['+ str(accessibility) + ']'
    suburl = "/api/events.json"
    url = BASEURL + suburl + query
    response = requests.get(url, auth=HTTPBasicAuth(DB_USER, DB_PASS))
    print('Request: ' + str(response.url))
    print('Status Code: ' + str(response.status_code))
    print(response.json()['items']['title'])
    #print(response.headers)
    #print(response.json())
    #print(response.text)
    #r_dict = response.json()
    #print(r_dict['title'])
    #print(json.dumps(response.text, indent=4))
    #return response