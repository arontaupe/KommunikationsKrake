# sb_db.CategoriesApi

All URIs are relative to *https://datenbank.sommerblut.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_categories**](CategoriesApi.md#get_all_categories) | **GET** /api/categories.json | get all categories
[**get_all_current_categories**](CategoriesApi.md#get_all_current_categories) | **GET** /api/categories/current.json | get all current categories
[**get_category_by_id**](CategoriesApi.md#get_category_by_id) | **GET** /api/categories/{categoryId}.json | Find category by ID

# **get_all_categories**
> Categories get_all_categories(accept_language=accept_language)

get all categories

get all categories without parameters

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
api_instance = sb_db.CategoriesApi(sb_db.ApiClient(configuration))
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # get all categories
    api_response = api_instance.get_all_categories(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_all_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Categories**](Categories.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_current_categories**
> Categories get_all_current_categories(accept_language=accept_language)

get all current categories

get all categories that are selected in current events

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
api_instance = sb_db.CategoriesApi(sb_db.ApiClient(configuration))
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # get all current categories
    api_response = api_instance.get_all_current_categories(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_all_current_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Categories**](Categories.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_by_id**
> Categories get_category_by_id(category_id, accept_language=accept_language)

Find category by ID

Returns a single category

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
api_instance = sb_db.CategoriesApi(sb_db.ApiClient(configuration))
category_id = 56 # int | ID of category to return
accept_language = 'accept_language_example' # str | request specific language (optional)

try:
    # Find category by ID
    api_response = api_instance.get_category_by_id(category_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| ID of category to return | 
 **accept_language** | **str**| request specific language | [optional] 

### Return type

[**Categories**](Categories.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

