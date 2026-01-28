from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bt_copy_document_info import BTCopyDocumentInfo
from ...models.bt_copy_document_params import BTCopyDocumentParams
from ...types import Response


def _get_kwargs(
    did: str,
    wid: str,
    *,
    body: BTCopyDocumentParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/documents/{did}/workspaces/{wid}/copy".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTCopyDocumentInfo | None:
    if response.status_code == 200:
        response_200 = BTCopyDocumentInfo.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTCopyDocumentInfo]:
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
    body: BTCopyDocumentParams,
) -> Response[BTCopyDocumentInfo]:
    """Copy workspace by document ID and workspace ID.

    Args:
        did (str):
        wid (str):
        body (BTCopyDocumentParams): Options for the new copied document.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTCopyDocumentInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        body=body,
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
    body: BTCopyDocumentParams,
) -> BTCopyDocumentInfo | None:
    """Copy workspace by document ID and workspace ID.

    Args:
        did (str):
        wid (str):
        body (BTCopyDocumentParams): Options for the new copied document.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTCopyDocumentInfo
    """

    return sync_detailed(
        did=did,
        wid=wid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTCopyDocumentParams,
) -> Response[BTCopyDocumentInfo]:
    """Copy workspace by document ID and workspace ID.

    Args:
        did (str):
        wid (str):
        body (BTCopyDocumentParams): Options for the new copied document.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTCopyDocumentInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTCopyDocumentParams,
) -> BTCopyDocumentInfo | None:
    """Copy workspace by document ID and workspace ID.

    Args:
        did (str):
        wid (str):
        body (BTCopyDocumentParams): Options for the new copied document.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTCopyDocumentInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            client=client,
            body=body,
        )
    ).parsed
