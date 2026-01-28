from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_assembly_mate_values_info import BTAssemblyMateValuesInfo
from ...types import Response


def _get_kwargs(
    did: str,
    wv: str,
    wvid: str,
    eid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assemblies/d/{did}/{wv}/{wvid}/e/{eid}/matevalues".format(
            did=quote(str(did), safe=""),
            wv=quote(str(wv), safe=""),
            wvid=quote(str(wvid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
    }

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
    wv: str,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTAssemblyMateValuesInfo]:
    """Get a list of mate values in the specified assembly.

     Describes the relative position of the first mate connector with respect to the second along the
    designated degrees of freedom (DOF) for mates in the specified assembly.

    Args:
        did (str):
        wv (str):
        wvid (str):
        eid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAssemblyMateValuesInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wv: str,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
) -> BTAssemblyMateValuesInfo | None:
    """Get a list of mate values in the specified assembly.

     Describes the relative position of the first mate connector with respect to the second along the
    designated degrees of freedom (DOF) for mates in the specified assembly.

    Args:
        did (str):
        wv (str):
        wvid (str):
        eid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAssemblyMateValuesInfo
    """

    return sync_detailed(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
        client=client,
    ).parsed


async def asyncio_detailed(
    did: str,
    wv: str,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTAssemblyMateValuesInfo]:
    """Get a list of mate values in the specified assembly.

     Describes the relative position of the first mate connector with respect to the second along the
    designated degrees of freedom (DOF) for mates in the specified assembly.

    Args:
        did (str):
        wv (str):
        wvid (str):
        eid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAssemblyMateValuesInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wv=wv,
        wvid=wvid,
        eid=eid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wv: str,
    wvid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
) -> BTAssemblyMateValuesInfo | None:
    """Get a list of mate values in the specified assembly.

     Describes the relative position of the first mate connector with respect to the second along the
    designated degrees of freedom (DOF) for mates in the specified assembly.

    Args:
        did (str):
        wv (str):
        wvid (str):
        eid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAssemblyMateValuesInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wv=wv,
            wvid=wvid,
            eid=eid,
            client=client,
        )
    ).parsed
