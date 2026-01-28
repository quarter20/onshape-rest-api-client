from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_webhook_info import BTWebhookInfo
from ...models.bt_webhook_params import BTWebhookParams
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BTWebhookParams | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTWebhookInfo:
    response_default = BTWebhookInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTWebhookInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BTWebhookParams | Unset = UNSET,
) -> Response[BTWebhookInfo]:
    """Create a new webhook.

     Click **Callbacks** below for a list of events your app can subscribe to. See [API Guide:
    Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation details.

    Args:
        body (BTWebhookParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTWebhookInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BTWebhookParams | Unset = UNSET,
) -> BTWebhookInfo | None:
    """Create a new webhook.

     Click **Callbacks** below for a list of events your app can subscribe to. See [API Guide:
    Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation details.

    Args:
        body (BTWebhookParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTWebhookInfo
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BTWebhookParams | Unset = UNSET,
) -> Response[BTWebhookInfo]:
    """Create a new webhook.

     Click **Callbacks** below for a list of events your app can subscribe to. See [API Guide:
    Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation details.

    Args:
        body (BTWebhookParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTWebhookInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BTWebhookParams | Unset = UNSET,
) -> BTWebhookInfo | None:
    """Create a new webhook.

     Click **Callbacks** below for a list of events your app can subscribe to. See [API Guide:
    Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation details.

    Args:
        body (BTWebhookParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTWebhookInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
