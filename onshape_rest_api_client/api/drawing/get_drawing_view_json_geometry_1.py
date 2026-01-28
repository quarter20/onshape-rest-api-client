from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_drawing_view_json_geometry_1_response_default import GetDrawingViewJsonGeometry1ResponseDefault
from ...models.get_drawing_view_json_geometry_1_wvm import GetDrawingViewJsonGeometry1Wvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetDrawingViewJsonGeometry1Wvm,
    wvmid: str,
    eid: str,
    viewid: str,
    *,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = "",
    change_id: str | Unset = "",
    scale: float | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["transactionId"] = transaction_id

    params["changeId"] = change_id

    params["scale"] = scale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/drawings/d/{did}/{wvm}/{wvmid}/e/{eid}/views/{viewid}/jsongeometry".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
            viewid=quote(str(viewid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetDrawingViewJsonGeometry1ResponseDefault:
    response_default = GetDrawingViewJsonGeometry1ResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetDrawingViewJsonGeometry1ResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetDrawingViewJsonGeometry1Wvm,
    wvmid: str,
    eid: str,
    viewid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = "",
    change_id: str | Unset = "",
    scale: float | Unset = UNSET,
) -> Response[GetDrawingViewJsonGeometry1ResponseDefault]:
    """Get view geometry of a drawing view in JSON format.

    Args:
        did (str):
        wvm (GetDrawingViewJsonGeometry1Wvm):
        wvmid (str):
        eid (str):
        viewid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):  Default: ''.
        change_id (str | Unset):  Default: ''.
        scale (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDrawingViewJsonGeometry1ResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        viewid=viewid,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        change_id=change_id,
        scale=scale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: GetDrawingViewJsonGeometry1Wvm,
    wvmid: str,
    eid: str,
    viewid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = "",
    change_id: str | Unset = "",
    scale: float | Unset = UNSET,
) -> GetDrawingViewJsonGeometry1ResponseDefault | None:
    """Get view geometry of a drawing view in JSON format.

    Args:
        did (str):
        wvm (GetDrawingViewJsonGeometry1Wvm):
        wvmid (str):
        eid (str):
        viewid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):  Default: ''.
        change_id (str | Unset):  Default: ''.
        scale (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDrawingViewJsonGeometry1ResponseDefault
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        viewid=viewid,
        client=client,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        change_id=change_id,
        scale=scale,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetDrawingViewJsonGeometry1Wvm,
    wvmid: str,
    eid: str,
    viewid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = "",
    change_id: str | Unset = "",
    scale: float | Unset = UNSET,
) -> Response[GetDrawingViewJsonGeometry1ResponseDefault]:
    """Get view geometry of a drawing view in JSON format.

    Args:
        did (str):
        wvm (GetDrawingViewJsonGeometry1Wvm):
        wvmid (str):
        eid (str):
        viewid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):  Default: ''.
        change_id (str | Unset):  Default: ''.
        scale (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDrawingViewJsonGeometry1ResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        viewid=viewid,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        change_id=change_id,
        scale=scale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetDrawingViewJsonGeometry1Wvm,
    wvmid: str,
    eid: str,
    viewid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = "",
    change_id: str | Unset = "",
    scale: float | Unset = UNSET,
) -> GetDrawingViewJsonGeometry1ResponseDefault | None:
    """Get view geometry of a drawing view in JSON format.

    Args:
        did (str):
        wvm (GetDrawingViewJsonGeometry1Wvm):
        wvmid (str):
        eid (str):
        viewid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):  Default: ''.
        change_id (str | Unset):  Default: ''.
        scale (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDrawingViewJsonGeometry1ResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            viewid=viewid,
            client=client,
            link_document_id=link_document_id,
            transaction_id=transaction_id,
            change_id=change_id,
            scale=scale,
        )
    ).parsed
