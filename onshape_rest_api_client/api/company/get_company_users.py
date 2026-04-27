from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_list_response_bt_company_user_info import BTListResponseBTCompanyUserInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cid: str,
    *,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "desc",
    q: str | Unset = "",
    include_global_permissions: bool | Unset = False,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sortColumn"] = sort_column

    params["sortOrder"] = sort_order

    params["q"] = q

    params["includeGlobalPermissions"] = include_global_permissions

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/companies/{cid}/users".format(
            cid=quote(str(cid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTListResponseBTCompanyUserInfo:
    response_default = BTListResponseBTCompanyUserInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTListResponseBTCompanyUserInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cid: str,
    *,
    client: AuthenticatedClient,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "desc",
    q: str | Unset = "",
    include_global_permissions: bool | Unset = False,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTListResponseBTCompanyUserInfo]:
    """Get a list of members in a company.

     Returns a list of members in the specified company.

    Args:
        cid (str):
        sort_column (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'desc'.
        q (str | Unset):  Default: ''.
        include_global_permissions (bool | Unset):  Default: False.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTCompanyUserInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
        sort_column=sort_column,
        sort_order=sort_order,
        q=q,
        include_global_permissions=include_global_permissions,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cid: str,
    *,
    client: AuthenticatedClient,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "desc",
    q: str | Unset = "",
    include_global_permissions: bool | Unset = False,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTListResponseBTCompanyUserInfo | None:
    """Get a list of members in a company.

     Returns a list of members in the specified company.

    Args:
        cid (str):
        sort_column (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'desc'.
        q (str | Unset):  Default: ''.
        include_global_permissions (bool | Unset):  Default: False.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTCompanyUserInfo
    """

    return sync_detailed(
        cid=cid,
        client=client,
        sort_column=sort_column,
        sort_order=sort_order,
        q=q,
        include_global_permissions=include_global_permissions,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    cid: str,
    *,
    client: AuthenticatedClient,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "desc",
    q: str | Unset = "",
    include_global_permissions: bool | Unset = False,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTListResponseBTCompanyUserInfo]:
    """Get a list of members in a company.

     Returns a list of members in the specified company.

    Args:
        cid (str):
        sort_column (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'desc'.
        q (str | Unset):  Default: ''.
        include_global_permissions (bool | Unset):  Default: False.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTCompanyUserInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
        sort_column=sort_column,
        sort_order=sort_order,
        q=q,
        include_global_permissions=include_global_permissions,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    *,
    client: AuthenticatedClient,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "desc",
    q: str | Unset = "",
    include_global_permissions: bool | Unset = False,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTListResponseBTCompanyUserInfo | None:
    """Get a list of members in a company.

     Returns a list of members in the specified company.

    Args:
        cid (str):
        sort_column (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'desc'.
        q (str | Unset):  Default: ''.
        include_global_permissions (bool | Unset):  Default: False.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTCompanyUserInfo
    """

    return (
        await asyncio_detailed(
            cid=cid,
            client=client,
            sort_column=sort_column,
            sort_order=sort_order,
            q=q,
            include_global_permissions=include_global_permissions,
            offset=offset,
            limit=limit,
        )
    ).parsed
