# coding: utf-8
#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class TenantControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.    
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_tenant_using_delete(self, tenant_id, **kwargs):  # noqa: E501
        """deleteTenant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.delete_tenant_using_delete(tenant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: tenantId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_tenant_using_delete_with_http_info(tenant_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_tenant_using_delete_with_http_info(tenant_id, **kwargs)  # noqa: E501
            return data

    def delete_tenant_using_delete_with_http_info(self, tenant_id, **kwargs):  # noqa: E501
        """deleteTenant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.delete_tenant_using_delete_with_http_info(tenant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: tenantId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params or
                params['tenant_id'] is None):
            raise ValueError(
                "Missing the required parameter `tenant_id` when calling `delete_tenant_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenantId'] = params['tenant_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/tenant/{tenantId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tenant_by_id_using_get(self, tenant_id, **kwargs):  # noqa: E501
        """getTenantById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenant_by_id_using_get(tenant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: tenantId (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tenant_by_id_using_get_with_http_info(tenant_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tenant_by_id_using_get_with_http_info(tenant_id, **kwargs)  # noqa: E501
            return data

    def get_tenant_by_id_using_get_with_http_info(self, tenant_id, **kwargs):  # noqa: E501
        """getTenantById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenant_by_id_using_get_with_http_info(tenant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: tenantId (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params or
                params['tenant_id'] is None):
            raise ValueError(
                "Missing the required parameter `tenant_id` when calling `get_tenant_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenantId'] = params['tenant_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/tenant/{tenantId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tenant',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tenants_using_get(self, page_size, page, **kwargs):  # noqa: E501
        """getTenants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenants_using_get(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :return: TextPageDataTenant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tenants_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tenants_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
            return data

    def get_tenants_using_get_with_http_info(self, page_size, page, **kwargs):  # noqa: E501
        """getTenants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenants_using_get_with_http_info(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :return: TextPageDataTenant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['text_search', 'sort_property', 'sort_order', 'page_size', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError(
                "Missing the required parameter `page_size` when calling `get_tenants_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_tenants_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/tenants{?textSearch,sortProperty,sortOrder,pageSize,page}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TextPageDataTenant',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_tenant_using_post(self, tenant, **kwargs):  # noqa: E501
        """saveTenant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.save_tenant_using_post(tenant, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Tenant tenant: tenant (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_tenant_using_post_with_http_info(tenant, **kwargs)  # noqa: E501
        else:
            (data) = self.save_tenant_using_post_with_http_info(tenant, **kwargs)  # noqa: E501
            return data

    def save_tenant_using_post_with_http_info(self, tenant, **kwargs):  # noqa: E501
        """saveTenant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.save_tenant_using_post_with_http_info(tenant, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Tenant tenant: tenant (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant' is set
        if ('tenant' not in params or
                params['tenant'] is None):
            raise ValueError(
                "Missing the required parameter `tenant` when calling `save_tenant_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tenant' in params:
            body_params = params['tenant']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/tenant', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tenant',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tenant_info_by_id_using_get(self, tenant_id, **kwargs):
        """getTenantInfoById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenant_info_by_id_using_get(tenant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: tenantId (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tenant_info_by_id_using_get_with_http_info(tenant_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tenant_info_by_id_using_get_with_http_info(tenant_id, **kwargs)  # noqa: E501
            return data

    def get_tenant_info_by_id_using_get_with_http_info(self, tenant_id, **kwargs):
        """getTenantInfoById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenant_info_by_id_using_get_with_http_info(tenant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: tenantId (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params or
                params['tenant_id'] is None):
            raise ValueError(
                "Missing the required parameter `tenant_id` when calling `get_tenant_info_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        if 'tenant_id' in params:
            path_params['tenantId'] = params['tenant_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/tenant/info/{tenantId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tenant',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tenant_infos_using_get(self, page_size, page, **kwargs):
        """getTenantInfos  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenant_infos_using_get(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :return: list[Tenant]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tenant_infos_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tenant_infos_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
            return data

    def get_tenant_infos_using_get_with_http_info(self, page_size, page, **kwargs):
        """getTenantInfos  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenant_infos_using_get_with_http_info(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :return: list[Tenant]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['text_search', 'sort_property', 'sort_order', 'page_size', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError(
                "Missing the required parameter `page_size` when calling `get_tenant_infos_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError(
                "Missing the required parameter `page` when calling `get_tenant_infos_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/tenantInfos{?textSearch,sortProperty,sortOrder,pageSize,page}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Tenant]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)