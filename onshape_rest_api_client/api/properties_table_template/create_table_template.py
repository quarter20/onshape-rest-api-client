from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_properties_table_template_info import BTPropertiesTableTemplateInfo
from ...models.bt_properties_table_template_params import BTPropertiesTableTemplateParams
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BTPropertiesTableTemplateParams,
    template_group_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["templateGroupId"] = template_group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tabletemplates",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTPropertiesTableTemplateInfo:
    response_default = BTPropertiesTableTemplateInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTPropertiesTableTemplateInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BTPropertiesTableTemplateParams,
    template_group_id: str | Unset = UNSET,
) -> Response[BTPropertiesTableTemplateInfo]:
    """Create a new properties table template.

    Args:
        template_group_id (str | Unset):
        body (BTPropertiesTableTemplateParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTPropertiesTableTemplateInfo]
    """

    kwargs = _get_kwargs(
        body=body,
        template_group_id=template_group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BTPropertiesTableTemplateParams,
    template_group_id: str | Unset = UNSET,
) -> BTPropertiesTableTemplateInfo | None:
    """Create a new properties table template.

    Args:
        template_group_id (str | Unset):
        body (BTPropertiesTableTemplateParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTPropertiesTableTemplateInfo
    """

    return sync_detailed(
        client=client,
        body=body,
        template_group_id=template_group_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BTPropertiesTableTemplateParams,
    template_group_id: str | Unset = UNSET,
) -> Response[BTPropertiesTableTemplateInfo]:
    """Create a new properties table template.

    Args:
        template_group_id (str | Unset):
        body (BTPropertiesTableTemplateParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTPropertiesTableTemplateInfo]
    """

    kwargs = _get_kwargs(
        body=body,
        template_group_id=template_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BTPropertiesTableTemplateParams,
    template_group_id: str | Unset = UNSET,
) -> BTPropertiesTableTemplateInfo | None:
    """Create a new properties table template.

    Args:
        template_group_id (str | Unset):
        body (BTPropertiesTableTemplateParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTPropertiesTableTemplateInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            template_group_id=template_group_id,
        )
    ).parsed
