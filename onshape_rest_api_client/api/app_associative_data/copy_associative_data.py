from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_associative_data_array_info import BTAppAssociativeDataArrayInfo
from ...models.bt_app_element_params_array_bt_copy_view_associative_data_params import (
    BTAppElementParamsArrayBTCopyViewAssociativeDataParams,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    *,
    body: BTAppElementParamsArrayBTCopyViewAssociativeDataParams | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/appelements/d/{did}/w/{wid}/e/{eid}/copyassociativedata".format(
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


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAppAssociativeDataArrayInfo:
    response_default = BTAppAssociativeDataArrayInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAppAssociativeDataArrayInfo]:
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
    body: BTAppElementParamsArrayBTCopyViewAssociativeDataParams | Unset = UNSET,
) -> Response[BTAppAssociativeDataArrayInfo]:
    """Copy associative data from one view to another.

     Can only be copied between tabs in the same document. You can manage associativity with
    [translateIds](https://cad.onshape.com/glassworks/explorer/#/PartStudio/translateIds).

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTAppElementParamsArrayBTCopyViewAssociativeDataParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppAssociativeDataArrayInfo]
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
    body: BTAppElementParamsArrayBTCopyViewAssociativeDataParams | Unset = UNSET,
) -> BTAppAssociativeDataArrayInfo | None:
    """Copy associative data from one view to another.

     Can only be copied between tabs in the same document. You can manage associativity with
    [translateIds](https://cad.onshape.com/glassworks/explorer/#/PartStudio/translateIds).

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTAppElementParamsArrayBTCopyViewAssociativeDataParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppAssociativeDataArrayInfo
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
    body: BTAppElementParamsArrayBTCopyViewAssociativeDataParams | Unset = UNSET,
) -> Response[BTAppAssociativeDataArrayInfo]:
    """Copy associative data from one view to another.

     Can only be copied between tabs in the same document. You can manage associativity with
    [translateIds](https://cad.onshape.com/glassworks/explorer/#/PartStudio/translateIds).

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTAppElementParamsArrayBTCopyViewAssociativeDataParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppAssociativeDataArrayInfo]
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
    body: BTAppElementParamsArrayBTCopyViewAssociativeDataParams | Unset = UNSET,
) -> BTAppAssociativeDataArrayInfo | None:
    """Copy associative data from one view to another.

     Can only be copied between tabs in the same document. You can manage associativity with
    [translateIds](https://cad.onshape.com/glassworks/explorer/#/PartStudio/translateIds).

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTAppElementParamsArrayBTCopyViewAssociativeDataParams | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppAssociativeDataArrayInfo
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
