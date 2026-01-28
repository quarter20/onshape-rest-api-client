from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_export_model_bodies_response_734 import BTExportModelBodiesResponse734
from ...models.get_part_studio_body_details_wvm import GetPartStudioBodyDetailsWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetPartStudioBodyDetailsWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    part_ids: list[str] | Unset = UNSET,
    include_surfaces: bool | Unset = False,
    include_composite_parts: bool | Unset = False,
    include_geometric_data: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params["rollbackBarIndex"] = rollback_bar_index

    params["elementMicroversionId"] = element_microversion_id

    json_part_ids: list[str] | Unset = UNSET
    if not isinstance(part_ids, Unset):
        json_part_ids = part_ids

    params["partIds"] = json_part_ids

    params["includeSurfaces"] = include_surfaces

    params["includeCompositeParts"] = include_composite_parts

    params["includeGeometricData"] = include_geometric_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/bodydetails".format(
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
) -> BTExportModelBodiesResponse734:
    response_default = BTExportModelBodiesResponse734.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTExportModelBodiesResponse734]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetPartStudioBodyDetailsWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    part_ids: list[str] | Unset = UNSET,
    include_surfaces: bool | Unset = False,
    include_composite_parts: bool | Unset = False,
    include_geometric_data: bool | Unset = True,
) -> Response[BTExportModelBodiesResponse734]:
    """Get the body details for a Part Studio.

     See the [Part Studios API Guide](https://onshape-public.github.io/docs/api-adv/partstudios/) for
    details and tutorials.

    Args:
        did (str):
        wvm (GetPartStudioBodyDetailsWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        part_ids (list[str] | Unset):
        include_surfaces (bool | Unset):  Default: False.
        include_composite_parts (bool | Unset):  Default: False.
        include_geometric_data (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTExportModelBodiesResponse734]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
        part_ids=part_ids,
        include_surfaces=include_surfaces,
        include_composite_parts=include_composite_parts,
        include_geometric_data=include_geometric_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetPartStudioBodyDetailsWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    part_ids: list[str] | Unset = UNSET,
    include_surfaces: bool | Unset = False,
    include_composite_parts: bool | Unset = False,
    include_geometric_data: bool | Unset = True,
) -> BTExportModelBodiesResponse734 | None:
    """Get the body details for a Part Studio.

     See the [Part Studios API Guide](https://onshape-public.github.io/docs/api-adv/partstudios/) for
    details and tutorials.

    Args:
        did (str):
        wvm (GetPartStudioBodyDetailsWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        part_ids (list[str] | Unset):
        include_surfaces (bool | Unset):  Default: False.
        include_composite_parts (bool | Unset):  Default: False.
        include_geometric_data (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTExportModelBodiesResponse734
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
        part_ids=part_ids,
        include_surfaces=include_surfaces,
        include_composite_parts=include_composite_parts,
        include_geometric_data=include_geometric_data,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetPartStudioBodyDetailsWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    part_ids: list[str] | Unset = UNSET,
    include_surfaces: bool | Unset = False,
    include_composite_parts: bool | Unset = False,
    include_geometric_data: bool | Unset = True,
) -> Response[BTExportModelBodiesResponse734]:
    """Get the body details for a Part Studio.

     See the [Part Studios API Guide](https://onshape-public.github.io/docs/api-adv/partstudios/) for
    details and tutorials.

    Args:
        did (str):
        wvm (GetPartStudioBodyDetailsWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        part_ids (list[str] | Unset):
        include_surfaces (bool | Unset):  Default: False.
        include_composite_parts (bool | Unset):  Default: False.
        include_geometric_data (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTExportModelBodiesResponse734]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
        part_ids=part_ids,
        include_surfaces=include_surfaces,
        include_composite_parts=include_composite_parts,
        include_geometric_data=include_geometric_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetPartStudioBodyDetailsWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
    part_ids: list[str] | Unset = UNSET,
    include_surfaces: bool | Unset = False,
    include_composite_parts: bool | Unset = False,
    include_geometric_data: bool | Unset = True,
) -> BTExportModelBodiesResponse734 | None:
    """Get the body details for a Part Studio.

     See the [Part Studios API Guide](https://onshape-public.github.io/docs/api-adv/partstudios/) for
    details and tutorials.

    Args:
        did (str):
        wvm (GetPartStudioBodyDetailsWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        part_ids (list[str] | Unset):
        include_surfaces (bool | Unset):  Default: False.
        include_composite_parts (bool | Unset):  Default: False.
        include_geometric_data (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTExportModelBodiesResponse734
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
            rollback_bar_index=rollback_bar_index,
            element_microversion_id=element_microversion_id,
            part_ids=part_ids,
            include_surfaces=include_surfaces,
            include_composite_parts=include_composite_parts,
            include_geometric_data=include_geometric_data,
        )
    ).parsed
