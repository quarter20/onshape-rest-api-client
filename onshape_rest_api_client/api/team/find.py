from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_global_tree_node_list_response_bt_team_info import BTGlobalTreeNodeListResponseBTTeamInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str | Unset = "",
    filter_: int | Unset = 0,
    uid: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    sort_column: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    include_company_owned_teams: bool | Unset = True,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params["filter"] = filter_

    params["uid"] = uid

    params["companyId"] = company_id

    params["sortColumn"] = sort_column

    params["sortOrder"] = sort_order

    params["includeCompanyOwnedTeams"] = include_company_owned_teams

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/teams",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTGlobalTreeNodeListResponseBTTeamInfo:
    response_default = BTGlobalTreeNodeListResponseBTTeamInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTGlobalTreeNodeListResponseBTTeamInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    query: str | Unset = "",
    filter_: int | Unset = 0,
    uid: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    sort_column: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    include_company_owned_teams: bool | Unset = True,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
) -> Response[BTGlobalTreeNodeListResponseBTTeamInfo]:
    """Get a list of all teams the current user belongs to.

    Args:
        query (str | Unset):  Default: ''.
        filter_ (int | Unset):  Default: 0.
        uid (str | Unset):
        company_id (str | Unset):
        sort_column (str | Unset):
        sort_order (str | Unset):  Default: 'asc'.
        include_company_owned_teams (bool | Unset):  Default: True.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTGlobalTreeNodeListResponseBTTeamInfo]
    """

    kwargs = _get_kwargs(
        query=query,
        filter_=filter_,
        uid=uid,
        company_id=company_id,
        sort_column=sort_column,
        sort_order=sort_order,
        include_company_owned_teams=include_company_owned_teams,
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
    query: str | Unset = "",
    filter_: int | Unset = 0,
    uid: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    sort_column: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    include_company_owned_teams: bool | Unset = True,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
) -> BTGlobalTreeNodeListResponseBTTeamInfo | None:
    """Get a list of all teams the current user belongs to.

    Args:
        query (str | Unset):  Default: ''.
        filter_ (int | Unset):  Default: 0.
        uid (str | Unset):
        company_id (str | Unset):
        sort_column (str | Unset):
        sort_order (str | Unset):  Default: 'asc'.
        include_company_owned_teams (bool | Unset):  Default: True.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTGlobalTreeNodeListResponseBTTeamInfo
    """

    return sync_detailed(
        client=client,
        query=query,
        filter_=filter_,
        uid=uid,
        company_id=company_id,
        sort_column=sort_column,
        sort_order=sort_order,
        include_company_owned_teams=include_company_owned_teams,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str | Unset = "",
    filter_: int | Unset = 0,
    uid: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    sort_column: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    include_company_owned_teams: bool | Unset = True,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
) -> Response[BTGlobalTreeNodeListResponseBTTeamInfo]:
    """Get a list of all teams the current user belongs to.

    Args:
        query (str | Unset):  Default: ''.
        filter_ (int | Unset):  Default: 0.
        uid (str | Unset):
        company_id (str | Unset):
        sort_column (str | Unset):
        sort_order (str | Unset):  Default: 'asc'.
        include_company_owned_teams (bool | Unset):  Default: True.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTGlobalTreeNodeListResponseBTTeamInfo]
    """

    kwargs = _get_kwargs(
        query=query,
        filter_=filter_,
        uid=uid,
        company_id=company_id,
        sort_column=sort_column,
        sort_order=sort_order,
        include_company_owned_teams=include_company_owned_teams,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str | Unset = "",
    filter_: int | Unset = 0,
    uid: str | Unset = UNSET,
    company_id: str | Unset = UNSET,
    sort_column: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    include_company_owned_teams: bool | Unset = True,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
) -> BTGlobalTreeNodeListResponseBTTeamInfo | None:
    """Get a list of all teams the current user belongs to.

    Args:
        query (str | Unset):  Default: ''.
        filter_ (int | Unset):  Default: 0.
        uid (str | Unset):
        company_id (str | Unset):
        sort_column (str | Unset):
        sort_order (str | Unset):  Default: 'asc'.
        include_company_owned_teams (bool | Unset):  Default: True.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTGlobalTreeNodeListResponseBTTeamInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            filter_=filter_,
            uid=uid,
            company_id=company_id,
            sort_column=sort_column,
            sort_order=sort_order,
            include_company_owned_teams=include_company_owned_teams,
            offset=offset,
            limit=limit,
        )
    ).parsed
