from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_variable_studio_scope_info import BTVariableStudioScopeInfo
from ...models.get_variable_studio_scope_wv import GetVariableStudioScopeWv
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wv: GetVariableStudioScopeWv,
    wvid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/variables/d/{did}/{wv}/{wvid}/e/{eid}/variablestudioscope".format(
            did=quote(str(did), safe=""),
            wv=quote(str(wv), safe=""),
            wvid=quote(str(wvid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTVariableStudioScopeInfo:
    response_default = BTVariableStudioScopeInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTVariableStudioScopeInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wv: GetVariableStudioScopeWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
) -> Response[BTVariableStudioScopeInfo]:
    """Get the scope of a Variable Studio.

    Args:
        did (str):
        wv (GetVariableStudioScopeWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTVariableStudioScopeInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        link_document_id=link_document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wv: GetVariableStudioScopeWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
) -> BTVariableStudioScopeInfo | None:
    """Get the scope of a Variable Studio.

    Args:
        did (str):
        wv (GetVariableStudioScopeWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTVariableStudioScopeInfo
    """

    return sync_detailed(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        client=client,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wv: GetVariableStudioScopeWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
) -> Response[BTVariableStudioScopeInfo]:
    """Get the scope of a Variable Studio.

    Args:
        did (str):
        wv (GetVariableStudioScopeWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTVariableStudioScopeInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wv: GetVariableStudioScopeWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
) -> BTVariableStudioScopeInfo | None:
    """Get the scope of a Variable Studio.

    Args:
        did (str):
        wv (GetVariableStudioScopeWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTVariableStudioScopeInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wv=wv,
            wvid=wvid,
            eid=eid,
            client=client,
            link_document_id=link_document_id,
        )
    ).parsed
