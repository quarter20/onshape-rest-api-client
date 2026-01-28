from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_thumbnail_info import BTThumbnailInfo
from ...types import Response


def _get_kwargs(
    did: str,
    wid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/thumbnails/d/{did}/w/{wid}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
        ),
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
    wid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTThumbnailInfo]:
    """Get the thumbnail info for a workspace.

     * By default, returns thumbnail info for the element with the most-recently generated image. If you
    pinned an element for the document thumbnail, that element will always be used for the document-
    level thumbnail, if it exists in the workspace.
    * See also: [Tech tip on how to change a document thumbnail in
    onshape](https://www.onshape.com/en/resource-center/tech-tips/tech-tip-how-to-change-a-document-
    thumbnail-in-onshape)

    Args:
        did (str):
        wid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTThumbnailInfo]
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
) -> BTThumbnailInfo | None:
    """Get the thumbnail info for a workspace.

     * By default, returns thumbnail info for the element with the most-recently generated image. If you
    pinned an element for the document thumbnail, that element will always be used for the document-
    level thumbnail, if it exists in the workspace.
    * See also: [Tech tip on how to change a document thumbnail in
    onshape](https://www.onshape.com/en/resource-center/tech-tips/tech-tip-how-to-change-a-document-
    thumbnail-in-onshape)

    Args:
        did (str):
        wid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTThumbnailInfo
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
) -> Response[BTThumbnailInfo]:
    """Get the thumbnail info for a workspace.

     * By default, returns thumbnail info for the element with the most-recently generated image. If you
    pinned an element for the document thumbnail, that element will always be used for the document-
    level thumbnail, if it exists in the workspace.
    * See also: [Tech tip on how to change a document thumbnail in
    onshape](https://www.onshape.com/en/resource-center/tech-tips/tech-tip-how-to-change-a-document-
    thumbnail-in-onshape)

    Args:
        did (str):
        wid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTThumbnailInfo]
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
) -> BTThumbnailInfo | None:
    """Get the thumbnail info for a workspace.

     * By default, returns thumbnail info for the element with the most-recently generated image. If you
    pinned an element for the document thumbnail, that element will always be used for the document-
    level thumbnail, if it exists in the workspace.
    * See also: [Tech tip on how to change a document thumbnail in
    onshape](https://www.onshape.com/en/resource-center/tech-tips/tech-tip-how-to-change-a-document-
    thumbnail-in-onshape)

    Args:
        did (str):
        wid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTThumbnailInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            client=client,
        )
    ).parsed
