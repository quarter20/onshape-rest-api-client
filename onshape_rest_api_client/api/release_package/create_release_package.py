from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_release_package_params import BTReleasePackageParams
from ...models.create_release_package_response_default import CreateReleasePackageResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    wfid: str,
    *,
    body: BTReleasePackageParams,
    debug_mode: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["debugMode"] = debug_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/releasepackages/release/{wfid}".format(
            wfid=quote(str(wfid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateReleasePackageResponseDefault:
    response_default = CreateReleasePackageResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateReleasePackageResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    wfid: str,
    *,
    client: AuthenticatedClient,
    body: BTReleasePackageParams,
    debug_mode: bool | Unset = False,
) -> Response[CreateReleasePackageResponseDefault]:
    """Create a new release package for one or more items.

     Once a release package is successfully created, use `updateReleasePackage` to update all desired
    item/package properties, and transition it to the desired state.

    To add items from other documents, you must select `Allow adding items from other documents` in your
    [Release management
    settings](https://cad.onshape.com/help/Content/Plans/release_management_2.htm#rel_candidate_dialog).

    Args:
        wfid (str):
        debug_mode (bool | Unset):  Default: False.
        body (BTReleasePackageParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateReleasePackageResponseDefault]
    """

    kwargs = _get_kwargs(
        wfid=wfid,
        body=body,
        debug_mode=debug_mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    wfid: str,
    *,
    client: AuthenticatedClient,
    body: BTReleasePackageParams,
    debug_mode: bool | Unset = False,
) -> CreateReleasePackageResponseDefault | None:
    """Create a new release package for one or more items.

     Once a release package is successfully created, use `updateReleasePackage` to update all desired
    item/package properties, and transition it to the desired state.

    To add items from other documents, you must select `Allow adding items from other documents` in your
    [Release management
    settings](https://cad.onshape.com/help/Content/Plans/release_management_2.htm#rel_candidate_dialog).

    Args:
        wfid (str):
        debug_mode (bool | Unset):  Default: False.
        body (BTReleasePackageParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateReleasePackageResponseDefault
    """

    return sync_detailed(
        wfid=wfid,
        client=client,
        body=body,
        debug_mode=debug_mode,
    ).parsed


async def asyncio_detailed(
    wfid: str,
    *,
    client: AuthenticatedClient,
    body: BTReleasePackageParams,
    debug_mode: bool | Unset = False,
) -> Response[CreateReleasePackageResponseDefault]:
    """Create a new release package for one or more items.

     Once a release package is successfully created, use `updateReleasePackage` to update all desired
    item/package properties, and transition it to the desired state.

    To add items from other documents, you must select `Allow adding items from other documents` in your
    [Release management
    settings](https://cad.onshape.com/help/Content/Plans/release_management_2.htm#rel_candidate_dialog).

    Args:
        wfid (str):
        debug_mode (bool | Unset):  Default: False.
        body (BTReleasePackageParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateReleasePackageResponseDefault]
    """

    kwargs = _get_kwargs(
        wfid=wfid,
        body=body,
        debug_mode=debug_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wfid: str,
    *,
    client: AuthenticatedClient,
    body: BTReleasePackageParams,
    debug_mode: bool | Unset = False,
) -> CreateReleasePackageResponseDefault | None:
    """Create a new release package for one or more items.

     Once a release package is successfully created, use `updateReleasePackage` to update all desired
    item/package properties, and transition it to the desired state.

    To add items from other documents, you must select `Allow adding items from other documents` in your
    [Release management
    settings](https://cad.onshape.com/help/Content/Plans/release_management_2.htm#rel_candidate_dialog).

    Args:
        wfid (str):
        debug_mode (bool | Unset):  Default: False.
        body (BTReleasePackageParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateReleasePackageResponseDefault
    """

    return (
        await asyncio_detailed(
            wfid=wfid,
            client=client,
            body=body,
            debug_mode=debug_mode,
        )
    ).parsed
