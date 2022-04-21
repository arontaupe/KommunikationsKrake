# sb_db.RunningEventsApi

All URIs are relative to *https://datenbank.sommerblut.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_next_event_dates**](RunningEventsApi.md#get_all_next_event_dates) | **GET** /api/events/running/next.json | returns all upcoming events
[**get_all_next_event_dates_by_event_id**](RunningEventsApi.md#get_all_next_event_dates_by_event_id) | **GET** /api/events/{eventId}/running/next.json | returns all upcoming eventDates for the given eventId
[**get_all_running_event_dates**](RunningEventsApi.md#get_all_running_event_dates) | **GET** /api/events/running.json | returns all running eventsDates
[**get_all_running_event_dates_by_event_id**](RunningEventsApi.md#get_all_running_event_dates_by_event_id) | **GET** /api/events/{eventId}/running.json | returns all running eventDates for the given eventId

# **get_all_next_event_dates**
> EventDates get_all_next_event_dates(accept_language=accept_language)

returns all upcoming events

get all upcoming eventDates

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
api_instance = sb_db.RunningEventsApi(sb_db.ApiClient(configuration))
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # returns all upcoming events
    api_response = api_instance.get_all_next_event_dates(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunningEventsApi->get_all_next_event_dates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**EventDates**](EventDates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_next_event_dates_by_event_id**
> EventDates get_all_next_event_dates_by_event_id(event_id, accept_language=accept_language)

returns all upcoming eventDates for the given eventId

returns all upcoming eventDates for the given eventId

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
api_instance = sb_db.RunningEventsApi(sb_db.ApiClient(configuration))
event_id = 56 # int | ID of event
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # returns all upcoming eventDates for the given eventId
    api_response = api_instance.get_all_next_event_dates_by_event_id(event_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunningEventsApi->get_all_next_event_dates_by_event_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| ID of event | 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**EventDates**](EventDates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_running_event_dates**
> EventDates get_all_running_event_dates(accept_language=accept_language)

returns all running eventsDates

returns all running eventDates

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
api_instance = sb_db.RunningEventsApi(sb_db.ApiClient(configuration))
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # returns all running eventsDates
    api_response = api_instance.get_all_running_event_dates(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunningEventsApi->get_all_running_event_dates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**EventDates**](EventDates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_running_event_dates_by_event_id**
> EventDates get_all_running_event_dates_by_event_id(event_id, accept_language=accept_language)

returns all running eventDates for the given eventId

returns all running eventDates for the given eventId

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
api_instance = sb_db.RunningEventsApi(sb_db.ApiClient(configuration))
event_id = 56 # int | ID of event
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # returns all running eventDates for the given eventId
    api_response = api_instance.get_all_running_event_dates_by_event_id(event_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunningEventsApi->get_all_running_event_dates_by_event_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| ID of event | 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**EventDates**](EventDates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

