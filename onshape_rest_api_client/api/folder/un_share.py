from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.un_share_response_default import UnShareResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    fid: str,
    eid: str,
    *,
    entry_type: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["entryType"] = entry_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/folders/{fid}/share/{eid}".format(
            fid=quote(str(fid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UnShareResponseDefault:
    response_default = UnShareResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UnShareResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    entry_type: int | Unset = 0,
) -> Response[UnShareResponseDefault]:
    """Remove permissions from the folder for the specified Access Control List (ACL) entry.

     * Provide the folder ID for the folder to unshare.
     * Provide the `entityType` for the type of entity to remove.
        * 0 (User)
        * 1 (Company)
        * 2 (Team)
        * 3 (Document)
        * 4 (Application)
    * Provide the entity ID in the `eid` param.

    Args:
        fid (str):
        eid (str):
        entry_type (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnShareResponseDefault]
    """

    kwargs = _get_kwargs(
        fid=fid,
        eid=eid,
        entry_type=entry_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    entry_type: int | Unset = 0,
) -> UnShareResponseDefault | None:
    """Remove permissions from the folder for the specified Access Control List (ACL) entry.

     * Provide the folder ID for the folder to unshare.
     * Provide the `entityType` for the type of entity to remove.
        * 0 (User)
        * 1 (Company)
        * 2 (Team)
        * 3 (Document)
        * 4 (Application)
    * Provide the entity ID in the `eid` param.

    Args:
        fid (str):
        eid (str):
        entry_type (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnShareResponseDefault
    """

    return sync_detailed(
        fid=fid,
        eid=eid,
        client=client,
        entry_type=entry_type,
    ).parsed


async def asyncio_detailed(
    fid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    entry_type: int | Unset = 0,
) -> Response[UnShareResponseDefault]:
    """Remove permissions from the folder for the specified Access Control List (ACL) entry.

     * Provide the folder ID for the folder to unshare.
     * Provide the `entityType` for the type of entity to remove.
        * 0 (User)
        * 1 (Company)
        * 2 (Team)
        * 3 (Document)
        * 4 (Application)
    * Provide the entity ID in the `eid` param.

    Args:
        fid (str):
        eid (str):
        entry_type (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnShareResponseDefault]
    """

    kwargs = _get_kwargs(
        fid=fid,
        eid=eid,
        entry_type=entry_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    entry_type: int | Unset = 0,
) -> UnShareResponseDefault | None:
    """Remove permissions from the folder for the specified Access Control List (ACL) entry.

     * Provide the folder ID for the folder to unshare.
     * Provide the `entityType` for the type of entity to remove.
        * 0 (User)
        * 1 (Company)
        * 2 (Team)
        * 3 (Document)
        * 4 (Application)
    * Provide the entity ID in the `eid` param.

    Args:
        fid (str):
        eid (str):
        entry_type (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnShareResponseDefault
    """

    return (
        await asyncio_detailed(
            fid=fid,
            eid=eid,
            client=client,
            entry_type=entry_type,
        )
    ).parsed
