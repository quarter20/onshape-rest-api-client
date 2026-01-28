from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_element_reference_info import BTAppElementReferenceInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    rid: str,
    *,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["transactionId"] = transaction_id

    params["parentChangeId"] = parent_change_id

    params["description"] = description

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/appelements/d/{did}/{wvm}/{wvmid}/e/{eid}/references/{rid}".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
            rid=quote(str(rid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAppElementReferenceInfo:
    response_default = BTAppElementReferenceInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAppElementReferenceInfo]:
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
    rid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
) -> Response[BTAppElementReferenceInfo]:
    """Delete an app element reference.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        rid (str):
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementReferenceInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        rid=rid,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        description=description,
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
    rid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
) -> BTAppElementReferenceInfo | None:
    """Delete an app element reference.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        rid (str):
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementReferenceInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        rid=rid,
        client=client,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        description=description,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    rid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
) -> Response[BTAppElementReferenceInfo]:
    """Delete an app element reference.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        rid (str):
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementReferenceInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        rid=rid,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        description=description,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    rid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
) -> BTAppElementReferenceInfo | None:
    """Delete an app element reference.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        rid (str):
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementReferenceInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            rid=rid,
            client=client,
            transaction_id=transaction_id,
            parent_change_id=parent_change_id,
            description=description,
        )
    ).parsed
