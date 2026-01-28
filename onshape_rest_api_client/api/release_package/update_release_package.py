from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_release_package_info import BTReleasePackageInfo
from ...models.bt_update_release_package_params import BTUpdateReleasePackageParams
from ...types import UNSET, Response, Unset


def _get_kwargs(
    rpid: str,
    *,
    body: BTUpdateReleasePackageParams,
    action: str | Unset = "UPDATE",
    wfaction: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["action"] = action

    params["wfaction"] = wfaction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/releasepackages/{rpid}".format(
            rpid=quote(str(rpid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
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
    body: BTUpdateReleasePackageParams,
    action: str | Unset = "UPDATE",
    wfaction: str | Unset = UNSET,
) -> Response[BTReleasePackageInfo]:
    """Update the release/obsoletion package/item properties.

     Use the `wfaction` query param to also perform a workflow transition.

    Args:
        rpid (str):
        action (str | Unset):  Default: 'UPDATE'.
        wfaction (str | Unset):
        body (BTUpdateReleasePackageParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTReleasePackageInfo]
    """

    kwargs = _get_kwargs(
        rpid=rpid,
        body=body,
        action=action,
        wfaction=wfaction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rpid: str,
    *,
    client: AuthenticatedClient,
    body: BTUpdateReleasePackageParams,
    action: str | Unset = "UPDATE",
    wfaction: str | Unset = UNSET,
) -> BTReleasePackageInfo | None:
    """Update the release/obsoletion package/item properties.

     Use the `wfaction` query param to also perform a workflow transition.

    Args:
        rpid (str):
        action (str | Unset):  Default: 'UPDATE'.
        wfaction (str | Unset):
        body (BTUpdateReleasePackageParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTReleasePackageInfo
    """

    return sync_detailed(
        rpid=rpid,
        client=client,
        body=body,
        action=action,
        wfaction=wfaction,
    ).parsed


async def asyncio_detailed(
    rpid: str,
    *,
    client: AuthenticatedClient,
    body: BTUpdateReleasePackageParams,
    action: str | Unset = "UPDATE",
    wfaction: str | Unset = UNSET,
) -> Response[BTReleasePackageInfo]:
    """Update the release/obsoletion package/item properties.

     Use the `wfaction` query param to also perform a workflow transition.

    Args:
        rpid (str):
        action (str | Unset):  Default: 'UPDATE'.
        wfaction (str | Unset):
        body (BTUpdateReleasePackageParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTReleasePackageInfo]
    """

    kwargs = _get_kwargs(
        rpid=rpid,
        body=body,
        action=action,
        wfaction=wfaction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rpid: str,
    *,
    client: AuthenticatedClient,
    body: BTUpdateReleasePackageParams,
    action: str | Unset = "UPDATE",
    wfaction: str | Unset = UNSET,
) -> BTReleasePackageInfo | None:
    """Update the release/obsoletion package/item properties.

     Use the `wfaction` query param to also perform a workflow transition.

    Args:
        rpid (str):
        action (str | Unset):  Default: 'UPDATE'.
        wfaction (str | Unset):
        body (BTUpdateReleasePackageParams):

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
            body=body,
            action=action,
            wfaction=wfaction,
        )
    ).parsed
