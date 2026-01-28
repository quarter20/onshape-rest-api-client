from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_assembly_mate_values_info import BTAssemblyMateValuesInfo
from ...types import Response


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    *,
    body: BTAssemblyMateValuesInfo,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/assemblies/d/{did}/w/{wid}/e/{eid}/matevalues".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAssemblyMateValuesInfo:
    response_default = BTAssemblyMateValuesInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAssemblyMateValuesInfo]:
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
    body: BTAssemblyMateValuesInfo,
) -> Response[BTAssemblyMateValuesInfo]:
    """Update mate values for the given mates in the specified assembly.

     * The input mates must support motion along the provided input degrees of freedom; otherwise, the
    input mate value will be ignored.
    * Values associated with multiple allowed degrees of freedom for a mate can be updated
    simultaneously.
    * Values associated with multiple mate features can be updated simultaneously.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTAssemblyMateValuesInfo): Get a list of mate values for all the mates of a
            specified assembly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAssemblyMateValuesInfo]
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
    body: BTAssemblyMateValuesInfo,
) -> BTAssemblyMateValuesInfo | None:
    """Update mate values for the given mates in the specified assembly.

     * The input mates must support motion along the provided input degrees of freedom; otherwise, the
    input mate value will be ignored.
    * Values associated with multiple allowed degrees of freedom for a mate can be updated
    simultaneously.
    * Values associated with multiple mate features can be updated simultaneously.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTAssemblyMateValuesInfo): Get a list of mate values for all the mates of a
            specified assembly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAssemblyMateValuesInfo
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
    body: BTAssemblyMateValuesInfo,
) -> Response[BTAssemblyMateValuesInfo]:
    """Update mate values for the given mates in the specified assembly.

     * The input mates must support motion along the provided input degrees of freedom; otherwise, the
    input mate value will be ignored.
    * Values associated with multiple allowed degrees of freedom for a mate can be updated
    simultaneously.
    * Values associated with multiple mate features can be updated simultaneously.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTAssemblyMateValuesInfo): Get a list of mate values for all the mates of a
            specified assembly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAssemblyMateValuesInfo]
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
    body: BTAssemblyMateValuesInfo,
) -> BTAssemblyMateValuesInfo | None:
    """Update mate values for the given mates in the specified assembly.

     * The input mates must support motion along the provided input degrees of freedom; otherwise, the
    input mate value will be ignored.
    * Values associated with multiple allowed degrees of freedom for a mate can be updated
    simultaneously.
    * Values associated with multiple mate features can be updated simultaneously.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTAssemblyMateValuesInfo): Get a list of mate values for all the mates of a
            specified assembly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAssemblyMateValuesInfo
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
