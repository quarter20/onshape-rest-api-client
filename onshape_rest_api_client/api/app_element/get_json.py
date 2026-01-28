from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_get_json_response_2137 import BTGetJsonResponse2137
from ...models.get_json_wvm import GetJsonWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetJsonWvm,
    wvmid: str,
    eid: str,
    *,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["transactionId"] = transaction_id

    params["changeId"] = change_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/appelements/d/{did}/{wvm}/{wvmid}/e/{eid}/content/json".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTGetJsonResponse2137:
    response_default = BTGetJsonResponse2137.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTGetJsonResponse2137]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetJsonWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> Response[BTGetJsonResponse2137]:
    """Get the full JSON tree for the specified workspace/version/microversion.

    Args:
        did (str):
        wvm (GetJsonWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        change_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTGetJsonResponse2137]
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
    wvm: GetJsonWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> BTGetJsonResponse2137 | None:
    """Get the full JSON tree for the specified workspace/version/microversion.

    Args:
        did (str):
        wvm (GetJsonWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        change_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTGetJsonResponse2137
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
    wvm: GetJsonWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> Response[BTGetJsonResponse2137]:
    """Get the full JSON tree for the specified workspace/version/microversion.

    Args:
        did (str):
        wvm (GetJsonWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        change_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTGetJsonResponse2137]
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
    wvm: GetJsonWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> BTGetJsonResponse2137 | None:
    """Get the full JSON tree for the specified workspace/version/microversion.

    Args:
        did (str):
        wvm (GetJsonWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        change_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTGetJsonResponse2137
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
