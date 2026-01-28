from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_array_info_bt_app_drawing_view_info import BTAppArrayInfoBTAppDrawingViewInfo
from ...models.get_drawing_views_1_wvm import GetDrawingViews1Wvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetDrawingViews1Wvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = "",
    change_id: str | Unset = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["transactionId"] = transaction_id

    params["changeId"] = change_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/drawings/d/{did}/{wvm}/{wvmid}/e/{eid}/views".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTAppArrayInfoBTAppDrawingViewInfo:
    response_default = BTAppArrayInfoBTAppDrawingViewInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAppArrayInfoBTAppDrawingViewInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetDrawingViews1Wvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = "",
    change_id: str | Unset = "",
) -> Response[BTAppArrayInfoBTAppDrawingViewInfo]:
    """Get details of all drawing views.

    Args:
        did (str):
        wvm (GetDrawingViews1Wvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):  Default: ''.
        change_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppArrayInfoBTAppDrawingViewInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        change_id=change_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetDrawingViews1Wvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = "",
    change_id: str | Unset = "",
) -> BTAppArrayInfoBTAppDrawingViewInfo | None:
    """Get details of all drawing views.

    Args:
        did (str):
        wvm (GetDrawingViews1Wvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):  Default: ''.
        change_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppArrayInfoBTAppDrawingViewInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        change_id=change_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetDrawingViews1Wvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = "",
    change_id: str | Unset = "",
) -> Response[BTAppArrayInfoBTAppDrawingViewInfo]:
    """Get details of all drawing views.

    Args:
        did (str):
        wvm (GetDrawingViews1Wvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):  Default: ''.
        change_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppArrayInfoBTAppDrawingViewInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        change_id=change_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetDrawingViews1Wvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = "",
    change_id: str | Unset = "",
) -> BTAppArrayInfoBTAppDrawingViewInfo | None:
    """Get details of all drawing views.

    Args:
        did (str):
        wvm (GetDrawingViews1Wvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):  Default: ''.
        change_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppArrayInfoBTAppDrawingViewInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            link_document_id=link_document_id,
            transaction_id=transaction_id,
            change_id=change_id,
        )
    ).parsed
