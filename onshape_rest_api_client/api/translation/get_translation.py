from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_translation_request_info import BTTranslationRequestInfo
from ...types import Response


def _get_kwargs(
    tid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/translations/{tid}".format(
            tid=quote(str(tid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTTranslationRequestInfo:
    response_default = BTTranslationRequestInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTTranslationRequestInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTTranslationRequestInfo]:
    """Get information on an in-progress or completed translation by translation ID.

     When the translation is complete, `requestState` changes from `ACTIVE` to `DONE` or `FAILED`. See
    [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for more
    details.

    When polling for translations to complete, use a reasonable interval (e.g., avoid polling multiple
    times a second, use an exponential backoff strategy, etc.) or use [Webhooks](/docs/app-dev/webhook).
    See [Rate Limiting](/docs/api-adv/errors/#429) and [API Limits](/docs/auth/limits) for more
    information.

    Args:
        tid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTTranslationRequestInfo]
    """

    kwargs = _get_kwargs(
        tid=tid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tid: str,
    *,
    client: AuthenticatedClient,
) -> BTTranslationRequestInfo | None:
    """Get information on an in-progress or completed translation by translation ID.

     When the translation is complete, `requestState` changes from `ACTIVE` to `DONE` or `FAILED`. See
    [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for more
    details.

    When polling for translations to complete, use a reasonable interval (e.g., avoid polling multiple
    times a second, use an exponential backoff strategy, etc.) or use [Webhooks](/docs/app-dev/webhook).
    See [Rate Limiting](/docs/api-adv/errors/#429) and [API Limits](/docs/auth/limits) for more
    information.

    Args:
        tid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTTranslationRequestInfo
    """

    return sync_detailed(
        tid=tid,
        client=client,
    ).parsed


async def asyncio_detailed(
    tid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTTranslationRequestInfo]:
    """Get information on an in-progress or completed translation by translation ID.

     When the translation is complete, `requestState` changes from `ACTIVE` to `DONE` or `FAILED`. See
    [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for more
    details.

    When polling for translations to complete, use a reasonable interval (e.g., avoid polling multiple
    times a second, use an exponential backoff strategy, etc.) or use [Webhooks](/docs/app-dev/webhook).
    See [Rate Limiting](/docs/api-adv/errors/#429) and [API Limits](/docs/auth/limits) for more
    information.

    Args:
        tid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTTranslationRequestInfo]
    """

    kwargs = _get_kwargs(
        tid=tid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tid: str,
    *,
    client: AuthenticatedClient,
) -> BTTranslationRequestInfo | None:
    """Get information on an in-progress or completed translation by translation ID.

     When the translation is complete, `requestState` changes from `ACTIVE` to `DONE` or `FAILED`. See
    [API Guide: Model Translation](https://onshape-public.github.io/docs/api-adv/translation/) for more
    details.

    When polling for translations to complete, use a reasonable interval (e.g., avoid polling multiple
    times a second, use an exponential backoff strategy, etc.) or use [Webhooks](/docs/app-dev/webhook).
    See [Rate Limiting](/docs/api-adv/errors/#429) and [API Limits](/docs/auth/limits) for more
    information.

    Args:
        tid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTTranslationRequestInfo
    """

    return (
        await asyncio_detailed(
            tid=tid,
            client=client,
        )
    ).parsed
