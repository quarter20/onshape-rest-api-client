from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_tessellated_entities_response_default import GetTessellatedEntitiesResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    sid: str,
    *,
    configuration: str | Unset = UNSET,
    entity_id: list[str] | Unset = UNSET,
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["configuration"] = configuration

    json_entity_id: list[str] | Unset = UNSET
    if not isinstance(entity_id, Unset):
        json_entity_id = entity_id

    params["entityId"] = json_entity_id

    params["angleTolerance"] = angle_tolerance

    params["chordTolerance"] = chord_tolerance

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/sketches/{sid}/tessellatedentities".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
            sid=quote(str(sid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetTessellatedEntitiesResponseDefault:
    response_default = GetTessellatedEntitiesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetTessellatedEntitiesResponseDefault]:
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
    sid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    entity_id: list[str] | Unset = UNSET,
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[GetTessellatedEntitiesResponseDefault]:
    """Get the tessellations of a sketch in a Part Studio.

     The accuracy of the tessellation to exact geometry is controlled by the `angleTolerance` and
    `chordTolerance` parameters. The tessellation points are computed closely enough so that neither the
    angle tolerance nor the chord tolerance are exceeded. For most parts, the angular tolerance is the
    most restrictive of the two default tolerances.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        sid (str):
        configuration (str | Unset):
        entity_id (list[str] | Unset):
        angle_tolerance (float | Unset):
        chord_tolerance (float | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTessellatedEntitiesResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        sid=sid,
        configuration=configuration,
        entity_id=entity_id,
        angle_tolerance=angle_tolerance,
        chord_tolerance=chord_tolerance,
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
    sid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    entity_id: list[str] | Unset = UNSET,
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> GetTessellatedEntitiesResponseDefault | None:
    """Get the tessellations of a sketch in a Part Studio.

     The accuracy of the tessellation to exact geometry is controlled by the `angleTolerance` and
    `chordTolerance` parameters. The tessellation points are computed closely enough so that neither the
    angle tolerance nor the chord tolerance are exceeded. For most parts, the angular tolerance is the
    most restrictive of the two default tolerances.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        sid (str):
        configuration (str | Unset):
        entity_id (list[str] | Unset):
        angle_tolerance (float | Unset):
        chord_tolerance (float | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTessellatedEntitiesResponseDefault
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        sid=sid,
        client=client,
        configuration=configuration,
        entity_id=entity_id,
        angle_tolerance=angle_tolerance,
        chord_tolerance=chord_tolerance,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    sid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    entity_id: list[str] | Unset = UNSET,
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[GetTessellatedEntitiesResponseDefault]:
    """Get the tessellations of a sketch in a Part Studio.

     The accuracy of the tessellation to exact geometry is controlled by the `angleTolerance` and
    `chordTolerance` parameters. The tessellation points are computed closely enough so that neither the
    angle tolerance nor the chord tolerance are exceeded. For most parts, the angular tolerance is the
    most restrictive of the two default tolerances.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        sid (str):
        configuration (str | Unset):
        entity_id (list[str] | Unset):
        angle_tolerance (float | Unset):
        chord_tolerance (float | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTessellatedEntitiesResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        sid=sid,
        configuration=configuration,
        entity_id=entity_id,
        angle_tolerance=angle_tolerance,
        chord_tolerance=chord_tolerance,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    sid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    entity_id: list[str] | Unset = UNSET,
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> GetTessellatedEntitiesResponseDefault | None:
    """Get the tessellations of a sketch in a Part Studio.

     The accuracy of the tessellation to exact geometry is controlled by the `angleTolerance` and
    `chordTolerance` parameters. The tessellation points are computed closely enough so that neither the
    angle tolerance nor the chord tolerance are exceeded. For most parts, the angular tolerance is the
    most restrictive of the two default tolerances.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        sid (str):
        configuration (str | Unset):
        entity_id (list[str] | Unset):
        angle_tolerance (float | Unset):
        chord_tolerance (float | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTessellatedEntitiesResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            sid=sid,
            client=client,
            configuration=configuration,
            entity_id=entity_id,
            angle_tolerance=angle_tolerance,
            chord_tolerance=chord_tolerance,
            link_document_id=link_document_id,
        )
    ).parsed
