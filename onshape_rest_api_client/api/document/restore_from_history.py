from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_restore_from_history_info import BTRestoreFromHistoryInfo
from ...models.bt_restore_info import BTRestoreInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    vm: str,
    vmid: str,
    *,
    body: BTRestoreInfo | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/documents/{did}/w/{wid}/restore/{vm}/{vmid}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            vm=quote(str(vm), safe=""),
            vmid=quote(str(vmid), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTRestoreFromHistoryInfo:
    response_default = BTRestoreFromHistoryInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTRestoreFromHistoryInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wid: str,
    vm: str,
    vmid: str,
    *,
    client: AuthenticatedClient,
    body: BTRestoreInfo | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> Response[BTRestoreFromHistoryInfo]:
    """Restore version or microversion to workspace by document ID, workspace ID, and version or
    microversion ID.

    Args:
        did (str):
        wid (str):
        vm (str):
        vmid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTRestoreInfo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTRestoreFromHistoryInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        vm=vm,
        vmid=vmid,
        body=body,
        link_document_id=link_document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    vm: str,
    vmid: str,
    *,
    client: AuthenticatedClient,
    body: BTRestoreInfo | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> BTRestoreFromHistoryInfo | None:
    """Restore version or microversion to workspace by document ID, workspace ID, and version or
    microversion ID.

    Args:
        did (str):
        wid (str):
        vm (str):
        vmid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTRestoreInfo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTRestoreFromHistoryInfo
    """

    return sync_detailed(
        did=did,
        wid=wid,
        vm=vm,
        vmid=vmid,
        client=client,
        body=body,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    vm: str,
    vmid: str,
    *,
    client: AuthenticatedClient,
    body: BTRestoreInfo | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> Response[BTRestoreFromHistoryInfo]:
    """Restore version or microversion to workspace by document ID, workspace ID, and version or
    microversion ID.

    Args:
        did (str):
        wid (str):
        vm (str):
        vmid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTRestoreInfo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTRestoreFromHistoryInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        vm=vm,
        vmid=vmid,
        body=body,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    vm: str,
    vmid: str,
    *,
    client: AuthenticatedClient,
    body: BTRestoreInfo | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> BTRestoreFromHistoryInfo | None:
    """Restore version or microversion to workspace by document ID, workspace ID, and version or
    microversion ID.

    Args:
        did (str):
        wid (str):
        vm (str):
        vmid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTRestoreInfo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTRestoreFromHistoryInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            vm=vm,
            vmid=vmid,
            client=client,
            body=body,
            link_document_id=link_document_id,
        )
    ).parsed
