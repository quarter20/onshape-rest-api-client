from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_assembly_definition_info import BTAssemblyDefinitionInfo
from ...models.get_assembly_definition_wvm import GetAssemblyDefinitionWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetAssemblyDefinitionWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    include_mate_features: bool | Unset = False,
    include_non_solids: bool | Unset = False,
    include_mate_connectors: bool | Unset = False,
    exclude_suppressed: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params["explodedViewId"] = exploded_view_id

    params["includeMateFeatures"] = include_mate_features

    params["includeNonSolids"] = include_non_solids

    params["includeMateConnectors"] = include_mate_connectors

    params["excludeSuppressed"] = exclude_suppressed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assemblies/d/{did}/{wvm}/{wvmid}/e/{eid}".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAssemblyDefinitionInfo:
    response_default = BTAssemblyDefinitionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAssemblyDefinitionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetAssemblyDefinitionWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    include_mate_features: bool | Unset = False,
    include_non_solids: bool | Unset = False,
    include_mate_connectors: bool | Unset = False,
    exclude_suppressed: bool | Unset = False,
) -> Response[BTAssemblyDefinitionInfo]:
    """Get definition information for the specified assembly.

     All coordinates and translation matrix components are in meters (m).

    Args:
        did (str):
        wvm (GetAssemblyDefinitionWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        exploded_view_id (str | Unset):
        include_mate_features (bool | Unset):  Default: False.
        include_non_solids (bool | Unset):  Default: False.
        include_mate_connectors (bool | Unset):  Default: False.
        exclude_suppressed (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAssemblyDefinitionInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        exploded_view_id=exploded_view_id,
        include_mate_features=include_mate_features,
        include_non_solids=include_non_solids,
        include_mate_connectors=include_mate_connectors,
        exclude_suppressed=exclude_suppressed,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetAssemblyDefinitionWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    include_mate_features: bool | Unset = False,
    include_non_solids: bool | Unset = False,
    include_mate_connectors: bool | Unset = False,
    exclude_suppressed: bool | Unset = False,
) -> BTAssemblyDefinitionInfo | None:
    """Get definition information for the specified assembly.

     All coordinates and translation matrix components are in meters (m).

    Args:
        did (str):
        wvm (GetAssemblyDefinitionWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        exploded_view_id (str | Unset):
        include_mate_features (bool | Unset):  Default: False.
        include_non_solids (bool | Unset):  Default: False.
        include_mate_connectors (bool | Unset):  Default: False.
        exclude_suppressed (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAssemblyDefinitionInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        configuration=configuration,
        exploded_view_id=exploded_view_id,
        include_mate_features=include_mate_features,
        include_non_solids=include_non_solids,
        include_mate_connectors=include_mate_connectors,
        exclude_suppressed=exclude_suppressed,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetAssemblyDefinitionWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    include_mate_features: bool | Unset = False,
    include_non_solids: bool | Unset = False,
    include_mate_connectors: bool | Unset = False,
    exclude_suppressed: bool | Unset = False,
) -> Response[BTAssemblyDefinitionInfo]:
    """Get definition information for the specified assembly.

     All coordinates and translation matrix components are in meters (m).

    Args:
        did (str):
        wvm (GetAssemblyDefinitionWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        exploded_view_id (str | Unset):
        include_mate_features (bool | Unset):  Default: False.
        include_non_solids (bool | Unset):  Default: False.
        include_mate_connectors (bool | Unset):  Default: False.
        exclude_suppressed (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAssemblyDefinitionInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        exploded_view_id=exploded_view_id,
        include_mate_features=include_mate_features,
        include_non_solids=include_non_solids,
        include_mate_connectors=include_mate_connectors,
        exclude_suppressed=exclude_suppressed,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetAssemblyDefinitionWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    include_mate_features: bool | Unset = False,
    include_non_solids: bool | Unset = False,
    include_mate_connectors: bool | Unset = False,
    exclude_suppressed: bool | Unset = False,
) -> BTAssemblyDefinitionInfo | None:
    """Get definition information for the specified assembly.

     All coordinates and translation matrix components are in meters (m).

    Args:
        did (str):
        wvm (GetAssemblyDefinitionWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        exploded_view_id (str | Unset):
        include_mate_features (bool | Unset):  Default: False.
        include_non_solids (bool | Unset):  Default: False.
        include_mate_connectors (bool | Unset):  Default: False.
        exclude_suppressed (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAssemblyDefinitionInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            link_document_id=link_document_id,
            configuration=configuration,
            exploded_view_id=exploded_view_id,
            include_mate_features=include_mate_features,
            include_non_solids=include_non_solids,
            include_mate_connectors=include_mate_connectors,
            exclude_suppressed=exclude_suppressed,
        )
    ).parsed
