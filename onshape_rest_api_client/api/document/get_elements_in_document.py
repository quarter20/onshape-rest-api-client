from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bt_document_element_info import BTDocumentElementInfo
from ...models.get_elements_in_document_wvm import GetElementsInDocumentWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetElementsInDocumentWvm,
    wvmid: str,
    *,
    link_document_id: str | Unset = "",
    element_type: str | Unset = "",
    element_id: str | Unset = "",
    with_thumbnails: bool | Unset = False,
    with_zip_contents: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["elementType"] = element_type

    params["elementId"] = element_id

    params["withThumbnails"] = with_thumbnails

    params["withZipContents"] = with_zip_contents

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents/d/{did}/{wvm}/{wvmid}/elements".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[BTDocumentElementInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BTDocumentElementInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[BTDocumentElementInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetElementsInDocumentWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    element_type: str | Unset = "",
    element_id: str | Unset = "",
    with_thumbnails: bool | Unset = False,
    with_zip_contents: bool | Unset = False,
) -> Response[list[BTDocumentElementInfo]]:
    """Retrieve tabs by document ID and workspace or version or microversion ID.

     This endpoint only returns the tabs and not folders in the document. Use the
    [getDocumentContents](#/Document/getDocumentContents) endpoint to get information about folders and
    tabs.

    Args:
        did (str):
        wvm (GetElementsInDocumentWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        element_type (str | Unset):  Default: ''.
        element_id (str | Unset):  Default: ''.
        with_thumbnails (bool | Unset):  Default: False.
        with_zip_contents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTDocumentElementInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        link_document_id=link_document_id,
        element_type=element_type,
        element_id=element_id,
        with_thumbnails=with_thumbnails,
        with_zip_contents=with_zip_contents,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetElementsInDocumentWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    element_type: str | Unset = "",
    element_id: str | Unset = "",
    with_thumbnails: bool | Unset = False,
    with_zip_contents: bool | Unset = False,
) -> list[BTDocumentElementInfo] | None:
    """Retrieve tabs by document ID and workspace or version or microversion ID.

     This endpoint only returns the tabs and not folders in the document. Use the
    [getDocumentContents](#/Document/getDocumentContents) endpoint to get information about folders and
    tabs.

    Args:
        did (str):
        wvm (GetElementsInDocumentWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        element_type (str | Unset):  Default: ''.
        element_id (str | Unset):  Default: ''.
        with_thumbnails (bool | Unset):  Default: False.
        with_zip_contents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTDocumentElementInfo]
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        client=client,
        link_document_id=link_document_id,
        element_type=element_type,
        element_id=element_id,
        with_thumbnails=with_thumbnails,
        with_zip_contents=with_zip_contents,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetElementsInDocumentWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    element_type: str | Unset = "",
    element_id: str | Unset = "",
    with_thumbnails: bool | Unset = False,
    with_zip_contents: bool | Unset = False,
) -> Response[list[BTDocumentElementInfo]]:
    """Retrieve tabs by document ID and workspace or version or microversion ID.

     This endpoint only returns the tabs and not folders in the document. Use the
    [getDocumentContents](#/Document/getDocumentContents) endpoint to get information about folders and
    tabs.

    Args:
        did (str):
        wvm (GetElementsInDocumentWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        element_type (str | Unset):  Default: ''.
        element_id (str | Unset):  Default: ''.
        with_thumbnails (bool | Unset):  Default: False.
        with_zip_contents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTDocumentElementInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        link_document_id=link_document_id,
        element_type=element_type,
        element_id=element_id,
        with_thumbnails=with_thumbnails,
        with_zip_contents=with_zip_contents,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetElementsInDocumentWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    element_type: str | Unset = "",
    element_id: str | Unset = "",
    with_thumbnails: bool | Unset = False,
    with_zip_contents: bool | Unset = False,
) -> list[BTDocumentElementInfo] | None:
    """Retrieve tabs by document ID and workspace or version or microversion ID.

     This endpoint only returns the tabs and not folders in the document. Use the
    [getDocumentContents](#/Document/getDocumentContents) endpoint to get information about folders and
    tabs.

    Args:
        did (str):
        wvm (GetElementsInDocumentWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        element_type (str | Unset):  Default: ''.
        element_id (str | Unset):  Default: ''.
        with_thumbnails (bool | Unset):  Default: False.
        with_zip_contents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTDocumentElementInfo]
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            client=client,
            link_document_id=link_document_id,
            element_type=element_type,
            element_id=element_id,
            with_thumbnails=with_thumbnails,
            with_zip_contents=with_zip_contents,
        )
    ).parsed
