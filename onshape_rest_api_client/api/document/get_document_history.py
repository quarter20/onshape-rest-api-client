from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_document_history_info import BTDocumentHistoryInfo
from ...types import Response


def _get_kwargs(
    did: str,
    wm: str,
    wmid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents/d/{did}/{wm}/{wmid}/documenthistory".format(
            did=quote(str(did), safe=""),
            wm=quote(str(wm), safe=""),
            wmid=quote(str(wmid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[BTDocumentHistoryInfo]:
    response_default = []
    _response_default = response.json()
    for response_default_item_data in _response_default:
        response_default_item = BTDocumentHistoryInfo.from_dict(response_default_item_data)

        response_default.append(response_default_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[BTDocumentHistoryInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wm: str,
    wmid: str,
    *,
    client: AuthenticatedClient,
) -> Response[list[BTDocumentHistoryInfo]]:
    """Retrieve document history by document ID and workspace or microversion ID.

    Args:
        did (str):
        wm (str):
        wmid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTDocumentHistoryInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        wm=wm,
        wmid=wmid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wm: str,
    wmid: str,
    *,
    client: AuthenticatedClient,
) -> list[BTDocumentHistoryInfo] | None:
    """Retrieve document history by document ID and workspace or microversion ID.

    Args:
        did (str):
        wm (str):
        wmid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTDocumentHistoryInfo]
    """

    return sync_detailed(
        did=did,
        wm=wm,
        wmid=wmid,
        client=client,
    ).parsed


async def asyncio_detailed(
    did: str,
    wm: str,
    wmid: str,
    *,
    client: AuthenticatedClient,
) -> Response[list[BTDocumentHistoryInfo]]:
    """Retrieve document history by document ID and workspace or microversion ID.

    Args:
        did (str):
        wm (str):
        wmid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BTDocumentHistoryInfo]]
    """

    kwargs = _get_kwargs(
        did=did,
        wm=wm,
        wmid=wmid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wm: str,
    wmid: str,
    *,
    client: AuthenticatedClient,
) -> list[BTDocumentHistoryInfo] | None:
    """Retrieve document history by document ID and workspace or microversion ID.

    Args:
        did (str):
        wm (str):
        wmid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BTDocumentHistoryInfo]
    """

    return (
        await asyncio_detailed(
            did=did,
            wm=wm,
            wmid=wmid,
            client=client,
        )
    ).parsed
