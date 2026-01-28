from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_company_user_info import BTCompanyUserInfo
from ...models.bt_company_user_params import BTCompanyUserParams
from ...types import Response


def _get_kwargs(
    cid: str,
    uid: str,
    *,
    body: BTCompanyUserParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/companies/{cid}/users/{uid}".format(
            cid=quote(str(cid), safe=""),
            uid=quote(str(uid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTCompanyUserInfo:
    response_default = BTCompanyUserInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTCompanyUserInfo]:
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
    client: AuthenticatedClient,
    body: BTCompanyUserParams,
) -> Response[BTCompanyUserInfo]:
    """Update the company's information for a user.

     Returns updated company user info. `globalPermissions` field is deprecated. Please use the
    following:
    * [addGlobalPermissionsForIdentity](#/Company/addGlobalPermissionsForIdentity)
    * [clearGlobalPermissions](#/Company/clearGlobalPermissions)

    Args:
        cid (str):
        uid (str):
        body (BTCompanyUserParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTCompanyUserInfo]
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
    client: AuthenticatedClient,
    body: BTCompanyUserParams,
) -> BTCompanyUserInfo | None:
    """Update the company's information for a user.

     Returns updated company user info. `globalPermissions` field is deprecated. Please use the
    following:
    * [addGlobalPermissionsForIdentity](#/Company/addGlobalPermissionsForIdentity)
    * [clearGlobalPermissions](#/Company/clearGlobalPermissions)

    Args:
        cid (str):
        uid (str):
        body (BTCompanyUserParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTCompanyUserInfo
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
    client: AuthenticatedClient,
    body: BTCompanyUserParams,
) -> Response[BTCompanyUserInfo]:
    """Update the company's information for a user.

     Returns updated company user info. `globalPermissions` field is deprecated. Please use the
    following:
    * [addGlobalPermissionsForIdentity](#/Company/addGlobalPermissionsForIdentity)
    * [clearGlobalPermissions](#/Company/clearGlobalPermissions)

    Args:
        cid (str):
        uid (str):
        body (BTCompanyUserParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTCompanyUserInfo]
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
    client: AuthenticatedClient,
    body: BTCompanyUserParams,
) -> BTCompanyUserInfo | None:
    """Update the company's information for a user.

     Returns updated company user info. `globalPermissions` field is deprecated. Please use the
    following:
    * [addGlobalPermissionsForIdentity](#/Company/addGlobalPermissionsForIdentity)
    * [clearGlobalPermissions](#/Company/clearGlobalPermissions)

    Args:
        cid (str):
        uid (str):
        body (BTCompanyUserParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTCompanyUserInfo
    """

    return (
        await asyncio_detailed(
            cid=cid,
            uid=uid,
            client=client,
            body=body,
        )
    ).parsed
