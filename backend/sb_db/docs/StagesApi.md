# sb_db.StagesApi

All URIs are relative to *https://datenbank.sommerblut.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_current_locations**](StagesApi.md#get_all_current_locations) | **GET** /api/locations/current.json | get all locations from current events
[**get_all_locations**](StagesApi.md#get_all_locations) | **GET** /api/locations.json | get all locations
[**get_location_by_id**](StagesApi.md#get_location_by_id) | **GET** /api/locations/{locationId}.json | Find location by ID

# **get_all_current_locations**
> Locations get_all_current_locations(accept_language=accept_language)

get all locations from current events

get all locations (stages) from current events

### Example
```python
from __future__ import print_function
import time
import sb_db
from sb_db.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sb_db.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sb_db.StagesApi(sb_db.ApiClient(configuration))
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # get all locations from current events
    api_response = api_instance.get_all_current_locations(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StagesApi->get_all_current_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Locations**](Locations.md)

### Authorization

[basicAuth](../../../../Downloads/sb_db_api/README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../../../Downloads/sb_db_api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../Downloads/sb_db_api/README.md#documentation-for-models) [[Back to README]](../../../../Downloads/sb_db_api/README.md)

# **get_all_locations**
> Locations get_all_locations(accept_language=accept_language)

get all locations

get all locations (stages)

### Example
```python
from __future__ import print_function
import time
import sb_db
from sb_db.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sb_db.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sb_db.StagesApi(sb_db.ApiClient(configuration))
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # get all locations
    api_response = api_instance.get_all_locations(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StagesApi->get_all_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Locations**](Locations.md)

### Authorization

[basicAuth](../../../../Downloads/sb_db_api/README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../../../Downloads/sb_db_api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../Downloads/sb_db_api/README.md#documentation-for-models) [[Back to README]](../../../../Downloads/sb_db_api/README.md)

# **get_location_by_id**
> Location get_location_by_id(location_id, accept_language=accept_language)

Find location by ID

Returns a single location (stage)

### Example
```python
from __future__ import print_function
import time
import sb_db
from sb_db.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = sb_db.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sb_db.StagesApi(sb_db.ApiClient(configuration))
location_id = 56 # int | ID of location to return
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # Find location by ID
    api_response = api_instance.get_location_by_id(location_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StagesApi->get_location_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| ID of location to return | 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Location**](Location.md)

### Authorization

[basicAuth](../../../../Downloads/sb_db_api/README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../../../Downloads/sb_db_api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../Downloads/sb_db_api/README.md#documentation-for-models) [[Back to README]](../../../../Downloads/sb_db_api/README.md)
