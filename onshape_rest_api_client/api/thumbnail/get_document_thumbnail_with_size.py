from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_document_thumbnail_with_size_response_default import GetDocumentThumbnailWithSizeResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    sz: str,
    *,
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["t"] = t

    params["skipDefaultImage"] = skip_default_image

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/thumbnails/d/{did}/w/{wid}/s/{sz}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            sz=quote(str(sz), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetDocumentThumbnailWithSizeResponseDefault:
    response_default = GetDocumentThumbnailWithSizeResponseDefault.from_dict(response.content)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetDocumentThumbnailWithSizeResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wid: str,
    sz: str,
    *,
    client: AuthenticatedClient,
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
) -> Response[GetDocumentThumbnailWithSizeResponseDefault]:
    """Get the thumbnail image with the given size for a document.

     * By default, returns thumbnail image for the element with the most-recently generated image. If you
    pinned an element for the document thumbnail, that element will always be used for the document-
    level thumbnail, if it exists in the workspace.
    * See also: [Tech tip on how to change a document thumbnail in
    onshape](https://www.onshape.com/en/resource-center/tech-tips/tech-tip-how-to-change-a-document-
    thumbnail-in-onshape)

    Args:
        did (str):
        wid (str):
        sz (str):
        t (str | Unset):
        skip_default_image (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDocumentThumbnailWithSizeResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        sz=sz,
        t=t,
        skip_default_image=skip_default_image,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    sz: str,
    *,
    client: AuthenticatedClient,
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
) -> GetDocumentThumbnailWithSizeResponseDefault | None:
    """Get the thumbnail image with the given size for a document.

     * By default, returns thumbnail image for the element with the most-recently generated image. If you
    pinned an element for the document thumbnail, that element will always be used for the document-
    level thumbnail, if it exists in the workspace.
    * See also: [Tech tip on how to change a document thumbnail in
    onshape](https://www.onshape.com/en/resource-center/tech-tips/tech-tip-how-to-change-a-document-
    thumbnail-in-onshape)

    Args:
        did (str):
        wid (str):
        sz (str):
        t (str | Unset):
        skip_default_image (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDocumentThumbnailWithSizeResponseDefault
    """

    return sync_detailed(
        did=did,
        wid=wid,
        sz=sz,
        client=client,
        t=t,
        skip_default_image=skip_default_image,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    sz: str,
    *,
    client: AuthenticatedClient,
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
) -> Response[GetDocumentThumbnailWithSizeResponseDefault]:
    """Get the thumbnail image with the given size for a document.

     * By default, returns thumbnail image for the element with the most-recently generated image. If you
    pinned an element for the document thumbnail, that element will always be used for the document-
    level thumbnail, if it exists in the workspace.
    * See also: [Tech tip on how to change a document thumbnail in
    onshape](https://www.onshape.com/en/resource-center/tech-tips/tech-tip-how-to-change-a-document-
    thumbnail-in-onshape)

    Args:
        did (str):
        wid (str):
        sz (str):
        t (str | Unset):
        skip_default_image (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDocumentThumbnailWithSizeResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        sz=sz,
        t=t,
        skip_default_image=skip_default_image,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    sz: str,
    *,
    client: AuthenticatedClient,
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
) -> GetDocumentThumbnailWithSizeResponseDefault | None:
    """Get the thumbnail image with the given size for a document.

     * By default, returns thumbnail image for the element with the most-recently generated image. If you
    pinned an element for the document thumbnail, that element will always be used for the document-
    level thumbnail, if it exists in the workspace.
    * See also: [Tech tip on how to change a document thumbnail in
    onshape](https://www.onshape.com/en/resource-center/tech-tips/tech-tip-how-to-change-a-document-
    thumbnail-in-onshape)

    Args:
        did (str):
        wid (str):
        sz (str):
        t (str | Unset):
        skip_default_image (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDocumentThumbnailWithSizeResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            sz=sz,
            client=client,
            t=t,
            skip_default_image=skip_default_image,
        )
    ).parsed
