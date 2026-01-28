from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_copy_element_params import BTCopyElementParams
from ...models.bt_document_element_info import BTDocumentElementInfo
from ...types import Response


def _get_kwargs(
    did: str,
    wid: str,
    *,
    body: BTCopyElementParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/elements/copyelement/{did}/workspace/{wid}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTDocumentElementInfo:
    response_default = BTDocumentElementInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTDocumentElementInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTCopyElementParams,
) -> Response[BTDocumentElementInfo]:
    """Copy an element from a source document.

     Specify the target document and workspace in the URL. Specify the source document, workspace, and
    element in the request body.
    If `anchorElementId` is specified, the copied element will be inserted after the anchor element. If
    not specified, the copied element will be inserted at the end of the tab list.

    Args:
        did (str):
        wid (str):
        body (BTCopyElementParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTDocumentElementInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTCopyElementParams,
) -> BTDocumentElementInfo | None:
    """Copy an element from a source document.

     Specify the target document and workspace in the URL. Specify the source document, workspace, and
    element in the request body.
    If `anchorElementId` is specified, the copied element will be inserted after the anchor element. If
    not specified, the copied element will be inserted at the end of the tab list.

    Args:
        did (str):
        wid (str):
        body (BTCopyElementParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTDocumentElementInfo
    """

    return sync_detailed(
        did=did,
        wid=wid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTCopyElementParams,
) -> Response[BTDocumentElementInfo]:
    """Copy an element from a source document.

     Specify the target document and workspace in the URL. Specify the source document, workspace, and
    element in the request body.
    If `anchorElementId` is specified, the copied element will be inserted after the anchor element. If
    not specified, the copied element will be inserted at the end of the tab list.

    Args:
        did (str):
        wid (str):
        body (BTCopyElementParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTDocumentElementInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTCopyElementParams,
) -> BTDocumentElementInfo | None:
    """Copy an element from a source document.

     Specify the target document and workspace in the URL. Specify the source document, workspace, and
    element in the request body.
    If `anchorElementId` is specified, the copied element will be inserted after the anchor element. If
    not specified, the copied element will be inserted at the end of the tab list.

    Args:
        did (str):
        wid (str):
        body (BTCopyElementParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTDocumentElementInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            client=client,
            body=body,
        )
    ).parsed
