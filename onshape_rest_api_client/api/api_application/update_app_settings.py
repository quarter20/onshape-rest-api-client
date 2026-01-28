from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_user_app_settings_params import BTUserAppSettingsParams
from ...models.update_app_settings_response_default import UpdateAppSettingsResponseDefault
from ...types import Response


def _get_kwargs(
    cid: str,
    uid: str,
    *,
    body: BTUserAppSettingsParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/applications/clients/{cid}/settings/users/{uid}".format(
            cid=quote(str(cid), safe=""),
            uid=quote(str(uid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateAppSettingsResponseDefault:
    response_default = UpdateAppSettingsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateAppSettingsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cid: str,
    uid: str,
    *,
    client: AuthenticatedClient | Client,
    body: BTUserAppSettingsParams,
) -> Response[UpdateAppSettingsResponseDefault]:
    """Update a user's application preference settings.

     This API is only usable with an OAuth token and only by the current user or admin.
    * Add or update a setting identified by key with value.
    * Operation and field may optionally be specified when updating Map type settings.
    * Field specifies the key of the setting Map to update.
    * Operation may be one of:
        * `ADD`: Add or update an existing field of the settings Map.
        * `UPDATE`: Update an existing field of the settings Map and return an error if the field does
    not exist.
        * `REMOVE`: Remove the field from the settings Map.

    Args:
        cid (str):
        uid (str):
        body (BTUserAppSettingsParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAppSettingsResponseDefault]
    """

    kwargs = _get_kwargs(
        cid=cid,
        uid=uid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cid: str,
    uid: str,
    *,
    client: AuthenticatedClient | Client,
    body: BTUserAppSettingsParams,
) -> UpdateAppSettingsResponseDefault | None:
    """Update a user's application preference settings.

     This API is only usable with an OAuth token and only by the current user or admin.
    * Add or update a setting identified by key with value.
    * Operation and field may optionally be specified when updating Map type settings.
    * Field specifies the key of the setting Map to update.
    * Operation may be one of:
        * `ADD`: Add or update an existing field of the settings Map.
        * `UPDATE`: Update an existing field of the settings Map and return an error if the field does
    not exist.
        * `REMOVE`: Remove the field from the settings Map.

    Args:
        cid (str):
        uid (str):
        body (BTUserAppSettingsParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAppSettingsResponseDefault
    """

    return sync_detailed(
        cid=cid,
        uid=uid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    cid: str,
    uid: str,
    *,
    client: AuthenticatedClient | Client,
    body: BTUserAppSettingsParams,
) -> Response[UpdateAppSettingsResponseDefault]:
    """Update a user's application preference settings.

     This API is only usable with an OAuth token and only by the current user or admin.
    * Add or update a setting identified by key with value.
    * Operation and field may optionally be specified when updating Map type settings.
    * Field specifies the key of the setting Map to update.
    * Operation may be one of:
        * `ADD`: Add or update an existing field of the settings Map.
        * `UPDATE`: Update an existing field of the settings Map and return an error if the field does
    not exist.
        * `REMOVE`: Remove the field from the settings Map.

    Args:
        cid (str):
        uid (str):
        body (BTUserAppSettingsParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAppSettingsResponseDefault]
    """

    kwargs = _get_kwargs(
        cid=cid,
        uid=uid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    uid: str,
    *,
    client: AuthenticatedClient | Client,
    body: BTUserAppSettingsParams,
) -> UpdateAppSettingsResponseDefault | None:
    """Update a user's application preference settings.

     This API is only usable with an OAuth token and only by the current user or admin.
    * Add or update a setting identified by key with value.
    * Operation and field may optionally be specified when updating Map type settings.
    * Field specifies the key of the setting Map to update.
    * Operation may be one of:
        * `ADD`: Add or update an existing field of the settings Map.
        * `UPDATE`: Update an existing field of the settings Map and return an error if the field does
    not exist.
        * `REMOVE`: Remove the field from the settings Map.

    Args:
        cid (str):
        uid (str):
        body (BTUserAppSettingsParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAppSettingsResponseDefault
    """

    return (
        await asyncio_detailed(
            cid=cid,
            uid=uid,
            client=client,
            body=body,
        )
    ).parsed
