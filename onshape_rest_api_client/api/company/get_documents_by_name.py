from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_global_tree_node_summary_info import BTGlobalTreeNodeSummaryInfo
from ...types import UNSET, Response


def _get_kwargs(
    cid: str,
    *,
    name: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/companies/{cid}/documentsbyname".format(
            cid=quote(str(cid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[BTGlobalTreeNodeSummaryInfo]:
    response_default = []
    _response_default = response.json()
    for response_default_item_data in _response_default:
        response_default_item = BTGlobalTreeNodeSummaryInfo.from_dict(response_default_item_data)

        response_default.append(response_default_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[BTGlobalTreeNodeSummaryInfo]]:
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
    name: str,
) -> Response[list[BTGlobalTreeNodeSummaryInfo]]:
    """Get document by exact document name.

     This API can only be called by company admins. Use the `name` field for the exact document name
    string.

    Args:
        cid (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTGlobalTreeNodeSummaryInfo]]
    """

    kwargs = _get_kwargs(
        cid=cid,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cid: str,
    *,
    client: AuthenticatedClient,
    name: str,
) -> list[BTGlobalTreeNodeSummaryInfo] | None:
    """Get document by exact document name.

     This API can only be called by company admins. Use the `name` field for the exact document name
    string.

    Args:
        cid (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTGlobalTreeNodeSummaryInfo]
    """

    return sync_detailed(
        cid=cid,
        client=client,
        name=name,
    ).parsed


async def asyncio_detailed(
    cid: str,
    *,
    client: AuthenticatedClient,
    name: str,
) -> Response[list[BTGlobalTreeNodeSummaryInfo]]:
    """Get document by exact document name.

     This API can only be called by company admins. Use the `name` field for the exact document name
    string.

    Args:
        cid (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTGlobalTreeNodeSummaryInfo]]
    """

    kwargs = _get_kwargs(
        cid=cid,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    *,
    client: AuthenticatedClient,
    name: str,
) -> list[BTGlobalTreeNodeSummaryInfo] | None:
    """Get document by exact document name.

     This API can only be called by company admins. Use the `name` field for the exact document name
    string.

    Args:
        cid (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTGlobalTreeNodeSummaryInfo]
    """

    return (
        await asyncio_detailed(
            cid=cid,
            client=client,
            name=name,
        )
    ).parsed
