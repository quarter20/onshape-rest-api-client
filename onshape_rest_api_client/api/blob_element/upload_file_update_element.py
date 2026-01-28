from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_document_element_processing_info import BTDocumentElementProcessingInfo
from ...models.upload_file_update_element_body import UploadFileUpdateElementBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    *,
    body: UploadFileUpdateElementBody | Unset = UNSET,
    link_document_id: str | Unset = "",
    parent_change_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["parentChangeId"] = parent_change_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/blobelements/d/{did}/w/{wid}/e/{eid}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTDocumentElementProcessingInfo:
    response_default = BTDocumentElementProcessingInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTDocumentElementProcessingInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: UploadFileUpdateElementBody | Unset = UNSET,
    link_document_id: str | Unset = "",
    parent_change_id: str | Unset = UNSET,
) -> Response[BTDocumentElementProcessingInfo]:
    r"""Update a blob element by uploading a file.

     Request body parameters are multipart fields, so you must use `\"Content-Type\":\"multipart/form-
    data\"` in the request header.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        parent_change_id (str | Unset):
        body (UploadFileUpdateElementBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTDocumentElementProcessingInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        body=body,
        link_document_id=link_document_id,
        parent_change_id=parent_change_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: UploadFileUpdateElementBody | Unset = UNSET,
    link_document_id: str | Unset = "",
    parent_change_id: str | Unset = UNSET,
) -> BTDocumentElementProcessingInfo | None:
    r"""Update a blob element by uploading a file.

     Request body parameters are multipart fields, so you must use `\"Content-Type\":\"multipart/form-
    data\"` in the request header.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        parent_change_id (str | Unset):
        body (UploadFileUpdateElementBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTDocumentElementProcessingInfo
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        client=client,
        body=body,
        link_document_id=link_document_id,
        parent_change_id=parent_change_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: UploadFileUpdateElementBody | Unset = UNSET,
    link_document_id: str | Unset = "",
    parent_change_id: str | Unset = UNSET,
) -> Response[BTDocumentElementProcessingInfo]:
    r"""Update a blob element by uploading a file.

     Request body parameters are multipart fields, so you must use `\"Content-Type\":\"multipart/form-
    data\"` in the request header.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        parent_change_id (str | Unset):
        body (UploadFileUpdateElementBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTDocumentElementProcessingInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        body=body,
        link_document_id=link_document_id,
        parent_change_id=parent_change_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: UploadFileUpdateElementBody | Unset = UNSET,
    link_document_id: str | Unset = "",
    parent_change_id: str | Unset = UNSET,
) -> BTDocumentElementProcessingInfo | None:
    r"""Update a blob element by uploading a file.

     Request body parameters are multipart fields, so you must use `\"Content-Type\":\"multipart/form-
    data\"` in the request header.

    Args:
        did (str):
        wid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        parent_change_id (str | Unset):
        body (UploadFileUpdateElementBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTDocumentElementProcessingInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            client=client,
            body=body,
            link_document_id=link_document_id,
            parent_change_id=parent_change_id,
        )
    ).parsed
