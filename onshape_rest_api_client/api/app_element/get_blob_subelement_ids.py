from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_element_ids_info import BTAppElementIdsInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["transactionId"] = transaction_id

    params["changeId"] = change_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/appelements/d/{did}/{wvm}/{wvmid}/e/{eid}/blob".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAppElementIdsInfo:
    response_default = BTAppElementIdsInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTAppElementIdsInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> Response[BTAppElementIdsInfo]:
    """Get a list of all blob subelement IDs for the specified workspace, version, or microversion.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        transaction_id (str | Unset):
        change_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementIdsInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        transaction_id=transaction_id,
        change_id=change_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> BTAppElementIdsInfo | None:
    """Get a list of all blob subelement IDs for the specified workspace, version, or microversion.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        transaction_id (str | Unset):
        change_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementIdsInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        transaction_id=transaction_id,
        change_id=change_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> Response[BTAppElementIdsInfo]:
    """Get a list of all blob subelement IDs for the specified workspace, version, or microversion.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        transaction_id (str | Unset):
        change_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementIdsInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        transaction_id=transaction_id,
        change_id=change_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> BTAppElementIdsInfo | None:
    """Get a list of all blob subelement IDs for the specified workspace, version, or microversion.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        transaction_id (str | Unset):
        change_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementIdsInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            transaction_id=transaction_id,
            change_id=change_id,
        )
    ).parsed
