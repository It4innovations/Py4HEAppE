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


class FileTransferApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def heappe_file_transfer_close_file_transfer_post(self, **kwargs):  # noqa: E501
        """Close file transfer tunnel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_file_transfer_close_file_transfer_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EndFileTransferModel body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_file_transfer_close_file_transfer_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_file_transfer_close_file_transfer_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_file_transfer_close_file_transfer_post_with_http_info(self, **kwargs):  # noqa: E501
        """Close file transfer tunnel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_file_transfer_close_file_transfer_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EndFileTransferModel body:
        :return: str
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
                    " to method heappe_file_transfer_close_file_transfer_post" % key
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
            '/heappe/FileTransfer/CloseFileTransfer', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_file_transfer_download_file_from_cluster_post(self, **kwargs):  # noqa: E501
        """Download specific file from Cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_file_transfer_download_file_from_cluster_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DownloadFileFromClusterModel body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_file_transfer_download_file_from_cluster_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_file_transfer_download_file_from_cluster_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_file_transfer_download_file_from_cluster_post_with_http_info(self, **kwargs):  # noqa: E501
        """Download specific file from Cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_file_transfer_download_file_from_cluster_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DownloadFileFromClusterModel body:
        :return: str
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
                    " to method heappe_file_transfer_download_file_from_cluster_post" % key
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
            '/heappe/FileTransfer/DownloadFileFromCluster', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_file_transfer_download_parts_of_job_files_from_cluster_post(self, **kwargs):  # noqa: E501
        """Download part of job files from Cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_file_transfer_download_parts_of_job_files_from_cluster_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DownloadPartsOfJobFilesFromClusterModel body:
        :return: list[JobFileContentExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_file_transfer_download_parts_of_job_files_from_cluster_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_file_transfer_download_parts_of_job_files_from_cluster_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_file_transfer_download_parts_of_job_files_from_cluster_post_with_http_info(self, **kwargs):  # noqa: E501
        """Download part of job files from Cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_file_transfer_download_parts_of_job_files_from_cluster_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DownloadPartsOfJobFilesFromClusterModel body:
        :return: list[JobFileContentExt]
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
                    " to method heappe_file_transfer_download_parts_of_job_files_from_cluster_post" % key
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
            '/heappe/FileTransfer/DownloadPartsOfJobFilesFromCluster', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JobFileContentExt]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_file_transfer_list_changed_files_for_job_get(self, **kwargs):  # noqa: E501
        """Get all changes files during job execution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_file_transfer_list_changed_files_for_job_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: Session code
        :param int SubmittedJobInfoId: SubmittedJobInfo ID
        :return: list[FileInformationExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_file_transfer_list_changed_files_for_job_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_file_transfer_list_changed_files_for_job_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_file_transfer_list_changed_files_for_job_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all changes files during job execution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_file_transfer_list_changed_files_for_job_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: Session code
        :param int SubmittedJobInfoId: SubmittedJobInfo ID
        :return: list[FileInformationExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['SessionCode', 'SubmittedJobInfoId']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_file_transfer_list_changed_files_for_job_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'SessionCode' in params:
            query_params.append(('SessionCode', params['SessionCode']))  # noqa: E501
        if 'SubmittedJobInfoId' in params:
            query_params.append(('SubmittedJobInfoId', params['SubmittedJobInfoId']))  # noqa: E501

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
            '/heappe/FileTransfer/ListChangedFilesForJob', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FileInformationExt]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_file_transfer_request_file_transfer_post(self, **kwargs):  # noqa: E501
        """Create file transfer tunnel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_file_transfer_request_file_transfer_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetFileTransferMethodModel body:
        :return: FileTransferMethodExt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_file_transfer_request_file_transfer_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_file_transfer_request_file_transfer_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_file_transfer_request_file_transfer_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create file transfer tunnel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_file_transfer_request_file_transfer_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetFileTransferMethodModel body:
        :return: FileTransferMethodExt
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
                    " to method heappe_file_transfer_request_file_transfer_post" % key
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
            '/heappe/FileTransfer/RequestFileTransfer', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileTransferMethodExt',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
