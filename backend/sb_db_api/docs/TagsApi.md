# sb_db.TagsApi

All URIs are relative to *https://datenbank.sommerblut.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_tags**](TagsApi.md#get_all_tags) | **GET** /api/tags.json | get all tags
[**get_tag_by_id**](TagsApi.md#get_tag_by_id) | **GET** /api/tag/{tagId}.json | Find tag by ID

# **get_all_tags**
> Tags get_all_tags(accept_language=accept_language)

get all tags

get all tags without parameters

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
api_instance = sb_db.TagsApi(sb_db.ApiClient(configuration))
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # get all tags
    api_response = api_instance.get_all_tags(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_all_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Tags**](Tags.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_by_id**
> Tag get_tag_by_id(tag_id, accept_language=accept_language)

Find tag by ID

Returns a single tag

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
api_instance = sb_db.TagsApi(sb_db.ApiClient(configuration))
tag_id = 56 # int | ID of tag to return
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # Find tag by ID
    api_response = api_instance.get_tag_by_id(tag_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tag_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **int**| ID of tag to return | 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

