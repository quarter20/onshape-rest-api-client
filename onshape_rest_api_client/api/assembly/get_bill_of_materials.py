from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_bill_of_materials_info import BTBillOfMaterialsInfo
from ...models.get_bill_of_materials_wvm import GetBillOfMaterialsWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetBillOfMaterialsWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    bom_column_ids: list[str] | Unset = UNSET,
    indented: bool | Unset = True,
    multi_level: bool | Unset = False,
    generate_if_absent: bool | Unset = False,
    template_id: str | Unset = UNSET,
    include_excluded: bool | Unset = UNSET,
    only_visible_columns: bool | Unset = UNSET,
    ignore_subassembly_bom_behavior: bool | Unset = UNSET,
    include_item_microversions: bool | Unset = False,
    include_top_level_assembly_row: bool | Unset = False,
    thumbnail: bool | Unset = False,
    respect_subassembly_bom_behavior: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    json_bom_column_ids: list[str] | Unset = UNSET
    if not isinstance(bom_column_ids, Unset):
        json_bom_column_ids = bom_column_ids

    params["bomColumnIds"] = json_bom_column_ids

    params["indented"] = indented

    params["multiLevel"] = multi_level

    params["generateIfAbsent"] = generate_if_absent

    params["templateId"] = template_id

    params["includeExcluded"] = include_excluded

    params["onlyVisibleColumns"] = only_visible_columns

    params["ignoreSubassemblyBomBehavior"] = ignore_subassembly_bom_behavior

    params["includeItemMicroversions"] = include_item_microversions

    params["includeTopLevelAssemblyRow"] = include_top_level_assembly_row

    params["thumbnail"] = thumbnail

    params["respectSubassemblyBomBehavior"] = respect_subassembly_bom_behavior

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assemblies/d/{did}/{wvm}/{wvmid}/e/{eid}/bom".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTBillOfMaterialsInfo:
    response_default = BTBillOfMaterialsInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTBillOfMaterialsInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetBillOfMaterialsWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    bom_column_ids: list[str] | Unset = UNSET,
    indented: bool | Unset = True,
    multi_level: bool | Unset = False,
    generate_if_absent: bool | Unset = False,
    template_id: str | Unset = UNSET,
    include_excluded: bool | Unset = UNSET,
    only_visible_columns: bool | Unset = UNSET,
    ignore_subassembly_bom_behavior: bool | Unset = UNSET,
    include_item_microversions: bool | Unset = False,
    include_top_level_assembly_row: bool | Unset = False,
    thumbnail: bool | Unset = False,
    respect_subassembly_bom_behavior: bool | Unset = False,
) -> Response[BTBillOfMaterialsInfo]:
    """Get the Bill Of Materials (BOM) content for the specified assembly.

     Returns the BOM in JSON in the Onshape BOM Standard format.

    Args:
        did (str):
        wvm (GetBillOfMaterialsWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        bom_column_ids (list[str] | Unset):
        indented (bool | Unset):  Default: True.
        multi_level (bool | Unset):  Default: False.
        generate_if_absent (bool | Unset):  Default: False.
        template_id (str | Unset):
        include_excluded (bool | Unset):
        only_visible_columns (bool | Unset):
        ignore_subassembly_bom_behavior (bool | Unset):
        include_item_microversions (bool | Unset):  Default: False.
        include_top_level_assembly_row (bool | Unset):  Default: False.
        thumbnail (bool | Unset):  Default: False.
        respect_subassembly_bom_behavior (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTBillOfMaterialsInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        bom_column_ids=bom_column_ids,
        indented=indented,
        multi_level=multi_level,
        generate_if_absent=generate_if_absent,
        template_id=template_id,
        include_excluded=include_excluded,
        only_visible_columns=only_visible_columns,
        ignore_subassembly_bom_behavior=ignore_subassembly_bom_behavior,
        include_item_microversions=include_item_microversions,
        include_top_level_assembly_row=include_top_level_assembly_row,
        thumbnail=thumbnail,
        respect_subassembly_bom_behavior=respect_subassembly_bom_behavior,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetBillOfMaterialsWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    bom_column_ids: list[str] | Unset = UNSET,
    indented: bool | Unset = True,
    multi_level: bool | Unset = False,
    generate_if_absent: bool | Unset = False,
    template_id: str | Unset = UNSET,
    include_excluded: bool | Unset = UNSET,
    only_visible_columns: bool | Unset = UNSET,
    ignore_subassembly_bom_behavior: bool | Unset = UNSET,
    include_item_microversions: bool | Unset = False,
    include_top_level_assembly_row: bool | Unset = False,
    thumbnail: bool | Unset = False,
    respect_subassembly_bom_behavior: bool | Unset = False,
) -> BTBillOfMaterialsInfo | None:
    """Get the Bill Of Materials (BOM) content for the specified assembly.

     Returns the BOM in JSON in the Onshape BOM Standard format.

    Args:
        did (str):
        wvm (GetBillOfMaterialsWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        bom_column_ids (list[str] | Unset):
        indented (bool | Unset):  Default: True.
        multi_level (bool | Unset):  Default: False.
        generate_if_absent (bool | Unset):  Default: False.
        template_id (str | Unset):
        include_excluded (bool | Unset):
        only_visible_columns (bool | Unset):
        ignore_subassembly_bom_behavior (bool | Unset):
        include_item_microversions (bool | Unset):  Default: False.
        include_top_level_assembly_row (bool | Unset):  Default: False.
        thumbnail (bool | Unset):  Default: False.
        respect_subassembly_bom_behavior (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTBillOfMaterialsInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        configuration=configuration,
        bom_column_ids=bom_column_ids,
        indented=indented,
        multi_level=multi_level,
        generate_if_absent=generate_if_absent,
        template_id=template_id,
        include_excluded=include_excluded,
        only_visible_columns=only_visible_columns,
        ignore_subassembly_bom_behavior=ignore_subassembly_bom_behavior,
        include_item_microversions=include_item_microversions,
        include_top_level_assembly_row=include_top_level_assembly_row,
        thumbnail=thumbnail,
        respect_subassembly_bom_behavior=respect_subassembly_bom_behavior,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetBillOfMaterialsWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    bom_column_ids: list[str] | Unset = UNSET,
    indented: bool | Unset = True,
    multi_level: bool | Unset = False,
    generate_if_absent: bool | Unset = False,
    template_id: str | Unset = UNSET,
    include_excluded: bool | Unset = UNSET,
    only_visible_columns: bool | Unset = UNSET,
    ignore_subassembly_bom_behavior: bool | Unset = UNSET,
    include_item_microversions: bool | Unset = False,
    include_top_level_assembly_row: bool | Unset = False,
    thumbnail: bool | Unset = False,
    respect_subassembly_bom_behavior: bool | Unset = False,
) -> Response[BTBillOfMaterialsInfo]:
    """Get the Bill Of Materials (BOM) content for the specified assembly.

     Returns the BOM in JSON in the Onshape BOM Standard format.

    Args:
        did (str):
        wvm (GetBillOfMaterialsWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        bom_column_ids (list[str] | Unset):
        indented (bool | Unset):  Default: True.
        multi_level (bool | Unset):  Default: False.
        generate_if_absent (bool | Unset):  Default: False.
        template_id (str | Unset):
        include_excluded (bool | Unset):
        only_visible_columns (bool | Unset):
        ignore_subassembly_bom_behavior (bool | Unset):
        include_item_microversions (bool | Unset):  Default: False.
        include_top_level_assembly_row (bool | Unset):  Default: False.
        thumbnail (bool | Unset):  Default: False.
        respect_subassembly_bom_behavior (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTBillOfMaterialsInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        bom_column_ids=bom_column_ids,
        indented=indented,
        multi_level=multi_level,
        generate_if_absent=generate_if_absent,
        template_id=template_id,
        include_excluded=include_excluded,
        only_visible_columns=only_visible_columns,
        ignore_subassembly_bom_behavior=ignore_subassembly_bom_behavior,
        include_item_microversions=include_item_microversions,
        include_top_level_assembly_row=include_top_level_assembly_row,
        thumbnail=thumbnail,
        respect_subassembly_bom_behavior=respect_subassembly_bom_behavior,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetBillOfMaterialsWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    bom_column_ids: list[str] | Unset = UNSET,
    indented: bool | Unset = True,
    multi_level: bool | Unset = False,
    generate_if_absent: bool | Unset = False,
    template_id: str | Unset = UNSET,
    include_excluded: bool | Unset = UNSET,
    only_visible_columns: bool | Unset = UNSET,
    ignore_subassembly_bom_behavior: bool | Unset = UNSET,
    include_item_microversions: bool | Unset = False,
    include_top_level_assembly_row: bool | Unset = False,
    thumbnail: bool | Unset = False,
    respect_subassembly_bom_behavior: bool | Unset = False,
) -> BTBillOfMaterialsInfo | None:
    """Get the Bill Of Materials (BOM) content for the specified assembly.

     Returns the BOM in JSON in the Onshape BOM Standard format.

    Args:
        did (str):
        wvm (GetBillOfMaterialsWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        bom_column_ids (list[str] | Unset):
        indented (bool | Unset):  Default: True.
        multi_level (bool | Unset):  Default: False.
        generate_if_absent (bool | Unset):  Default: False.
        template_id (str | Unset):
        include_excluded (bool | Unset):
        only_visible_columns (bool | Unset):
        ignore_subassembly_bom_behavior (bool | Unset):
        include_item_microversions (bool | Unset):  Default: False.
        include_top_level_assembly_row (bool | Unset):  Default: False.
        thumbnail (bool | Unset):  Default: False.
        respect_subassembly_bom_behavior (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTBillOfMaterialsInfo
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
            bom_column_ids=bom_column_ids,
            indented=indented,
            multi_level=multi_level,
            generate_if_absent=generate_if_absent,
            template_id=template_id,
            include_excluded=include_excluded,
            only_visible_columns=only_visible_columns,
            ignore_subassembly_bom_behavior=ignore_subassembly_bom_behavior,
            include_item_microversions=include_item_microversions,
            include_top_level_assembly_row=include_top_level_assembly_row,
            thumbnail=thumbnail,
            respect_subassembly_bom_behavior=respect_subassembly_bom_behavior,
        )
    ).parsed
