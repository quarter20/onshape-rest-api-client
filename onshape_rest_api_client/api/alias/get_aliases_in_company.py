from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_list_response_bt_alias_info import BTListResponseBTAliasInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    prefix: str | Unset = "",
    sort_column: str | Unset = "name",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["prefix"] = prefix

    params["sortColumn"] = sort_column

    params["sortOrder"] = sort_order

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/aliases",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTListResponseBTAliasInfo:
    response_default = BTListResponseBTAliasInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTListResponseBTAliasInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    prefix: str | Unset = "",
    sort_column: str | Unset = "name",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTListResponseBTAliasInfo]:
    """Get a list of all aliases that exist for your enterprise.

    Args:
        prefix (str | Unset):  Default: ''.
        sort_column (str | Unset):  Default: 'name'.
        sort_order (str | Unset):  Default: 'asc'.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTAliasInfo]
    """

    kwargs = _get_kwargs(
        prefix=prefix,
        sort_column=sort_column,
        sort_order=sort_order,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    prefix: str | Unset = "",
    sort_column: str | Unset = "name",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTListResponseBTAliasInfo | None:
    """Get a list of all aliases that exist for your enterprise.

    Args:
        prefix (str | Unset):  Default: ''.
        sort_column (str | Unset):  Default: 'name'.
        sort_order (str | Unset):  Default: 'asc'.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTAliasInfo
    """

    return sync_detailed(
        client=client,
        prefix=prefix,
        sort_column=sort_column,
        sort_order=sort_order,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    prefix: str | Unset = "",
    sort_column: str | Unset = "name",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTListResponseBTAliasInfo]:
    """Get a list of all aliases that exist for your enterprise.

    Args:
        prefix (str | Unset):  Default: ''.
        sort_column (str | Unset):  Default: 'name'.
        sort_order (str | Unset):  Default: 'asc'.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTAliasInfo]
    """

    kwargs = _get_kwargs(
        prefix=prefix,
        sort_column=sort_column,
        sort_order=sort_order,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    prefix: str | Unset = "",
    sort_column: str | Unset = "name",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTListResponseBTAliasInfo | None:
    """Get a list of all aliases that exist for your enterprise.

    Args:
        prefix (str | Unset):  Default: ''.
        sort_column (str | Unset):  Default: 'name'.
        sort_order (str | Unset):  Default: 'asc'.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTAliasInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            prefix=prefix,
            sort_column=sort_column,
            sort_order=sort_order,
            offset=offset,
            limit=limit,
        )
    ).parsed
