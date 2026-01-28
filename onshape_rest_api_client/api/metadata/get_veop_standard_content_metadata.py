from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_metadata_object_info import BTMetadataObjectInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    vid: str,
    eid: str,
    pid: str,
    *,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    include_computed_properties: bool | Unset = True,
    include_computed_assembly_properties: bool | Unset = False,
    thumbnail: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["configuration"] = configuration

    params["linkDocumentId"] = link_document_id

    params["includeComputedProperties"] = include_computed_properties

    params["includeComputedAssemblyProperties"] = include_computed_assembly_properties

    params["thumbnail"] = thumbnail

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/metadata/standardcontent/d/{did}/v/{vid}/e/{eid}/p/{pid}".format(
            did=quote(str(did), safe=""),
            vid=quote(str(vid), safe=""),
            eid=quote(str(eid), safe=""),
            pid=quote(str(pid), safe=""),
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
    vid: str,
    eid: str,
    pid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    include_computed_properties: bool | Unset = True,
    include_computed_assembly_properties: bool | Unset = False,
    thumbnail: bool | Unset = False,
) -> Response[BTMetadataObjectInfo]:
    """Get the metadata for a standard content part.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * Specify the part in the `pid` path parameter.
    * The `configuration` and `linkDocumentId` query parameters are required.
    * `includeComputedProperties` can be used to include or omit computed properties. Default value is
    `true`.
    * `includeComputedAssemblyProperties` can be used to query computed assembly properties which are
    generally expensive. Default value is `false`.
    * You can also choose to include a `thumbnail`. Default value is `false`.

    Args:
        did (str):
        vid (str):
        eid (str):
        pid (str):
        configuration (str | Unset):
        link_document_id (str | Unset):
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
        vid=vid,
        eid=eid,
        pid=pid,
        configuration=configuration,
        link_document_id=link_document_id,
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
    vid: str,
    eid: str,
    pid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    include_computed_properties: bool | Unset = True,
    include_computed_assembly_properties: bool | Unset = False,
    thumbnail: bool | Unset = False,
) -> BTMetadataObjectInfo | None:
    """Get the metadata for a standard content part.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * Specify the part in the `pid` path parameter.
    * The `configuration` and `linkDocumentId` query parameters are required.
    * `includeComputedProperties` can be used to include or omit computed properties. Default value is
    `true`.
    * `includeComputedAssemblyProperties` can be used to query computed assembly properties which are
    generally expensive. Default value is `false`.
    * You can also choose to include a `thumbnail`. Default value is `false`.

    Args:
        did (str):
        vid (str):
        eid (str):
        pid (str):
        configuration (str | Unset):
        link_document_id (str | Unset):
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
        vid=vid,
        eid=eid,
        pid=pid,
        client=client,
        configuration=configuration,
        link_document_id=link_document_id,
        include_computed_properties=include_computed_properties,
        include_computed_assembly_properties=include_computed_assembly_properties,
        thumbnail=thumbnail,
    ).parsed


async def asyncio_detailed(
    did: str,
    vid: str,
    eid: str,
    pid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    include_computed_properties: bool | Unset = True,
    include_computed_assembly_properties: bool | Unset = False,
    thumbnail: bool | Unset = False,
) -> Response[BTMetadataObjectInfo]:
    """Get the metadata for a standard content part.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * Specify the part in the `pid` path parameter.
    * The `configuration` and `linkDocumentId` query parameters are required.
    * `includeComputedProperties` can be used to include or omit computed properties. Default value is
    `true`.
    * `includeComputedAssemblyProperties` can be used to query computed assembly properties which are
    generally expensive. Default value is `false`.
    * You can also choose to include a `thumbnail`. Default value is `false`.

    Args:
        did (str):
        vid (str):
        eid (str):
        pid (str):
        configuration (str | Unset):
        link_document_id (str | Unset):
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
        vid=vid,
        eid=eid,
        pid=pid,
        configuration=configuration,
        link_document_id=link_document_id,
        include_computed_properties=include_computed_properties,
        include_computed_assembly_properties=include_computed_assembly_properties,
        thumbnail=thumbnail,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    vid: str,
    eid: str,
    pid: str,
    *,
    client: AuthenticatedClient,
    configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    include_computed_properties: bool | Unset = True,
    include_computed_assembly_properties: bool | Unset = False,
    thumbnail: bool | Unset = False,
) -> BTMetadataObjectInfo | None:
    """Get the metadata for a standard content part.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * Specify the part in the `pid` path parameter.
    * The `configuration` and `linkDocumentId` query parameters are required.
    * `includeComputedProperties` can be used to include or omit computed properties. Default value is
    `true`.
    * `includeComputedAssemblyProperties` can be used to query computed assembly properties which are
    generally expensive. Default value is `false`.
    * You can also choose to include a `thumbnail`. Default value is `false`.

    Args:
        did (str):
        vid (str):
        eid (str):
        pid (str):
        configuration (str | Unset):
        link_document_id (str | Unset):
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
            vid=vid,
            eid=eid,
            pid=pid,
            client=client,
            configuration=configuration,
            link_document_id=link_document_id,
            include_computed_properties=include_computed_properties,
            include_computed_assembly_properties=include_computed_assembly_properties,
            thumbnail=thumbnail,
        )
    ).parsed
