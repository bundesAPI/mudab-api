# mudab.DefaultApi

All URIs are relative to *https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_mess_stationen**](DefaultApi.md#list_mess_stationen) | **POST** /STATION_SMALL | Liste aller Messstationen
[**list_messwerte_plc**](DefaultApi.md#list_messwerte_plc) | **POST** /V_MESSWERTE_PLC | Liste aller Messwerte der gefilterten PLC Stationen
[**list_parameter**](DefaultApi.md#list_parameter) | **POST** /MV_PARAMETER | Liste aller Parameter
[**list_parameter_values**](DefaultApi.md#list_parameter_values) | **POST** /MV_STATION_MSMNT | Liste aller Messwerte
[**list_parameters_biologie**](DefaultApi.md#list_parameters_biologie) | **POST** /MV_PARAMETER_BIOLOGIE | Liste aller Parameter im Biologie Kompartiment
[**list_parameters_biota**](DefaultApi.md#list_parameters_biota) | **POST** /MV_PARAMETER_BIOTA | Liste aller Parameter im Biota Kompartiment
[**list_parameters_plc**](DefaultApi.md#list_parameters_plc) | **POST** /V_GEMESSENE_PARA_PLC | Liste aller Parameter der PLC Stationen
[**list_parameters_sediment**](DefaultApi.md#list_parameters_sediment) | **POST** /MV_PARAMETER_SEDIMENT | Liste aller Parameter im Sediment Kompartiment
[**list_parameters_wasser**](DefaultApi.md#list_parameters_wasser) | **POST** /MV_PARAMETER_WASSER | Liste aller Parameter im Wasser Kompartiment
[**list_plc_stations**](DefaultApi.md#list_plc_stations) | **POST** /V_PLC_STATION | Liste aller HELCOM PLC Stationen
[**list_projekt_stationen**](DefaultApi.md#list_projekt_stationen) | **POST** /PROJECTSTATION_SMALL | Liste aller Projekt Stationen


# **list_mess_stationen**
> ListMessStationen200Response list_mess_stationen()

Liste aller Messstationen

Gibt eine filterbare Liste aller Messtationen in der Datenbank zurück. Filterbare Attribute sind die Felder die aus dem Messstation Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.filter_request import FilterRequest
from deutschland.mudab.model.list_mess_stationen200_response import ListMessStationen200Response
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Messstationen
        api_response = api_instance.list_mess_stationen(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_mess_stationen: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**ListMessStationen200Response**](ListMessStationen200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_messwerte_plc**
> ListMesswertePlc200Response list_messwerte_plc()

Liste aller Messwerte der gefilterten PLC Stationen

Gibt eine filterbare Liste aller Messwerte welche durch PLC Stationen gemessen wurden zurück. Filterbare Attribute sind die Felder die aus dem MesswertPLC Schema kommen, z.B. STATION_CODE 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.list_messwerte_plc200_response import ListMesswertePlc200Response
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Messwerte der gefilterten PLC Stationen
        api_response = api_instance.list_messwerte_plc(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_messwerte_plc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**ListMesswertePlc200Response**](ListMesswertePlc200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameter**
> ListParameter200Response list_parameter()

Liste aller Parameter

Gibt eine filterbare Liste aller Parameter in der Datenbank zurück. Filterbare Attribute sind die Felder die aus dem Parameter Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.list_parameter200_response import ListParameter200Response
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Parameter
        api_response = api_instance.list_parameter(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_parameter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**ListParameter200Response**](ListParameter200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameter_values**
> ListParameterValues200Response list_parameter_values()

Liste aller Messwerte

Gibt eine filterbare Liste aller Messwerte in der Datenbank zurück. Filterbare Attribute sind die Felder die aus dem ParameterValue Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.list_parameter_values200_response import ListParameterValues200Response
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Messwerte
        api_response = api_instance.list_parameter_values(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_parameter_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**ListParameterValues200Response**](ListParameterValues200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameters_biologie**
> ListParametersBiologie200Response list_parameters_biologie()

Liste aller Parameter im Biologie Kompartiment

Gibt eine filterbare Liste aller Parameter in der Datenbank aus dem Kompartiment Biologie zurück. Filterbare Attribute sind die Felder die aus dem Parameter Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.list_parameters_biologie200_response import ListParametersBiologie200Response
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Parameter im Biologie Kompartiment
        api_response = api_instance.list_parameters_biologie(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_parameters_biologie: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**ListParametersBiologie200Response**](ListParametersBiologie200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameters_biota**
> ListParametersBiota200Response list_parameters_biota()

Liste aller Parameter im Biota Kompartiment

Gibt eine filterbare Liste aller Parameter in der Datenbank aus dem Kompartiment Biota zurück. Filterbare Attribute sind die Felder die aus dem Parameter Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.list_parameters_biota200_response import ListParametersBiota200Response
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Parameter im Biota Kompartiment
        api_response = api_instance.list_parameters_biota(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_parameters_biota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**ListParametersBiota200Response**](ListParametersBiota200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameters_plc**
> ListParametersPlc200Response list_parameters_plc()

Liste aller Parameter der PLC Stationen

Gibt eine filterbare Liste aller Parameter welche durch die gefilterten PLC Stationen gemessen werden zurück. Filterbare Attribute sind die Felder die aus dem ParameterPLC Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.filter_request import FilterRequest
from deutschland.mudab.model.list_parameters_plc200_response import ListParametersPlc200Response
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Parameter der PLC Stationen
        api_response = api_instance.list_parameters_plc(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_parameters_plc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**ListParametersPlc200Response**](ListParametersPlc200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameters_sediment**
> ListParametersSediment200Response list_parameters_sediment()

Liste aller Parameter im Sediment Kompartiment

Gibt eine filterbare Liste aller Parameter in der Datenbank aus dem Kompartiment Sediment zurück. Filterbare Attribute sind die Felder die aus dem Parameter Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.filter_request import FilterRequest
from deutschland.mudab.model.list_parameters_sediment200_response import ListParametersSediment200Response
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Parameter im Sediment Kompartiment
        api_response = api_instance.list_parameters_sediment(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_parameters_sediment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**ListParametersSediment200Response**](ListParametersSediment200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameters_wasser**
> ListParametersWasser200Response list_parameters_wasser()

Liste aller Parameter im Wasser Kompartiment

Gibt eine filterbare Liste aller Parameter in der Datenbank aus dem Kompartiment Wasser zurück. Filterbare Attribute sind die Felder die aus dem Parameter Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.list_parameters_wasser200_response import ListParametersWasser200Response
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Parameter im Wasser Kompartiment
        api_response = api_instance.list_parameters_wasser(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_parameters_wasser: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**ListParametersWasser200Response**](ListParametersWasser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_plc_stations**
> ListPlcStations200Response list_plc_stations()

Liste aller HELCOM PLC Stationen

Gibt eine filterbare Liste aller HELCOM PLC Stationen in der Datenbank zurück. Filterbare Attribute sind die Felder die aus dem HelcomPLCStation Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.list_plc_stations200_response import ListPlcStations200Response
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller HELCOM PLC Stationen
        api_response = api_instance.list_plc_stations(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_plc_stations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**ListPlcStations200Response**](ListPlcStations200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projekt_stationen**
> ListProjektStationen200Response list_projekt_stationen()

Liste aller Projekt Stationen

Gibt eine filterbare Liste aller Projektstation in der Datenbank zurück. Filterbare Attribute sind die Felder die aus dem ProjectStation Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.list_projekt_stationen200_response import ListProjektStationen200Response
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/mudab/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Projekt Stationen
        api_response = api_instance.list_projekt_stationen(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_projekt_stationen: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**ListProjektStationen200Response**](ListProjektStationen200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

