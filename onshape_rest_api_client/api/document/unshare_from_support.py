from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.unshare_from_support_response_default import UnshareFromSupportResponseDefault
from ...types import Response


def _get_kwargs(
    did: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/documents/{did}/shareWithSupport".format(
            did=quote(str(did), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UnshareFromSupportResponseDefault:
    response_default = UnshareFromSupportResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UnshareFromSupportResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[UnshareFromSupportResponseDefault]:
    """Unshare document with support.

    Args:
        did (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnshareFromSupportResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    *,
    client: AuthenticatedClient | Client,
) -> UnshareFromSupportResponseDefault | None:
    """Unshare document with support.

    Args:
        did (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnshareFromSupportResponseDefault
    """

    return sync_detailed(
        did=did,
        client=client,
    ).parsed


async def asyncio_detailed(
    did: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[UnshareFromSupportResponseDefault]:
    """Unshare document with support.

    Args:
        did (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnshareFromSupportResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    *,
    client: AuthenticatedClient | Client,
) -> UnshareFromSupportResponseDefault | None:
    """Unshare document with support.

    Args:
        did (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnshareFromSupportResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            client=client,
        )
    ).parsed
