# sb_db.DatesOfEventsApi

All URIs are relative to *https://datenbank.sommerblut.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_dates_of_events**](DatesOfEventsApi.md#get_all_dates_of_events) | **GET** /api/events/dates.json | get all dates of events
[**get_dates_of_events_by_year**](DatesOfEventsApi.md#get_dates_of_events_by_year) | **GET** /api/festivals/{year}/events/dates.json | find dates of events by year

# **get_all_dates_of_events**
> Dates get_all_dates_of_events(order=order, entries=entries, page=page, year=year, archive=archive, category=category, tag=tag, accessible=accessible, location=location, time=time, from_date=from_date, to_date=to_date, accept_language=accept_language)

get all dates of events

returns all dates of events and the related events

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
api_instance = sb_db.DatesOfEventsApi(sb_db.ApiClient(configuration))
order = ['order_example'] # list[str] | Sets the order of returning event dates (d - descending)<br>Example: /api/events.json?order=[\"location\"]<br>Possible Values:<br> - date<br> - date-d<br> - event<br> - event-d<br> - artist<br> - artist-d<br> - location<br> - location-d (optional)
entries = 56 # int | Number of entries per page to return (standard = 10)<br>Example: /api/events.json?entries=5 (optional)
page = 56 # int | Number of page<br>Example: /api/events.json?page=2 (optional)
year = 56 # int | returns event dates of events of the given year<br>Example: /api/events.json?year=2020 (optional)
archive = 56 # int | returns event dates of events of archived or not archived festivals<br>Example: /api/events.json?archive=1 (optional)
category = [56] # list[int] | returns event dates of events that have a category with the given categoryId<br>Example: /api/events.json?category=[100] (optional)
tag = [56] # list[int] | returns event dates of events that have a tag with the given tagId<br>Example: /api/events.json?tag=[100] (optional)
accessible = [56] # list[int] | returns event dates of events that have a accessibility with the given accessibilityID<br>Example: /api/events.json?accessible=[100] (optional)
location = [56] # list[int] | returns event dates of events that have a location with the given locationID<br>Example: /api/events.json?location=[100] (optional)
time = ['time_example'] # list[str] | returns events with event dates in the given timeframe<br>Example: /api/events.json?time=[\"today\"]<br>Possible Values:<br> - today<br> - upcoming<br> - past (optional)
from_date = ['from_date_example'] # list[str] | returns events with event dates from the given date<br>Example: /api/events.json?fromDate=[\"2022-02-14 00:00:00\"] (optional)
to_date = ['to_date_example'] # list[str] | returns events with event dates to the given date<br>Example: /api/events.json?toDate=[\"2022-02-14 00:00:00\"] (optional)
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # get all dates of events
    api_response = api_instance.get_all_dates_of_events(order=order, entries=entries, page=page, year=year, archive=archive, category=category, tag=tag, accessible=accessible, location=location, time=time, from_date=from_date, to_date=to_date, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatesOfEventsApi->get_all_dates_of_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**list[str]**](str.md)| Sets the order of returning event dates (d - descending)&lt;br&gt;Example: /api/events.json?order&#x3D;[\&quot;location\&quot;]&lt;br&gt;Possible Values:&lt;br&gt; - date&lt;br&gt; - date-d&lt;br&gt; - event&lt;br&gt; - event-d&lt;br&gt; - artist&lt;br&gt; - artist-d&lt;br&gt; - location&lt;br&gt; - location-d | [optional] 
 **entries** | **int**| Number of entries per page to return (standard &#x3D; 10)&lt;br&gt;Example: /api/events.json?entries&#x3D;5 | [optional] 
 **page** | **int**| Number of page&lt;br&gt;Example: /api/events.json?page&#x3D;2 | [optional] 
 **year** | **int**| returns event dates of events of the given year&lt;br&gt;Example: /api/events.json?year&#x3D;2020 | [optional] 
 **archive** | **int**| returns event dates of events of archived or not archived festivals&lt;br&gt;Example: /api/events.json?archive&#x3D;1 | [optional] 
 **category** | [**list[int]**](int.md)| returns event dates of events that have a category with the given categoryId&lt;br&gt;Example: /api/events.json?category&#x3D;[100] | [optional] 
 **tag** | [**list[int]**](int.md)| returns event dates of events that have a tag with the given tagId&lt;br&gt;Example: /api/events.json?tag&#x3D;[100] | [optional] 
 **accessible** | [**list[int]**](int.md)| returns event dates of events that have a accessibility with the given accessibilityID&lt;br&gt;Example: /api/events.json?accessible&#x3D;[100] | [optional] 
 **location** | [**list[int]**](int.md)| returns event dates of events that have a location with the given locationID&lt;br&gt;Example: /api/events.json?location&#x3D;[100] | [optional] 
 **time** | [**list[str]**](str.md)| returns events with event dates in the given timeframe&lt;br&gt;Example: /api/events.json?time&#x3D;[\&quot;today\&quot;]&lt;br&gt;Possible Values:&lt;br&gt; - today&lt;br&gt; - upcoming&lt;br&gt; - past | [optional] 
 **from_date** | [**list[str]**](str.md)| returns events with event dates from the given date&lt;br&gt;Example: /api/events.json?fromDate&#x3D;[\&quot;2022-02-14 00:00:00\&quot;] | [optional] 
 **to_date** | [**list[str]**](str.md)| returns events with event dates to the given date&lt;br&gt;Example: /api/events.json?toDate&#x3D;[\&quot;2022-02-14 00:00:00\&quot;] | [optional] 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Dates**](Dates.md)

### Authorization

[basicAuth](../../../../Downloads/sb_db_api/README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../../../Downloads/sb_db_api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../Downloads/sb_db_api/README.md#documentation-for-models) [[Back to README]](../../../../Downloads/sb_db_api/README.md)

# **get_dates_of_events_by_year**
> Dates get_dates_of_events_by_year(year, order=order, entries=entries, page=page, archive=archive, category=category, tag=tag, accessible=accessible, location=location, time=time, from_date=from_date, to_date=to_date, accept_language=accept_language)

find dates of events by year

returns all dates of events and the related events in the provided year

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
api_instance = sb_db.DatesOfEventsApi(sb_db.ApiClient(configuration))
year = 56 # int | Year of festival for event dates to return
order = ['order_example'] # list[str] | Sets the order of returning event dates (d - descending)<br>Example: /api/events.json?order=[\"location\"]<br>Possible Values:<br> - date<br> - date-d<br> - event<br> - event-d<br> - artist<br> - artist-d<br> - location<br> - location-d (optional)
entries = 56 # int | Number of entries per page to return (standard = 10)<br>Example: /api/events.json?entries=5 (optional)
page = 56 # int | Number of page<br>Example: /api/events.json?page=2 (optional)
archive = 56 # int | returns event dates of events of archived or not archived festivals<br>Example: /api/events.json?archive=1 (optional)
category = [56] # list[int] | returns event dates of events that have a category with the given categoryId<br>Example: /api/events.json?category=[100] (optional)
tag = [56] # list[int] | returns event dates of events that have a tag with the given tagId<br>Example: /api/events.json?tag=[100] (optional)
accessible = [56] # list[int] | returns event dates of events that have a accessibility with the given accessibilityID<br>Example: /api/events.json?accessible=[100] (optional)
location = [56] # list[int] | returns event dates of events that have a location with the given locationID<br>Example: /api/events.json?location=[100] (optional)
time = ['time_example'] # list[str] | returns events with event dates in the given timeframe<br>Example: /api/events.json?time=[\"today\"]<br>Possible Values:<br> - today<br> - upcoming<br> - past (optional)
from_date = ['from_date_example'] # list[str] | returns events with event dates from the given date<br>Example: /api/events.json?fromDate=[\"2022-02-14 00:00:00\"] (optional)
to_date = ['to_date_example'] # list[str] | returns events with event dates to the given date<br>Example: /api/events.json?toDate=[\"2022-02-14 00:00:00\"] (optional)
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # find dates of events by year
    api_response = api_instance.get_dates_of_events_by_year(year, order=order, entries=entries, page=page, archive=archive, category=category, tag=tag, accessible=accessible, location=location, time=time, from_date=from_date, to_date=to_date, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatesOfEventsApi->get_dates_of_events_by_year: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year of festival for event dates to return | 
 **order** | [**list[str]**](str.md)| Sets the order of returning event dates (d - descending)&lt;br&gt;Example: /api/events.json?order&#x3D;[\&quot;location\&quot;]&lt;br&gt;Possible Values:&lt;br&gt; - date&lt;br&gt; - date-d&lt;br&gt; - event&lt;br&gt; - event-d&lt;br&gt; - artist&lt;br&gt; - artist-d&lt;br&gt; - location&lt;br&gt; - location-d | [optional] 
 **entries** | **int**| Number of entries per page to return (standard &#x3D; 10)&lt;br&gt;Example: /api/events.json?entries&#x3D;5 | [optional] 
 **page** | **int**| Number of page&lt;br&gt;Example: /api/events.json?page&#x3D;2 | [optional] 
 **archive** | **int**| returns event dates of events of archived or not archived festivals&lt;br&gt;Example: /api/events.json?archive&#x3D;1 | [optional] 
 **category** | [**list[int]**](int.md)| returns event dates of events that have a category with the given categoryId&lt;br&gt;Example: /api/events.json?category&#x3D;[100] | [optional] 
 **tag** | [**list[int]**](int.md)| returns event dates of events that have a tag with the given tagId&lt;br&gt;Example: /api/events.json?tag&#x3D;[100] | [optional] 
 **accessible** | [**list[int]**](int.md)| returns event dates of events that have a accessibility with the given accessibilityID&lt;br&gt;Example: /api/events.json?accessible&#x3D;[100] | [optional] 
 **location** | [**list[int]**](int.md)| returns event dates of events that have a location with the given locationID&lt;br&gt;Example: /api/events.json?location&#x3D;[100] | [optional] 
 **time** | [**list[str]**](str.md)| returns events with event dates in the given timeframe&lt;br&gt;Example: /api/events.json?time&#x3D;[\&quot;today\&quot;]&lt;br&gt;Possible Values:&lt;br&gt; - today&lt;br&gt; - upcoming&lt;br&gt; - past | [optional] 
 **from_date** | [**list[str]**](str.md)| returns events with event dates from the given date&lt;br&gt;Example: /api/events.json?fromDate&#x3D;[\&quot;2022-02-14 00:00:00\&quot;] | [optional] 
 **to_date** | [**list[str]**](str.md)| returns events with event dates to the given date&lt;br&gt;Example: /api/events.json?toDate&#x3D;[\&quot;2022-02-14 00:00:00\&quot;] | [optional] 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Dates**](Dates.md)

### Authorization

[basicAuth](../../../../Downloads/sb_db_api/README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../../../Downloads/sb_db_api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../Downloads/sb_db_api/README.md#documentation-for-models) [[Back to README]](../../../../Downloads/sb_db_api/README.md)
