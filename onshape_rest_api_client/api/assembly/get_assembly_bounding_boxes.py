from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_bounding_box_info import BTBoundingBoxInfo
from ...models.get_assembly_bounding_boxes_wvm import GetAssemblyBoundingBoxesWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetAssemblyBoundingBoxesWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    include_hidden: bool | Unset = UNSET,
    display_state_id: str | Unset = UNSET,
    named_position_id: str | Unset = UNSET,
    include_sketches: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params["explodedViewId"] = exploded_view_id

    params["includeHidden"] = include_hidden

    params["displayStateId"] = display_state_id

    params["namedPositionId"] = named_position_id

    params["includeSketches"] = include_sketches

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assemblies/d/{did}/{wvm}/{wvmid}/e/{eid}/boundingboxes".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTBoundingBoxInfo:
    response_default = BTBoundingBoxInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTBoundingBoxInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetAssemblyBoundingBoxesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    include_hidden: bool | Unset = UNSET,
    display_state_id: str | Unset = UNSET,
    named_position_id: str | Unset = UNSET,
    include_sketches: bool | Unset = False,
) -> Response[BTBoundingBoxInfo]:
    """Get bounding box information for the specified assembly.

    Args:
        did (str):
        wvm (GetAssemblyBoundingBoxesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        exploded_view_id (str | Unset):
        include_hidden (bool | Unset):
        display_state_id (str | Unset):
        named_position_id (str | Unset):
        include_sketches (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTBoundingBoxInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        exploded_view_id=exploded_view_id,
        include_hidden=include_hidden,
        display_state_id=display_state_id,
        named_position_id=named_position_id,
        include_sketches=include_sketches,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetAssemblyBoundingBoxesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    include_hidden: bool | Unset = UNSET,
    display_state_id: str | Unset = UNSET,
    named_position_id: str | Unset = UNSET,
    include_sketches: bool | Unset = False,
) -> BTBoundingBoxInfo | None:
    """Get bounding box information for the specified assembly.

    Args:
        did (str):
        wvm (GetAssemblyBoundingBoxesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        exploded_view_id (str | Unset):
        include_hidden (bool | Unset):
        display_state_id (str | Unset):
        named_position_id (str | Unset):
        include_sketches (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTBoundingBoxInfo
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
        include_hidden=include_hidden,
        display_state_id=display_state_id,
        named_position_id=named_position_id,
        include_sketches=include_sketches,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetAssemblyBoundingBoxesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    include_hidden: bool | Unset = UNSET,
    display_state_id: str | Unset = UNSET,
    named_position_id: str | Unset = UNSET,
    include_sketches: bool | Unset = False,
) -> Response[BTBoundingBoxInfo]:
    """Get bounding box information for the specified assembly.

    Args:
        did (str):
        wvm (GetAssemblyBoundingBoxesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        exploded_view_id (str | Unset):
        include_hidden (bool | Unset):
        display_state_id (str | Unset):
        named_position_id (str | Unset):
        include_sketches (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTBoundingBoxInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        exploded_view_id=exploded_view_id,
        include_hidden=include_hidden,
        display_state_id=display_state_id,
        named_position_id=named_position_id,
        include_sketches=include_sketches,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetAssemblyBoundingBoxesWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    exploded_view_id: str | Unset = UNSET,
    include_hidden: bool | Unset = UNSET,
    display_state_id: str | Unset = UNSET,
    named_position_id: str | Unset = UNSET,
    include_sketches: bool | Unset = False,
) -> BTBoundingBoxInfo | None:
    """Get bounding box information for the specified assembly.

    Args:
        did (str):
        wvm (GetAssemblyBoundingBoxesWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        exploded_view_id (str | Unset):
        include_hidden (bool | Unset):
        display_state_id (str | Unset):
        named_position_id (str | Unset):
        include_sketches (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTBoundingBoxInfo
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
            include_hidden=include_hidden,
            display_state_id=display_state_id,
            named_position_id=named_position_id,
            include_sketches=include_sketches,
        )
    ).parsed
