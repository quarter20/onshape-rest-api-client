from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.update_wvep_metadata_iden import UpdateWVEPMetadataIden
from ...models.update_wvep_metadata_response_default import UpdateWVEPMetadataResponseDefault
from ...models.update_wvep_metadata_wvm import UpdateWVEPMetadataWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: UpdateWVEPMetadataWvm,
    wvmid: str,
    eid: str,
    iden: UpdateWVEPMetadataIden,
    pid: str,
    *,
    body: str,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params["rollbackBarIndex"] = rollback_bar_index

    params["elementMicroversionId"] = element_microversion_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/metadata/d/{did}/{wvm}/{wvmid}/e/{eid}/{iden}/{pid}".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
            iden=quote(str(iden), safe=""),
            pid=quote(str(pid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateWVEPMetadataResponseDefault:
    response_default = UpdateWVEPMetadataResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateWVEPMetadataResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: UpdateWVEPMetadataWvm,
    wvmid: str,
    eid: str,
    iden: UpdateWVEPMetadataIden,
    pid: str,
    *,
    client: AuthenticatedClient,
    body: str,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
) -> Response[UpdateWVEPMetadataResponseDefault]:
    """Update the metadata for a part.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * Specify the part in the `iden` or `pid` path parameter.
    * The `configuration` optional query parameter uses the default configuration unless otherwise
    specified.
    * `linkDocumentId` can be specified where applicable. Combined with `inferMetadataOwner` (default
    value is `false`), this is used to infer metadata owner.
    * Specify the property metadata to update in the Request body.

    Args:
        did (str):
        wvm (UpdateWVEPMetadataWvm):
        wvmid (str):
        eid (str):
        iden (UpdateWVEPMetadataIden):
        pid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWVEPMetadataResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        iden=iden,
        pid=pid,
        body=body,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: UpdateWVEPMetadataWvm,
    wvmid: str,
    eid: str,
    iden: UpdateWVEPMetadataIden,
    pid: str,
    *,
    client: AuthenticatedClient,
    body: str,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
) -> UpdateWVEPMetadataResponseDefault | None:
    """Update the metadata for a part.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * Specify the part in the `iden` or `pid` path parameter.
    * The `configuration` optional query parameter uses the default configuration unless otherwise
    specified.
    * `linkDocumentId` can be specified where applicable. Combined with `inferMetadataOwner` (default
    value is `false`), this is used to infer metadata owner.
    * Specify the property metadata to update in the Request body.

    Args:
        did (str):
        wvm (UpdateWVEPMetadataWvm):
        wvmid (str):
        eid (str):
        iden (UpdateWVEPMetadataIden):
        pid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWVEPMetadataResponseDefault
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        iden=iden,
        pid=pid,
        client=client,
        body=body,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: UpdateWVEPMetadataWvm,
    wvmid: str,
    eid: str,
    iden: UpdateWVEPMetadataIden,
    pid: str,
    *,
    client: AuthenticatedClient,
    body: str,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
) -> Response[UpdateWVEPMetadataResponseDefault]:
    """Update the metadata for a part.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * Specify the part in the `iden` or `pid` path parameter.
    * The `configuration` optional query parameter uses the default configuration unless otherwise
    specified.
    * `linkDocumentId` can be specified where applicable. Combined with `inferMetadataOwner` (default
    value is `false`), this is used to infer metadata owner.
    * Specify the property metadata to update in the Request body.

    Args:
        did (str):
        wvm (UpdateWVEPMetadataWvm):
        wvmid (str):
        eid (str):
        iden (UpdateWVEPMetadataIden):
        pid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWVEPMetadataResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        iden=iden,
        pid=pid,
        body=body,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: UpdateWVEPMetadataWvm,
    wvmid: str,
    eid: str,
    iden: UpdateWVEPMetadataIden,
    pid: str,
    *,
    client: AuthenticatedClient,
    body: str,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
) -> UpdateWVEPMetadataResponseDefault | None:
    """Update the metadata for a part.

     See [API Guide: Metadata](https://onshape-public.github.io/docs/api-adv/metadata/) for details.
    * Specify the part in the `iden` or `pid` path parameter.
    * The `configuration` optional query parameter uses the default configuration unless otherwise
    specified.
    * `linkDocumentId` can be specified where applicable. Combined with `inferMetadataOwner` (default
    value is `false`), this is used to infer metadata owner.
    * Specify the property metadata to update in the Request body.

    Args:
        did (str):
        wvm (UpdateWVEPMetadataWvm):
        wvmid (str):
        eid (str):
        iden (UpdateWVEPMetadataIden):
        pid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWVEPMetadataResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            iden=iden,
            pid=pid,
            client=client,
            body=body,
            link_document_id=link_document_id,
            configuration=configuration,
            rollback_bar_index=rollback_bar_index,
            element_microversion_id=element_microversion_id,
        )
    ).parsed
