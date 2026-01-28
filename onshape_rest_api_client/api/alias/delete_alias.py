from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_alias_response_default import DeleteAliasResponseDefault
from ...types import Response


def _get_kwargs(
    aid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/aliases/{aid}".format(
            aid=quote(str(aid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteAliasResponseDefault:
    response_default = DeleteAliasResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteAliasResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    aid: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteAliasResponseDefault]:
    """Delete an alias from your enterprise.

     `Manage users and teams` global permission is required to call this API.

    Args:
        aid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAliasResponseDefault]
    """

    kwargs = _get_kwargs(
        aid=aid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    aid: str,
    *,
    client: AuthenticatedClient,
) -> DeleteAliasResponseDefault | None:
    """Delete an alias from your enterprise.

     `Manage users and teams` global permission is required to call this API.

    Args:
        aid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAliasResponseDefault
    """

    return sync_detailed(
        aid=aid,
        client=client,
    ).parsed


async def asyncio_detailed(
    aid: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteAliasResponseDefault]:
    """Delete an alias from your enterprise.

     `Manage users and teams` global permission is required to call this API.

    Args:
        aid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAliasResponseDefault]
    """

    kwargs = _get_kwargs(
        aid=aid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    aid: str,
    *,
    client: AuthenticatedClient,
) -> DeleteAliasResponseDefault | None:
    """Delete an alias from your enterprise.

     `Manage users and teams` global permission is required to call this API.

    Args:
        aid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAliasResponseDefault
    """

    return (
        await asyncio_detailed(
            aid=aid,
            client=client,
        )
    ).parsed
