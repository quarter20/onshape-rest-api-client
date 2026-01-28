from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_element_modify_info import BTAppElementModifyInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    bid: str,
    *,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["transactionId"] = transaction_id

    params["changeId"] = change_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/appelements/d/{did}/w/{wid}/e/{eid}/blob/{bid}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
            bid=quote(str(bid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAppElementModifyInfo:
    response_default = BTAppElementModifyInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAppElementModifyInfo]:
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
    bid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> Response[BTAppElementModifyInfo]:
    """Delete a blob subelement from an app element.

    Args:
        did (str):
        wid (str):
        eid (str):
        bid (str):
        transaction_id (str | Unset):
        change_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementModifyInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        bid=bid,
        transaction_id=transaction_id,
        change_id=change_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    eid: str,
    bid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> BTAppElementModifyInfo | None:
    """Delete a blob subelement from an app element.

    Args:
        did (str):
        wid (str):
        eid (str):
        bid (str):
        transaction_id (str | Unset):
        change_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementModifyInfo
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        bid=bid,
        client=client,
        transaction_id=transaction_id,
        change_id=change_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    bid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> Response[BTAppElementModifyInfo]:
    """Delete a blob subelement from an app element.

    Args:
        did (str):
        wid (str):
        eid (str):
        bid (str):
        transaction_id (str | Unset):
        change_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementModifyInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        bid=bid,
        transaction_id=transaction_id,
        change_id=change_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    bid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> BTAppElementModifyInfo | None:
    """Delete a blob subelement from an app element.

    Args:
        did (str):
        wid (str):
        eid (str):
        bid (str):
        transaction_id (str | Unset):
        change_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementModifyInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            bid=bid,
            client=client,
            transaction_id=transaction_id,
            change_id=change_id,
        )
    ).parsed
