from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_metadata_object_info import BTMetadataObjectInfo
from ...models.get_wmve_metadata_wvm import GetWMVEMetadataWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetWMVEMetadataWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    configuration: str | Unset = UNSET,
    infer_metadata_owner: bool | Unset = False,
    depth: str | Unset = "1",
    include_computed_properties: bool | Unset = True,
    include_computed_assembly_properties: bool | Unset = False,
    thumbnail: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params["inferMetadataOwner"] = infer_metadata_owner

    params["depth"] = depth

    params["includeComputedProperties"] = include_computed_properties

    params["includeComputedAssemblyProperties"] = include_computed_assembly_properties

    params["thumbnail"] = thumbnail

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/metadata/d/{did}/{wvm}/{wvmid}/e/{eid}".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTMetadataObjectInfo:
    response_default = BTMetadataObjectInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTMetadataObjectInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetWMVEMetadataWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = UNSET,
    infer_metadata_owner: bool | Unset = False,
    depth: str | Unset = "1",
    include_computed_properties: bool | Unset = True,
    include_computed_assembly_properties: bool | Unset = False,
    thumbnail: bool | Unset = False,
) -> Response[BTMetadataObjectInfo]:
    """Get the metadata for an element.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * `linkDocumentId` can be specified where applicable and this combined with the query param
    `inferMetadataOwner` (default value is `false`) will be used to infer metadata owner.
    * `configuration` optional query parameter defaults to default configuration.
    * You can specify an optional `depth` query parameter to get multiple levels in an assembly. Default
    `depth` is `1`.
    * `includeComputedProperties` can be used to include or omit computed properties. Default value is
    `true`.
    * `includeComputedAssemblyProperties` can be used to query computed assembly properties which are
    generally expensive. Default value is `false`.
    * You can also choose to include a `thumbnail`. Default value is `false`.

    Args:
        did (str):
        wvm (GetWMVEMetadataWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):
        infer_metadata_owner (bool | Unset):  Default: False.
        depth (str | Unset):  Default: '1'.
        include_computed_properties (bool | Unset):  Default: True.
        include_computed_assembly_properties (bool | Unset):  Default: False.
        thumbnail (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTMetadataObjectInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        infer_metadata_owner=infer_metadata_owner,
        depth=depth,
        include_computed_properties=include_computed_properties,
        include_computed_assembly_properties=include_computed_assembly_properties,
        thumbnail=thumbnail,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetWMVEMetadataWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = UNSET,
    infer_metadata_owner: bool | Unset = False,
    depth: str | Unset = "1",
    include_computed_properties: bool | Unset = True,
    include_computed_assembly_properties: bool | Unset = False,
    thumbnail: bool | Unset = False,
) -> BTMetadataObjectInfo | None:
    """Get the metadata for an element.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * `linkDocumentId` can be specified where applicable and this combined with the query param
    `inferMetadataOwner` (default value is `false`) will be used to infer metadata owner.
    * `configuration` optional query parameter defaults to default configuration.
    * You can specify an optional `depth` query parameter to get multiple levels in an assembly. Default
    `depth` is `1`.
    * `includeComputedProperties` can be used to include or omit computed properties. Default value is
    `true`.
    * `includeComputedAssemblyProperties` can be used to query computed assembly properties which are
    generally expensive. Default value is `false`.
    * You can also choose to include a `thumbnail`. Default value is `false`.

    Args:
        did (str):
        wvm (GetWMVEMetadataWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):
        infer_metadata_owner (bool | Unset):  Default: False.
        depth (str | Unset):  Default: '1'.
        include_computed_properties (bool | Unset):  Default: True.
        include_computed_assembly_properties (bool | Unset):  Default: False.
        thumbnail (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTMetadataObjectInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        configuration=configuration,
        infer_metadata_owner=infer_metadata_owner,
        depth=depth,
        include_computed_properties=include_computed_properties,
        include_computed_assembly_properties=include_computed_assembly_properties,
        thumbnail=thumbnail,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetWMVEMetadataWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = UNSET,
    infer_metadata_owner: bool | Unset = False,
    depth: str | Unset = "1",
    include_computed_properties: bool | Unset = True,
    include_computed_assembly_properties: bool | Unset = False,
    thumbnail: bool | Unset = False,
) -> Response[BTMetadataObjectInfo]:
    """Get the metadata for an element.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * `linkDocumentId` can be specified where applicable and this combined with the query param
    `inferMetadataOwner` (default value is `false`) will be used to infer metadata owner.
    * `configuration` optional query parameter defaults to default configuration.
    * You can specify an optional `depth` query parameter to get multiple levels in an assembly. Default
    `depth` is `1`.
    * `includeComputedProperties` can be used to include or omit computed properties. Default value is
    `true`.
    * `includeComputedAssemblyProperties` can be used to query computed assembly properties which are
    generally expensive. Default value is `false`.
    * You can also choose to include a `thumbnail`. Default value is `false`.

    Args:
        did (str):
        wvm (GetWMVEMetadataWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):
        infer_metadata_owner (bool | Unset):  Default: False.
        depth (str | Unset):  Default: '1'.
        include_computed_properties (bool | Unset):  Default: True.
        include_computed_assembly_properties (bool | Unset):  Default: False.
        thumbnail (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTMetadataObjectInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
        infer_metadata_owner=infer_metadata_owner,
        depth=depth,
        include_computed_properties=include_computed_properties,
        include_computed_assembly_properties=include_computed_assembly_properties,
        thumbnail=thumbnail,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetWMVEMetadataWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = UNSET,
    infer_metadata_owner: bool | Unset = False,
    depth: str | Unset = "1",
    include_computed_properties: bool | Unset = True,
    include_computed_assembly_properties: bool | Unset = False,
    thumbnail: bool | Unset = False,
) -> BTMetadataObjectInfo | None:
    """Get the metadata for an element.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * `linkDocumentId` can be specified where applicable and this combined with the query param
    `inferMetadataOwner` (default value is `false`) will be used to infer metadata owner.
    * `configuration` optional query parameter defaults to default configuration.
    * You can specify an optional `depth` query parameter to get multiple levels in an assembly. Default
    `depth` is `1`.
    * `includeComputedProperties` can be used to include or omit computed properties. Default value is
    `true`.
    * `includeComputedAssemblyProperties` can be used to query computed assembly properties which are
    generally expensive. Default value is `false`.
    * You can also choose to include a `thumbnail`. Default value is `false`.

    Args:
        did (str):
        wvm (GetWMVEMetadataWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):
        infer_metadata_owner (bool | Unset):  Default: False.
        depth (str | Unset):  Default: '1'.
        include_computed_properties (bool | Unset):  Default: True.
        include_computed_assembly_properties (bool | Unset):  Default: False.
        thumbnail (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTMetadataObjectInfo
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
            infer_metadata_owner=infer_metadata_owner,
            depth=depth,
            include_computed_properties=include_computed_properties,
            include_computed_assembly_properties=include_computed_assembly_properties,
            thumbnail=thumbnail,
        )
    ).parsed
