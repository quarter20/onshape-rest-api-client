from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_user_settings_info import BTUserSettingsInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    includematerials: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["includematerials"] = includematerials

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/settings",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTUserSettingsInfo:
    response_default = BTUserSettingsInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTUserSettingsInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    includematerials: bool | Unset = True,
) -> Response[BTUserSettingsInfo]:
    """Get the user settings for the signed-in user (i.e., you) for the current session.

     * Non-admins can call this API for their own user ID.
    * Mouse button settings are contained in `reverseScrollWheelZoomDirection` and
    `viewManipulationMouseKeyMapping`.
    * For each action in `viewManipulationMouseKeyMapping`, an array of modifier key/mouse combos is
    provided that performs that action.
    * Possible modifier keys include `SHIFT` and `CTRL`.
    * Possible mouse buttons include `MMB` (middle mouse button), `RMB` (right mouse button), and
    `SCROLLWHEEL`.
    * Scrolling forward zooms in, unless `reverseScrollWheelZoomDirection` is set to `true`.

    Args:
        includematerials (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTUserSettingsInfo]
    """

    kwargs = _get_kwargs(
        includematerials=includematerials,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    includematerials: bool | Unset = True,
) -> BTUserSettingsInfo | None:
    """Get the user settings for the signed-in user (i.e., you) for the current session.

     * Non-admins can call this API for their own user ID.
    * Mouse button settings are contained in `reverseScrollWheelZoomDirection` and
    `viewManipulationMouseKeyMapping`.
    * For each action in `viewManipulationMouseKeyMapping`, an array of modifier key/mouse combos is
    provided that performs that action.
    * Possible modifier keys include `SHIFT` and `CTRL`.
    * Possible mouse buttons include `MMB` (middle mouse button), `RMB` (right mouse button), and
    `SCROLLWHEEL`.
    * Scrolling forward zooms in, unless `reverseScrollWheelZoomDirection` is set to `true`.

    Args:
        includematerials (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTUserSettingsInfo
    """

    return sync_detailed(
        client=client,
        includematerials=includematerials,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    includematerials: bool | Unset = True,
) -> Response[BTUserSettingsInfo]:
    """Get the user settings for the signed-in user (i.e., you) for the current session.

     * Non-admins can call this API for their own user ID.
    * Mouse button settings are contained in `reverseScrollWheelZoomDirection` and
    `viewManipulationMouseKeyMapping`.
    * For each action in `viewManipulationMouseKeyMapping`, an array of modifier key/mouse combos is
    provided that performs that action.
    * Possible modifier keys include `SHIFT` and `CTRL`.
    * Possible mouse buttons include `MMB` (middle mouse button), `RMB` (right mouse button), and
    `SCROLLWHEEL`.
    * Scrolling forward zooms in, unless `reverseScrollWheelZoomDirection` is set to `true`.

    Args:
        includematerials (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTUserSettingsInfo]
    """

    kwargs = _get_kwargs(
        includematerials=includematerials,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    includematerials: bool | Unset = True,
) -> BTUserSettingsInfo | None:
    """Get the user settings for the signed-in user (i.e., you) for the current session.

     * Non-admins can call this API for their own user ID.
    * Mouse button settings are contained in `reverseScrollWheelZoomDirection` and
    `viewManipulationMouseKeyMapping`.
    * For each action in `viewManipulationMouseKeyMapping`, an array of modifier key/mouse combos is
    provided that performs that action.
    * Possible modifier keys include `SHIFT` and `CTRL`.
    * Possible mouse buttons include `MMB` (middle mouse button), `RMB` (right mouse button), and
    `SCROLLWHEEL`.
    * Scrolling forward zooms in, unless `reverseScrollWheelZoomDirection` is set to `true`.

    Args:
        includematerials (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTUserSettingsInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            includematerials=includematerials,
        )
    ).parsed
