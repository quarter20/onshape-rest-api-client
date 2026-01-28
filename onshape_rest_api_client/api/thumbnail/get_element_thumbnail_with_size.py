from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_element_thumbnail_with_size_response_default import GetElementThumbnailWithSizeResponseDefault
from ...models.get_element_thumbnail_with_size_wv import GetElementThumbnailWithSizeWv
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wv: GetElementThumbnailWithSizeWv,
    wvid: str,
    eid: str,
    sz: str,
    *,
    link_document_id: str | Unset = "",
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
    reject_empty: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["t"] = t

    params["skipDefaultImage"] = skip_default_image

    params["rejectEmpty"] = reject_empty

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/thumbnails/d/{did}/{wv}/{wvid}/e/{eid}/s/{sz}".format(
            did=quote(str(did), safe=""),
            wv=quote(str(wv), safe=""),
            wvid=quote(str(wvid), safe=""),
            eid=quote(str(eid), safe=""),
            sz=quote(str(sz), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetElementThumbnailWithSizeResponseDefault:
    response_default = GetElementThumbnailWithSizeResponseDefault.from_dict(response.content)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetElementThumbnailWithSizeResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wv: GetElementThumbnailWithSizeWv,
    wvid: str,
    eid: str,
    sz: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
    reject_empty: bool | Unset = False,
) -> Response[GetElementThumbnailWithSizeResponseDefault]:
    """Get the thumbnail image with the given size for an element.

    Args:
        did (str):
        wv (GetElementThumbnailWithSizeWv):
        wvid (str):
        eid (str):
        sz (str):
        link_document_id (str | Unset):  Default: ''.
        t (str | Unset):
        skip_default_image (str | Unset):  Default: ''.
        reject_empty (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetElementThumbnailWithSizeResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        sz=sz,
        link_document_id=link_document_id,
        t=t,
        skip_default_image=skip_default_image,
        reject_empty=reject_empty,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wv: GetElementThumbnailWithSizeWv,
    wvid: str,
    eid: str,
    sz: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
    reject_empty: bool | Unset = False,
) -> GetElementThumbnailWithSizeResponseDefault | None:
    """Get the thumbnail image with the given size for an element.

    Args:
        did (str):
        wv (GetElementThumbnailWithSizeWv):
        wvid (str):
        eid (str):
        sz (str):
        link_document_id (str | Unset):  Default: ''.
        t (str | Unset):
        skip_default_image (str | Unset):  Default: ''.
        reject_empty (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetElementThumbnailWithSizeResponseDefault
    """

    return sync_detailed(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        sz=sz,
        client=client,
        link_document_id=link_document_id,
        t=t,
        skip_default_image=skip_default_image,
        reject_empty=reject_empty,
    ).parsed


async def asyncio_detailed(
    did: str,
    wv: GetElementThumbnailWithSizeWv,
    wvid: str,
    eid: str,
    sz: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
    reject_empty: bool | Unset = False,
) -> Response[GetElementThumbnailWithSizeResponseDefault]:
    """Get the thumbnail image with the given size for an element.

    Args:
        did (str):
        wv (GetElementThumbnailWithSizeWv):
        wvid (str):
        eid (str):
        sz (str):
        link_document_id (str | Unset):  Default: ''.
        t (str | Unset):
        skip_default_image (str | Unset):  Default: ''.
        reject_empty (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetElementThumbnailWithSizeResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        sz=sz,
        link_document_id=link_document_id,
        t=t,
        skip_default_image=skip_default_image,
        reject_empty=reject_empty,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wv: GetElementThumbnailWithSizeWv,
    wvid: str,
    eid: str,
    sz: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    t: str | Unset = UNSET,
    skip_default_image: str | Unset = "",
    reject_empty: bool | Unset = False,
) -> GetElementThumbnailWithSizeResponseDefault | None:
    """Get the thumbnail image with the given size for an element.

    Args:
        did (str):
        wv (GetElementThumbnailWithSizeWv):
        wvid (str):
        eid (str):
        sz (str):
        link_document_id (str | Unset):  Default: ''.
        t (str | Unset):
        skip_default_image (str | Unset):  Default: ''.
        reject_empty (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetElementThumbnailWithSizeResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wv=wv,
            wvid=wvid,
            eid=eid,
            sz=sz,
            client=client,
            link_document_id=link_document_id,
            t=t,
            skip_default_image=skip_default_image,
            reject_empty=reject_empty,
        )
    ).parsed
