# sb_db.LocationsApi

All URIs are relative to *https://datenbank.sommerblut.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_current_location_groups**](LocationsApi.md#get_all_current_location_groups) | **GET** /api/locationGroups/current.json | get all locationsGroups from current events
[**get_all_location_groups**](LocationsApi.md#get_all_location_groups) | **GET** /api/locationGroups.json | get all locationGroups
[**get_location_group_by_id**](LocationsApi.md#get_location_group_by_id) | **GET** /api/locationGroups/{locationGroupId}.json | Find locationGroup by ID

# **get_all_current_location_groups**
> LocationGroups get_all_current_location_groups(accept_language=accept_language)

get all locationsGroups from current events

get all locationsGroups from current events with all related locations

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
api_instance = sb_db.LocationsApi(sb_db.ApiClient(configuration))
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # get all locationsGroups from current events
    api_response = api_instance.get_all_current_location_groups(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_all_current_location_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**LocationGroups**](LocationGroups.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_location_groups**
> LocationGroups get_all_location_groups(accept_language=accept_language)

get all locationGroups

get all locationGroups with all related locations

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
api_instance = sb_db.LocationsApi(sb_db.ApiClient(configuration))
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # get all locationGroups
    api_response = api_instance.get_all_location_groups(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_all_location_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**LocationGroups**](LocationGroups.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_group_by_id**
> LocationGroup get_location_group_by_id(location_group_id, accept_language=accept_language)

Find locationGroup by ID

Returns a single locationGroup with all related locations

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
api_instance = sb_db.LocationsApi(sb_db.ApiClient(configuration))
location_group_id = 56 # int | ID of locationGroup to return
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # Find locationGroup by ID
    api_response = api_instance.get_location_group_by_id(location_group_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_location_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_group_id** | **int**| ID of locationGroup to return | 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**LocationGroup**](LocationGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

