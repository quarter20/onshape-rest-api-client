from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_acl_info import BTAclInfo
from ...types import Response


def _get_kwargs(
    did: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents/{did}/acl".format(
            did=quote(str(did), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAclInfo:
    response_default = BTAclInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTAclInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTAclInfo]:
    """Retrieve access control list by document ID.

    Args:
        did (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAclInfo]
    """

    kwargs = _get_kwargs(
        did=did,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    *,
    client: AuthenticatedClient,
) -> BTAclInfo | None:
    """Retrieve access control list by document ID.

    Args:
        did (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAclInfo
    """

    return sync_detailed(
        did=did,
        client=client,
    ).parsed


async def asyncio_detailed(
    did: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTAclInfo]:
    """Retrieve access control list by document ID.

    Args:
        did (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAclInfo]
    """

    kwargs = _get_kwargs(
        did=did,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    *,
    client: AuthenticatedClient,
) -> BTAclInfo | None:
    """Retrieve access control list by document ID.

    Args:
        did (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAclInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            client=client,
        )
    ).parsed
