from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_thumbnail_info import BTThumbnailInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    vid: str,
    *,
    link_document_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/thumbnails/d/{did}/v/{vid}".format(
            did=quote(str(did), safe=""),
            vid=quote(str(vid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTThumbnailInfo:
    response_default = BTThumbnailInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTThumbnailInfo]:
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
    link_document_id: str | Unset = UNSET,
) -> Response[BTThumbnailInfo]:
    """Get the thumbnail info for a version of a document.

     * By default, returns thumbnail info for the element with the most-recently generated image. If you
    pinned an element for the document thumbnail, that element will always be used for the document-
    level thumbnail, if it exists in the workspace.
    * See also: [Tech tip on how to change a document thumbnail in
    onshape](https://www.onshape.com/en/resource-center/tech-tips/tech-tip-how-to-change-a-document-
    thumbnail-in-onshape)

    Args:
        did (str):
        vid (str):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTThumbnailInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        vid=vid,
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
    link_document_id: str | Unset = UNSET,
) -> BTThumbnailInfo | None:
    """Get the thumbnail info for a version of a document.

     * By default, returns thumbnail info for the element with the most-recently generated image. If you
    pinned an element for the document thumbnail, that element will always be used for the document-
    level thumbnail, if it exists in the workspace.
    * See also: [Tech tip on how to change a document thumbnail in
    onshape](https://www.onshape.com/en/resource-center/tech-tips/tech-tip-how-to-change-a-document-
    thumbnail-in-onshape)

    Args:
        did (str):
        vid (str):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTThumbnailInfo
    """

    return sync_detailed(
        did=did,
        vid=vid,
        client=client,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = UNSET,
) -> Response[BTThumbnailInfo]:
    """Get the thumbnail info for a version of a document.

     * By default, returns thumbnail info for the element with the most-recently generated image. If you
    pinned an element for the document thumbnail, that element will always be used for the document-
    level thumbnail, if it exists in the workspace.
    * See also: [Tech tip on how to change a document thumbnail in
    onshape](https://www.onshape.com/en/resource-center/tech-tips/tech-tip-how-to-change-a-document-
    thumbnail-in-onshape)

    Args:
        did (str):
        vid (str):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTThumbnailInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        vid=vid,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    vid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = UNSET,
) -> BTThumbnailInfo | None:
    """Get the thumbnail info for a version of a document.

     * By default, returns thumbnail info for the element with the most-recently generated image. If you
    pinned an element for the document thumbnail, that element will always be used for the document-
    level thumbnail, if it exists in the workspace.
    * See also: [Tech tip on how to change a document thumbnail in
    onshape](https://www.onshape.com/en/resource-center/tech-tips/tech-tip-how-to-change-a-document-
    thumbnail-in-onshape)

    Args:
        did (str):
        vid (str):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTThumbnailInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            vid=vid,
            client=client,
            link_document_id=link_document_id,
        )
    ).parsed
