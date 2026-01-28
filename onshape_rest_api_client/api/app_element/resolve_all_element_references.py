from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.resolve_all_element_references_response_default import ResolveAllElementReferencesResponseDefault
from ...models.resolve_all_element_references_wvm import ResolveAllElementReferencesWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: ResolveAllElementReferencesWvm,
    wvmid: str,
    *,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    reference_ids: str | Unset = "",
    element_ids: str | Unset = "",
    drawings_only: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["transactionId"] = transaction_id

    params["parentChangeId"] = parent_change_id

    params["includeInternal"] = include_internal

    params["referenceIds"] = reference_ids

    params["elementIds"] = element_ids

    params["drawingsOnly"] = drawings_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/appelements/d/{did}/{wvm}/{wvmid}/resolvereferences".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ResolveAllElementReferencesResponseDefault:
    response_default = ResolveAllElementReferencesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResolveAllElementReferencesResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: ResolveAllElementReferencesWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    reference_ids: str | Unset = "",
    element_ids: str | Unset = "",
    drawings_only: bool | Unset = False,
) -> Response[ResolveAllElementReferencesResponseDefault]:
    """Resolves bulk app element references.

     Resolve all references for all workspace elements. For bulk operations  only. Use
    `resolveReferences` for a single element.

    Args:
        did (str):
        wvm (ResolveAllElementReferencesWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        include_internal (bool | Unset):  Default: False.
        reference_ids (str | Unset):  Default: ''.
        element_ids (str | Unset):  Default: ''.
        drawings_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResolveAllElementReferencesResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        include_internal=include_internal,
        reference_ids=reference_ids,
        element_ids=element_ids,
        drawings_only=drawings_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: ResolveAllElementReferencesWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    reference_ids: str | Unset = "",
    element_ids: str | Unset = "",
    drawings_only: bool | Unset = False,
) -> ResolveAllElementReferencesResponseDefault | None:
    """Resolves bulk app element references.

     Resolve all references for all workspace elements. For bulk operations  only. Use
    `resolveReferences` for a single element.

    Args:
        did (str):
        wvm (ResolveAllElementReferencesWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        include_internal (bool | Unset):  Default: False.
        reference_ids (str | Unset):  Default: ''.
        element_ids (str | Unset):  Default: ''.
        drawings_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResolveAllElementReferencesResponseDefault
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        client=client,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        include_internal=include_internal,
        reference_ids=reference_ids,
        element_ids=element_ids,
        drawings_only=drawings_only,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: ResolveAllElementReferencesWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    reference_ids: str | Unset = "",
    element_ids: str | Unset = "",
    drawings_only: bool | Unset = False,
) -> Response[ResolveAllElementReferencesResponseDefault]:
    """Resolves bulk app element references.

     Resolve all references for all workspace elements. For bulk operations  only. Use
    `resolveReferences` for a single element.

    Args:
        did (str):
        wvm (ResolveAllElementReferencesWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        include_internal (bool | Unset):  Default: False.
        reference_ids (str | Unset):  Default: ''.
        element_ids (str | Unset):  Default: ''.
        drawings_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResolveAllElementReferencesResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        include_internal=include_internal,
        reference_ids=reference_ids,
        element_ids=element_ids,
        drawings_only=drawings_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: ResolveAllElementReferencesWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    include_internal: bool | Unset = False,
    reference_ids: str | Unset = "",
    element_ids: str | Unset = "",
    drawings_only: bool | Unset = False,
) -> ResolveAllElementReferencesResponseDefault | None:
    """Resolves bulk app element references.

     Resolve all references for all workspace elements. For bulk operations  only. Use
    `resolveReferences` for a single element.

    Args:
        did (str):
        wvm (ResolveAllElementReferencesWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        include_internal (bool | Unset):  Default: False.
        reference_ids (str | Unset):  Default: ''.
        element_ids (str | Unset):  Default: ''.
        drawings_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResolveAllElementReferencesResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            client=client,
            link_document_id=link_document_id,
            transaction_id=transaction_id,
            parent_change_id=parent_change_id,
            include_internal=include_internal,
            reference_ids=reference_ids,
            element_ids=element_ids,
            drawings_only=drawings_only,
        )
    ).parsed
