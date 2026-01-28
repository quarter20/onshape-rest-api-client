from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_release_package_info import BTReleasePackageInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    rpid: str,
    *,
    detailed: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["detailed"] = detailed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/releasepackages/{rpid}".format(
            rpid=quote(str(rpid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTReleasePackageInfo:
    response_default = BTReleasePackageInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTReleasePackageInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rpid: str,
    *,
    client: AuthenticatedClient,
    detailed: bool | Unset = False,
) -> Response[BTReleasePackageInfo]:
    """Get details about the specified release package.

    Args:
        rpid (str):
        detailed (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTReleasePackageInfo]
    """

    kwargs = _get_kwargs(
        rpid=rpid,
        detailed=detailed,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rpid: str,
    *,
    client: AuthenticatedClient,
    detailed: bool | Unset = False,
) -> BTReleasePackageInfo | None:
    """Get details about the specified release package.

    Args:
        rpid (str):
        detailed (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTReleasePackageInfo
    """

    return sync_detailed(
        rpid=rpid,
        client=client,
        detailed=detailed,
    ).parsed


async def asyncio_detailed(
    rpid: str,
    *,
    client: AuthenticatedClient,
    detailed: bool | Unset = False,
) -> Response[BTReleasePackageInfo]:
    """Get details about the specified release package.

    Args:
        rpid (str):
        detailed (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTReleasePackageInfo]
    """

    kwargs = _get_kwargs(
        rpid=rpid,
        detailed=detailed,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rpid: str,
    *,
    client: AuthenticatedClient,
    detailed: bool | Unset = False,
) -> BTReleasePackageInfo | None:
    """Get details about the specified release package.

    Args:
        rpid (str):
        detailed (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTReleasePackageInfo
    """

    return (
        await asyncio_detailed(
            rpid=rpid,
            client=client,
            detailed=detailed,
        )
    ).parsed
