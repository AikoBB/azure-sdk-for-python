# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._support_tickets_operations import (
    build_check_name_availability_request,
    build_create_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SupportTicketsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.support.aio.MicrosoftSupport`'s
        :attr:`support_tickets` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def check_name_availability(
        self,
        check_name_availability_input: _models.CheckNameAvailabilityInput,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CheckNameAvailabilityOutput:
        """Check the availability of a resource name. This API should be used to check the uniqueness of
        the name for support ticket creation for the selected subscription.

        :param check_name_availability_input: Input to check. Required.
        :type check_name_availability_input: ~azure.mgmt.support.models.CheckNameAvailabilityInput
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CheckNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.support.models.CheckNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def check_name_availability(
        self, check_name_availability_input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CheckNameAvailabilityOutput:
        """Check the availability of a resource name. This API should be used to check the uniqueness of
        the name for support ticket creation for the selected subscription.

        :param check_name_availability_input: Input to check. Required.
        :type check_name_availability_input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CheckNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.support.models.CheckNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def check_name_availability(
        self, check_name_availability_input: Union[_models.CheckNameAvailabilityInput, IO[bytes]], **kwargs: Any
    ) -> _models.CheckNameAvailabilityOutput:
        """Check the availability of a resource name. This API should be used to check the uniqueness of
        the name for support ticket creation for the selected subscription.

        :param check_name_availability_input: Input to check. Is either a CheckNameAvailabilityInput
         type or a IO[bytes] type. Required.
        :type check_name_availability_input: ~azure.mgmt.support.models.CheckNameAvailabilityInput or
         IO[bytes]
        :return: CheckNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.support.models.CheckNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CheckNameAvailabilityOutput] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(check_name_availability_input, (IOBase, bytes)):
            _content = check_name_availability_input
        else:
            _json = self._serialize.body(check_name_availability_input, "CheckNameAvailabilityInput")

        _request = build_check_name_availability_request(
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CheckNameAvailabilityOutput", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list(
        self, top: Optional[int] = None, filter: Optional[str] = None, **kwargs: Any
    ) -> AsyncIterable["_models.SupportTicketDetails"]:
        """Lists all the support tickets for an Azure subscription. You can also filter the support
        tickets by *Status*\ , *CreatedDate*\ , *ServiceId*\ , and *ProblemClassificationId* using the
        $filter parameter. Output will be a paged result with *nextLink*\ , using which you can
        retrieve the next set of support tickets. :code:`<br/>`:code:`<br/>`Support ticket data is
        available for 18 months after ticket creation. If a ticket was created more than 18 months ago,
        a request for data might cause an error.

        :param top: The number of values to return in the collection. Default is 25 and max is 100.
         Default value is None.
        :type top: int
        :param filter: The filter to apply on the operation. We support 'odata v4.0' filter semantics.
         `Learn more <https://docs.microsoft.com/odata/concepts/queryoptions-overview>`_. *Status*\ ,
         *ServiceId*\ , and *ProblemClassificationId* filters can only be used with Equals ('eq')
         operator. For *CreatedDate* filter, the supported operators are Greater Than ('gt') and Greater
         Than or Equals ('ge'). When using both filters, combine them using the logical 'AND'. Default
         value is None.
        :type filter: str
        :return: An iterator like instance of either SupportTicketDetails or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.support.models.SupportTicketDetails]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.SupportTicketsListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    top=top,
                    filter=filter,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SupportTicketsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def get(self, support_ticket_name: str, **kwargs: Any) -> _models.SupportTicketDetails:
        """Get ticket details for an Azure subscription. Support ticket data is available for 18 months
        after ticket creation. If a ticket was created more than 18 months ago, a request for data
        might cause an error.

        :param support_ticket_name: Support ticket name. Required.
        :type support_ticket_name: str
        :return: SupportTicketDetails or the result of cls(response)
        :rtype: ~azure.mgmt.support.models.SupportTicketDetails
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.SupportTicketDetails] = kwargs.pop("cls", None)

        _request = build_get_request(
            support_ticket_name=support_ticket_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SupportTicketDetails", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self,
        support_ticket_name: str,
        update_support_ticket: _models.UpdateSupportTicket,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SupportTicketDetails:
        """This API allows you to update the severity level, ticket status, advanced diagnostic consent
        and your contact information in the support ticket.:code:`<br/>`:code:`<br/>`Note: The severity
        levels cannot be changed if a support ticket is actively being worked upon by an Azure support
        engineer. In such a case, contact your support engineer to request severity update by adding a
        new communication using the Communications API.

        :param support_ticket_name: Support ticket name. Required.
        :type support_ticket_name: str
        :param update_support_ticket: UpdateSupportTicket object. Required.
        :type update_support_ticket: ~azure.mgmt.support.models.UpdateSupportTicket
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SupportTicketDetails or the result of cls(response)
        :rtype: ~azure.mgmt.support.models.SupportTicketDetails
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        support_ticket_name: str,
        update_support_ticket: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SupportTicketDetails:
        """This API allows you to update the severity level, ticket status, advanced diagnostic consent
        and your contact information in the support ticket.:code:`<br/>`:code:`<br/>`Note: The severity
        levels cannot be changed if a support ticket is actively being worked upon by an Azure support
        engineer. In such a case, contact your support engineer to request severity update by adding a
        new communication using the Communications API.

        :param support_ticket_name: Support ticket name. Required.
        :type support_ticket_name: str
        :param update_support_ticket: UpdateSupportTicket object. Required.
        :type update_support_ticket: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SupportTicketDetails or the result of cls(response)
        :rtype: ~azure.mgmt.support.models.SupportTicketDetails
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        support_ticket_name: str,
        update_support_ticket: Union[_models.UpdateSupportTicket, IO[bytes]],
        **kwargs: Any
    ) -> _models.SupportTicketDetails:
        """This API allows you to update the severity level, ticket status, advanced diagnostic consent
        and your contact information in the support ticket.:code:`<br/>`:code:`<br/>`Note: The severity
        levels cannot be changed if a support ticket is actively being worked upon by an Azure support
        engineer. In such a case, contact your support engineer to request severity update by adding a
        new communication using the Communications API.

        :param support_ticket_name: Support ticket name. Required.
        :type support_ticket_name: str
        :param update_support_ticket: UpdateSupportTicket object. Is either a UpdateSupportTicket type
         or a IO[bytes] type. Required.
        :type update_support_ticket: ~azure.mgmt.support.models.UpdateSupportTicket or IO[bytes]
        :return: SupportTicketDetails or the result of cls(response)
        :rtype: ~azure.mgmt.support.models.SupportTicketDetails
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SupportTicketDetails] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(update_support_ticket, (IOBase, bytes)):
            _content = update_support_ticket
        else:
            _json = self._serialize.body(update_support_ticket, "UpdateSupportTicket")

        _request = build_update_request(
            support_ticket_name=support_ticket_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SupportTicketDetails", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _create_initial(
        self,
        support_ticket_name: str,
        create_support_ticket_parameters: Union[_models.SupportTicketDetails, IO[bytes]],
        **kwargs: Any
    ) -> Optional[_models.SupportTicketDetails]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.SupportTicketDetails]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_support_ticket_parameters, (IOBase, bytes)):
            _content = create_support_ticket_parameters
        else:
            _json = self._serialize.body(create_support_ticket_parameters, "SupportTicketDetails")

        _request = build_create_request(
            support_ticket_name=support_ticket_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("SupportTicketDetails", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create(
        self,
        support_ticket_name: str,
        create_support_ticket_parameters: _models.SupportTicketDetails,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SupportTicketDetails]:
        """Creates a new support ticket for Subscription and Service limits (Quota), Technical, Billing,
        and Subscription Management issues for the specified subscription. Learn the `prerequisites
        <https://aka.ms/supportAPI>`_ required to create a support
        ticket.:code:`<br/>`:code:`<br/>`Always call the Services and ProblemClassifications API to get
        the most recent set of services and problem categories required for support ticket
        creation.:code:`<br/>`:code:`<br/>`Adding attachments is not currently supported via the API.
        To add a file to an existing support ticket, visit the `Manage support ticket
        <https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/managesupportrequest>`_
        page in the Azure portal, select the support ticket, and use the file upload control to add a
        new file.:code:`<br/>`:code:`<br/>`Providing consent to share diagnostic information with Azure
        support is currently not supported via the API. The Azure support engineer working on your
        ticket will reach out to you for consent if your issue requires gathering diagnostic
        information from your Azure resources.:code:`<br/>`:code:`<br/>`\ **Creating a support ticket
        for on-behalf-of**\ : Include *x-ms-authorization-auxiliary* header to provide an auxiliary
        token as per `documentation
        <https://docs.microsoft.com/azure/azure-resource-manager/management/authenticate-multi-tenant>`_.
        The primary token will be from the tenant for whom a support ticket is being raised against the
        subscription, i.e. Cloud solution provider (CSP) customer tenant. The auxiliary token will be
        from the Cloud solution provider (CSP) partner tenant.

        :param support_ticket_name: Support ticket name. Required.
        :type support_ticket_name: str
        :param create_support_ticket_parameters: Support ticket request payload. Required.
        :type create_support_ticket_parameters: ~azure.mgmt.support.models.SupportTicketDetails
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either SupportTicketDetails or the result
         of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.support.models.SupportTicketDetails]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create(
        self,
        support_ticket_name: str,
        create_support_ticket_parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SupportTicketDetails]:
        """Creates a new support ticket for Subscription and Service limits (Quota), Technical, Billing,
        and Subscription Management issues for the specified subscription. Learn the `prerequisites
        <https://aka.ms/supportAPI>`_ required to create a support
        ticket.:code:`<br/>`:code:`<br/>`Always call the Services and ProblemClassifications API to get
        the most recent set of services and problem categories required for support ticket
        creation.:code:`<br/>`:code:`<br/>`Adding attachments is not currently supported via the API.
        To add a file to an existing support ticket, visit the `Manage support ticket
        <https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/managesupportrequest>`_
        page in the Azure portal, select the support ticket, and use the file upload control to add a
        new file.:code:`<br/>`:code:`<br/>`Providing consent to share diagnostic information with Azure
        support is currently not supported via the API. The Azure support engineer working on your
        ticket will reach out to you for consent if your issue requires gathering diagnostic
        information from your Azure resources.:code:`<br/>`:code:`<br/>`\ **Creating a support ticket
        for on-behalf-of**\ : Include *x-ms-authorization-auxiliary* header to provide an auxiliary
        token as per `documentation
        <https://docs.microsoft.com/azure/azure-resource-manager/management/authenticate-multi-tenant>`_.
        The primary token will be from the tenant for whom a support ticket is being raised against the
        subscription, i.e. Cloud solution provider (CSP) customer tenant. The auxiliary token will be
        from the Cloud solution provider (CSP) partner tenant.

        :param support_ticket_name: Support ticket name. Required.
        :type support_ticket_name: str
        :param create_support_ticket_parameters: Support ticket request payload. Required.
        :type create_support_ticket_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either SupportTicketDetails or the result
         of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.support.models.SupportTicketDetails]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create(
        self,
        support_ticket_name: str,
        create_support_ticket_parameters: Union[_models.SupportTicketDetails, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SupportTicketDetails]:
        """Creates a new support ticket for Subscription and Service limits (Quota), Technical, Billing,
        and Subscription Management issues for the specified subscription. Learn the `prerequisites
        <https://aka.ms/supportAPI>`_ required to create a support
        ticket.:code:`<br/>`:code:`<br/>`Always call the Services and ProblemClassifications API to get
        the most recent set of services and problem categories required for support ticket
        creation.:code:`<br/>`:code:`<br/>`Adding attachments is not currently supported via the API.
        To add a file to an existing support ticket, visit the `Manage support ticket
        <https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/managesupportrequest>`_
        page in the Azure portal, select the support ticket, and use the file upload control to add a
        new file.:code:`<br/>`:code:`<br/>`Providing consent to share diagnostic information with Azure
        support is currently not supported via the API. The Azure support engineer working on your
        ticket will reach out to you for consent if your issue requires gathering diagnostic
        information from your Azure resources.:code:`<br/>`:code:`<br/>`\ **Creating a support ticket
        for on-behalf-of**\ : Include *x-ms-authorization-auxiliary* header to provide an auxiliary
        token as per `documentation
        <https://docs.microsoft.com/azure/azure-resource-manager/management/authenticate-multi-tenant>`_.
        The primary token will be from the tenant for whom a support ticket is being raised against the
        subscription, i.e. Cloud solution provider (CSP) customer tenant. The auxiliary token will be
        from the Cloud solution provider (CSP) partner tenant.

        :param support_ticket_name: Support ticket name. Required.
        :type support_ticket_name: str
        :param create_support_ticket_parameters: Support ticket request payload. Is either a
         SupportTicketDetails type or a IO[bytes] type. Required.
        :type create_support_ticket_parameters: ~azure.mgmt.support.models.SupportTicketDetails or
         IO[bytes]
        :return: An instance of AsyncLROPoller that returns either SupportTicketDetails or the result
         of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.support.models.SupportTicketDetails]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SupportTicketDetails] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_initial(
                support_ticket_name=support_ticket_name,
                create_support_ticket_parameters=create_support_ticket_parameters,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("SupportTicketDetails", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.SupportTicketDetails].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.SupportTicketDetails](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )
