from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_item_response_default import DeleteItemResponseDefault
from ...types import Response


def _get_kwargs(
    iid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/items/{iid}".format(
            iid=quote(str(iid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteItemResponseDefault:
    response_default = DeleteItemResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteItemResponseDefault]:
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
) -> Response[DeleteItemResponseDefault]:
    """Delete an item.

     Items can only be deleted if `publishState = 0` (`PENDING`). [`GET /items/{iid}`](#/Items/getItem)
    to get the `publishState`.

    Args:
        iid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteItemResponseDefault]
    """

    kwargs = _get_kwargs(
        iid=iid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    iid: str,
    *,
    client: AuthenticatedClient,
) -> DeleteItemResponseDefault | None:
    """Delete an item.

     Items can only be deleted if `publishState = 0` (`PENDING`). [`GET /items/{iid}`](#/Items/getItem)
    to get the `publishState`.

    Args:
        iid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteItemResponseDefault
    """

    return sync_detailed(
        iid=iid,
        client=client,
    ).parsed


async def asyncio_detailed(
    iid: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteItemResponseDefault]:
    """Delete an item.

     Items can only be deleted if `publishState = 0` (`PENDING`). [`GET /items/{iid}`](#/Items/getItem)
    to get the `publishState`.

    Args:
        iid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteItemResponseDefault]
    """

    kwargs = _get_kwargs(
        iid=iid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    iid: str,
    *,
    client: AuthenticatedClient,
) -> DeleteItemResponseDefault | None:
    """Delete an item.

     Items can only be deleted if `publishState = 0` (`PENDING`). [`GET /items/{iid}`](#/Items/getItem)
    to get the `publishState`.

    Args:
        iid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteItemResponseDefault
    """

    return (
        await asyncio_detailed(
            iid=iid,
            client=client,
        )
    ).parsed
