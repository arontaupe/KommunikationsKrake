# sb_db.FestivalsApi

All URIs are relative to *https://datenbank.sommerblut.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_festival_years**](FestivalsApi.md#get_all_festival_years) | **GET** /api/festivals/years.json | get all festival years
[**get_all_festivals**](FestivalsApi.md#get_all_festivals) | **GET** /api/festivals.json | get all festivals
[**get_festival_by_id**](FestivalsApi.md#get_festival_by_id) | **GET** /api/festivals/{festivalId}.json | find festival by ID

# **get_all_festival_years**
> list[str] get_all_festival_years(accept_language=accept_language)

get all festival years

get all festival years

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
api_instance = sb_db.FestivalsApi(sb_db.ApiClient(configuration))
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # get all festival years
    api_response = api_instance.get_all_festival_years(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FestivalsApi->get_all_festival_years: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| request specific language | [optional] 

### Return type

**list[str]**

### Authorization

[basicAuth](../../../../Downloads/sb_db_api/README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../../../Downloads/sb_db_api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../Downloads/sb_db_api/README.md#documentation-for-models) [[Back to README]](../../../../Downloads/sb_db_api/README.md)

# **get_all_festivals**
> Festivals get_all_festivals(year=year, archive=archive, accept_language=accept_language)

get all festivals

get all festivals without parameters

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
api_instance = sb_db.FestivalsApi(sb_db.ApiClient(configuration))
year = 56 # int | returns festivals of the given year (optional)
archive = true # bool | returns all archived or not archived festivals (value 0 or 1) (optional)
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # get all festivals
    api_response = api_instance.get_all_festivals(year=year, archive=archive, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FestivalsApi->get_all_festivals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| returns festivals of the given year | [optional] 
 **archive** | **bool**| returns all archived or not archived festivals (value 0 or 1) | [optional] 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Festivals**](Festivals.md)

### Authorization

[basicAuth](../../../../Downloads/sb_db_api/README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, Language

[[Back to top]](#) [[Back to API list]](../../../../Downloads/sb_db_api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../Downloads/sb_db_api/README.md#documentation-for-models) [[Back to README]](../../../../Downloads/sb_db_api/README.md)

# **get_festival_by_id**
> Festival get_festival_by_id(festival_id, accept_language=accept_language)

find festival by ID

returns a single festival

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
api_instance = sb_db.FestivalsApi(sb_db.ApiClient(configuration))
festival_id = 56 # int | ID of festival to return
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # find festival by ID
    api_response = api_instance.get_festival_by_id(festival_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FestivalsApi->get_festival_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **festival_id** | **int**| ID of festival to return | 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Festival**](Festival.md)

### Authorization

[basicAuth](../../../../Downloads/sb_db_api/README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../../../Downloads/sb_db_api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../Downloads/sb_db_api/README.md#documentation-for-models) [[Back to README]](../../../../Downloads/sb_db_api/README.md)
