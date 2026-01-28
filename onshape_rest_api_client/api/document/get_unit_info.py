from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_unit_info import BTUnitInfo
from ...models.get_unit_info_wvm import GetUnitInfoWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetUnitInfoWvm,
    wvmid: str,
    *,
    link_document_id: str | Unset = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents/d/{did}/{wvm}/{wvmid}/unitinfo".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTUnitInfo:
    response_default = BTUnitInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTUnitInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetUnitInfoWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient | Client,
    link_document_id: str | Unset = "",
) -> Response[BTUnitInfo]:
    """Get the selected units and precision by document ID and workspace or version or microversion ID.

    Args:
        did (str):
        wvm (GetUnitInfoWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTUnitInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        link_document_id=link_document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetUnitInfoWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient | Client,
    link_document_id: str | Unset = "",
) -> BTUnitInfo | None:
    """Get the selected units and precision by document ID and workspace or version or microversion ID.

    Args:
        did (str):
        wvm (GetUnitInfoWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTUnitInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        client=client,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetUnitInfoWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient | Client,
    link_document_id: str | Unset = "",
) -> Response[BTUnitInfo]:
    """Get the selected units and precision by document ID and workspace or version or microversion ID.

    Args:
        did (str):
        wvm (GetUnitInfoWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTUnitInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetUnitInfoWvm,
    wvmid: str,
    *,
    client: AuthenticatedClient | Client,
    link_document_id: str | Unset = "",
) -> BTUnitInfo | None:
    """Get the selected units and precision by document ID and workspace or version or microversion ID.

    Args:
        did (str):
        wvm (GetUnitInfoWvm):
        wvmid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTUnitInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            client=client,
            link_document_id=link_document_id,
        )
    ).parsed
