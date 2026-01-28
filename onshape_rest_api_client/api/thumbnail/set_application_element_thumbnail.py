from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_application_element_thumbnail_params_array import BTApplicationElementThumbnailParamsArray
from ...models.set_application_element_thumbnail_response_default import SetApplicationElementThumbnailResponseDefault
from ...models.set_application_element_thumbnail_wv import SetApplicationElementThumbnailWv
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wv: SetApplicationElementThumbnailWv,
    wvid: str,
    eid: str,
    *,
    body: BTApplicationElementThumbnailParamsArray,
    link_document_id: str | Unset = "",
    overwrite: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["overwrite"] = overwrite

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/thumbnails/d/{did}/{wv}/{wvid}/e/{eid}".format(
            did=quote(str(did), safe=""),
            wv=quote(str(wv), safe=""),
            wvid=quote(str(wvid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SetApplicationElementThumbnailResponseDefault:
    response_default = SetApplicationElementThumbnailResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SetApplicationElementThumbnailResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wv: SetApplicationElementThumbnailWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTApplicationElementThumbnailParamsArray,
    link_document_id: str | Unset = "",
    overwrite: bool | Unset = False,
) -> Response[SetApplicationElementThumbnailResponseDefault]:
    """Set the thumbnail image for an application element.

     * Allows 3rd-party applications to set thumbnails for their elements.
    * Application elements can have both primary and secondary thumbnails. A primary thumbnail
    represents the top-level of the element. A secondary thumbnail can represent sub-components of the
    element (e.g., a drawing sheet).
    * To update one or more thumbnails, you must set the overwrite query param to `true` and supply the
    entire set of thumbnails. All previous thumbnails will be deleted prior to updating the element with
    the latest images.

    Args:
        did (str):
        wv (SetApplicationElementThumbnailWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        overwrite (bool | Unset):  Default: False.
        body (BTApplicationElementThumbnailParamsArray):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetApplicationElementThumbnailResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        body=body,
        link_document_id=link_document_id,
        overwrite=overwrite,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wv: SetApplicationElementThumbnailWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTApplicationElementThumbnailParamsArray,
    link_document_id: str | Unset = "",
    overwrite: bool | Unset = False,
) -> SetApplicationElementThumbnailResponseDefault | None:
    """Set the thumbnail image for an application element.

     * Allows 3rd-party applications to set thumbnails for their elements.
    * Application elements can have both primary and secondary thumbnails. A primary thumbnail
    represents the top-level of the element. A secondary thumbnail can represent sub-components of the
    element (e.g., a drawing sheet).
    * To update one or more thumbnails, you must set the overwrite query param to `true` and supply the
    entire set of thumbnails. All previous thumbnails will be deleted prior to updating the element with
    the latest images.

    Args:
        did (str):
        wv (SetApplicationElementThumbnailWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        overwrite (bool | Unset):  Default: False.
        body (BTApplicationElementThumbnailParamsArray):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetApplicationElementThumbnailResponseDefault
    """

    return sync_detailed(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        client=client,
        body=body,
        link_document_id=link_document_id,
        overwrite=overwrite,
    ).parsed


async def asyncio_detailed(
    did: str,
    wv: SetApplicationElementThumbnailWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTApplicationElementThumbnailParamsArray,
    link_document_id: str | Unset = "",
    overwrite: bool | Unset = False,
) -> Response[SetApplicationElementThumbnailResponseDefault]:
    """Set the thumbnail image for an application element.

     * Allows 3rd-party applications to set thumbnails for their elements.
    * Application elements can have both primary and secondary thumbnails. A primary thumbnail
    represents the top-level of the element. A secondary thumbnail can represent sub-components of the
    element (e.g., a drawing sheet).
    * To update one or more thumbnails, you must set the overwrite query param to `true` and supply the
    entire set of thumbnails. All previous thumbnails will be deleted prior to updating the element with
    the latest images.

    Args:
        did (str):
        wv (SetApplicationElementThumbnailWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        overwrite (bool | Unset):  Default: False.
        body (BTApplicationElementThumbnailParamsArray):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetApplicationElementThumbnailResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        body=body,
        link_document_id=link_document_id,
        overwrite=overwrite,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wv: SetApplicationElementThumbnailWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTApplicationElementThumbnailParamsArray,
    link_document_id: str | Unset = "",
    overwrite: bool | Unset = False,
) -> SetApplicationElementThumbnailResponseDefault | None:
    """Set the thumbnail image for an application element.

     * Allows 3rd-party applications to set thumbnails for their elements.
    * Application elements can have both primary and secondary thumbnails. A primary thumbnail
    represents the top-level of the element. A secondary thumbnail can represent sub-components of the
    element (e.g., a drawing sheet).
    * To update one or more thumbnails, you must set the overwrite query param to `true` and supply the
    entire set of thumbnails. All previous thumbnails will be deleted prior to updating the element with
    the latest images.

    Args:
        did (str):
        wv (SetApplicationElementThumbnailWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        overwrite (bool | Unset):  Default: False.
        body (BTApplicationElementThumbnailParamsArray):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetApplicationElementThumbnailResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wv=wv,
            wvid=wvid,
            eid=eid,
            client=client,
            body=body,
            link_document_id=link_document_id,
            overwrite=overwrite,
        )
    ).parsed
