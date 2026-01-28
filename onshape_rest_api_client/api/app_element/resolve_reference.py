from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_element_reference_resolve_info import BTAppElementReferenceResolveInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    rid: str,
    *,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    link_document_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["transactionId"] = transaction_id

    params["parentChangeId"] = parent_change_id

    params["includeInternal"] = include_internal

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/appelements/d/{did}/{wvm}/{wvmid}/e/{eid}/references/{rid}".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
            rid=quote(str(rid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTAppElementReferenceResolveInfo:
    response_default = BTAppElementReferenceResolveInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAppElementReferenceResolveInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    rid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    link_document_id: str | Unset = UNSET,
) -> Response[BTAppElementReferenceResolveInfo]:
    """Resolves a single reference to an app element.

     For single operations only. Use `resolveReferences` for bulk operations.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        rid (str):
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        include_internal (bool | Unset):  Default: False.
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementReferenceResolveInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        rid=rid,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        include_internal=include_internal,
        link_document_id=link_document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    rid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    link_document_id: str | Unset = UNSET,
) -> BTAppElementReferenceResolveInfo | None:
    """Resolves a single reference to an app element.

     For single operations only. Use `resolveReferences` for bulk operations.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        rid (str):
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        include_internal (bool | Unset):  Default: False.
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementReferenceResolveInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        rid=rid,
        client=client,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        include_internal=include_internal,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    rid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    link_document_id: str | Unset = UNSET,
) -> Response[BTAppElementReferenceResolveInfo]:
    """Resolves a single reference to an app element.

     For single operations only. Use `resolveReferences` for bulk operations.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        rid (str):
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        include_internal (bool | Unset):  Default: False.
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementReferenceResolveInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        rid=rid,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        include_internal=include_internal,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    rid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    link_document_id: str | Unset = UNSET,
) -> BTAppElementReferenceResolveInfo | None:
    """Resolves a single reference to an app element.

     For single operations only. Use `resolveReferences` for bulk operations.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        rid (str):
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        include_internal (bool | Unset):  Default: False.
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementReferenceResolveInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            rid=rid,
            client=client,
            transaction_id=transaction_id,
            parent_change_id=parent_change_id,
            include_internal=include_internal,
            link_document_id=link_document_id,
        )
    ).parsed
