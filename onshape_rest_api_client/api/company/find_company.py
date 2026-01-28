from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_list_response_bt_company_info import BTListResponseBTCompanyInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    uid: str | Unset = UNSET,
    active_only: bool | Unset = True,
    include_all: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["uid"] = uid

    params["activeOnly"] = active_only

    params["includeAll"] = include_all

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/companies",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTListResponseBTCompanyInfo:
    response_default = BTListResponseBTCompanyInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTListResponseBTCompanyInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    uid: str | Unset = UNSET,
    active_only: bool | Unset = True,
    include_all: bool | Unset = False,
) -> Response[BTListResponseBTCompanyInfo]:
    """Get all companies to which the specified user belongs.

     If no user is specified, will return all companies associated with the current user.

    Args:
        uid (str | Unset):
        active_only (bool | Unset):  Default: True.
        include_all (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTCompanyInfo]
    """

    kwargs = _get_kwargs(
        uid=uid,
        active_only=active_only,
        include_all=include_all,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    uid: str | Unset = UNSET,
    active_only: bool | Unset = True,
    include_all: bool | Unset = False,
) -> BTListResponseBTCompanyInfo | None:
    """Get all companies to which the specified user belongs.

     If no user is specified, will return all companies associated with the current user.

    Args:
        uid (str | Unset):
        active_only (bool | Unset):  Default: True.
        include_all (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTCompanyInfo
    """

    return sync_detailed(
        client=client,
        uid=uid,
        active_only=active_only,
        include_all=include_all,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    uid: str | Unset = UNSET,
    active_only: bool | Unset = True,
    include_all: bool | Unset = False,
) -> Response[BTListResponseBTCompanyInfo]:
    """Get all companies to which the specified user belongs.

     If no user is specified, will return all companies associated with the current user.

    Args:
        uid (str | Unset):
        active_only (bool | Unset):  Default: True.
        include_all (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTListResponseBTCompanyInfo]
    """

    kwargs = _get_kwargs(
        uid=uid,
        active_only=active_only,
        include_all=include_all,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    uid: str | Unset = UNSET,
    active_only: bool | Unset = True,
    include_all: bool | Unset = False,
) -> BTListResponseBTCompanyInfo | None:
    """Get all companies to which the specified user belongs.

     If no user is specified, will return all companies associated with the current user.

    Args:
        uid (str | Unset):
        active_only (bool | Unset):  Default: True.
        include_all (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTListResponseBTCompanyInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            uid=uid,
            active_only=active_only,
            include_all=include_all,
        )
    ).parsed
