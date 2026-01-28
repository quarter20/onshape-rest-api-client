from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_export_tessellated_edges_response_327 import BTExportTessellatedEdgesResponse327
from ...models.get_edges_wvm import GetEdgesWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetEdgesWvm,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    precomputed_level_of_detail: str | Unset = UNSET,
    edge_id: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params["rollbackBarIndex"] = rollback_bar_index

    params["elementMicroversionId"] = element_microversion_id

    params["angleTolerance"] = angle_tolerance

    params["chordTolerance"] = chord_tolerance

    params["precomputedLevelOfDetail"] = precomputed_level_of_detail

    json_edge_id: list[str] | Unset = UNSET
    if not isinstance(edge_id, Unset):
        json_edge_id = edge_id

    params["edgeId"] = json_edge_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/parts/d/{did}/{wvm}/{wvmid}/e/{eid}/partid/{partid}/tessellatededges".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
            partid=quote(str(partid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTExportTessellatedEdgesResponse327:
    response_default = BTExportTessellatedEdgesResponse327.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTExportTessellatedEdgesResponse327]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetEdgesWvm,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    precomputed_level_of_detail: str | Unset = UNSET,
    edge_id: list[str] | Unset = UNSET,
) -> Response[BTExportTessellatedEdgesResponse327]:
    """Get a list of a part's tessellation edges.

     Returns the coordinates (in meters) of each edge's endpoints.

    Args:
        did (str):
        wvm (GetEdgesWvm):
        wvmid (str):
        eid (str):
        partid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        angle_tolerance (float | Unset):
        chord_tolerance (float | Unset):
        precomputed_level_of_detail (str | Unset):
        edge_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTExportTessellatedEdgesResponse327]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        partid=partid,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
        angle_tolerance=angle_tolerance,
        chord_tolerance=chord_tolerance,
        precomputed_level_of_detail=precomputed_level_of_detail,
        edge_id=edge_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetEdgesWvm,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    precomputed_level_of_detail: str | Unset = UNSET,
    edge_id: list[str] | Unset = UNSET,
) -> BTExportTessellatedEdgesResponse327 | None:
    """Get a list of a part's tessellation edges.

     Returns the coordinates (in meters) of each edge's endpoints.

    Args:
        did (str):
        wvm (GetEdgesWvm):
        wvmid (str):
        eid (str):
        partid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        angle_tolerance (float | Unset):
        chord_tolerance (float | Unset):
        precomputed_level_of_detail (str | Unset):
        edge_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTExportTessellatedEdgesResponse327
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        partid=partid,
        client=client,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
        angle_tolerance=angle_tolerance,
        chord_tolerance=chord_tolerance,
        precomputed_level_of_detail=precomputed_level_of_detail,
        edge_id=edge_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetEdgesWvm,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    precomputed_level_of_detail: str | Unset = UNSET,
    edge_id: list[str] | Unset = UNSET,
) -> Response[BTExportTessellatedEdgesResponse327]:
    """Get a list of a part's tessellation edges.

     Returns the coordinates (in meters) of each edge's endpoints.

    Args:
        did (str):
        wvm (GetEdgesWvm):
        wvmid (str):
        eid (str):
        partid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        angle_tolerance (float | Unset):
        chord_tolerance (float | Unset):
        precomputed_level_of_detail (str | Unset):
        edge_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTExportTessellatedEdgesResponse327]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        partid=partid,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
        angle_tolerance=angle_tolerance,
        chord_tolerance=chord_tolerance,
        precomputed_level_of_detail=precomputed_level_of_detail,
        edge_id=edge_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetEdgesWvm,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    precomputed_level_of_detail: str | Unset = UNSET,
    edge_id: list[str] | Unset = UNSET,
) -> BTExportTessellatedEdgesResponse327 | None:
    """Get a list of a part's tessellation edges.

     Returns the coordinates (in meters) of each edge's endpoints.

    Args:
        did (str):
        wvm (GetEdgesWvm):
        wvmid (str):
        eid (str):
        partid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        angle_tolerance (float | Unset):
        chord_tolerance (float | Unset):
        precomputed_level_of_detail (str | Unset):
        edge_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTExportTessellatedEdgesResponse327
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            partid=partid,
            client=client,
            link_document_id=link_document_id,
            configuration=configuration,
            rollback_bar_index=rollback_bar_index,
            element_microversion_id=element_microversion_id,
            angle_tolerance=angle_tolerance,
            chord_tolerance=chord_tolerance,
            precomputed_level_of_detail=precomputed_level_of_detail,
            edge_id=edge_id,
        )
    ).parsed
