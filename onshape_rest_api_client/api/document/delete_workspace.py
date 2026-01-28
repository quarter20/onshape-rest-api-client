from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_workspace_response_default import DeleteWorkspaceResponseDefault
from ...types import Response


def _get_kwargs(
    did: str,
    wid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/documents/d/{did}/workspaces/{wid}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteWorkspaceResponseDefault:
    response_default = DeleteWorkspaceResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteWorkspaceResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteWorkspaceResponseDefault]:
    """Delete workspace by document ID and workspace ID.

    Args:
        did (str):
        wid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWorkspaceResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
) -> DeleteWorkspaceResponseDefault | None:
    """Delete workspace by document ID and workspace ID.

    Args:
        did (str):
        wid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWorkspaceResponseDefault
    """

    return sync_detailed(
        did=did,
        wid=wid,
        client=client,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteWorkspaceResponseDefault]:
    """Delete workspace by document ID and workspace ID.

    Args:
        did (str):
        wid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWorkspaceResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
) -> DeleteWorkspaceResponseDefault | None:
    """Delete workspace by document ID and workspace ID.

    Args:
        did (str):
        wid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWorkspaceResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            client=client,
        )
    ).parsed
