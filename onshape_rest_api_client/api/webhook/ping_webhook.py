from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.ping_webhook_response_default import PingWebhookResponseDefault
from ...types import Response


def _get_kwargs(
    webhookid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks/{webhookid}/ping".format(
            webhookid=quote(str(webhookid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PingWebhookResponseDefault:
    response_default = PingWebhookResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PingWebhookResponseDefault]:
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
) -> Response[PingWebhookResponseDefault]:
    """Ping a webhook.

     See [API Guide: Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation
    details.

    Args:
        webhookid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PingWebhookResponseDefault]
    """

    kwargs = _get_kwargs(
        webhookid=webhookid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhookid: str,
    *,
    client: AuthenticatedClient,
) -> PingWebhookResponseDefault | None:
    """Ping a webhook.

     See [API Guide: Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation
    details.

    Args:
        webhookid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PingWebhookResponseDefault
    """

    return sync_detailed(
        webhookid=webhookid,
        client=client,
    ).parsed


async def asyncio_detailed(
    webhookid: str,
    *,
    client: AuthenticatedClient,
) -> Response[PingWebhookResponseDefault]:
    """Ping a webhook.

     See [API Guide: Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation
    details.

    Args:
        webhookid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PingWebhookResponseDefault]
    """

    kwargs = _get_kwargs(
        webhookid=webhookid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhookid: str,
    *,
    client: AuthenticatedClient,
) -> PingWebhookResponseDefault | None:
    """Ping a webhook.

     See [API Guide: Webhooks](https://onshape-public.github.io/docs/app-dev/webhook/) for implementation
    details.

    Args:
        webhookid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PingWebhookResponseDefault
    """

    return (
        await asyncio_detailed(
            webhookid=webhookid,
            client=client,
        )
    ).parsed
