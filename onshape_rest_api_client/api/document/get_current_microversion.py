from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_microversion_info import BTMicroversionInfo
from ...types import Response


def _get_kwargs(
    did: str,
    wv: str,
    wvid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents/d/{did}/{wv}/{wvid}/currentmicroversion".format(
            did=quote(str(did), safe=""),
            wv=quote(str(wv), safe=""),
            wvid=quote(str(wvid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTMicroversionInfo:
    response_default = BTMicroversionInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTMicroversionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wv: str,
    wvid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTMicroversionInfo]:
    """Retrieve current microversion by document ID and workspace or version ID.

    Args:
        did (str):
        wv (str):
        wvid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTMicroversionInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wv: str,
    wvid: str,
    *,
    client: AuthenticatedClient,
) -> BTMicroversionInfo | None:
    """Retrieve current microversion by document ID and workspace or version ID.

    Args:
        did (str):
        wv (str):
        wvid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTMicroversionInfo
    """

    return sync_detailed(
        did=did,
        wv=wv,
        wvid=wvid,
        client=client,
    ).parsed


async def asyncio_detailed(
    did: str,
    wv: str,
    wvid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTMicroversionInfo]:
    """Retrieve current microversion by document ID and workspace or version ID.

    Args:
        did (str):
        wv (str):
        wvid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTMicroversionInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wv: str,
    wvid: str,
    *,
    client: AuthenticatedClient,
) -> BTMicroversionInfo | None:
    """Retrieve current microversion by document ID and workspace or version ID.

    Args:
        did (str):
        wv (str):
        wvid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTMicroversionInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wv=wv,
            wvid=wvid,
            client=client,
        )
    ).parsed
