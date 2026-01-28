from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_root_diff_info import BTRootDiffInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    workspace_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    microversion_id: str | Unset = UNSET,
    source_configuration: str | Unset = UNSET,
    target_configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    params["versionId"] = version_id

    params["microversionId"] = microversion_id

    params["sourceConfiguration"] = source_configuration

    params["targetConfiguration"] = target_configuration

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/compare".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTRootDiffInfo:
    response_default = BTRootDiffInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTRootDiffInfo]:
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
    workspace_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    microversion_id: str | Unset = UNSET,
    source_configuration: str | Unset = UNSET,
    target_configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[BTRootDiffInfo]:
    """Get the differences between two Part Studios in a single document.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        workspace_id (str | Unset):
        version_id (str | Unset):
        microversion_id (str | Unset):
        source_configuration (str | Unset):
        target_configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTRootDiffInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        workspace_id=workspace_id,
        version_id=version_id,
        microversion_id=microversion_id,
        source_configuration=source_configuration,
        target_configuration=target_configuration,
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
    workspace_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    microversion_id: str | Unset = UNSET,
    source_configuration: str | Unset = UNSET,
    target_configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> BTRootDiffInfo | None:
    """Get the differences between two Part Studios in a single document.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        workspace_id (str | Unset):
        version_id (str | Unset):
        microversion_id (str | Unset):
        source_configuration (str | Unset):
        target_configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTRootDiffInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        workspace_id=workspace_id,
        version_id=version_id,
        microversion_id=microversion_id,
        source_configuration=source_configuration,
        target_configuration=target_configuration,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    microversion_id: str | Unset = UNSET,
    source_configuration: str | Unset = UNSET,
    target_configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> Response[BTRootDiffInfo]:
    """Get the differences between two Part Studios in a single document.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        workspace_id (str | Unset):
        version_id (str | Unset):
        microversion_id (str | Unset):
        source_configuration (str | Unset):
        target_configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTRootDiffInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        workspace_id=workspace_id,
        version_id=version_id,
        microversion_id=microversion_id,
        source_configuration=source_configuration,
        target_configuration=target_configuration,
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
    workspace_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    microversion_id: str | Unset = UNSET,
    source_configuration: str | Unset = UNSET,
    target_configuration: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
) -> BTRootDiffInfo | None:
    """Get the differences between two Part Studios in a single document.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        workspace_id (str | Unset):
        version_id (str | Unset):
        microversion_id (str | Unset):
        source_configuration (str | Unset):
        target_configuration (str | Unset):
        link_document_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTRootDiffInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            workspace_id=workspace_id,
            version_id=version_id,
            microversion_id=microversion_id,
            source_configuration=source_configuration,
            target_configuration=target_configuration,
            link_document_id=link_document_id,
        )
    ).parsed
