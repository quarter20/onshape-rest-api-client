from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_purchase_info import BTPurchaseInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    all_: bool | Unset = False,
    own_purchase_only: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["all"] = all_

    params["ownPurchaseOnly"] = own_purchase_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/purchases",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[BTPurchaseInfo]:
    response_default = []
    _response_default = response.json()
    for response_default_item_data in _response_default:
        response_default_item = BTPurchaseInfo.from_dict(response_default_item_data)

        response_default.append(response_default_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[BTPurchaseInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    all_: bool | Unset = False,
    own_purchase_only: bool | Unset = False,
) -> Response[list[BTPurchaseInfo]]:
    """Get a list of all app purchases made by the current user.

     This API should be used within the context of an OAuth-enabled application.

    Args:
        all_ (bool | Unset):  Default: False.
        own_purchase_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTPurchaseInfo]]
    """

    kwargs = _get_kwargs(
        all_=all_,
        own_purchase_only=own_purchase_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    all_: bool | Unset = False,
    own_purchase_only: bool | Unset = False,
) -> list[BTPurchaseInfo] | None:
    """Get a list of all app purchases made by the current user.

     This API should be used within the context of an OAuth-enabled application.

    Args:
        all_ (bool | Unset):  Default: False.
        own_purchase_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTPurchaseInfo]
    """

    return sync_detailed(
        client=client,
        all_=all_,
        own_purchase_only=own_purchase_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    all_: bool | Unset = False,
    own_purchase_only: bool | Unset = False,
) -> Response[list[BTPurchaseInfo]]:
    """Get a list of all app purchases made by the current user.

     This API should be used within the context of an OAuth-enabled application.

    Args:
        all_ (bool | Unset):  Default: False.
        own_purchase_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTPurchaseInfo]]
    """

    kwargs = _get_kwargs(
        all_=all_,
        own_purchase_only=own_purchase_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    all_: bool | Unset = False,
    own_purchase_only: bool | Unset = False,
) -> list[BTPurchaseInfo] | None:
    """Get a list of all app purchases made by the current user.

     This API should be used within the context of an OAuth-enabled application.

    Args:
        all_ (bool | Unset):  Default: False.
        own_purchase_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTPurchaseInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
            all_=all_,
            own_purchase_only=own_purchase_only,
        )
    ).parsed
