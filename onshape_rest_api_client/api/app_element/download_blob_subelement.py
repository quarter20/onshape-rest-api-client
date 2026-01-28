from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    did: str,
    vm: str,
    vmid: str,
    eid: str,
    bid: str,
    *,
    content_disposition: str | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    params: dict[str, Any] = {}

    params["contentDisposition"] = content_disposition

    params["transactionId"] = transaction_id

    params["changeId"] = change_id

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/appelements/d/{did}/{vm}/{vmid}/e/{eid}/blob/{bid}".format(
            did=quote(str(did), safe=""),
            vm=quote(str(vm), safe=""),
            vmid=quote(str(vmid), safe=""),
            eid=quote(str(eid), safe=""),
            bid=quote(str(bid), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> File:
    response_default = File(payload=BytesIO(response.json()))

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    vm: str,
    vmid: str,
    eid: str,
    bid: str,
    *,
    client: AuthenticatedClient,
    content_disposition: str | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> Response[File]:
    """Download a blob subelement from the specified app element.

     Download a blob subelement as a file.

    Args:
        did (str):
        vm (str):
        vmid (str):
        eid (str):
        bid (str):
        content_disposition (str | Unset):
        transaction_id (str | Unset):
        change_id (str | Unset):
        link_document_id (str | Unset):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        did=did,
        vm=vm,
        vmid=vmid,
        eid=eid,
        bid=bid,
        content_disposition=content_disposition,
        transaction_id=transaction_id,
        change_id=change_id,
        link_document_id=link_document_id,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    vm: str,
    vmid: str,
    eid: str,
    bid: str,
    *,
    client: AuthenticatedClient,
    content_disposition: str | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> File | None:
    """Download a blob subelement from the specified app element.

     Download a blob subelement as a file.

    Args:
        did (str):
        vm (str):
        vmid (str):
        eid (str):
        bid (str):
        content_disposition (str | Unset):
        transaction_id (str | Unset):
        change_id (str | Unset):
        link_document_id (str | Unset):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        did=did,
        vm=vm,
        vmid=vmid,
        eid=eid,
        bid=bid,
        client=client,
        content_disposition=content_disposition,
        transaction_id=transaction_id,
        change_id=change_id,
        link_document_id=link_document_id,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    did: str,
    vm: str,
    vmid: str,
    eid: str,
    bid: str,
    *,
    client: AuthenticatedClient,
    content_disposition: str | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> Response[File]:
    """Download a blob subelement from the specified app element.

     Download a blob subelement as a file.

    Args:
        did (str):
        vm (str):
        vmid (str):
        eid (str):
        bid (str):
        content_disposition (str | Unset):
        transaction_id (str | Unset):
        change_id (str | Unset):
        link_document_id (str | Unset):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        did=did,
        vm=vm,
        vmid=vmid,
        eid=eid,
        bid=bid,
        content_disposition=content_disposition,
        transaction_id=transaction_id,
        change_id=change_id,
        link_document_id=link_document_id,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    vm: str,
    vmid: str,
    eid: str,
    bid: str,
    *,
    client: AuthenticatedClient,
    content_disposition: str | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> File | None:
    """Download a blob subelement from the specified app element.

     Download a blob subelement as a file.

    Args:
        did (str):
        vm (str):
        vmid (str):
        eid (str):
        bid (str):
        content_disposition (str | Unset):
        transaction_id (str | Unset):
        change_id (str | Unset):
        link_document_id (str | Unset):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            did=did,
            vm=vm,
            vmid=vmid,
            eid=eid,
            bid=bid,
            client=client,
            content_disposition=content_disposition,
            transaction_id=transaction_id,
            change_id=change_id,
            link_document_id=link_document_id,
            if_none_match=if_none_match,
        )
    ).parsed
