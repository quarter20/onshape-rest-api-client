from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_element_modify_info import BTAppElementModifyInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    subelement_ids: list[str] | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_subelement_ids: list[str] | Unset = UNSET
    if not isinstance(subelement_ids, Unset):
        json_subelement_ids = subelement_ids

    params["subelementIds"] = json_subelement_ids

    params["transactionId"] = transaction_id

    params["parentChangeId"] = parent_change_id

    params["description"] = description

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/appelements/d/{did}/{wvm}/{wvmid}/e/{eid}/content/subelements".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
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
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    subelement_ids: list[str] | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
) -> Response[BTAppElementModifyInfo]:
    """Delete multiple subelements array by document ID, workspace or version or microversion ID, tab ID,
    and subelement IDs.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        subelement_ids (list[str] | Unset):
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementModifyInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        subelement_ids=subelement_ids,
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
    *,
    client: AuthenticatedClient,
    subelement_ids: list[str] | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
) -> BTAppElementModifyInfo | None:
    """Delete multiple subelements array by document ID, workspace or version or microversion ID, tab ID,
    and subelement IDs.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        subelement_ids (list[str] | Unset):
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementModifyInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        subelement_ids=subelement_ids,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        description=description,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    subelement_ids: list[str] | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
) -> Response[BTAppElementModifyInfo]:
    """Delete multiple subelements array by document ID, workspace or version or microversion ID, tab ID,
    and subelement IDs.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        subelement_ids (list[str] | Unset):
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementModifyInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        subelement_ids=subelement_ids,
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
    *,
    client: AuthenticatedClient,
    subelement_ids: list[str] | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    parent_change_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
) -> BTAppElementModifyInfo | None:
    """Delete multiple subelements array by document ID, workspace or version or microversion ID, tab ID,
    and subelement IDs.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        subelement_ids (list[str] | Unset):
        transaction_id (str | Unset):
        parent_change_id (str | Unset):
        description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementModifyInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            subelement_ids=subelement_ids,
            transaction_id=transaction_id,
            parent_change_id=parent_change_id,
            description=description,
        )
    ).parsed
