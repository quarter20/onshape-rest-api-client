from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_document_notes_params import BTDocumentNotesParams
from ...models.bt_global_tree_node_summary_info import BTGlobalTreeNodeSummaryInfo
from ...types import Response


def _get_kwargs(
    did: str,
    *,
    body: BTDocumentNotesParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/documents/{did}/notes".format(
            did=quote(str(did), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTGlobalTreeNodeSummaryInfo:
    response_default = BTGlobalTreeNodeSummaryInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTGlobalTreeNodeSummaryInfo]:
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
    body: BTDocumentNotesParams,
) -> Response[BTGlobalTreeNodeSummaryInfo]:
    """Update document notes by document ID.

     Use this endpoint to update documents notes. Use
    [updateDocumentAttributes](#/Document/updateDocumentAttributes) to update other document attributes.

    Args:
        did (str):
        body (BTDocumentNotesParams): Parameters for updating document notes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTGlobalTreeNodeSummaryInfo]
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
    body: BTDocumentNotesParams,
) -> BTGlobalTreeNodeSummaryInfo | None:
    """Update document notes by document ID.

     Use this endpoint to update documents notes. Use
    [updateDocumentAttributes](#/Document/updateDocumentAttributes) to update other document attributes.

    Args:
        did (str):
        body (BTDocumentNotesParams): Parameters for updating document notes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTGlobalTreeNodeSummaryInfo
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
    body: BTDocumentNotesParams,
) -> Response[BTGlobalTreeNodeSummaryInfo]:
    """Update document notes by document ID.

     Use this endpoint to update documents notes. Use
    [updateDocumentAttributes](#/Document/updateDocumentAttributes) to update other document attributes.

    Args:
        did (str):
        body (BTDocumentNotesParams): Parameters for updating document notes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTGlobalTreeNodeSummaryInfo]
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
    body: BTDocumentNotesParams,
) -> BTGlobalTreeNodeSummaryInfo | None:
    """Update document notes by document ID.

     Use this endpoint to update documents notes. Use
    [updateDocumentAttributes](#/Document/updateDocumentAttributes) to update other document attributes.

    Args:
        did (str):
        body (BTDocumentNotesParams): Parameters for updating document notes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTGlobalTreeNodeSummaryInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            client=client,
            body=body,
        )
    ).parsed
