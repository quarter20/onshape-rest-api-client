from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_sketch_info_response_default import GetSketchInfoResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    configuration: str | Unset = UNSET,
    sketch_id: list[str] | Unset = UNSET,
    output_3d: bool | Unset = False,
    curve_points: bool | Unset = False,
    include_geometry: bool | Unset = True,
    link_document_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["configuration"] = configuration

    json_sketch_id: list[str] | Unset = UNSET
    if not isinstance(sketch_id, Unset):
        json_sketch_id = sketch_id

    params["sketchId"] = json_sketch_id

    params["output3D"] = output_3d

    params["curvePoints"] = curve_points

    params["includeGeometry"] = include_geometry

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/sketches".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetSketchInfoResponseDefault:
    response_default = GetSketchInfoResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSketchInfoResponseDefault]:
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
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    sketch_id: list[str] | Unset = UNSET,
    output_3d: bool | Unset = False,
    curve_points: bool | Unset = False,
    include_geometry: bool | Unset = True,
    link_document_id: str | Unset = UNSET,
) -> Response[GetSketchInfoResponseDefault]:
    """Get information for all sketches in Part Studio.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        configuration (str | Unset):
        sketch_id (list[str] | Unset):
        output_3d (bool | Unset):  Default: False.
        curve_points (bool | Unset):  Default: False.
        include_geometry (bool | Unset):  Default: True.
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSketchInfoResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        configuration=configuration,
        sketch_id=sketch_id,
        output_3d=output_3d,
        curve_points=curve_points,
        include_geometry=include_geometry,
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
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    sketch_id: list[str] | Unset = UNSET,
    output_3d: bool | Unset = False,
    curve_points: bool | Unset = False,
    include_geometry: bool | Unset = True,
    link_document_id: str | Unset = UNSET,
) -> GetSketchInfoResponseDefault | None:
    """Get information for all sketches in Part Studio.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        configuration (str | Unset):
        sketch_id (list[str] | Unset):
        output_3d (bool | Unset):  Default: False.
        curve_points (bool | Unset):  Default: False.
        include_geometry (bool | Unset):  Default: True.
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSketchInfoResponseDefault
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        configuration=configuration,
        sketch_id=sketch_id,
        output_3d=output_3d,
        curve_points=curve_points,
        include_geometry=include_geometry,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    sketch_id: list[str] | Unset = UNSET,
    output_3d: bool | Unset = False,
    curve_points: bool | Unset = False,
    include_geometry: bool | Unset = True,
    link_document_id: str | Unset = UNSET,
) -> Response[GetSketchInfoResponseDefault]:
    """Get information for all sketches in Part Studio.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        configuration (str | Unset):
        sketch_id (list[str] | Unset):
        output_3d (bool | Unset):  Default: False.
        curve_points (bool | Unset):  Default: False.
        include_geometry (bool | Unset):  Default: True.
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSketchInfoResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        configuration=configuration,
        sketch_id=sketch_id,
        output_3d=output_3d,
        curve_points=curve_points,
        include_geometry=include_geometry,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    sketch_id: list[str] | Unset = UNSET,
    output_3d: bool | Unset = False,
    curve_points: bool | Unset = False,
    include_geometry: bool | Unset = True,
    link_document_id: str | Unset = UNSET,
) -> GetSketchInfoResponseDefault | None:
    """Get information for all sketches in Part Studio.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        configuration (str | Unset):
        sketch_id (list[str] | Unset):
        output_3d (bool | Unset):  Default: False.
        curve_points (bool | Unset):  Default: False.
        include_geometry (bool | Unset):  Default: True.
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSketchInfoResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            configuration=configuration,
            sketch_id=sketch_id,
            output_3d=output_3d,
            curve_points=curve_points,
            include_geometry=include_geometry,
            link_document_id=link_document_id,
        )
    ).parsed
