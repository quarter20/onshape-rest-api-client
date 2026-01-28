from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_list_response_bt_comment_info import BTListResponseBTCommentInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    did: str | Unset = "",
    object_type: int | Unset = 6,
    pid: str | Unset = "",
    eid: str | Unset = "",
    filter_: int | Unset = 0,
    resolved: bool | Unset = True,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["did"] = did

    params["objectType"] = object_type

    params["pid"] = pid

    params["eid"] = eid

    params["filter"] = filter_

    params["resolved"] = resolved

    params["sortColumn"] = sort_column

    params["sortOrder"] = sort_order

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/comments",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTListResponseBTCommentInfo:
    response_default = BTListResponseBTCommentInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTListResponseBTCommentInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    did: str | Unset = "",
    object_type: int | Unset = 6,
    pid: str | Unset = "",
    eid: str | Unset = "",
    filter_: int | Unset = 0,
    resolved: bool | Unset = True,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTListResponseBTCommentInfo]:
    """Get a list of comments in a document.

    Args:
        did (str | Unset):  Default: ''.
        object_type (int | Unset):  Default: 6.
        pid (str | Unset):  Default: ''.
        eid (str | Unset):  Default: ''.
        filter_ (int | Unset):  Default: 0.
        resolved (bool | Unset):  Default: True.
        sort_column (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'asc'.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTCommentInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        object_type=object_type,
        pid=pid,
        eid=eid,
        filter_=filter_,
        resolved=resolved,
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
    did: str | Unset = "",
    object_type: int | Unset = 6,
    pid: str | Unset = "",
    eid: str | Unset = "",
    filter_: int | Unset = 0,
    resolved: bool | Unset = True,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTListResponseBTCommentInfo | None:
    """Get a list of comments in a document.

    Args:
        did (str | Unset):  Default: ''.
        object_type (int | Unset):  Default: 6.
        pid (str | Unset):  Default: ''.
        eid (str | Unset):  Default: ''.
        filter_ (int | Unset):  Default: 0.
        resolved (bool | Unset):  Default: True.
        sort_column (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'asc'.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTCommentInfo
    """

    return sync_detailed(
        client=client,
        did=did,
        object_type=object_type,
        pid=pid,
        eid=eid,
        filter_=filter_,
        resolved=resolved,
        sort_column=sort_column,
        sort_order=sort_order,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    did: str | Unset = "",
    object_type: int | Unset = 6,
    pid: str | Unset = "",
    eid: str | Unset = "",
    filter_: int | Unset = 0,
    resolved: bool | Unset = True,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTListResponseBTCommentInfo]:
    """Get a list of comments in a document.

    Args:
        did (str | Unset):  Default: ''.
        object_type (int | Unset):  Default: 6.
        pid (str | Unset):  Default: ''.
        eid (str | Unset):  Default: ''.
        filter_ (int | Unset):  Default: 0.
        resolved (bool | Unset):  Default: True.
        sort_column (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'asc'.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTCommentInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        object_type=object_type,
        pid=pid,
        eid=eid,
        filter_=filter_,
        resolved=resolved,
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
    did: str | Unset = "",
    object_type: int | Unset = 6,
    pid: str | Unset = "",
    eid: str | Unset = "",
    filter_: int | Unset = 0,
    resolved: bool | Unset = True,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "asc",
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTListResponseBTCommentInfo | None:
    """Get a list of comments in a document.

    Args:
        did (str | Unset):  Default: ''.
        object_type (int | Unset):  Default: 6.
        pid (str | Unset):  Default: ''.
        eid (str | Unset):  Default: ''.
        filter_ (int | Unset):  Default: 0.
        resolved (bool | Unset):  Default: True.
        sort_column (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'asc'.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTCommentInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            did=did,
            object_type=object_type,
            pid=pid,
            eid=eid,
            filter_=filter_,
            resolved=resolved,
            sort_column=sort_column,
            sort_order=sort_order,
            offset=offset,
            limit=limit,
        )
    ).parsed
