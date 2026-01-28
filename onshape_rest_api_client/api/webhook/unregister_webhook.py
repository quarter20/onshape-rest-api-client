from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.unregister_webhook_response_default import UnregisterWebhookResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    webhookid: str,
    *,
    block_notification: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["blockNotification"] = block_notification

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/webhooks/{webhookid}".format(
            webhookid=quote(str(webhookid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UnregisterWebhookResponseDefault:
    response_default = UnregisterWebhookResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UnregisterWebhookResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhookid: str,
    *,
    client: AuthenticatedClient,
    block_notification: bool | Unset = False,
) -> Response[UnregisterWebhookResponseDefault]:
    """Unregister a webhook.

     See [API Guide: Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation
    details.

    Args:
        webhookid (str):
        block_notification (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnregisterWebhookResponseDefault]
    """

    kwargs = _get_kwargs(
        webhookid=webhookid,
        block_notification=block_notification,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhookid: str,
    *,
    client: AuthenticatedClient,
    block_notification: bool | Unset = False,
) -> UnregisterWebhookResponseDefault | None:
    """Unregister a webhook.

     See [API Guide: Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation
    details.

    Args:
        webhookid (str):
        block_notification (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnregisterWebhookResponseDefault
    """

    return sync_detailed(
        webhookid=webhookid,
        client=client,
        block_notification=block_notification,
    ).parsed


async def asyncio_detailed(
    webhookid: str,
    *,
    client: AuthenticatedClient,
    block_notification: bool | Unset = False,
) -> Response[UnregisterWebhookResponseDefault]:
    """Unregister a webhook.

     See [API Guide: Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation
    details.

    Args:
        webhookid (str):
        block_notification (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnregisterWebhookResponseDefault]
    """

    kwargs = _get_kwargs(
        webhookid=webhookid,
        block_notification=block_notification,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhookid: str,
    *,
    client: AuthenticatedClient,
    block_notification: bool | Unset = False,
) -> UnregisterWebhookResponseDefault | None:
    """Unregister a webhook.

     See [API Guide: Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation
    details.

    Args:
        webhookid (str):
        block_notification (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnregisterWebhookResponseDefault
    """

    return (
        await asyncio_detailed(
            webhookid=webhookid,
            client=client,
            block_notification=block_notification,
        )
    ).parsed
