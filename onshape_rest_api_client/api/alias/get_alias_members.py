from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_list_response_bt_alias_entry_info import BTListResponseBTAliasEntryInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    aid: str,
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
        "url": "/aliases/{aid}/members".format(
            aid=quote(str(aid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTListResponseBTAliasEntryInfo:
    response_default = BTListResponseBTAliasEntryInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTListResponseBTAliasEntryInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    aid: str,
    *,
    client: AuthenticatedClient,
    prefix: str | Unset = "",
    sort_column: str | Unset = "name",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTListResponseBTAliasEntryInfo]:
    """Get all users and teams assigned to an alias.

     This is a search-like endpoint that returns a subset of the member list. Use `getAlias` to return
    all members every time it's called.

    Args:
        aid (str):
        prefix (str | Unset):  Default: ''.
        sort_column (str | Unset):  Default: 'name'.
        sort_order (str | Unset):  Default: 'asc'.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTAliasEntryInfo]
    """

    kwargs = _get_kwargs(
        aid=aid,
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
    aid: str,
    *,
    client: AuthenticatedClient,
    prefix: str | Unset = "",
    sort_column: str | Unset = "name",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTListResponseBTAliasEntryInfo | None:
    """Get all users and teams assigned to an alias.

     This is a search-like endpoint that returns a subset of the member list. Use `getAlias` to return
    all members every time it's called.

    Args:
        aid (str):
        prefix (str | Unset):  Default: ''.
        sort_column (str | Unset):  Default: 'name'.
        sort_order (str | Unset):  Default: 'asc'.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTAliasEntryInfo
    """

    return sync_detailed(
        aid=aid,
        client=client,
        prefix=prefix,
        sort_column=sort_column,
        sort_order=sort_order,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    aid: str,
    *,
    client: AuthenticatedClient,
    prefix: str | Unset = "",
    sort_column: str | Unset = "name",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTListResponseBTAliasEntryInfo]:
    """Get all users and teams assigned to an alias.

     This is a search-like endpoint that returns a subset of the member list. Use `getAlias` to return
    all members every time it's called.

    Args:
        aid (str):
        prefix (str | Unset):  Default: ''.
        sort_column (str | Unset):  Default: 'name'.
        sort_order (str | Unset):  Default: 'asc'.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTAliasEntryInfo]
    """

    kwargs = _get_kwargs(
        aid=aid,
        prefix=prefix,
        sort_column=sort_column,
        sort_order=sort_order,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    aid: str,
    *,
    client: AuthenticatedClient,
    prefix: str | Unset = "",
    sort_column: str | Unset = "name",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTListResponseBTAliasEntryInfo | None:
    """Get all users and teams assigned to an alias.

     This is a search-like endpoint that returns a subset of the member list. Use `getAlias` to return
    all members every time it's called.

    Args:
        aid (str):
        prefix (str | Unset):  Default: ''.
        sort_column (str | Unset):  Default: 'name'.
        sort_order (str | Unset):  Default: 'asc'.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTAliasEntryInfo
    """

    return (
        await asyncio_detailed(
            aid=aid,
            client=client,
            prefix=prefix,
            sort_column=sort_column,
            sort_order=sort_order,
            offset=offset,
            limit=limit,
        )
    ).parsed
