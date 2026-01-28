from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_translation_response_default import DeleteTranslationResponseDefault
from ...types import Response


def _get_kwargs(
    tid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/translations/{tid}".format(
            tid=quote(str(tid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteTranslationResponseDefault:
    response_default = DeleteTranslationResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteTranslationResponseDefault]:
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
) -> Response[DeleteTranslationResponseDefault]:
    """Delete a translation request.

    Args:
        tid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTranslationResponseDefault]
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
) -> DeleteTranslationResponseDefault | None:
    """Delete a translation request.

    Args:
        tid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTranslationResponseDefault
    """

    return sync_detailed(
        tid=tid,
        client=client,
    ).parsed


async def asyncio_detailed(
    tid: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteTranslationResponseDefault]:
    """Delete a translation request.

    Args:
        tid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTranslationResponseDefault]
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
) -> DeleteTranslationResponseDefault | None:
    """Delete a translation request.

    Args:
        tid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTranslationResponseDefault
    """

    return (
        await asyncio_detailed(
            tid=tid,
            client=client,
        )
    ).parsed
