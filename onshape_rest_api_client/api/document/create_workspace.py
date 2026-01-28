from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_version_or_workspace_params import BTVersionOrWorkspaceParams
from ...models.bt_workspace_info import BTWorkspaceInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    *,
    body: BTVersionOrWorkspaceParams | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/documents/d/{did}/workspaces".format(
            did=quote(str(did), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTWorkspaceInfo:
    response_default = BTWorkspaceInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTWorkspaceInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    *,
    client: AuthenticatedClient,
    body: BTVersionOrWorkspaceParams | Unset = UNSET,
) -> Response[BTWorkspaceInfo]:
    """Create workspace by document ID.

    Args:
        did (str):
        body (BTVersionOrWorkspaceParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTWorkspaceInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    *,
    client: AuthenticatedClient,
    body: BTVersionOrWorkspaceParams | Unset = UNSET,
) -> BTWorkspaceInfo | None:
    """Create workspace by document ID.

    Args:
        did (str):
        body (BTVersionOrWorkspaceParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTWorkspaceInfo
    """

    return sync_detailed(
        did=did,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    *,
    client: AuthenticatedClient,
    body: BTVersionOrWorkspaceParams | Unset = UNSET,
) -> Response[BTWorkspaceInfo]:
    """Create workspace by document ID.

    Args:
        did (str):
        body (BTVersionOrWorkspaceParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTWorkspaceInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    *,
    client: AuthenticatedClient,
    body: BTVersionOrWorkspaceParams | Unset = UNSET,
) -> BTWorkspaceInfo | None:
    """Create workspace by document ID.

    Args:
        did (str):
        body (BTVersionOrWorkspaceParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTWorkspaceInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            client=client,
            body=body,
        )
    ).parsed
