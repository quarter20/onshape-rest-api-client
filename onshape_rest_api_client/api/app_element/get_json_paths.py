from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_get_json_paths_1697 import BTGetJsonPaths1697
from ...models.bt_get_json_paths_response_1544 import BTGetJsonPathsResponse1544
from ...models.get_json_paths_wvm import GetJsonPathsWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: GetJsonPathsWvm,
    wvmid: str,
    eid: str,
    *,
    body: BTGetJsonPaths1697 | Unset = UNSET,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["transactionId"] = transaction_id

    params["changeId"] = change_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/appelements/d/{did}/{wvm}/{wvmid}/e/{eid}/content/jsonpaths".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTGetJsonPathsResponse1544:
    response_default = BTGetJsonPathsResponse1544.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTGetJsonPathsResponse1544]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: GetJsonPathsWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTGetJsonPaths1697 | Unset = UNSET,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> Response[BTGetJsonPathsResponse1544]:
    """Get the JSON at specified paths for an element.

     Use this endpoint to return the JSON at the specified path instead of returning the entire JSON for
    the element. This POST endpoint does not write any information.

    Args:
        did (str):
        wvm (GetJsonPathsWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        change_id (str | Unset):
        body (BTGetJsonPaths1697 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTGetJsonPathsResponse1544]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        body=body,
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
    wvm: GetJsonPathsWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTGetJsonPaths1697 | Unset = UNSET,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> BTGetJsonPathsResponse1544 | None:
    """Get the JSON at specified paths for an element.

     Use this endpoint to return the JSON at the specified path instead of returning the entire JSON for
    the element. This POST endpoint does not write any information.

    Args:
        did (str):
        wvm (GetJsonPathsWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        change_id (str | Unset):
        body (BTGetJsonPaths1697 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTGetJsonPathsResponse1544
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        body=body,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        change_id=change_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: GetJsonPathsWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTGetJsonPaths1697 | Unset = UNSET,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> Response[BTGetJsonPathsResponse1544]:
    """Get the JSON at specified paths for an element.

     Use this endpoint to return the JSON at the specified path instead of returning the entire JSON for
    the element. This POST endpoint does not write any information.

    Args:
        did (str):
        wvm (GetJsonPathsWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        change_id (str | Unset):
        body (BTGetJsonPaths1697 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTGetJsonPathsResponse1544]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        body=body,
        link_document_id=link_document_id,
        transaction_id=transaction_id,
        change_id=change_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: GetJsonPathsWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTGetJsonPaths1697 | Unset = UNSET,
    link_document_id: str | Unset = "",
    transaction_id: str | Unset = UNSET,
    change_id: str | Unset = UNSET,
) -> BTGetJsonPathsResponse1544 | None:
    """Get the JSON at specified paths for an element.

     Use this endpoint to return the JSON at the specified path instead of returning the entire JSON for
    the element. This POST endpoint does not write any information.

    Args:
        did (str):
        wvm (GetJsonPathsWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        transaction_id (str | Unset):
        change_id (str | Unset):
        body (BTGetJsonPaths1697 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTGetJsonPathsResponse1544
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            body=body,
            link_document_id=link_document_id,
            transaction_id=transaction_id,
            change_id=change_id,
        )
    ).parsed
