# coding: utf-8

"""
    Sommerblut-Database

    Event and festival info  # noqa: E501

    OpenAPI spec version: 1.5.0
    Contact: support@xtain.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sb_db.api_client import ApiClient


class AccessibilitiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_accessibility_by_id(self, accessibility_id, **kwargs):  # noqa: E501
        """Find accessibility by ID  # noqa: E501

        Returns a single accessibility  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_accessibility_by_id(accessibility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int accessibility_id: ID of accessibility to return (required)
        :param str accept_language: request specific language
        :return: Accessibility
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_accessibility_by_id_with_http_info(accessibility_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_accessibility_by_id_with_http_info(accessibility_id, **kwargs)  # noqa: E501
            return data

    def get_accessibility_by_id_with_http_info(self, accessibility_id, **kwargs):  # noqa: E501
        """Find accessibility by ID  # noqa: E501

        Returns a single accessibility  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_accessibility_by_id_with_http_info(accessibility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int accessibility_id: ID of accessibility to return (required)
        :param str accept_language: request specific language
        :return: Accessibility
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['accessibility_id', 'accept_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_accessibility_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'accessibility_id' is set
        if ('accessibility_id' not in params or
                params['accessibility_id'] is None):
            raise ValueError("Missing the required parameter `accessibility_id` when calling `get_accessibility_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'accessibility_id' in params:
            path_params['accessibilityId'] = params['accessibility_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/accessibilities/{accessibilityId}.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Accessibility',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_accessibilities(self, **kwargs):  # noqa: E501
        """get all accessibilities  # noqa: E501

        get all accessibilities without parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_accessibilities(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str accept_language: request specific language
        :return: Accessibilities
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_accessibilities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_accessibilities_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_accessibilities_with_http_info(self, **kwargs):  # noqa: E501
        """get all accessibilities  # noqa: E501

        get all accessibilities without parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_accessibilities_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str accept_language: request specific language
        :return: Accessibilities
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['accept_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_accessibilities" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/accessibilities.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Accessibilities',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
