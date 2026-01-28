from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bt_version_info import BTVersionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    vid: str,
    *,
    parents: bool | Unset = False,
    link_document_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["parents"] = parents

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents/d/{did}/versions/{vid}".format(
            did=quote(str(did), safe=""),
            vid=quote(str(vid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTVersionInfo | None:
    if response.status_code == 200:
        response_200 = BTVersionInfo.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTVersionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
    parents: bool | Unset = False,
    link_document_id: str | Unset = UNSET,
) -> Response[BTVersionInfo]:
    """Retrieve version by document ID and version ID.

    Args:
        did (str):
        vid (str):
        parents (bool | Unset):  Default: False.
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTVersionInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        vid=vid,
        parents=parents,
        link_document_id=link_document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
    parents: bool | Unset = False,
    link_document_id: str | Unset = UNSET,
) -> BTVersionInfo | None:
    """Retrieve version by document ID and version ID.

    Args:
        did (str):
        vid (str):
        parents (bool | Unset):  Default: False.
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTVersionInfo
    """

    return sync_detailed(
        did=did,
        vid=vid,
        client=client,
        parents=parents,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
    parents: bool | Unset = False,
    link_document_id: str | Unset = UNSET,
) -> Response[BTVersionInfo]:
    """Retrieve version by document ID and version ID.

    Args:
        did (str):
        vid (str):
        parents (bool | Unset):  Default: False.
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTVersionInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        vid=vid,
        parents=parents,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
    parents: bool | Unset = False,
    link_document_id: str | Unset = UNSET,
) -> BTVersionInfo | None:
    """Retrieve version by document ID and version ID.

    Args:
        did (str):
        vid (str):
        parents (bool | Unset):  Default: False.
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTVersionInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            vid=vid,
            client=client,
            parents=parents,
            link_document_id=link_document_id,
        )
    ).parsed
