from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_global_permission_info import BTGlobalPermissionInfo
from ...types import Response


def _get_kwargs(
    cid: str,
    type_: int,
    id: str,
    *,
    body: list[int],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/companies/{cid}/globalpermission/{type_}/{id}".format(
            cid=quote(str(cid), safe=""),
            type_=quote(str(type_), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTGlobalPermissionInfo:
    response_default = BTGlobalPermissionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTGlobalPermissionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cid: str,
    type_: int,
    id: str,
    *,
    client: AuthenticatedClient,
    body: list[int],
) -> Response[BTGlobalPermissionInfo]:
    """Add one or more global permissions to company user or team.

     List of global permissions to grant. See [Onshape Help: Global
    Permissions](https://cad.onshape.com/help/Content/Plans/global_permissions.htm#Assignin) for details
    on each of the available permissions.
     * `0`: Manage role based access control
     * `1`: Manage users, teams, and aliases
     * `2`: Enterprise administrator
     * `3`: Permanently delete
     * `4`: Analytics administrator
     * `5`: Invite guest users
     * `6`: Create projects
     * `7`: Approve releases
     * `8`: Enable link sharing
     * `9`: Create releases
     * `10`: Allow access to the App Store
     * `11`: Create documents and folders in the Enterprise root
     * `12`: Allow access to public documents
     * `17`: Manage non-geometric items
     * `18`: Manage workflows
     * `19`: Transfer documents out of Enterprise
     * `20`: Sync to Arena
     * `21`: Create tasks
     * `22`: Manage standard content metadata
     * `23`: Workspace protection permissions
     * `24`: Import files
     * `25`: Use revision tools  * `26`: Export files

    Args:
        cid (str):
        type_ (int):
        id (str):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTGlobalPermissionInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
        type_=type_,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cid: str,
    type_: int,
    id: str,
    *,
    client: AuthenticatedClient,
    body: list[int],
) -> BTGlobalPermissionInfo | None:
    """Add one or more global permissions to company user or team.

     List of global permissions to grant. See [Onshape Help: Global
    Permissions](https://cad.onshape.com/help/Content/Plans/global_permissions.htm#Assignin) for details
    on each of the available permissions.
     * `0`: Manage role based access control
     * `1`: Manage users, teams, and aliases
     * `2`: Enterprise administrator
     * `3`: Permanently delete
     * `4`: Analytics administrator
     * `5`: Invite guest users
     * `6`: Create projects
     * `7`: Approve releases
     * `8`: Enable link sharing
     * `9`: Create releases
     * `10`: Allow access to the App Store
     * `11`: Create documents and folders in the Enterprise root
     * `12`: Allow access to public documents
     * `17`: Manage non-geometric items
     * `18`: Manage workflows
     * `19`: Transfer documents out of Enterprise
     * `20`: Sync to Arena
     * `21`: Create tasks
     * `22`: Manage standard content metadata
     * `23`: Workspace protection permissions
     * `24`: Import files
     * `25`: Use revision tools  * `26`: Export files

    Args:
        cid (str):
        type_ (int):
        id (str):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTGlobalPermissionInfo
    """

    return sync_detailed(
        cid=cid,
        type_=type_,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    cid: str,
    type_: int,
    id: str,
    *,
    client: AuthenticatedClient,
    body: list[int],
) -> Response[BTGlobalPermissionInfo]:
    """Add one or more global permissions to company user or team.

     List of global permissions to grant. See [Onshape Help: Global
    Permissions](https://cad.onshape.com/help/Content/Plans/global_permissions.htm#Assignin) for details
    on each of the available permissions.
     * `0`: Manage role based access control
     * `1`: Manage users, teams, and aliases
     * `2`: Enterprise administrator
     * `3`: Permanently delete
     * `4`: Analytics administrator
     * `5`: Invite guest users
     * `6`: Create projects
     * `7`: Approve releases
     * `8`: Enable link sharing
     * `9`: Create releases
     * `10`: Allow access to the App Store
     * `11`: Create documents and folders in the Enterprise root
     * `12`: Allow access to public documents
     * `17`: Manage non-geometric items
     * `18`: Manage workflows
     * `19`: Transfer documents out of Enterprise
     * `20`: Sync to Arena
     * `21`: Create tasks
     * `22`: Manage standard content metadata
     * `23`: Workspace protection permissions
     * `24`: Import files
     * `25`: Use revision tools  * `26`: Export files

    Args:
        cid (str):
        type_ (int):
        id (str):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTGlobalPermissionInfo]
    """

    kwargs = _get_kwargs(
        cid=cid,
        type_=type_,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    type_: int,
    id: str,
    *,
    client: AuthenticatedClient,
    body: list[int],
) -> BTGlobalPermissionInfo | None:
    """Add one or more global permissions to company user or team.

     List of global permissions to grant. See [Onshape Help: Global
    Permissions](https://cad.onshape.com/help/Content/Plans/global_permissions.htm#Assignin) for details
    on each of the available permissions.
     * `0`: Manage role based access control
     * `1`: Manage users, teams, and aliases
     * `2`: Enterprise administrator
     * `3`: Permanently delete
     * `4`: Analytics administrator
     * `5`: Invite guest users
     * `6`: Create projects
     * `7`: Approve releases
     * `8`: Enable link sharing
     * `9`: Create releases
     * `10`: Allow access to the App Store
     * `11`: Create documents and folders in the Enterprise root
     * `12`: Allow access to public documents
     * `17`: Manage non-geometric items
     * `18`: Manage workflows
     * `19`: Transfer documents out of Enterprise
     * `20`: Sync to Arena
     * `21`: Create tasks
     * `22`: Manage standard content metadata
     * `23`: Workspace protection permissions
     * `24`: Import files
     * `25`: Use revision tools  * `26`: Export files

    Args:
        cid (str):
        type_ (int):
        id (str):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTGlobalPermissionInfo
    """

    return (
        await asyncio_detailed(
            cid=cid,
            type_=type_,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
