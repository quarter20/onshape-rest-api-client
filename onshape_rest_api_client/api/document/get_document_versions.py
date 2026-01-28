from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_version_info import BTVersionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents/d/{did}/versions".format(
            did=quote(str(did), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[BTVersionInfo]:
    response_default = []
    _response_default = response.json()
    for response_default_item_data in _response_default:
        response_default_item = BTVersionInfo.from_dict(response_default_item_data)

        response_default.append(response_default_item)

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[BTVersionInfo]]:
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
    offset: int | Unset = 0,
    limit: int | Unset = 0,
) -> Response[list[BTVersionInfo]]:
    """Retrieve versions by document ID.

    Args:
        did (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTVersionInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 0,
) -> list[BTVersionInfo] | None:
    """Retrieve versions by document ID.

    Args:
        did (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTVersionInfo]
    """

    return sync_detailed(
        did=did,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    did: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 0,
) -> Response[list[BTVersionInfo]]:
    """Retrieve versions by document ID.

    Args:
        did (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTVersionInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 0,
) -> list[BTVersionInfo] | None:
    """Retrieve versions by document ID.

    Args:
        did (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTVersionInfo]
    """

    return (
        await asyncio_detailed(
            did=did,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
