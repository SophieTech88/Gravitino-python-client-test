# swagger_client.DefaultApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_metalakes_get**](DefaultApi.md#api_metalakes_get) | **GET** /api/metalakes | 

# **api_metalakes_get**
> Metalakes api_metalakes_get()



Returns a list of all metalakes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.api_metalakes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_metalakes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Metalakes**](Metalakes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

