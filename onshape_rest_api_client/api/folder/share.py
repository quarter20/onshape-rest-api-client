from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_acl_info import BTAclInfo
from ...models.bt_share_params import BTShareParams
from ...types import Response


def _get_kwargs(
    fid: str,
    *,
    body: BTShareParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/folders/{fid}/share".format(
            fid=quote(str(fid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
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
    body: BTShareParams,
) -> Response[BTAclInfo]:
    """Share folder with an entity.

     * Specify the type of entity to share with using `entries.entryType`:
        * 0 (User)
        * 1 (Company)
        * 2 (Team)
        * 3 (Document)
        * 4 (Application)
    * Provide one of the identifiers in the `entries` object in the request body.
        * You can share with non-Onshape users with the `email` field when `entryType=0`.
     * Provide the string for the permission set. Do not include the integer in parentheses:
        * OWNER (100): Object owner. Implies all permissions including those not listed such as
    permission to transfer ownership.
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
        body (BTShareParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAclInfo]
    """

    kwargs = _get_kwargs(
        fid=fid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fid: str,
    *,
    client: AuthenticatedClient,
    body: BTShareParams,
) -> BTAclInfo | None:
    """Share folder with an entity.

     * Specify the type of entity to share with using `entries.entryType`:
        * 0 (User)
        * 1 (Company)
        * 2 (Team)
        * 3 (Document)
        * 4 (Application)
    * Provide one of the identifiers in the `entries` object in the request body.
        * You can share with non-Onshape users with the `email` field when `entryType=0`.
     * Provide the string for the permission set. Do not include the integer in parentheses:
        * OWNER (100): Object owner. Implies all permissions including those not listed such as
    permission to transfer ownership.
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
        body (BTShareParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAclInfo
    """

    return sync_detailed(
        fid=fid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    fid: str,
    *,
    client: AuthenticatedClient,
    body: BTShareParams,
) -> Response[BTAclInfo]:
    """Share folder with an entity.

     * Specify the type of entity to share with using `entries.entryType`:
        * 0 (User)
        * 1 (Company)
        * 2 (Team)
        * 3 (Document)
        * 4 (Application)
    * Provide one of the identifiers in the `entries` object in the request body.
        * You can share with non-Onshape users with the `email` field when `entryType=0`.
     * Provide the string for the permission set. Do not include the integer in parentheses:
        * OWNER (100): Object owner. Implies all permissions including those not listed such as
    permission to transfer ownership.
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
        body (BTShareParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAclInfo]
    """

    kwargs = _get_kwargs(
        fid=fid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fid: str,
    *,
    client: AuthenticatedClient,
    body: BTShareParams,
) -> BTAclInfo | None:
    """Share folder with an entity.

     * Specify the type of entity to share with using `entries.entryType`:
        * 0 (User)
        * 1 (Company)
        * 2 (Team)
        * 3 (Document)
        * 4 (Application)
    * Provide one of the identifiers in the `entries` object in the request body.
        * You can share with non-Onshape users with the `email` field when `entryType=0`.
     * Provide the string for the permission set. Do not include the integer in parentheses:
        * OWNER (100): Object owner. Implies all permissions including those not listed such as
    permission to transfer ownership.
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
        body (BTShareParams):

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
            body=body,
        )
    ).parsed
