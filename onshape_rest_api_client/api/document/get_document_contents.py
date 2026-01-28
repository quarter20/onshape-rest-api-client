from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_document_contents_info import BTDocumentContentsInfo
from ...models.gbt_element_type import GBTElementType
from ...models.get_document_contents_wvm import GetDocumentContentsWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetDocumentContentsWvm,
    wvmid: str,
    *,
    link_document_id: str | Unset = "",
    element_type: GBTElementType | Unset = UNSET,
    element_id: str | Unset = UNSET,
    with_zip_contents: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    json_element_type: str | Unset = UNSET
    if not isinstance(element_type, Unset):
        json_element_type = element_type.value

    params["elementType"] = json_element_type

    params["elementId"] = element_id

    params["withZipContents"] = with_zip_contents

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents/d/{did}/{wvm}/{wvmid}/contents".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTDocumentContentsInfo:
    response_default = BTDocumentContentsInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTDocumentContentsInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetDocumentContentsWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    element_type: GBTElementType | Unset = UNSET,
    element_id: str | Unset = UNSET,
    with_zip_contents: bool | Unset = False,
) -> Response[BTDocumentContentsInfo]:
    """Retrieve tabs and folders by document ID and workspace or version or microversion ID.

     Returns information on tabs and folders in the document.

    Args:
        did (str):
        wvm (GetDocumentContentsWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        element_type (GBTElementType | Unset):
        element_id (str | Unset):
        with_zip_contents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTDocumentContentsInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        link_document_id=link_document_id,
        element_type=element_type,
        element_id=element_id,
        with_zip_contents=with_zip_contents,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetDocumentContentsWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    element_type: GBTElementType | Unset = UNSET,
    element_id: str | Unset = UNSET,
    with_zip_contents: bool | Unset = False,
) -> BTDocumentContentsInfo | None:
    """Retrieve tabs and folders by document ID and workspace or version or microversion ID.

     Returns information on tabs and folders in the document.

    Args:
        did (str):
        wvm (GetDocumentContentsWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        element_type (GBTElementType | Unset):
        element_id (str | Unset):
        with_zip_contents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTDocumentContentsInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        client=client,
        link_document_id=link_document_id,
        element_type=element_type,
        element_id=element_id,
        with_zip_contents=with_zip_contents,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetDocumentContentsWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    element_type: GBTElementType | Unset = UNSET,
    element_id: str | Unset = UNSET,
    with_zip_contents: bool | Unset = False,
) -> Response[BTDocumentContentsInfo]:
    """Retrieve tabs and folders by document ID and workspace or version or microversion ID.

     Returns information on tabs and folders in the document.

    Args:
        did (str):
        wvm (GetDocumentContentsWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        element_type (GBTElementType | Unset):
        element_id (str | Unset):
        with_zip_contents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTDocumentContentsInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        link_document_id=link_document_id,
        element_type=element_type,
        element_id=element_id,
        with_zip_contents=with_zip_contents,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetDocumentContentsWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    element_type: GBTElementType | Unset = UNSET,
    element_id: str | Unset = UNSET,
    with_zip_contents: bool | Unset = False,
) -> BTDocumentContentsInfo | None:
    """Retrieve tabs and folders by document ID and workspace or version or microversion ID.

     Returns information on tabs and folders in the document.

    Args:
        did (str):
        wvm (GetDocumentContentsWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        element_type (GBTElementType | Unset):
        element_id (str | Unset):
        with_zip_contents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTDocumentContentsInfo
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
            with_zip_contents=with_zip_contents,
        )
    ).parsed
