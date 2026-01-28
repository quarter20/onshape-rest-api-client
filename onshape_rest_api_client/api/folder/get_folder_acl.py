from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_acl_info import BTAclInfo
from ...types import Response


def _get_kwargs(
    fid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/folders/{fid}/acl".format(
            fid=quote(str(fid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAclInfo:
    response_default = BTAclInfo.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BTAclInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTAclInfo]:
    """Get the Access Control List (ACL) for a folder to view permissions.

     Returns the ACL of permission objects. Each object contains:
    * The type of entity
        * 0 (User)
        * 1 (Company)
        * 2 (Team)
        * 3 (Document)
        * 4 (Application)
     * The ID of the entity for the specified type.
    * The permissions for that entity.
        *  OWNER (100): All permissions, including those not listed, such as permission to transfer
    ownership.
        * DELETE (90)
        * RESHARE (80)
        * WRITE (70)
        * READ (60)
        * LINK (50)
        * COPY (30): Can copy workspace
        * EXPORT (20): Can export geometry
        * COMMENT (10)
        * ANONYMOUS_ACCESS (5): Special, restricted read access

    Args:
        fid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAclInfo]
    """

    kwargs = _get_kwargs(
        fid=fid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fid: str,
    *,
    client: AuthenticatedClient,
) -> BTAclInfo | None:
    """Get the Access Control List (ACL) for a folder to view permissions.

     Returns the ACL of permission objects. Each object contains:
    * The type of entity
        * 0 (User)
        * 1 (Company)
        * 2 (Team)
        * 3 (Document)
        * 4 (Application)
     * The ID of the entity for the specified type.
    * The permissions for that entity.
        *  OWNER (100): All permissions, including those not listed, such as permission to transfer
    ownership.
        * DELETE (90)
        * RESHARE (80)
        * WRITE (70)
        * READ (60)
        * LINK (50)
        * COPY (30): Can copy workspace
        * EXPORT (20): Can export geometry
        * COMMENT (10)
        * ANONYMOUS_ACCESS (5): Special, restricted read access

    Args:
        fid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAclInfo
    """

    return sync_detailed(
        fid=fid,
        client=client,
    ).parsed


async def asyncio_detailed(
    fid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BTAclInfo]:
    """Get the Access Control List (ACL) for a folder to view permissions.

     Returns the ACL of permission objects. Each object contains:
    * The type of entity
        * 0 (User)
        * 1 (Company)
        * 2 (Team)
        * 3 (Document)
        * 4 (Application)
     * The ID of the entity for the specified type.
    * The permissions for that entity.
        *  OWNER (100): All permissions, including those not listed, such as permission to transfer
    ownership.
        * DELETE (90)
        * RESHARE (80)
        * WRITE (70)
        * READ (60)
        * LINK (50)
        * COPY (30): Can copy workspace
        * EXPORT (20): Can export geometry
        * COMMENT (10)
        * ANONYMOUS_ACCESS (5): Special, restricted read access

    Args:
        fid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAclInfo]
    """

    kwargs = _get_kwargs(
        fid=fid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fid: str,
    *,
    client: AuthenticatedClient,
) -> BTAclInfo | None:
    """Get the Access Control List (ACL) for a folder to view permissions.

     Returns the ACL of permission objects. Each object contains:
    * The type of entity
        * 0 (User)
        * 1 (Company)
        * 2 (Team)
        * 3 (Document)
        * 4 (Application)
     * The ID of the entity for the specified type.
    * The permissions for that entity.
        *  OWNER (100): All permissions, including those not listed, such as permission to transfer
    ownership.
        * DELETE (90)
        * RESHARE (80)
        * WRITE (70)
        * READ (60)
        * LINK (50)
        * COPY (30): Can copy workspace
        * EXPORT (20): Can export geometry
        * COMMENT (10)
        * ANONYMOUS_ACCESS (5): Special, restricted read access

    Args:
        fid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAclInfo
    """

    return (
        await asyncio_detailed(
            fid=fid,
            client=client,
        )
    ).parsed
