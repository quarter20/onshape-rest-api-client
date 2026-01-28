from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bt_link_to_latest_document_info import BTLinkToLatestDocumentInfo
from ...models.bt_link_to_latest_document_params import BTLinkToLatestDocumentParams
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    *,
    body: BTLinkToLatestDocumentParams | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/documents/d/{did}/w/{wid}/e/{eid}/latestdocumentreferences".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTLinkToLatestDocumentInfo | None:
    if response.status_code == 200:
        response_200 = BTLinkToLatestDocumentInfo.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTLinkToLatestDocumentInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTLinkToLatestDocumentParams | Unset = UNSET,
) -> Response[BTLinkToLatestDocumentInfo]:
    """Update external references to latest by document ID, workspace ID, and tab ID.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTLinkToLatestDocumentParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTLinkToLatestDocumentInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTLinkToLatestDocumentParams | Unset = UNSET,
) -> BTLinkToLatestDocumentInfo | None:
    """Update external references to latest by document ID, workspace ID, and tab ID.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTLinkToLatestDocumentParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTLinkToLatestDocumentInfo
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTLinkToLatestDocumentParams | Unset = UNSET,
) -> Response[BTLinkToLatestDocumentInfo]:
    """Update external references to latest by document ID, workspace ID, and tab ID.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTLinkToLatestDocumentParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTLinkToLatestDocumentInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTLinkToLatestDocumentParams | Unset = UNSET,
) -> BTLinkToLatestDocumentInfo | None:
    """Update external references to latest by document ID, workspace ID, and tab ID.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTLinkToLatestDocumentParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTLinkToLatestDocumentInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            client=client,
            body=body,
        )
    ).parsed
