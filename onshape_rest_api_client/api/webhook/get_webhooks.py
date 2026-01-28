from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_list_response_bt_webhook_info import BTListResponseBTWebhookInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    company: str | Unset = "",
    user: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["company"] = company

    params["user"] = user

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhooks",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTListResponseBTWebhookInfo:
    response_default = BTListResponseBTWebhookInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTListResponseBTWebhookInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    company: str | Unset = "",
    user: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTListResponseBTWebhookInfo]:
    """Get a list of all webhooks registered by a user or company.

     See [API Guide: Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation
    details.

    Args:
        company (str | Unset):  Default: ''.
        user (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTWebhookInfo]
    """

    kwargs = _get_kwargs(
        company=company,
        user=user,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    company: str | Unset = "",
    user: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTListResponseBTWebhookInfo | None:
    """Get a list of all webhooks registered by a user or company.

     See [API Guide: Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation
    details.

    Args:
        company (str | Unset):  Default: ''.
        user (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTWebhookInfo
    """

    return sync_detailed(
        client=client,
        company=company,
        user=user,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    company: str | Unset = "",
    user: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[BTListResponseBTWebhookInfo]:
    """Get a list of all webhooks registered by a user or company.

     See [API Guide: Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation
    details.

    Args:
        company (str | Unset):  Default: ''.
        user (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTWebhookInfo]
    """

    kwargs = _get_kwargs(
        company=company,
        user=user,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    company: str | Unset = "",
    user: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> BTListResponseBTWebhookInfo | None:
    """Get a list of all webhooks registered by a user or company.

     See [API Guide: Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation
    details.

    Args:
        company (str | Unset):  Default: ''.
        user (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTWebhookInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            company=company,
            user=user,
            offset=offset,
            limit=limit,
        )
    ).parsed
