from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_sync_app_element_params import BTSyncAppElementParams
from ...models.sync_app_elements_response_default import SyncAppElementsResponseDefault
from ...types import Response


def _get_kwargs(
    did: str,
    wid: str,
    *,
    body: BTSyncAppElementParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/documents/d/{did}/w/{wid}/syncAppElements".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SyncAppElementsResponseDefault:
    response_default = SyncAppElementsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SyncAppElementsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTSyncAppElementParams,
) -> Response[SyncAppElementsResponseDefault]:
    """
    Args:
        did (str):
        wid (str):
        body (BTSyncAppElementParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyncAppElementsResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTSyncAppElementParams,
) -> SyncAppElementsResponseDefault | None:
    """
    Args:
        did (str):
        wid (str):
        body (BTSyncAppElementParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyncAppElementsResponseDefault
    """

    return sync_detailed(
        did=did,
        wid=wid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTSyncAppElementParams,
) -> Response[SyncAppElementsResponseDefault]:
    """
    Args:
        did (str):
        wid (str):
        body (BTSyncAppElementParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyncAppElementsResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTSyncAppElementParams,
) -> SyncAppElementsResponseDefault | None:
    """
    Args:
        did (str):
        wid (str):
        body (BTSyncAppElementParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyncAppElementsResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            client=client,
            body=body,
        )
    ).parsed
