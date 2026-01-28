from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_element_references_resolve_info import BTAppElementReferencesResolveInfo
from ...models.resolve_references_wvm import ResolveReferencesWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: ResolveReferencesWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    reference_ids: str | Unset = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["transactionId"] = transaction_id

    params["parentChangeId"] = parent_change_id

    params["includeInternal"] = include_internal

    params["referenceIds"] = reference_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/appelements/d/{did}/{wvm}/{wvmid}/e/{eid}/resolvereferences".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTAppElementReferencesResolveInfo:
    response_default = BTAppElementReferencesResolveInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAppElementReferencesResolveInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: ResolveReferencesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    reference_ids: str | Unset = "",
) -> Response[BTAppElementReferencesResolveInfo]:
    """Resolves bulk app element references.

     For bulk operations only. Use `resolveReference` for a single operation.

    Args:
        did (str):
        wvm (ResolveReferencesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        include_internal (bool | Unset):  Default: False.
        reference_ids (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementReferencesResolveInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        include_internal=include_internal,
        reference_ids=reference_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: ResolveReferencesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    reference_ids: str | Unset = "",
) -> BTAppElementReferencesResolveInfo | None:
    """Resolves bulk app element references.

     For bulk operations only. Use `resolveReference` for a single operation.

    Args:
        did (str):
        wvm (ResolveReferencesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        include_internal (bool | Unset):  Default: False.
        reference_ids (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementReferencesResolveInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        include_internal=include_internal,
        reference_ids=reference_ids,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: ResolveReferencesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    reference_ids: str | Unset = "",
) -> Response[BTAppElementReferencesResolveInfo]:
    """Resolves bulk app element references.

     For bulk operations only. Use `resolveReference` for a single operation.

    Args:
        did (str):
        wvm (ResolveReferencesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        include_internal (bool | Unset):  Default: False.
        reference_ids (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementReferencesResolveInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        include_internal=include_internal,
        reference_ids=reference_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: ResolveReferencesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    reference_ids: str | Unset = "",
) -> BTAppElementReferencesResolveInfo | None:
    """Resolves bulk app element references.

     For bulk operations only. Use `resolveReference` for a single operation.

    Args:
        did (str):
        wvm (ResolveReferencesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        include_internal (bool | Unset):  Default: False.
        reference_ids (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementReferencesResolveInfo
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
            parent_change_id=parent_change_id,
            include_internal=include_internal,
            reference_ids=reference_ids,
        )
    ).parsed
