from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.btapi_application_extension_info import BTAPIApplicationExtensionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    cid: str,
    *,
    valid_purchases: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["validPurchases"] = valid_purchases

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/applications/extensions/user/{uid}/client/{cid}".format(
            uid=quote(str(uid), safe=""),
            cid=quote(str(cid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[BTAPIApplicationExtensionInfo]:
    response_default = []
    _response_default = response.json()
    for response_default_item_data in _response_default:
        response_default_item = BTAPIApplicationExtensionInfo.from_dict(response_default_item_data)

        response_default.append(response_default_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[BTAPIApplicationExtensionInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uid: str,
    cid: str,
    *,
    client: AuthenticatedClient,
    valid_purchases: bool | Unset = False,
) -> Response[list[BTAPIApplicationExtensionInfo]]:
    """Get a list of the client extensions the specified user has granted/accepted terms for.

    Args:
        uid (str):
        cid (str):
        valid_purchases (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTAPIApplicationExtensionInfo]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        cid=cid,
        valid_purchases=valid_purchases,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    cid: str,
    *,
    client: AuthenticatedClient,
    valid_purchases: bool | Unset = False,
) -> list[BTAPIApplicationExtensionInfo] | None:
    """Get a list of the client extensions the specified user has granted/accepted terms for.

    Args:
        uid (str):
        cid (str):
        valid_purchases (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTAPIApplicationExtensionInfo]
    """

    return sync_detailed(
        uid=uid,
        cid=cid,
        client=client,
        valid_purchases=valid_purchases,
    ).parsed


async def asyncio_detailed(
    uid: str,
    cid: str,
    *,
    client: AuthenticatedClient,
    valid_purchases: bool | Unset = False,
) -> Response[list[BTAPIApplicationExtensionInfo]]:
    """Get a list of the client extensions the specified user has granted/accepted terms for.

    Args:
        uid (str):
        cid (str):
        valid_purchases (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTAPIApplicationExtensionInfo]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        cid=cid,
        valid_purchases=valid_purchases,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    cid: str,
    *,
    client: AuthenticatedClient,
    valid_purchases: bool | Unset = False,
) -> list[BTAPIApplicationExtensionInfo] | None:
    """Get a list of the client extensions the specified user has granted/accepted terms for.

    Args:
        uid (str):
        cid (str):
        valid_purchases (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTAPIApplicationExtensionInfo]
    """

    return (
        await asyncio_detailed(
            uid=uid,
            cid=cid,
            client=client,
            valid_purchases=valid_purchases,
        )
    ).parsed
