from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.btb_export_model_params import BTBExportModelParams
from ...models.export_2_json_response_default import Export2JsonResponseDefault
from ...models.export_2_json_wv import Export2JsonWv
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wv: Export2JsonWv,
    wvid: str,
    eid: str,
    *,
    body: BTBExportModelParams | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/documents/d/{did}/{wv}/{wvid}/e/{eid}/export".format(
            did=quote(str(did), safe=""),
            wv=quote(str(wv), safe=""),
            wvid=quote(str(wvid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Export2JsonResponseDefault:
    response_default = Export2JsonResponseDefault.from_dict(response.content)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Export2JsonResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wv: Export2JsonWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTBExportModelParams | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> Response[Export2JsonResponseDefault]:
    """Export document by document ID, workspace or version ID, and tab ID.

    Args:
        did (str):
        wv (Export2JsonWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTBExportModelParams | Unset): Onshape document export schema

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Export2JsonResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        body=body,
        link_document_id=link_document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wv: Export2JsonWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTBExportModelParams | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> Export2JsonResponseDefault | None:
    """Export document by document ID, workspace or version ID, and tab ID.

    Args:
        did (str):
        wv (Export2JsonWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTBExportModelParams | Unset): Onshape document export schema

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Export2JsonResponseDefault
    """

    return sync_detailed(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        client=client,
        body=body,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wv: Export2JsonWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTBExportModelParams | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> Response[Export2JsonResponseDefault]:
    """Export document by document ID, workspace or version ID, and tab ID.

    Args:
        did (str):
        wv (Export2JsonWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTBExportModelParams | Unset): Onshape document export schema

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Export2JsonResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        body=body,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wv: Export2JsonWv,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTBExportModelParams | Unset = UNSET,
    link_document_id: str | Unset = "",
) -> Export2JsonResponseDefault | None:
    """Export document by document ID, workspace or version ID, and tab ID.

    Args:
        did (str):
        wv (Export2JsonWv):
        wvid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTBExportModelParams | Unset): Onshape document export schema

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Export2JsonResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wv=wv,
            wvid=wvid,
            eid=eid,
            client=client,
            body=body,
            link_document_id=link_document_id,
        )
    ).parsed
