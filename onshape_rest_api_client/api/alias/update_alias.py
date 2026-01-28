from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_alias_info import BTAliasInfo
from ...models.bt_alias_params import BTAliasParams
from ...types import Response


def _get_kwargs(
    aid: str,
    *,
    body: BTAliasParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/aliases/{aid}".format(
            aid=quote(str(aid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAliasInfo:
    response_default = BTAliasInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTAliasInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    aid: str,
    *,
    client: AuthenticatedClient,
    body: BTAliasParams,
) -> Response[BTAliasInfo]:
    """Add, remove, replace, or rename entries in an alias list.

     `Manage users and teams` global permission is required to call this API.
    * Add new users in the `additions` array.
    * Remove existing users in the `removals` array. Attempts to remove a user that does not exist in
    the Alias list will have no effect.
    * Replace the entire Alias list with the `entries` array.
    * You can also update the alias' `name` and `description`.
    For example, given an Alias with members userA and userB:
    * `additions: [userC]` results in [userA, userB, userC]
    * `removals: [userB]` results in [userA]
    * `entries: [userC, user D]` results in [userC, userD]

    Args:
        aid (str):
        body (BTAliasParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAliasInfo]
    """

    kwargs = _get_kwargs(
        aid=aid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    aid: str,
    *,
    client: AuthenticatedClient,
    body: BTAliasParams,
) -> BTAliasInfo | None:
    """Add, remove, replace, or rename entries in an alias list.

     `Manage users and teams` global permission is required to call this API.
    * Add new users in the `additions` array.
    * Remove existing users in the `removals` array. Attempts to remove a user that does not exist in
    the Alias list will have no effect.
    * Replace the entire Alias list with the `entries` array.
    * You can also update the alias' `name` and `description`.
    For example, given an Alias with members userA and userB:
    * `additions: [userC]` results in [userA, userB, userC]
    * `removals: [userB]` results in [userA]
    * `entries: [userC, user D]` results in [userC, userD]

    Args:
        aid (str):
        body (BTAliasParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAliasInfo
    """

    return sync_detailed(
        aid=aid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    aid: str,
    *,
    client: AuthenticatedClient,
    body: BTAliasParams,
) -> Response[BTAliasInfo]:
    """Add, remove, replace, or rename entries in an alias list.

     `Manage users and teams` global permission is required to call this API.
    * Add new users in the `additions` array.
    * Remove existing users in the `removals` array. Attempts to remove a user that does not exist in
    the Alias list will have no effect.
    * Replace the entire Alias list with the `entries` array.
    * You can also update the alias' `name` and `description`.
    For example, given an Alias with members userA and userB:
    * `additions: [userC]` results in [userA, userB, userC]
    * `removals: [userB]` results in [userA]
    * `entries: [userC, user D]` results in [userC, userD]

    Args:
        aid (str):
        body (BTAliasParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAliasInfo]
    """

    kwargs = _get_kwargs(
        aid=aid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    aid: str,
    *,
    client: AuthenticatedClient,
    body: BTAliasParams,
) -> BTAliasInfo | None:
    """Add, remove, replace, or rename entries in an alias list.

     `Manage users and teams` global permission is required to call this API.
    * Add new users in the `additions` array.
    * Remove existing users in the `removals` array. Attempts to remove a user that does not exist in
    the Alias list will have no effect.
    * Replace the entire Alias list with the `entries` array.
    * You can also update the alias' `name` and `description`.
    For example, given an Alias with members userA and userB:
    * `additions: [userC]` results in [userA, userB, userC]
    * `removals: [userB]` results in [userA]
    * `entries: [userC, user D]` results in [userC, userD]

    Args:
        aid (str):
        body (BTAliasParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAliasInfo
    """

    return (
        await asyncio_detailed(
            aid=aid,
            client=client,
            body=body,
        )
    ).parsed
