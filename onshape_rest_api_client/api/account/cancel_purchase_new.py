from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.cancel_purchase_new_response_default import CancelPurchaseNewResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    aid: str,
    pid: str,
    *,
    cancel_immediately: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cancelImmediately"] = cancel_immediately

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/accounts/{aid}/purchases/{pid}".format(
            aid=quote(str(aid), safe=""),
            pid=quote(str(pid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CancelPurchaseNewResponseDefault:
    response_default = CancelPurchaseNewResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CancelPurchaseNewResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    aid: str,
    pid: str,
    *,
    client: AuthenticatedClient,
    cancel_immediately: bool | Unset = False,
) -> Response[CancelPurchaseNewResponseDefault]:
    """Cancel a recurring subscription for the specified account ID and purchase ID.

    Args:
        aid (str):
        pid (str):
        cancel_immediately (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelPurchaseNewResponseDefault]
    """

    kwargs = _get_kwargs(
        aid=aid,
        pid=pid,
        cancel_immediately=cancel_immediately,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    aid: str,
    pid: str,
    *,
    client: AuthenticatedClient,
    cancel_immediately: bool | Unset = False,
) -> CancelPurchaseNewResponseDefault | None:
    """Cancel a recurring subscription for the specified account ID and purchase ID.

    Args:
        aid (str):
        pid (str):
        cancel_immediately (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelPurchaseNewResponseDefault
    """

    return sync_detailed(
        aid=aid,
        pid=pid,
        client=client,
        cancel_immediately=cancel_immediately,
    ).parsed


async def asyncio_detailed(
    aid: str,
    pid: str,
    *,
    client: AuthenticatedClient,
    cancel_immediately: bool | Unset = False,
) -> Response[CancelPurchaseNewResponseDefault]:
    """Cancel a recurring subscription for the specified account ID and purchase ID.

    Args:
        aid (str):
        pid (str):
        cancel_immediately (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelPurchaseNewResponseDefault]
    """

    kwargs = _get_kwargs(
        aid=aid,
        pid=pid,
        cancel_immediately=cancel_immediately,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    aid: str,
    pid: str,
    *,
    client: AuthenticatedClient,
    cancel_immediately: bool | Unset = False,
) -> CancelPurchaseNewResponseDefault | None:
    """Cancel a recurring subscription for the specified account ID and purchase ID.

    Args:
        aid (str):
        pid (str):
        cancel_immediately (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelPurchaseNewResponseDefault
    """

    return (
        await asyncio_detailed(
            aid=aid,
            pid=pid,
            client=client,
            cancel_immediately=cancel_immediately,
        )
    ).parsed
