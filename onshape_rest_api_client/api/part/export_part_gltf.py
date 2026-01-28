from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.export_part_gltf_wvm import ExportPartGltfWvm
from ...models.gl_tf import GlTF
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: ExportPartGltfWvm,
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
    output_separate_face_nodes: bool | Unset = False,
    face_id: list[str] | Unset = UNSET,
    output_face_appearances: bool | Unset = False,
    max_facet_width: float | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params["rollbackBarIndex"] = rollback_bar_index

    params["elementMicroversionId"] = element_microversion_id

    params["angleTolerance"] = angle_tolerance

    params["chordTolerance"] = chord_tolerance

    params["precomputedLevelOfDetail"] = precomputed_level_of_detail

    params["outputSeparateFaceNodes"] = output_separate_face_nodes

    json_face_id: list[str] | Unset = UNSET
    if not isinstance(face_id, Unset):
        json_face_id = face_id

    params["faceId"] = json_face_id

    params["outputFaceAppearances"] = output_face_appearances

    params["maxFacetWidth"] = max_facet_width

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/parts/d/{did}/{wvm}/{wvmid}/e/{eid}/partid/{partid}/gltf".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
            partid=quote(str(partid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GlTF | None:
    if response.status_code == 200:
        response_200 = GlTF.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GlTF]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: ExportPartGltfWvm,
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
    output_separate_face_nodes: bool | Unset = False,
    face_id: list[str] | Unset = UNSET,
    output_face_appearances: bool | Unset = False,
    max_facet_width: float | Unset = UNSET,
) -> Response[GlTF]:
    """Synchronously export a part to a glTF file.

     Creates a synchronous export of the part (with limited tessellation settings) to a glTF file.
    * Returns a 307 redirect from which to download the exported file.
    * Export is much faster than asynchronous endpoints at the expense of limited control on
    tessellation settings.
    * Use the [PartStudio/createPartStudioTranslation](#/PartStudio/createPartStudioTranslation)
    asynchronous export for greater control.

    See [API Guide: Synchronous Exports](https://onshape-public.github.io/docs/api-
    adv/translation/#synchronous-exports) for more details.

    Args:
        did (str):
        wvm (ExportPartGltfWvm):
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
        output_separate_face_nodes (bool | Unset):  Default: False.
        face_id (list[str] | Unset):
        output_face_appearances (bool | Unset):  Default: False.
        max_facet_width (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GlTF]
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
        output_separate_face_nodes=output_separate_face_nodes,
        face_id=face_id,
        output_face_appearances=output_face_appearances,
        max_facet_width=max_facet_width,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: ExportPartGltfWvm,
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
    output_separate_face_nodes: bool | Unset = False,
    face_id: list[str] | Unset = UNSET,
    output_face_appearances: bool | Unset = False,
    max_facet_width: float | Unset = UNSET,
) -> GlTF | None:
    """Synchronously export a part to a glTF file.

     Creates a synchronous export of the part (with limited tessellation settings) to a glTF file.
    * Returns a 307 redirect from which to download the exported file.
    * Export is much faster than asynchronous endpoints at the expense of limited control on
    tessellation settings.
    * Use the [PartStudio/createPartStudioTranslation](#/PartStudio/createPartStudioTranslation)
    asynchronous export for greater control.

    See [API Guide: Synchronous Exports](https://onshape-public.github.io/docs/api-
    adv/translation/#synchronous-exports) for more details.

    Args:
        did (str):
        wvm (ExportPartGltfWvm):
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
        output_separate_face_nodes (bool | Unset):  Default: False.
        face_id (list[str] | Unset):
        output_face_appearances (bool | Unset):  Default: False.
        max_facet_width (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GlTF
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
        output_separate_face_nodes=output_separate_face_nodes,
        face_id=face_id,
        output_face_appearances=output_face_appearances,
        max_facet_width=max_facet_width,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: ExportPartGltfWvm,
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
    output_separate_face_nodes: bool | Unset = False,
    face_id: list[str] | Unset = UNSET,
    output_face_appearances: bool | Unset = False,
    max_facet_width: float | Unset = UNSET,
) -> Response[GlTF]:
    """Synchronously export a part to a glTF file.

     Creates a synchronous export of the part (with limited tessellation settings) to a glTF file.
    * Returns a 307 redirect from which to download the exported file.
    * Export is much faster than asynchronous endpoints at the expense of limited control on
    tessellation settings.
    * Use the [PartStudio/createPartStudioTranslation](#/PartStudio/createPartStudioTranslation)
    asynchronous export for greater control.

    See [API Guide: Synchronous Exports](https://onshape-public.github.io/docs/api-
    adv/translation/#synchronous-exports) for more details.

    Args:
        did (str):
        wvm (ExportPartGltfWvm):
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
        output_separate_face_nodes (bool | Unset):  Default: False.
        face_id (list[str] | Unset):
        output_face_appearances (bool | Unset):  Default: False.
        max_facet_width (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GlTF]
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
        output_separate_face_nodes=output_separate_face_nodes,
        face_id=face_id,
        output_face_appearances=output_face_appearances,
        max_facet_width=max_facet_width,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: ExportPartGltfWvm,
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
    output_separate_face_nodes: bool | Unset = False,
    face_id: list[str] | Unset = UNSET,
    output_face_appearances: bool | Unset = False,
    max_facet_width: float | Unset = UNSET,
) -> GlTF | None:
    """Synchronously export a part to a glTF file.

     Creates a synchronous export of the part (with limited tessellation settings) to a glTF file.
    * Returns a 307 redirect from which to download the exported file.
    * Export is much faster than asynchronous endpoints at the expense of limited control on
    tessellation settings.
    * Use the [PartStudio/createPartStudioTranslation](#/PartStudio/createPartStudioTranslation)
    asynchronous export for greater control.

    See [API Guide: Synchronous Exports](https://onshape-public.github.io/docs/api-
    adv/translation/#synchronous-exports) for more details.

    Args:
        did (str):
        wvm (ExportPartGltfWvm):
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
        output_separate_face_nodes (bool | Unset):  Default: False.
        face_id (list[str] | Unset):
        output_face_appearances (bool | Unset):  Default: False.
        max_facet_width (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GlTF
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
            output_separate_face_nodes=output_separate_face_nodes,
            face_id=face_id,
            output_face_appearances=output_face_appearances,
            max_facet_width=max_facet_width,
        )
    ).parsed
