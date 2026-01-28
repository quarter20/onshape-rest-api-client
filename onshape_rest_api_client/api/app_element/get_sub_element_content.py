from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_element_content_info import BTAppElementContentInfo
from ...models.get_sub_element_content_wvm import GetSubElementContentWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetSubElementContentWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
    base_change_id: str | Unset = UNSET,
    subelement_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["transactionId"] = transaction_id

    params["changeId"] = change_id

    params["baseChangeId"] = base_change_id

    params["subelementId"] = subelement_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/appelements/d/{did}/{wvm}/{wvmid}/e/{eid}/content".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAppElementContentInfo:
    response_default = BTAppElementContentInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAppElementContentInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetSubElementContentWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
    base_change_id: str | Unset = UNSET,
    subelement_id: str | Unset = UNSET,
) -> Response[BTAppElementContentInfo]:
    """Get a list of all subelement IDs in a specified workspace/version/microversion.

    Args:
        did (str):
        wvm (GetSubElementContentWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        change_id (str | Unset):
        base_change_id (str | Unset):
        subelement_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementContentInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        change_id=change_id,
        base_change_id=base_change_id,
        subelement_id=subelement_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetSubElementContentWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
    base_change_id: str | Unset = UNSET,
    subelement_id: str | Unset = UNSET,
) -> BTAppElementContentInfo | None:
    """Get a list of all subelement IDs in a specified workspace/version/microversion.

    Args:
        did (str):
        wvm (GetSubElementContentWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        change_id (str | Unset):
        base_change_id (str | Unset):
        subelement_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementContentInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        change_id=change_id,
        base_change_id=base_change_id,
        subelement_id=subelement_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetSubElementContentWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
    base_change_id: str | Unset = UNSET,
    subelement_id: str | Unset = UNSET,
) -> Response[BTAppElementContentInfo]:
    """Get a list of all subelement IDs in a specified workspace/version/microversion.

    Args:
        did (str):
        wvm (GetSubElementContentWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        change_id (str | Unset):
        base_change_id (str | Unset):
        subelement_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementContentInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        change_id=change_id,
        base_change_id=base_change_id,
        subelement_id=subelement_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetSubElementContentWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
    base_change_id: str | Unset = UNSET,
    subelement_id: str | Unset = UNSET,
) -> BTAppElementContentInfo | None:
    """Get a list of all subelement IDs in a specified workspace/version/microversion.

    Args:
        did (str):
        wvm (GetSubElementContentWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        change_id (str | Unset):
        base_change_id (str | Unset):
        subelement_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementContentInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            link_document_id=link_document_id,
            transaction_id=transaction_id,
            change_id=change_id,
            base_change_id=base_change_id,
            subelement_id=subelement_id,
        )
    ).parsed
