from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_part_metadata_info import BTPartMetadataInfo
from ...models.get_parts_wmv_wvm import GetPartsWMVWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetPartsWMVWvm,
    wvmid: str,
    *,
    link_document_id: str | Unset = "",
    element_id: str,
    configuration: str | Unset = "",
    with_thumbnails: bool | Unset = False,
    include_property_defaults: bool | Unset = False,
    include_flat_parts: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["elementId"] = element_id

    params["configuration"] = configuration

    params["withThumbnails"] = with_thumbnails

    params["includePropertyDefaults"] = include_property_defaults

    params["includeFlatParts"] = include_flat_parts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/parts/d/{did}/{wvm}/{wvmid}".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[BTPartMetadataInfo]:
    response_default = []
    _response_default = response.json()
    for response_default_item_data in _response_default:
        response_default_item = BTPartMetadataInfo.from_dict(response_default_item_data)

        response_default.append(response_default_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[BTPartMetadataInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetPartsWMVWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    element_id: str,
    configuration: str | Unset = "",
    with_thumbnails: bool | Unset = False,
    include_property_defaults: bool | Unset = False,
    include_flat_parts: bool | Unset = UNSET,
) -> Response[list[BTPartMetadataInfo]]:
    """Get all parts in a workspace, version, or microversion.

    Args:
        did (str):
        wvm (GetPartsWMVWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        element_id (str):
        configuration (str | Unset):  Default: ''.
        with_thumbnails (bool | Unset):  Default: False.
        include_property_defaults (bool | Unset):  Default: False.
        include_flat_parts (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTPartMetadataInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        link_document_id=link_document_id,
        element_id=element_id,
        configuration=configuration,
        with_thumbnails=with_thumbnails,
        include_property_defaults=include_property_defaults,
        include_flat_parts=include_flat_parts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetPartsWMVWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    element_id: str,
    configuration: str | Unset = "",
    with_thumbnails: bool | Unset = False,
    include_property_defaults: bool | Unset = False,
    include_flat_parts: bool | Unset = UNSET,
) -> list[BTPartMetadataInfo] | None:
    """Get all parts in a workspace, version, or microversion.

    Args:
        did (str):
        wvm (GetPartsWMVWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        element_id (str):
        configuration (str | Unset):  Default: ''.
        with_thumbnails (bool | Unset):  Default: False.
        include_property_defaults (bool | Unset):  Default: False.
        include_flat_parts (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTPartMetadataInfo]
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        client=client,
        link_document_id=link_document_id,
        element_id=element_id,
        configuration=configuration,
        with_thumbnails=with_thumbnails,
        include_property_defaults=include_property_defaults,
        include_flat_parts=include_flat_parts,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetPartsWMVWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    element_id: str,
    configuration: str | Unset = "",
    with_thumbnails: bool | Unset = False,
    include_property_defaults: bool | Unset = False,
    include_flat_parts: bool | Unset = UNSET,
) -> Response[list[BTPartMetadataInfo]]:
    """Get all parts in a workspace, version, or microversion.

    Args:
        did (str):
        wvm (GetPartsWMVWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        element_id (str):
        configuration (str | Unset):  Default: ''.
        with_thumbnails (bool | Unset):  Default: False.
        include_property_defaults (bool | Unset):  Default: False.
        include_flat_parts (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTPartMetadataInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        link_document_id=link_document_id,
        element_id=element_id,
        configuration=configuration,
        with_thumbnails=with_thumbnails,
        include_property_defaults=include_property_defaults,
        include_flat_parts=include_flat_parts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetPartsWMVWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    element_id: str,
    configuration: str | Unset = "",
    with_thumbnails: bool | Unset = False,
    include_property_defaults: bool | Unset = False,
    include_flat_parts: bool | Unset = UNSET,
) -> list[BTPartMetadataInfo] | None:
    """Get all parts in a workspace, version, or microversion.

    Args:
        did (str):
        wvm (GetPartsWMVWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.
        element_id (str):
        configuration (str | Unset):  Default: ''.
        with_thumbnails (bool | Unset):  Default: False.
        include_property_defaults (bool | Unset):  Default: False.
        include_flat_parts (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTPartMetadataInfo]
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            client=client,
            link_document_id=link_document_id,
            element_id=element_id,
            configuration=configuration,
            with_thumbnails=with_thumbnails,
            include_property_defaults=include_property_defaults,
            include_flat_parts=include_flat_parts,
        )
    ).parsed
