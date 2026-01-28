from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_assembly_item_metadata_info import BTAssemblyItemMetadataInfo
from ...models.get_full_assembly_metadata_wvm import GetFullAssemblyMetadataWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetFullAssemblyMetadataWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    configuration: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/metadata/d/{did}/{wvm}/{wvmid}/e/{eid}/assembly-debug".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAssemblyItemMetadataInfo:
    response_default = BTAssemblyItemMetadataInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAssemblyItemMetadataInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetFullAssemblyMetadataWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = UNSET,
) -> Response[BTAssemblyItemMetadataInfo]:
    """Get the metadata for an assembly, including supporting metadata.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * `linkDocumentId` can be specified where applicable and this combined with the query param
    `inferMetadataOwner` (default value is `false`) will be used to infer metadata owner.
    * `configuration` optional query parameter defaults to default configuration.
    * `includeComputedProperties` can be used to include or omit computed properties. Default value is
    `true`.
    * `includeComputedAssemblyProperties` can be used to query computed assembly properties which are
    generally expensive. Default value is `false`.
    * You can also choose to include a `thumbnail`. Default value is `false`.

    Args:
        did (str):
        wvm (GetFullAssemblyMetadataWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAssemblyItemMetadataInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetFullAssemblyMetadataWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = UNSET,
) -> BTAssemblyItemMetadataInfo | None:
    """Get the metadata for an assembly, including supporting metadata.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * `linkDocumentId` can be specified where applicable and this combined with the query param
    `inferMetadataOwner` (default value is `false`) will be used to infer metadata owner.
    * `configuration` optional query parameter defaults to default configuration.
    * `includeComputedProperties` can be used to include or omit computed properties. Default value is
    `true`.
    * `includeComputedAssemblyProperties` can be used to query computed assembly properties which are
    generally expensive. Default value is `false`.
    * You can also choose to include a `thumbnail`. Default value is `false`.

    Args:
        did (str):
        wvm (GetFullAssemblyMetadataWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAssemblyItemMetadataInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        configuration=configuration,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetFullAssemblyMetadataWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = UNSET,
) -> Response[BTAssemblyItemMetadataInfo]:
    """Get the metadata for an assembly, including supporting metadata.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * `linkDocumentId` can be specified where applicable and this combined with the query param
    `inferMetadataOwner` (default value is `false`) will be used to infer metadata owner.
    * `configuration` optional query parameter defaults to default configuration.
    * `includeComputedProperties` can be used to include or omit computed properties. Default value is
    `true`.
    * `includeComputedAssemblyProperties` can be used to query computed assembly properties which are
    generally expensive. Default value is `false`.
    * You can also choose to include a `thumbnail`. Default value is `false`.

    Args:
        did (str):
        wvm (GetFullAssemblyMetadataWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAssemblyItemMetadataInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        configuration=configuration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetFullAssemblyMetadataWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    configuration: str | Unset = UNSET,
) -> BTAssemblyItemMetadataInfo | None:
    """Get the metadata for an assembly, including supporting metadata.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * `linkDocumentId` can be specified where applicable and this combined with the query param
    `inferMetadataOwner` (default value is `false`) will be used to infer metadata owner.
    * `configuration` optional query parameter defaults to default configuration.
    * `includeComputedProperties` can be used to include or omit computed properties. Default value is
    `true`.
    * `includeComputedAssemblyProperties` can be used to query computed assembly properties which are
    generally expensive. Default value is `false`.
    * You can also choose to include a `thumbnail`. Default value is `false`.

    Args:
        did (str):
        wvm (GetFullAssemblyMetadataWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAssemblyItemMetadataInfo
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
        )
    ).parsed
