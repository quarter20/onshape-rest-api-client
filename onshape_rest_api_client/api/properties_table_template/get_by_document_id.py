from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_properties_table_template_info import BTPropertiesTableTemplateInfo
from ...models.bt_properties_table_template_type import BTPropertiesTableTemplateType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    *,
    template_type: BTPropertiesTableTemplateType | Unset = UNSET,
    only_active: bool | Unset = True,
    include_defaults: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_template_type: str | Unset = UNSET
    if not isinstance(template_type, Unset):
        json_template_type = template_type.value

    params["templateType"] = json_template_type

    params["onlyActive"] = only_active

    params["includeDefaults"] = include_defaults

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tabletemplates/d/{did}".format(
            did=quote(str(did), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[BTPropertiesTableTemplateInfo]:
    response_default = []
    _response_default = response.json()
    for response_default_item_data in _response_default:
        response_default_item = BTPropertiesTableTemplateInfo.from_dict(response_default_item_data)

        response_default.append(response_default_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[BTPropertiesTableTemplateInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    *,
    client: AuthenticatedClient,
    template_type: BTPropertiesTableTemplateType | Unset = UNSET,
    only_active: bool | Unset = True,
    include_defaults: bool | Unset = True,
) -> Response[list[BTPropertiesTableTemplateInfo]]:
    """Get all table templates that are available to use on the provided document.

    Args:
        did (str):
        template_type (BTPropertiesTableTemplateType | Unset):
        only_active (bool | Unset):  Default: True.
        include_defaults (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTPropertiesTableTemplateInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        template_type=template_type,
        only_active=only_active,
        include_defaults=include_defaults,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    *,
    client: AuthenticatedClient,
    template_type: BTPropertiesTableTemplateType | Unset = UNSET,
    only_active: bool | Unset = True,
    include_defaults: bool | Unset = True,
) -> list[BTPropertiesTableTemplateInfo] | None:
    """Get all table templates that are available to use on the provided document.

    Args:
        did (str):
        template_type (BTPropertiesTableTemplateType | Unset):
        only_active (bool | Unset):  Default: True.
        include_defaults (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTPropertiesTableTemplateInfo]
    """

    return sync_detailed(
        did=did,
        client=client,
        template_type=template_type,
        only_active=only_active,
        include_defaults=include_defaults,
    ).parsed


async def asyncio_detailed(
    did: str,
    *,
    client: AuthenticatedClient,
    template_type: BTPropertiesTableTemplateType | Unset = UNSET,
    only_active: bool | Unset = True,
    include_defaults: bool | Unset = True,
) -> Response[list[BTPropertiesTableTemplateInfo]]:
    """Get all table templates that are available to use on the provided document.

    Args:
        did (str):
        template_type (BTPropertiesTableTemplateType | Unset):
        only_active (bool | Unset):  Default: True.
        include_defaults (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTPropertiesTableTemplateInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        template_type=template_type,
        only_active=only_active,
        include_defaults=include_defaults,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    *,
    client: AuthenticatedClient,
    template_type: BTPropertiesTableTemplateType | Unset = UNSET,
    only_active: bool | Unset = True,
    include_defaults: bool | Unset = True,
) -> list[BTPropertiesTableTemplateInfo] | None:
    """Get all table templates that are available to use on the provided document.

    Args:
        did (str):
        template_type (BTPropertiesTableTemplateType | Unset):
        only_active (bool | Unset):  Default: True.
        include_defaults (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTPropertiesTableTemplateInfo]
    """

    return (
        await asyncio_detailed(
            did=did,
            client=client,
            template_type=template_type,
            only_active=only_active,
            include_defaults=include_defaults,
        )
    ).parsed
