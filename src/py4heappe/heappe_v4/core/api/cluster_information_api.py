# coding: utf-8

"""
    HEAppE Web API

    HEAppE middleware API v4.2.1  # noqa: E501

    OpenAPI spec version: v4.2.1
    Contact: support.heappe@it4i.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from py4heappe.heappe_v4.core.api_client import ApiClient


class ClusterInformationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def heappe_cluster_information_current_cluster_node_usage_get(self, **kwargs):  # noqa: E501
        """Get actual cluster node usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_cluster_information_current_cluster_node_usage_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: Session code
        :param int ClusterNodeId: ClusterNode ID
        :param int ProjectId: Project ID
        :return: ClusterNodeUsageExt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_cluster_information_current_cluster_node_usage_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_cluster_information_current_cluster_node_usage_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_cluster_information_current_cluster_node_usage_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get actual cluster node usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_cluster_information_current_cluster_node_usage_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: Session code
        :param int ClusterNodeId: ClusterNode ID
        :param int ProjectId: Project ID
        :return: ClusterNodeUsageExt
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['SessionCode', 'ClusterNodeId', 'ProjectId']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_cluster_information_current_cluster_node_usage_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'SessionCode' in params:
            query_params.append(('SessionCode', params['SessionCode']))  # noqa: E501
        if 'ClusterNodeId' in params:
            query_params.append(('ClusterNodeId', params['ClusterNodeId']))  # noqa: E501
        if 'ProjectId' in params:
            query_params.append(('ProjectId', params['ProjectId']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heappe/ClusterInformation/CurrentClusterNodeUsage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClusterNodeUsageExt',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_cluster_information_list_available_clusters_get(self, **kwargs):  # noqa: E501
        """Get available clusters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_cluster_information_list_available_clusters_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ClusterExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_cluster_information_list_available_clusters_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_cluster_information_list_available_clusters_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_cluster_information_list_available_clusters_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get available clusters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_cluster_information_list_available_clusters_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ClusterExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_cluster_information_list_available_clusters_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heappe/ClusterInformation/ListAvailableClusters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ClusterExt]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_cluster_information_request_command_template_parameters_name_post(self, **kwargs):  # noqa: E501
        """Get command template parameters name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_cluster_information_request_command_template_parameters_name_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetCommandTemplateParametersNameModel body:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_cluster_information_request_command_template_parameters_name_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_cluster_information_request_command_template_parameters_name_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_cluster_information_request_command_template_parameters_name_post_with_http_info(self, **kwargs):  # noqa: E501
        """Get command template parameters name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_cluster_information_request_command_template_parameters_name_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetCommandTemplateParametersNameModel body:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_cluster_information_request_command_template_parameters_name_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heappe/ClusterInformation/RequestCommandTemplateParametersName', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
