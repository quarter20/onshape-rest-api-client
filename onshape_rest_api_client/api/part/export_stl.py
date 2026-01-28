from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.export_stl_response_default import ExportStlResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    mode: str | Unset = "text",
    grouping: bool | Unset = True,
    scale: float | Unset = 1.0,
    units: str | Unset = "inch",
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    max_facet_width: float | Unset = UNSET,
    min_facet_width: float | Unset = UNSET,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["mode"] = mode

    params["grouping"] = grouping

    params["scale"] = scale

    params["units"] = units

    params["angleTolerance"] = angle_tolerance

    params["chordTolerance"] = chord_tolerance

    params["maxFacetWidth"] = max_facet_width

    params["minFacetWidth"] = min_facet_width

    params["configuration"] = configuration

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/parts/d/{did}/{wvm}/{wvmid}/e/{eid}/partid/{partid}/stl".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
            partid=quote(str(partid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExportStlResponseDefault:
    response_default = ExportStlResponseDefault.from_dict(response.content)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExportStlResponseDefault]:
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
    partid: str,
    *,
    client: AuthenticatedClient,
    mode: str | Unset = "text",
    grouping: bool | Unset = True,
    scale: float | Unset = 1.0,
    units: str | Unset = "inch",
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    max_facet_width: float | Unset = UNSET,
    min_facet_width: float | Unset = UNSET,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[ExportStlResponseDefault]:
    """Synchronously export a part to an STL file.

     Creates a synchronous export of the part (with limited tessellation settings) to an STL file.
    * Returns a 307 redirect from which to download the exported file.
    * Export is much faster than asynchronous endpoints at the expense of limited control on
    tessellation settings.
    * Use the [PartStudio/createPartStudioTranslation](#/PartStudio/createPartStudioTranslation)
    asynchronous export for greater control.

    See [API Guide: Synchronous Exports](https://onshape-public.github.io/docs/api-
    adv/translation/#synchronous-exports) for more details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        partid (str):
        mode (str | Unset):  Default: 'text'.
        grouping (bool | Unset):  Default: True.
        scale (float | Unset):  Default: 1.0.
        units (str | Unset):  Default: 'inch'.
        angle_tolerance (float | Unset):
        chord_tolerance (float | Unset):
        max_facet_width (float | Unset):
        min_facet_width (float | Unset):
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportStlResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        partid=partid,
        mode=mode,
        grouping=grouping,
        scale=scale,
        units=units,
        angle_tolerance=angle_tolerance,
        chord_tolerance=chord_tolerance,
        max_facet_width=max_facet_width,
        min_facet_width=min_facet_width,
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
    partid: str,
    *,
    client: AuthenticatedClient,
    mode: str | Unset = "text",
    grouping: bool | Unset = True,
    scale: float | Unset = 1.0,
    units: str | Unset = "inch",
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    max_facet_width: float | Unset = UNSET,
    min_facet_width: float | Unset = UNSET,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> ExportStlResponseDefault | None:
    """Synchronously export a part to an STL file.

     Creates a synchronous export of the part (with limited tessellation settings) to an STL file.
    * Returns a 307 redirect from which to download the exported file.
    * Export is much faster than asynchronous endpoints at the expense of limited control on
    tessellation settings.
    * Use the [PartStudio/createPartStudioTranslation](#/PartStudio/createPartStudioTranslation)
    asynchronous export for greater control.

    See [API Guide: Synchronous Exports](https://onshape-public.github.io/docs/api-
    adv/translation/#synchronous-exports) for more details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        partid (str):
        mode (str | Unset):  Default: 'text'.
        grouping (bool | Unset):  Default: True.
        scale (float | Unset):  Default: 1.0.
        units (str | Unset):  Default: 'inch'.
        angle_tolerance (float | Unset):
        chord_tolerance (float | Unset):
        max_facet_width (float | Unset):
        min_facet_width (float | Unset):
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportStlResponseDefault
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        partid=partid,
        client=client,
        mode=mode,
        grouping=grouping,
        scale=scale,
        units=units,
        angle_tolerance=angle_tolerance,
        chord_tolerance=chord_tolerance,
        max_facet_width=max_facet_width,
        min_facet_width=min_facet_width,
        configuration=configuration,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    partid: str,
    *,
    client: AuthenticatedClient,
    mode: str | Unset = "text",
    grouping: bool | Unset = True,
    scale: float | Unset = 1.0,
    units: str | Unset = "inch",
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    max_facet_width: float | Unset = UNSET,
    min_facet_width: float | Unset = UNSET,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[ExportStlResponseDefault]:
    """Synchronously export a part to an STL file.

     Creates a synchronous export of the part (with limited tessellation settings) to an STL file.
    * Returns a 307 redirect from which to download the exported file.
    * Export is much faster than asynchronous endpoints at the expense of limited control on
    tessellation settings.
    * Use the [PartStudio/createPartStudioTranslation](#/PartStudio/createPartStudioTranslation)
    asynchronous export for greater control.

    See [API Guide: Synchronous Exports](https://onshape-public.github.io/docs/api-
    adv/translation/#synchronous-exports) for more details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        partid (str):
        mode (str | Unset):  Default: 'text'.
        grouping (bool | Unset):  Default: True.
        scale (float | Unset):  Default: 1.0.
        units (str | Unset):  Default: 'inch'.
        angle_tolerance (float | Unset):
        chord_tolerance (float | Unset):
        max_facet_width (float | Unset):
        min_facet_width (float | Unset):
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportStlResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        partid=partid,
        mode=mode,
        grouping=grouping,
        scale=scale,
        units=units,
        angle_tolerance=angle_tolerance,
        chord_tolerance=chord_tolerance,
        max_facet_width=max_facet_width,
        min_facet_width=min_facet_width,
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
    partid: str,
    *,
    client: AuthenticatedClient,
    mode: str | Unset = "text",
    grouping: bool | Unset = True,
    scale: float | Unset = 1.0,
    units: str | Unset = "inch",
    angle_tolerance: float | Unset = UNSET,
    chord_tolerance: float | Unset = UNSET,
    max_facet_width: float | Unset = UNSET,
    min_facet_width: float | Unset = UNSET,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> ExportStlResponseDefault | None:
    """Synchronously export a part to an STL file.

     Creates a synchronous export of the part (with limited tessellation settings) to an STL file.
    * Returns a 307 redirect from which to download the exported file.
    * Export is much faster than asynchronous endpoints at the expense of limited control on
    tessellation settings.
    * Use the [PartStudio/createPartStudioTranslation](#/PartStudio/createPartStudioTranslation)
    asynchronous export for greater control.

    See [API Guide: Synchronous Exports](https://onshape-public.github.io/docs/api-
    adv/translation/#synchronous-exports) for more details.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        partid (str):
        mode (str | Unset):  Default: 'text'.
        grouping (bool | Unset):  Default: True.
        scale (float | Unset):  Default: 1.0.
        units (str | Unset):  Default: 'inch'.
        angle_tolerance (float | Unset):
        chord_tolerance (float | Unset):
        max_facet_width (float | Unset):
        min_facet_width (float | Unset):
        configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportStlResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            partid=partid,
            client=client,
            mode=mode,
            grouping=grouping,
            scale=scale,
            units=units,
            angle_tolerance=angle_tolerance,
            chord_tolerance=chord_tolerance,
            max_facet_width=max_facet_width,
            min_facet_width=min_facet_width,
            configuration=configuration,
            link_document_id=link_document_id,
        )
    ).parsed
