from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_merge_preview_info import BTMergePreviewInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    *,
    link_document_id: str | Unset = "",
    source_type: str,
    source_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["sourceType"] = source_type

    params["sourceId"] = source_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents/{did}/w/{wid}/mergePreview".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTMergePreviewInfo:
    response_default = BTMergePreviewInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTMergePreviewInfo]:
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
    link_document_id: str | Unset = "",
    source_type: str,
    source_id: str,
) -> Response[BTMergePreviewInfo]:
    """Merge preview of changes that will occur based on document ID, workspace ID and source
    workspace/version ID

    Args:
        did (str):
        wid (str):
        link_document_id (str | Unset):  Default: ''.
        source_type (str):
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTMergePreviewInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        link_document_id=link_document_id,
        source_type=source_type,
        source_id=source_id,
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
    link_document_id: str | Unset = "",
    source_type: str,
    source_id: str,
) -> BTMergePreviewInfo | None:
    """Merge preview of changes that will occur based on document ID, workspace ID and source
    workspace/version ID

    Args:
        did (str):
        wid (str):
        link_document_id (str | Unset):  Default: ''.
        source_type (str):
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTMergePreviewInfo
    """

    return sync_detailed(
        did=did,
        wid=wid,
        client=client,
        link_document_id=link_document_id,
        source_type=source_type,
        source_id=source_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    source_type: str,
    source_id: str,
) -> Response[BTMergePreviewInfo]:
    """Merge preview of changes that will occur based on document ID, workspace ID and source
    workspace/version ID

    Args:
        did (str):
        wid (str):
        link_document_id (str | Unset):  Default: ''.
        source_type (str):
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTMergePreviewInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        link_document_id=link_document_id,
        source_type=source_type,
        source_id=source_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    source_type: str,
    source_id: str,
) -> BTMergePreviewInfo | None:
    """Merge preview of changes that will occur based on document ID, workspace ID and source
    workspace/version ID

    Args:
        did (str):
        wid (str):
        link_document_id (str | Unset):  Default: ''.
        source_type (str):
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTMergePreviewInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            client=client,
            link_document_id=link_document_id,
            source_type=source_type,
            source_id=source_id,
        )
    ).parsed
