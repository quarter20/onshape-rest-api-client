from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_shaded_views_info import BTShadedViewsInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    view_matrix: str | Unset = "front",
    output_height: int | Unset = 500,
    output_width: int | Unset = 500,
    pixel_size: float | Unset = 0.003,
    edges: str | Unset = "show",
    show_all_parts: bool | Unset = False,
    include_surfaces: bool | Unset = False,
    use_anti_aliasing: bool | Unset = False,
    include_wires: bool | Unset = False,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["viewMatrix"] = view_matrix

    params["outputHeight"] = output_height

    params["outputWidth"] = output_width

    params["pixelSize"] = pixel_size

    params["edges"] = edges

    params["showAllParts"] = show_all_parts

    params["includeSurfaces"] = include_surfaces

    params["useAntiAliasing"] = use_anti_aliasing

    params["includeWires"] = include_wires

    params["configuration"] = configuration

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/shadedviews".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTShadedViewsInfo:
    response_default = BTShadedViewsInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTShadedViewsInfo]:
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
    view_matrix: str | Unset = "front",
    output_height: int | Unset = 500,
    output_width: int | Unset = 500,
    pixel_size: float | Unset = 0.003,
    edges: str | Unset = "show",
    show_all_parts: bool | Unset = False,
    include_surfaces: bool | Unset = False,
    use_anti_aliasing: bool | Unset = False,
    include_wires: bool | Unset = False,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[BTShadedViewsInfo]:
    """Get a list of shaded views for a Part Studio.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        view_matrix (str | Unset):  Default: 'front'.
        output_height (int | Unset):  Default: 500.
        output_width (int | Unset):  Default: 500.
        pixel_size (float | Unset):  Default: 0.003.
        edges (str | Unset):  Default: 'show'.
        show_all_parts (bool | Unset):  Default: False.
        include_surfaces (bool | Unset):  Default: False.
        use_anti_aliasing (bool | Unset):  Default: False.
        include_wires (bool | Unset):  Default: False.
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTShadedViewsInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        view_matrix=view_matrix,
        output_height=output_height,
        output_width=output_width,
        pixel_size=pixel_size,
        edges=edges,
        show_all_parts=show_all_parts,
        include_surfaces=include_surfaces,
        use_anti_aliasing=use_anti_aliasing,
        include_wires=include_wires,
        configuration=configuration,
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
    view_matrix: str | Unset = "front",
    output_height: int | Unset = 500,
    output_width: int | Unset = 500,
    pixel_size: float | Unset = 0.003,
    edges: str | Unset = "show",
    show_all_parts: bool | Unset = False,
    include_surfaces: bool | Unset = False,
    use_anti_aliasing: bool | Unset = False,
    include_wires: bool | Unset = False,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> BTShadedViewsInfo | None:
    """Get a list of shaded views for a Part Studio.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        view_matrix (str | Unset):  Default: 'front'.
        output_height (int | Unset):  Default: 500.
        output_width (int | Unset):  Default: 500.
        pixel_size (float | Unset):  Default: 0.003.
        edges (str | Unset):  Default: 'show'.
        show_all_parts (bool | Unset):  Default: False.
        include_surfaces (bool | Unset):  Default: False.
        use_anti_aliasing (bool | Unset):  Default: False.
        include_wires (bool | Unset):  Default: False.
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTShadedViewsInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        view_matrix=view_matrix,
        output_height=output_height,
        output_width=output_width,
        pixel_size=pixel_size,
        edges=edges,
        show_all_parts=show_all_parts,
        include_surfaces=include_surfaces,
        use_anti_aliasing=use_anti_aliasing,
        include_wires=include_wires,
        configuration=configuration,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    view_matrix: str | Unset = "front",
    output_height: int | Unset = 500,
    output_width: int | Unset = 500,
    pixel_size: float | Unset = 0.003,
    edges: str | Unset = "show",
    show_all_parts: bool | Unset = False,
    include_surfaces: bool | Unset = False,
    use_anti_aliasing: bool | Unset = False,
    include_wires: bool | Unset = False,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[BTShadedViewsInfo]:
    """Get a list of shaded views for a Part Studio.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        view_matrix (str | Unset):  Default: 'front'.
        output_height (int | Unset):  Default: 500.
        output_width (int | Unset):  Default: 500.
        pixel_size (float | Unset):  Default: 0.003.
        edges (str | Unset):  Default: 'show'.
        show_all_parts (bool | Unset):  Default: False.
        include_surfaces (bool | Unset):  Default: False.
        use_anti_aliasing (bool | Unset):  Default: False.
        include_wires (bool | Unset):  Default: False.
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTShadedViewsInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        view_matrix=view_matrix,
        output_height=output_height,
        output_width=output_width,
        pixel_size=pixel_size,
        edges=edges,
        show_all_parts=show_all_parts,
        include_surfaces=include_surfaces,
        use_anti_aliasing=use_anti_aliasing,
        include_wires=include_wires,
        configuration=configuration,
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
    view_matrix: str | Unset = "front",
    output_height: int | Unset = 500,
    output_width: int | Unset = 500,
    pixel_size: float | Unset = 0.003,
    edges: str | Unset = "show",
    show_all_parts: bool | Unset = False,
    include_surfaces: bool | Unset = False,
    use_anti_aliasing: bool | Unset = False,
    include_wires: bool | Unset = False,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> BTShadedViewsInfo | None:
    """Get a list of shaded views for a Part Studio.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        view_matrix (str | Unset):  Default: 'front'.
        output_height (int | Unset):  Default: 500.
        output_width (int | Unset):  Default: 500.
        pixel_size (float | Unset):  Default: 0.003.
        edges (str | Unset):  Default: 'show'.
        show_all_parts (bool | Unset):  Default: False.
        include_surfaces (bool | Unset):  Default: False.
        use_anti_aliasing (bool | Unset):  Default: False.
        include_wires (bool | Unset):  Default: False.
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTShadedViewsInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            view_matrix=view_matrix,
            output_height=output_height,
            output_width=output_width,
            pixel_size=pixel_size,
            edges=edges,
            show_all_parts=show_all_parts,
            include_surfaces=include_surfaces,
            use_anti_aliasing=use_anti_aliasing,
            include_wires=include_wires,
            configuration=configuration,
            link_document_id=link_document_id,
        )
    ).parsed
