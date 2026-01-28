from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bt_global_tree_node_list_response import BTGlobalTreeNodeListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = "",
    filter_: int | Unset = UNSET,
    owner: str | Unset = "",
    owner_type: int | Unset = 1,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "desc",
    label: str | Unset = UNSET,
    project: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["q"] = q

    params["filter"] = filter_

    params["owner"] = owner

    params["ownerType"] = owner_type

    params["sortColumn"] = sort_column

    params["sortOrder"] = sort_order

    params["label"] = label

    params["project"] = project

    params["parentId"] = parent_id

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTGlobalTreeNodeListResponse | None:
    if response.status_code == 200:
        response_200 = BTGlobalTreeNodeListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTGlobalTreeNodeListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = "",
    filter_: int | Unset = UNSET,
    owner: str | Unset = "",
    owner_type: int | Unset = 1,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "desc",
    label: str | Unset = UNSET,
    project: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTGlobalTreeNodeListResponse]:
    """Get a list of documents that meet the criteria you specify.

    Args:
        q (str | Unset):  Default: ''.
        filter_ (int | Unset):
        owner (str | Unset):  Default: ''.
        owner_type (int | Unset):  Default: 1.
        sort_column (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'desc'.
        label (str | Unset):
        project (str | Unset):
        parent_id (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTGlobalTreeNodeListResponse]
    """

    kwargs = _get_kwargs(
        q=q,
        filter_=filter_,
        owner=owner,
        owner_type=owner_type,
        sort_column=sort_column,
        sort_order=sort_order,
        label=label,
        project=project,
        parent_id=parent_id,
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
    q: str | Unset = "",
    filter_: int | Unset = UNSET,
    owner: str | Unset = "",
    owner_type: int | Unset = 1,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "desc",
    label: str | Unset = UNSET,
    project: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTGlobalTreeNodeListResponse | None:
    """Get a list of documents that meet the criteria you specify.

    Args:
        q (str | Unset):  Default: ''.
        filter_ (int | Unset):
        owner (str | Unset):  Default: ''.
        owner_type (int | Unset):  Default: 1.
        sort_column (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'desc'.
        label (str | Unset):
        project (str | Unset):
        parent_id (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTGlobalTreeNodeListResponse
    """

    return sync_detailed(
        client=client,
        q=q,
        filter_=filter_,
        owner=owner,
        owner_type=owner_type,
        sort_column=sort_column,
        sort_order=sort_order,
        label=label,
        project=project,
        parent_id=parent_id,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = "",
    filter_: int | Unset = UNSET,
    owner: str | Unset = "",
    owner_type: int | Unset = 1,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "desc",
    label: str | Unset = UNSET,
    project: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTGlobalTreeNodeListResponse]:
    """Get a list of documents that meet the criteria you specify.

    Args:
        q (str | Unset):  Default: ''.
        filter_ (int | Unset):
        owner (str | Unset):  Default: ''.
        owner_type (int | Unset):  Default: 1.
        sort_column (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'desc'.
        label (str | Unset):
        project (str | Unset):
        parent_id (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTGlobalTreeNodeListResponse]
    """

    kwargs = _get_kwargs(
        q=q,
        filter_=filter_,
        owner=owner,
        owner_type=owner_type,
        sort_column=sort_column,
        sort_order=sort_order,
        label=label,
        project=project,
        parent_id=parent_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str | Unset = "",
    filter_: int | Unset = UNSET,
    owner: str | Unset = "",
    owner_type: int | Unset = 1,
    sort_column: str | Unset = "createdAt",
    sort_order: str | Unset = "desc",
    label: str | Unset = UNSET,
    project: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTGlobalTreeNodeListResponse | None:
    """Get a list of documents that meet the criteria you specify.

    Args:
        q (str | Unset):  Default: ''.
        filter_ (int | Unset):
        owner (str | Unset):  Default: ''.
        owner_type (int | Unset):  Default: 1.
        sort_column (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'desc'.
        label (str | Unset):
        project (str | Unset):
        parent_id (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTGlobalTreeNodeListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            filter_=filter_,
            owner=owner,
            owner_type=owner_type,
            sort_column=sort_column,
            sort_order=sort_order,
            label=label,
            project=project,
            parent_id=parent_id,
            offset=offset,
            limit=limit,
        )
    ).parsed
