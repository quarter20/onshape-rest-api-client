from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_associative_data_array_info import BTAppAssociativeDataArrayInfo
from ...types import Response


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    body: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/appelements/d/{did}/{wvm}/{wvmid}/e/{eid}/associativedata".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
    }

    _kwargs["json"] = body

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
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: str,
) -> Response[BTAppAssociativeDataArrayInfo]:
    """Set the associative data for the specified app element.

     You can manage associativity with
    [translateIds](https://cad.onshape.com/glassworks/explorer/#/PartStudio/translateIds).

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppAssociativeDataArrayInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        body=body,
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
    body: str,
) -> BTAppAssociativeDataArrayInfo | None:
    """Set the associative data for the specified app element.

     You can manage associativity with
    [translateIds](https://cad.onshape.com/glassworks/explorer/#/PartStudio/translateIds).

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppAssociativeDataArrayInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: str,
) -> Response[BTAppAssociativeDataArrayInfo]:
    """Set the associative data for the specified app element.

     You can manage associativity with
    [translateIds](https://cad.onshape.com/glassworks/explorer/#/PartStudio/translateIds).

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppAssociativeDataArrayInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        body=body,
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
    body: str,
) -> BTAppAssociativeDataArrayInfo | None:
    """Set the associative data for the specified app element.

     You can manage associativity with
    [translateIds](https://cad.onshape.com/glassworks/explorer/#/PartStudio/translateIds).

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppAssociativeDataArrayInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            body=body,
        )
    ).parsed
