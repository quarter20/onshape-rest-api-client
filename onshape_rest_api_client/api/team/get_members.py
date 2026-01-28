from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_list_response_bt_team_member_info import BTListResponseBTTeamMemberInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tid: str,
    *,
    sort_column: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    q: str | Unset = "",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sortColumn"] = sort_column

    params["sortOrder"] = sort_order

    params["q"] = q

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/teams/{tid}/members".format(
            tid=quote(str(tid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTListResponseBTTeamMemberInfo:
    response_default = BTListResponseBTTeamMemberInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTListResponseBTTeamMemberInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tid: str,
    *,
    client: AuthenticatedClient,
    sort_column: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    q: str | Unset = "",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTListResponseBTTeamMemberInfo]:
    """Get a list of a team's members.

     Returns a maximum of 20 per page.

    Args:
        tid (str):
        sort_column (str | Unset):
        sort_order (str | Unset):  Default: 'asc'.
        q (str | Unset):  Default: ''.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTTeamMemberInfo]
    """

    kwargs = _get_kwargs(
        tid=tid,
        sort_column=sort_column,
        sort_order=sort_order,
        q=q,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tid: str,
    *,
    client: AuthenticatedClient,
    sort_column: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    q: str | Unset = "",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTListResponseBTTeamMemberInfo | None:
    """Get a list of a team's members.

     Returns a maximum of 20 per page.

    Args:
        tid (str):
        sort_column (str | Unset):
        sort_order (str | Unset):  Default: 'asc'.
        q (str | Unset):  Default: ''.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTTeamMemberInfo
    """

    return sync_detailed(
        tid=tid,
        client=client,
        sort_column=sort_column,
        sort_order=sort_order,
        q=q,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    tid: str,
    *,
    client: AuthenticatedClient,
    sort_column: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    q: str | Unset = "",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTListResponseBTTeamMemberInfo]:
    """Get a list of a team's members.

     Returns a maximum of 20 per page.

    Args:
        tid (str):
        sort_column (str | Unset):
        sort_order (str | Unset):  Default: 'asc'.
        q (str | Unset):  Default: ''.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTTeamMemberInfo]
    """

    kwargs = _get_kwargs(
        tid=tid,
        sort_column=sort_column,
        sort_order=sort_order,
        q=q,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tid: str,
    *,
    client: AuthenticatedClient,
    sort_column: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    q: str | Unset = "",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTListResponseBTTeamMemberInfo | None:
    """Get a list of a team's members.

     Returns a maximum of 20 per page.

    Args:
        tid (str):
        sort_column (str | Unset):
        sort_order (str | Unset):  Default: 'asc'.
        q (str | Unset):  Default: ''.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTTeamMemberInfo
    """

    return (
        await asyncio_detailed(
            tid=tid,
            client=client,
            sort_column=sort_column,
            sort_order=sort_order,
            q=q,
            offset=offset,
            limit=limit,
        )
    ).parsed
