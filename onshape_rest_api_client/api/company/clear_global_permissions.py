from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.clear_global_permissions_response_default import ClearGlobalPermissionsResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cid: str,
    type_: int,
    id: str,
    *,
    permission: list[int] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_permission: list[int] | Unset = UNSET
    if not isinstance(permission, Unset):
        json_permission = permission

    params["permission"] = json_permission

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/companies/{cid}/globalpermission/{type_}/{id}".format(
            cid=quote(str(cid), safe=""),
            type_=quote(str(type_), safe=""),
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClearGlobalPermissionsResponseDefault:
    response_default = ClearGlobalPermissionsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ClearGlobalPermissionsResponseDefault]:
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
    permission: list[int] | Unset = UNSET,
) -> Response[ClearGlobalPermissionsResponseDefault]:
    """Remove global permissions for a company user or team.

     Clear all or some of a user's global permissions

    Args:
        cid (str):
        type_ (int):
        id (str):
        permission (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClearGlobalPermissionsResponseDefault]
    """

    kwargs = _get_kwargs(
        cid=cid,
        type_=type_,
        id=id,
        permission=permission,
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
    permission: list[int] | Unset = UNSET,
) -> ClearGlobalPermissionsResponseDefault | None:
    """Remove global permissions for a company user or team.

     Clear all or some of a user's global permissions

    Args:
        cid (str):
        type_ (int):
        id (str):
        permission (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClearGlobalPermissionsResponseDefault
    """

    return sync_detailed(
        cid=cid,
        type_=type_,
        id=id,
        client=client,
        permission=permission,
    ).parsed


async def asyncio_detailed(
    cid: str,
    type_: int,
    id: str,
    *,
    client: AuthenticatedClient,
    permission: list[int] | Unset = UNSET,
) -> Response[ClearGlobalPermissionsResponseDefault]:
    """Remove global permissions for a company user or team.

     Clear all or some of a user's global permissions

    Args:
        cid (str):
        type_ (int):
        id (str):
        permission (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClearGlobalPermissionsResponseDefault]
    """

    kwargs = _get_kwargs(
        cid=cid,
        type_=type_,
        id=id,
        permission=permission,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    type_: int,
    id: str,
    *,
    client: AuthenticatedClient,
    permission: list[int] | Unset = UNSET,
) -> ClearGlobalPermissionsResponseDefault | None:
    """Remove global permissions for a company user or team.

     Clear all or some of a user's global permissions

    Args:
        cid (str):
        type_ (int):
        id (str):
        permission (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClearGlobalPermissionsResponseDefault
    """

    return (
        await asyncio_detailed(
            cid=cid,
            type_=type_,
            id=id,
            client=client,
            permission=permission,
        )
    ).parsed
