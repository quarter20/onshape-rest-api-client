from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_export_tessellated_faces_response_898 import BTExportTessellatedFacesResponse898
from ...models.get_faces_1_wvm import GetFaces1Wvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetFaces1Wvm,
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
    face_id: list[str] | Unset = UNSET,
    output_face_appearances: bool | Unset = False,
    max_facet_width: float | Unset = UNSET,
    output_vertex_normals: bool | Unset = False,
    output_facet_normals: bool | Unset = True,
    output_texture_coordinates: bool | Unset = False,
    output_index_table: bool | Unset = False,
    output_error_faces: bool | Unset = False,
    combine_composite_part_constituents: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params["rollbackBarIndex"] = rollback_bar_index

    params["elementMicroversionId"] = element_microversion_id

    params["angleTolerance"] = angle_tolerance

    params["chordTolerance"] = chord_tolerance

    params["precomputedLevelOfDetail"] = precomputed_level_of_detail

    json_face_id: list[str] | Unset = UNSET
    if not isinstance(face_id, Unset):
        json_face_id = face_id

    params["faceId"] = json_face_id

    params["outputFaceAppearances"] = output_face_appearances

    params["maxFacetWidth"] = max_facet_width

    params["outputVertexNormals"] = output_vertex_normals

    params["outputFacetNormals"] = output_facet_normals

    params["outputTextureCoordinates"] = output_texture_coordinates

    params["outputIndexTable"] = output_index_table

    params["outputErrorFaces"] = output_error_faces

    params["combineCompositePartConstituents"] = combine_composite_part_constituents

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/parts/d/{did}/{wvm}/{wvmid}/e/{eid}/partid/{partid}/tessellatedfaces".format(
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
) -> BTExportTessellatedFacesResponse898:
    response_default = BTExportTessellatedFacesResponse898.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTExportTessellatedFacesResponse898]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetFaces1Wvm,
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
    face_id: list[str] | Unset = UNSET,
    output_face_appearances: bool | Unset = False,
    max_facet_width: float | Unset = UNSET,
    output_vertex_normals: bool | Unset = False,
    output_facet_normals: bool | Unset = True,
    output_texture_coordinates: bool | Unset = False,
    output_index_table: bool | Unset = False,
    output_error_faces: bool | Unset = False,
    combine_composite_part_constituents: bool | Unset = False,
) -> Response[BTExportTessellatedFacesResponse898]:
    """Get a list of a part's tessellation faces.

     Coordinates are in meters (m).

    Args:
        did (str):
        wvm (GetFaces1Wvm):
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
        face_id (list[str] | Unset):
        output_face_appearances (bool | Unset):  Default: False.
        max_facet_width (float | Unset):
        output_vertex_normals (bool | Unset):  Default: False.
        output_facet_normals (bool | Unset):  Default: True.
        output_texture_coordinates (bool | Unset):  Default: False.
        output_index_table (bool | Unset):  Default: False.
        output_error_faces (bool | Unset):  Default: False.
        combine_composite_part_constituents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTExportTessellatedFacesResponse898]
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
        face_id=face_id,
        output_face_appearances=output_face_appearances,
        max_facet_width=max_facet_width,
        output_vertex_normals=output_vertex_normals,
        output_facet_normals=output_facet_normals,
        output_texture_coordinates=output_texture_coordinates,
        output_index_table=output_index_table,
        output_error_faces=output_error_faces,
        combine_composite_part_constituents=combine_composite_part_constituents,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetFaces1Wvm,
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
    face_id: list[str] | Unset = UNSET,
    output_face_appearances: bool | Unset = False,
    max_facet_width: float | Unset = UNSET,
    output_vertex_normals: bool | Unset = False,
    output_facet_normals: bool | Unset = True,
    output_texture_coordinates: bool | Unset = False,
    output_index_table: bool | Unset = False,
    output_error_faces: bool | Unset = False,
    combine_composite_part_constituents: bool | Unset = False,
) -> BTExportTessellatedFacesResponse898 | None:
    """Get a list of a part's tessellation faces.

     Coordinates are in meters (m).

    Args:
        did (str):
        wvm (GetFaces1Wvm):
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
        face_id (list[str] | Unset):
        output_face_appearances (bool | Unset):  Default: False.
        max_facet_width (float | Unset):
        output_vertex_normals (bool | Unset):  Default: False.
        output_facet_normals (bool | Unset):  Default: True.
        output_texture_coordinates (bool | Unset):  Default: False.
        output_index_table (bool | Unset):  Default: False.
        output_error_faces (bool | Unset):  Default: False.
        combine_composite_part_constituents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTExportTessellatedFacesResponse898
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
        face_id=face_id,
        output_face_appearances=output_face_appearances,
        max_facet_width=max_facet_width,
        output_vertex_normals=output_vertex_normals,
        output_facet_normals=output_facet_normals,
        output_texture_coordinates=output_texture_coordinates,
        output_index_table=output_index_table,
        output_error_faces=output_error_faces,
        combine_composite_part_constituents=combine_composite_part_constituents,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetFaces1Wvm,
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
    face_id: list[str] | Unset = UNSET,
    output_face_appearances: bool | Unset = False,
    max_facet_width: float | Unset = UNSET,
    output_vertex_normals: bool | Unset = False,
    output_facet_normals: bool | Unset = True,
    output_texture_coordinates: bool | Unset = False,
    output_index_table: bool | Unset = False,
    output_error_faces: bool | Unset = False,
    combine_composite_part_constituents: bool | Unset = False,
) -> Response[BTExportTessellatedFacesResponse898]:
    """Get a list of a part's tessellation faces.

     Coordinates are in meters (m).

    Args:
        did (str):
        wvm (GetFaces1Wvm):
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
        face_id (list[str] | Unset):
        output_face_appearances (bool | Unset):  Default: False.
        max_facet_width (float | Unset):
        output_vertex_normals (bool | Unset):  Default: False.
        output_facet_normals (bool | Unset):  Default: True.
        output_texture_coordinates (bool | Unset):  Default: False.
        output_index_table (bool | Unset):  Default: False.
        output_error_faces (bool | Unset):  Default: False.
        combine_composite_part_constituents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTExportTessellatedFacesResponse898]
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
        face_id=face_id,
        output_face_appearances=output_face_appearances,
        max_facet_width=max_facet_width,
        output_vertex_normals=output_vertex_normals,
        output_facet_normals=output_facet_normals,
        output_texture_coordinates=output_texture_coordinates,
        output_index_table=output_index_table,
        output_error_faces=output_error_faces,
        combine_composite_part_constituents=combine_composite_part_constituents,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetFaces1Wvm,
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
    face_id: list[str] | Unset = UNSET,
    output_face_appearances: bool | Unset = False,
    max_facet_width: float | Unset = UNSET,
    output_vertex_normals: bool | Unset = False,
    output_facet_normals: bool | Unset = True,
    output_texture_coordinates: bool | Unset = False,
    output_index_table: bool | Unset = False,
    output_error_faces: bool | Unset = False,
    combine_composite_part_constituents: bool | Unset = False,
) -> BTExportTessellatedFacesResponse898 | None:
    """Get a list of a part's tessellation faces.

     Coordinates are in meters (m).

    Args:
        did (str):
        wvm (GetFaces1Wvm):
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
        face_id (list[str] | Unset):
        output_face_appearances (bool | Unset):  Default: False.
        max_facet_width (float | Unset):
        output_vertex_normals (bool | Unset):  Default: False.
        output_facet_normals (bool | Unset):  Default: True.
        output_texture_coordinates (bool | Unset):  Default: False.
        output_index_table (bool | Unset):  Default: False.
        output_error_faces (bool | Unset):  Default: False.
        combine_composite_part_constituents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTExportTessellatedFacesResponse898
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
            face_id=face_id,
            output_face_appearances=output_face_appearances,
            max_facet_width=max_facet_width,
            output_vertex_normals=output_vertex_normals,
            output_facet_normals=output_facet_normals,
            output_texture_coordinates=output_texture_coordinates,
            output_index_table=output_index_table,
            output_error_faces=output_error_faces,
            combine_composite_part_constituents=combine_composite_part_constituents,
        )
    ).parsed
