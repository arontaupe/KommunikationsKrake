# sb_db.AccessibilitiesApi

All URIs are relative to *https://datenbank.sommerblut.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accessibility_by_id**](AccessibilitiesApi.md#get_accessibility_by_id) | **GET** /api/accessibilities/{accessibilityId}.json | Find accessibility by ID
[**get_all_accessibilities**](AccessibilitiesApi.md#get_all_accessibilities) | **GET** /api/accessibilities.json | get all accessibilities

# **get_accessibility_by_id**
> Accessibility get_accessibility_by_id(accessibility_id, accept_language=accept_language)

Find accessibility by ID

Returns a single accessibility

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
api_instance = sb_db.AccessibilitiesApi(sb_db.ApiClient(configuration))
accessibility_id = 56 # int | ID of accessibility to return
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # Find accessibility by ID
    api_response = api_instance.get_accessibility_by_id(accessibility_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessibilitiesApi->get_accessibility_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessibility_id** | **int**| ID of accessibility to return | 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Accessibility**](Accessibility.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_accessibilities**
> Accessibilities get_all_accessibilities(accept_language=accept_language)

get all accessibilities

get all accessibilities without parameters

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
api_instance = sb_db.AccessibilitiesApi(sb_db.ApiClient(configuration))
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # get all accessibilities
    api_response = api_instance.get_all_accessibilities(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessibilitiesApi->get_all_accessibilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Accessibilities**](Accessibilities.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

