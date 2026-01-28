from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_element_bulk_modify_info import BTAppElementBulkModifyInfo
from ...models.bt_app_element_commit_transaction_params import BTAppElementCommitTransactionParams
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    *,
    body: BTAppElementCommitTransactionParams,
    link_document_id: str | Unset = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/appelements/d/{did}/w/{wid}/transactions".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAppElementBulkModifyInfo:
    response_default = BTAppElementBulkModifyInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAppElementBulkModifyInfo]:
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
    body: BTAppElementCommitTransactionParams,
    link_document_id: str | Unset = "",
) -> Response[BTAppElementBulkModifyInfo]:
    """Merge multiple transactions into one microversion.

     If successful, all transactions will be committed to a single microversion. If the call raises an
    error, nothing will be committed.

    Args:
        did (str):
        wid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTAppElementCommitTransactionParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementBulkModifyInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
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
    *,
    client: AuthenticatedClient,
    body: BTAppElementCommitTransactionParams,
    link_document_id: str | Unset = "",
) -> BTAppElementBulkModifyInfo | None:
    """Merge multiple transactions into one microversion.

     If successful, all transactions will be committed to a single microversion. If the call raises an
    error, nothing will be committed.

    Args:
        did (str):
        wid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTAppElementCommitTransactionParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementBulkModifyInfo
    """

    return sync_detailed(
        did=did,
        wid=wid,
        client=client,
        body=body,
        link_document_id=link_document_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTAppElementCommitTransactionParams,
    link_document_id: str | Unset = "",
) -> Response[BTAppElementBulkModifyInfo]:
    """Merge multiple transactions into one microversion.

     If successful, all transactions will be committed to a single microversion. If the call raises an
    error, nothing will be committed.

    Args:
        did (str):
        wid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTAppElementCommitTransactionParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementBulkModifyInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        body=body,
        link_document_id=link_document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    *,
    client: AuthenticatedClient,
    body: BTAppElementCommitTransactionParams,
    link_document_id: str | Unset = "",
) -> BTAppElementBulkModifyInfo | None:
    """Merge multiple transactions into one microversion.

     If successful, all transactions will be committed to a single microversion. If the call raises an
    error, nothing will be committed.

    Args:
        did (str):
        wid (str):
        link_document_id (str | Unset):  Default: ''.
        body (BTAppElementCommitTransactionParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementBulkModifyInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            client=client,
            body=body,
            link_document_id=link_document_id,
        )
    ).parsed
