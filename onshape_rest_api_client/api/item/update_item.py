from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_item_info import BTItemInfo
from ...models.bt_item_params import BTItemParams
from ...types import Response


def _get_kwargs(
    iid: str,
    *,
    body: BTItemParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/items/{iid}".format(
            iid=quote(str(iid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTItemInfo:
    response_default = BTItemInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTItemInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    iid: str,
    *,
    client: AuthenticatedClient,
    body: BTItemParams,
) -> Response[BTItemInfo]:
    """Update an item.

    Args:
        iid (str):
        body (BTItemParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTItemInfo]
    """

    kwargs = _get_kwargs(
        iid=iid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    iid: str,
    *,
    client: AuthenticatedClient,
    body: BTItemParams,
) -> BTItemInfo | None:
    """Update an item.

    Args:
        iid (str):
        body (BTItemParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTItemInfo
    """

    return sync_detailed(
        iid=iid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    iid: str,
    *,
    client: AuthenticatedClient,
    body: BTItemParams,
) -> Response[BTItemInfo]:
    """Update an item.

    Args:
        iid (str):
        body (BTItemParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTItemInfo]
    """

    kwargs = _get_kwargs(
        iid=iid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    iid: str,
    *,
    client: AuthenticatedClient,
    body: BTItemParams,
) -> BTItemInfo | None:
    """Update an item.

    Args:
        iid (str):
        body (BTItemParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTItemInfo
    """

    return (
        await asyncio_detailed(
            iid=iid,
            client=client,
            body=body,
        )
    ).parsed
