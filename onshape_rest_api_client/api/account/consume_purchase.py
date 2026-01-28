from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_purchase_identity_params import BTPurchaseIdentityParams
from ...models.bt_purchase_info import BTPurchaseInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pid: str,
    *,
    body: BTPurchaseIdentityParams | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/purchases/{pid}/consume".format(
            pid=quote(str(pid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTPurchaseInfo:
    response_default = BTPurchaseInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTPurchaseInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pid: str,
    *,
    client: AuthenticatedClient,
    body: BTPurchaseIdentityParams | Unset = UNSET,
) -> Response[BTPurchaseInfo]:
    """Mark a purchase as consumed by the current user.

    Args:
        pid (str):
        body (BTPurchaseIdentityParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTPurchaseInfo]
    """

    kwargs = _get_kwargs(
        pid=pid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pid: str,
    *,
    client: AuthenticatedClient,
    body: BTPurchaseIdentityParams | Unset = UNSET,
) -> BTPurchaseInfo | None:
    """Mark a purchase as consumed by the current user.

    Args:
        pid (str):
        body (BTPurchaseIdentityParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTPurchaseInfo
    """

    return sync_detailed(
        pid=pid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    pid: str,
    *,
    client: AuthenticatedClient,
    body: BTPurchaseIdentityParams | Unset = UNSET,
) -> Response[BTPurchaseInfo]:
    """Mark a purchase as consumed by the current user.

    Args:
        pid (str):
        body (BTPurchaseIdentityParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTPurchaseInfo]
    """

    kwargs = _get_kwargs(
        pid=pid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pid: str,
    *,
    client: AuthenticatedClient,
    body: BTPurchaseIdentityParams | Unset = UNSET,
) -> BTPurchaseInfo | None:
    """Mark a purchase as consumed by the current user.

    Args:
        pid (str):
        body (BTPurchaseIdentityParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTPurchaseInfo
    """

    return (
        await asyncio_detailed(
            pid=pid,
            client=client,
            body=body,
        )
    ).parsed
