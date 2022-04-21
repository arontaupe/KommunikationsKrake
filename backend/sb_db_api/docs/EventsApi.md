# sb_db.EventsApi

All URIs are relative to *https://datenbank.sommerblut.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_events**](EventsApi.md#get_all_events) | **GET** /api/events.json | get all events
[**get_current_events**](EventsApi.md#get_current_events) | **GET** /api/festivals/current/events.json | get all current events
[**get_event_by_id**](EventsApi.md#get_event_by_id) | **GET** /api/events/{eventId}.json | Find event by ID
[**get_events_by_name**](EventsApi.md#get_events_by_name) | **GET** /api/events/{eventName}.details.json | Find events by name
[**get_events_by_year**](EventsApi.md#get_events_by_year) | **GET** /api/festivals/{year}/events.json | find events by year

# **get_all_events**
> Events get_all_events(order=order, entries=entries, page=page, year=year, archive=archive, category=category, tag=tag, accessible=accessible, location=location, time=time, from_date=from_date, to_date=to_date, accept_language=accept_language)

get all events

get all events

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
api_instance = sb_db.EventsApi(sb_db.ApiClient(configuration))
order = ['order_example'] # list[str] | Sets the order of returning events (d - descending)<br>Example: /api/events.json?order=[\"location\"]<br>Possible Values:<br> - date<br> - date-d<br> - event<br> - event-d<br> - artist<br> - artist-d<br> - location<br> - location-d (optional)
entries = 56 # int | Number of entries per page to return (standard = 10)<br>Example: /api/events.json?entries=5 (optional)
page = 56 # int | Number of page<br>Example: /api/events.json?page=2 (optional)
year = 56 # int | returns all events of the given year<br>Example: /api/events.json?year=2020 (optional)
archive = 56 # int | returns all events of archived or not archived festivals<br>Example: /api/events.json?archive=1 (optional)
category = [56] # list[int] | returns events that have a category with the given categoryId<br>Example: /api/events.json?category=[100] (optional)
tag = [56] # list[int] | returns events that have a tag with the given tagId<br>Example: /api/events.json?tag=[100] (optional)
accessible = [56] # list[int] | returns events that have a accessibility with the given accessibilityID<br>Example: /api/events.json?accessible=[100] (optional)
location = [56] # list[int] | returns events that have a location with the given locationID<br>Example: /api/events.json?location=[100] (optional)
time = ['time_example'] # list[str] | returns events with event dates in the given timeframe<br>Example: /api/events.json?time=[\"today\"]<br>Possible Values:<br> - today<br> - upcoming<br> - past (optional)
from_date = ['from_date_example'] # list[str] | returns events with event dates from the given date<br>Example: /api/events.json?fromDate=[\"2022-02-14 00:00:00\"] (optional)
to_date = ['to_date_example'] # list[str] | returns events with event dates to the given date<br>Example: /api/events.json?toDate=[\"2022-02-14 00:00:00\"] (optional)
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # get all events
    api_response = api_instance.get_all_events(order=order, entries=entries, page=page, year=year, archive=archive, category=category, tag=tag, accessible=accessible, location=location, time=time, from_date=from_date, to_date=to_date, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_all_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**list[str]**](str.md)| Sets the order of returning events (d - descending)&lt;br&gt;Example: /api/events.json?order&#x3D;[\&quot;location\&quot;]&lt;br&gt;Possible Values:&lt;br&gt; - date&lt;br&gt; - date-d&lt;br&gt; - event&lt;br&gt; - event-d&lt;br&gt; - artist&lt;br&gt; - artist-d&lt;br&gt; - location&lt;br&gt; - location-d | [optional] 
 **entries** | **int**| Number of entries per page to return (standard &#x3D; 10)&lt;br&gt;Example: /api/events.json?entries&#x3D;5 | [optional] 
 **page** | **int**| Number of page&lt;br&gt;Example: /api/events.json?page&#x3D;2 | [optional] 
 **year** | **int**| returns all events of the given year&lt;br&gt;Example: /api/events.json?year&#x3D;2020 | [optional] 
 **archive** | **int**| returns all events of archived or not archived festivals&lt;br&gt;Example: /api/events.json?archive&#x3D;1 | [optional] 
 **category** | [**list[int]**](int.md)| returns events that have a category with the given categoryId&lt;br&gt;Example: /api/events.json?category&#x3D;[100] | [optional] 
 **tag** | [**list[int]**](int.md)| returns events that have a tag with the given tagId&lt;br&gt;Example: /api/events.json?tag&#x3D;[100] | [optional] 
 **accessible** | [**list[int]**](int.md)| returns events that have a accessibility with the given accessibilityID&lt;br&gt;Example: /api/events.json?accessible&#x3D;[100] | [optional] 
 **location** | [**list[int]**](int.md)| returns events that have a location with the given locationID&lt;br&gt;Example: /api/events.json?location&#x3D;[100] | [optional] 
 **time** | [**list[str]**](str.md)| returns events with event dates in the given timeframe&lt;br&gt;Example: /api/events.json?time&#x3D;[\&quot;today\&quot;]&lt;br&gt;Possible Values:&lt;br&gt; - today&lt;br&gt; - upcoming&lt;br&gt; - past | [optional] 
 **from_date** | [**list[str]**](str.md)| returns events with event dates from the given date&lt;br&gt;Example: /api/events.json?fromDate&#x3D;[\&quot;2022-02-14 00:00:00\&quot;] | [optional] 
 **to_date** | [**list[str]**](str.md)| returns events with event dates to the given date&lt;br&gt;Example: /api/events.json?toDate&#x3D;[\&quot;2022-02-14 00:00:00\&quot;] | [optional] 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Events**](Events.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_events**
> Events get_current_events(order=order, entries=entries, page=page, year=year, category=category, tag=tag, accessible=accessible, location=location, time=time, from_date=from_date, to_date=to_date, accept_language=accept_language)

get all current events

returns all published events that are not already archived

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
api_instance = sb_db.EventsApi(sb_db.ApiClient(configuration))
order = ['order_example'] # list[str] | Sets the order of returning events (d - descending)<br>Example: /api/events.json?order=[\"location\"]<br>Possible Values:<br> - date<br> - date-d<br> - event<br> - event-d<br> - artist<br> - artist-d<br> - location<br> - location-d (optional)
entries = 56 # int | Number of entries per page to return (standard = 10)<br>Example: /api/events.json?entries=5 (optional)
page = 56 # int | Number of page<br>Example: /api/events.json?page=2 (optional)
year = 56 # int | returns all events of the given year<br>Example: /api/events.json?year=2020 (optional)
category = [56] # list[int] | returns events that have a category with the given categoryId<br>Example: /api/events.json?category=[100] (optional)
tag = [56] # list[int] | returns events that have a tag with the given tagId<br>Example: /api/events.json?tag=[100] (optional)
accessible = [56] # list[int] | returns events that have a accessibility with the given accessibilityID<br>Example: /api/events.json?accessible=[100] (optional)
location = [56] # list[int] | returns events that have a location with the given locationID<br>Example: /api/events.json?location=[100] (optional)
time = ['time_example'] # list[str] | returns events with event dates in the given timeframe<br>Example: /api/events.json?time=[\"today\"]<br>Possible Values:<br> - today<br> - upcoming<br> - past (optional)
from_date = ['from_date_example'] # list[str] | returns events with event dates from the given date<br>Example: /api/events.json?fromDate=[\"2022-02-14 00:00:00\"] (optional)
to_date = ['to_date_example'] # list[str] | returns events with event dates to the given date<br>Example: /api/events.json?toDate=[\"2022-02-14 00:00:00\"] (optional)
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # get all current events
    api_response = api_instance.get_current_events(order=order, entries=entries, page=page, year=year, category=category, tag=tag, accessible=accessible, location=location, time=time, from_date=from_date, to_date=to_date, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_current_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**list[str]**](str.md)| Sets the order of returning events (d - descending)&lt;br&gt;Example: /api/events.json?order&#x3D;[\&quot;location\&quot;]&lt;br&gt;Possible Values:&lt;br&gt; - date&lt;br&gt; - date-d&lt;br&gt; - event&lt;br&gt; - event-d&lt;br&gt; - artist&lt;br&gt; - artist-d&lt;br&gt; - location&lt;br&gt; - location-d | [optional] 
 **entries** | **int**| Number of entries per page to return (standard &#x3D; 10)&lt;br&gt;Example: /api/events.json?entries&#x3D;5 | [optional] 
 **page** | **int**| Number of page&lt;br&gt;Example: /api/events.json?page&#x3D;2 | [optional] 
 **year** | **int**| returns all events of the given year&lt;br&gt;Example: /api/events.json?year&#x3D;2020 | [optional] 
 **category** | [**list[int]**](int.md)| returns events that have a category with the given categoryId&lt;br&gt;Example: /api/events.json?category&#x3D;[100] | [optional] 
 **tag** | [**list[int]**](int.md)| returns events that have a tag with the given tagId&lt;br&gt;Example: /api/events.json?tag&#x3D;[100] | [optional] 
 **accessible** | [**list[int]**](int.md)| returns events that have a accessibility with the given accessibilityID&lt;br&gt;Example: /api/events.json?accessible&#x3D;[100] | [optional] 
 **location** | [**list[int]**](int.md)| returns events that have a location with the given locationID&lt;br&gt;Example: /api/events.json?location&#x3D;[100] | [optional] 
 **time** | [**list[str]**](str.md)| returns events with event dates in the given timeframe&lt;br&gt;Example: /api/events.json?time&#x3D;[\&quot;today\&quot;]&lt;br&gt;Possible Values:&lt;br&gt; - today&lt;br&gt; - upcoming&lt;br&gt; - past | [optional] 
 **from_date** | [**list[str]**](str.md)| returns events with event dates from the given date&lt;br&gt;Example: /api/events.json?fromDate&#x3D;[\&quot;2022-02-14 00:00:00\&quot;] | [optional] 
 **to_date** | [**list[str]**](str.md)| returns events with event dates to the given date&lt;br&gt;Example: /api/events.json?toDate&#x3D;[\&quot;2022-02-14 00:00:00\&quot;] | [optional] 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Events**](Events.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_by_id**
> Event get_event_by_id(event_id, accept_language=accept_language)

Find event by ID

Returns a single event

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
api_instance = sb_db.EventsApi(sb_db.ApiClient(configuration))
event_id = 56 # int | ID of event to return
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # Find event by ID
    api_response = api_instance.get_event_by_id(event_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_event_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| ID of event to return | 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Event**](Event.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_by_name**
> Events get_events_by_name(event_name, accept_language=accept_language)

Find events by name

Returns all events with the given name

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
api_instance = sb_db.EventsApi(sb_db.ApiClient(configuration))
event_name = 'event_name_example' # str | Name of events to return
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # Find events by name
    api_response = api_instance.get_events_by_name(event_name, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| Name of events to return | 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Events**](Events.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_by_year**
> Events get_events_by_year(year, order=order, entries=entries, page=page, archive=archive, category=category, tag=tag, accessible=accessible, location=location, time=time, from_date=from_date, to_date=to_date, accept_language=accept_language)

find events by year

returns all published events in the provided year

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
api_instance = sb_db.EventsApi(sb_db.ApiClient(configuration))
year = 56 # int | Year of festival for events to return
order = ['order_example'] # list[str] | Sets the order of returning events (d - descending)<br>Example: /api/events.json?order=[\"location\"]<br>Possible Values:<br> - date<br> - date-d<br> - event<br> - event-d<br> - artist<br> - artist-d<br> - location<br> - location-d (optional)
entries = 56 # int | Number of entries per page to return (standard = 10)<br>Example: /api/events.json?entries=5 (optional)
page = 56 # int | Number of page<br>Example: /api/events.json?page=2 (optional)
archive = 56 # int | returns all events of archived or not archived festivals<br>Example: /api/events.json?archive=1 (optional)
category = [56] # list[int] | returns events that have a category with the given categoryId<br>Example: /api/events.json?category=[100] (optional)
tag = [56] # list[int] | returns events that have a tag with the given tagId<br>Example: /api/events.json?tag=[100] (optional)
accessible = [56] # list[int] | returns events that have a accessibility with the given accessibilityID<br>Example: /api/events.json?accessible=[100] (optional)
location = [56] # list[int] | returns events that have a location with the given locationID<br>Example: /api/events.json?location=[100] (optional)
time = ['time_example'] # list[str] | returns events with event dates in the given timeframe<br>Example: /api/events.json?time=[\"today\"]<br>Possible Values:<br> - today<br> - upcoming<br> - past (optional)
from_date = ['from_date_example'] # list[str] | returns events with event dates from the given date<br>Example: /api/events.json?fromDate=[\"2022-02-14 00:00:00\"] (optional)
to_date = ['to_date_example'] # list[str] | returns events with event dates to the given date<br>Example: /api/events.json?toDate=[\"2022-02-14 00:00:00\"] (optional)
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # find events by year
    api_response = api_instance.get_events_by_year(year, order=order, entries=entries, page=page, archive=archive, category=category, tag=tag, accessible=accessible, location=location, time=time, from_date=from_date, to_date=to_date, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events_by_year: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year of festival for events to return | 
 **order** | [**list[str]**](str.md)| Sets the order of returning events (d - descending)&lt;br&gt;Example: /api/events.json?order&#x3D;[\&quot;location\&quot;]&lt;br&gt;Possible Values:&lt;br&gt; - date&lt;br&gt; - date-d&lt;br&gt; - event&lt;br&gt; - event-d&lt;br&gt; - artist&lt;br&gt; - artist-d&lt;br&gt; - location&lt;br&gt; - location-d | [optional] 
 **entries** | **int**| Number of entries per page to return (standard &#x3D; 10)&lt;br&gt;Example: /api/events.json?entries&#x3D;5 | [optional] 
 **page** | **int**| Number of page&lt;br&gt;Example: /api/events.json?page&#x3D;2 | [optional] 
 **archive** | **int**| returns all events of archived or not archived festivals&lt;br&gt;Example: /api/events.json?archive&#x3D;1 | [optional] 
 **category** | [**list[int]**](int.md)| returns events that have a category with the given categoryId&lt;br&gt;Example: /api/events.json?category&#x3D;[100] | [optional] 
 **tag** | [**list[int]**](int.md)| returns events that have a tag with the given tagId&lt;br&gt;Example: /api/events.json?tag&#x3D;[100] | [optional] 
 **accessible** | [**list[int]**](int.md)| returns events that have a accessibility with the given accessibilityID&lt;br&gt;Example: /api/events.json?accessible&#x3D;[100] | [optional] 
 **location** | [**list[int]**](int.md)| returns events that have a location with the given locationID&lt;br&gt;Example: /api/events.json?location&#x3D;[100] | [optional] 
 **time** | [**list[str]**](str.md)| returns events with event dates in the given timeframe&lt;br&gt;Example: /api/events.json?time&#x3D;[\&quot;today\&quot;]&lt;br&gt;Possible Values:&lt;br&gt; - today&lt;br&gt; - upcoming&lt;br&gt; - past | [optional] 
 **from_date** | [**list[str]**](str.md)| returns events with event dates from the given date&lt;br&gt;Example: /api/events.json?fromDate&#x3D;[\&quot;2022-02-14 00:00:00\&quot;] | [optional] 
 **to_date** | [**list[str]**](str.md)| returns events with event dates to the given date&lt;br&gt;Example: /api/events.json?toDate&#x3D;[\&quot;2022-02-14 00:00:00\&quot;] | [optional] 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Events**](Events.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

