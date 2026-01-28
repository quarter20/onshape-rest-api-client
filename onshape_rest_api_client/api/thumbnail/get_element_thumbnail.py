from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_thumbnail_info import BTThumbnailInfo
from ...models.get_element_thumbnail_wv import GetElementThumbnailWv
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wv: GetElementThumbnailWv,
    wvid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/thumbnails/d/{did}/{wv}/{wvid}/e/{eid}".format(
            did=quote(str(did), safe=""),
            wv=quote(str(wv), safe=""),
            wvid=quote(str(wvid), safe=""),
            eid=quote(str(eid), safe=""),
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
    wv: GetElementThumbnailWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
) -> Response[BTThumbnailInfo]:
    """Get the thumbnail info structure for an element.

     Returns thumbnail info for the given document, workspace or version, and element.

    Args:
        did (str):
        wv (GetElementThumbnailWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTThumbnailInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        link_document_id=link_document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wv: GetElementThumbnailWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
) -> BTThumbnailInfo | None:
    """Get the thumbnail info structure for an element.

     Returns thumbnail info for the given document, workspace or version, and element.

    Args:
        did (str):
        wv (GetElementThumbnailWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTThumbnailInfo
    """

    return sync_detailed(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wv: GetElementThumbnailWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
) -> Response[BTThumbnailInfo]:
    """Get the thumbnail info structure for an element.

     Returns thumbnail info for the given document, workspace or version, and element.

    Args:
        did (str):
        wv (GetElementThumbnailWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTThumbnailInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wv: GetElementThumbnailWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
) -> BTThumbnailInfo | None:
    """Get the thumbnail info structure for an element.

     Returns thumbnail info for the given document, workspace or version, and element.

    Args:
        did (str):
        wv (GetElementThumbnailWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTThumbnailInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wv=wv,
            wvid=wvid,
            eid=eid,
            client=client,
            link_document_id=link_document_id,
        )
    ).parsed
