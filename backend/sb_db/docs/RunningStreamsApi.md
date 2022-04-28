# sb_db.RunningStreamsApi

All URIs are relative to *https://datenbank.sommerblut.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_next_streams**](RunningStreamsApi.md#get_all_next_streams) | **GET** /api/events/stream/running/next.json | returns all upcoming streams
[**get_all_next_streams_by_event_id**](RunningStreamsApi.md#get_all_next_streams_by_event_id) | **GET** /api/events/{eventId}/stream/running/next.json | returns all upcoming streams for the given eventId
[**get_all_running_streams**](RunningStreamsApi.md#get_all_running_streams) | **GET** /api/events/stream/running.json | returns all running streams
[**get_all_running_streams_by_event_id**](RunningStreamsApi.md#get_all_running_streams_by_event_id) | **GET** /api/events/{eventId}/stream/running.json | returns all running streams for the given eventId

# **get_all_next_streams**
> EventDates get_all_next_streams(accept_language=accept_language)

returns all upcoming streams

returns all upcoming eventDates, that are streamed

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
api_instance = sb_db.RunningStreamsApi(sb_db.ApiClient(configuration))
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # returns all upcoming streams
    api_response = api_instance.get_all_next_streams(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunningStreamsApi->get_all_next_streams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**EventDates**](EventDates.md)

### Authorization

[basicAuth](../../../../Downloads/sb_db_api/README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../../../Downloads/sb_db_api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../Downloads/sb_db_api/README.md#documentation-for-models) [[Back to README]](../../../../Downloads/sb_db_api/README.md)

# **get_all_next_streams_by_event_id**
> EventDates get_all_next_streams_by_event_id(event_id, accept_language=accept_language)

returns all upcoming streams for the given eventId

returns all upcoming eventDates for the given eventId, that are streamed

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
api_instance = sb_db.RunningStreamsApi(sb_db.ApiClient(configuration))
event_id = 56 # int | ID of event
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # returns all upcoming streams for the given eventId
    api_response = api_instance.get_all_next_streams_by_event_id(event_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunningStreamsApi->get_all_next_streams_by_event_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| ID of event | 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**EventDates**](EventDates.md)

### Authorization

[basicAuth](../../../../Downloads/sb_db_api/README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../../../Downloads/sb_db_api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../Downloads/sb_db_api/README.md#documentation-for-models) [[Back to README]](../../../../Downloads/sb_db_api/README.md)

# **get_all_running_streams**
> EventDates get_all_running_streams(accept_language=accept_language)

returns all running streams

get all eventDates, that are running and are streamed

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
api_instance = sb_db.RunningStreamsApi(sb_db.ApiClient(configuration))
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # returns all running streams
    api_response = api_instance.get_all_running_streams(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunningStreamsApi->get_all_running_streams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**EventDates**](EventDates.md)

### Authorization

[basicAuth](../../../../Downloads/sb_db_api/README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../../../Downloads/sb_db_api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../Downloads/sb_db_api/README.md#documentation-for-models) [[Back to README]](../../../../Downloads/sb_db_api/README.md)

# **get_all_running_streams_by_event_id**
> EventDates get_all_running_streams_by_event_id(event_id, accept_language=accept_language)

returns all running streams for the given eventId

returns all eventDates for the given eventId, that are running and are streamed

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
api_instance = sb_db.RunningStreamsApi(sb_db.ApiClient(configuration))
event_id = 56 # int | ID of event
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # returns all running streams for the given eventId
    api_response = api_instance.get_all_running_streams_by_event_id(event_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunningStreamsApi->get_all_running_streams_by_event_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| ID of event | 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**EventDates**](EventDates.md)

### Authorization

[basicAuth](../../../../Downloads/sb_db_api/README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../../../Downloads/sb_db_api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../Downloads/sb_db_api/README.md#documentation-for-models) [[Back to README]](../../../../Downloads/sb_db_api/README.md)
