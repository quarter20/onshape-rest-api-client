from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.remove_user_from_company_response_default import RemoveUserFromCompanyResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cid: str,
    uid: str,
    *,
    remove_from_teams: bool | Unset = True,
    remove_direct_shares: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["removeFromTeams"] = remove_from_teams

    params["removeDirectShares"] = remove_direct_shares

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/companies/{cid}/users/{uid}".format(
            cid=quote(str(cid), safe=""),
            uid=quote(str(uid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RemoveUserFromCompanyResponseDefault:
    response_default = RemoveUserFromCompanyResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RemoveUserFromCompanyResponseDefault]:
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
    remove_from_teams: bool | Unset = True,
    remove_direct_shares: bool | Unset = True,
) -> Response[RemoveUserFromCompanyResponseDefault]:
    """Remove a user from a company, company teams, and all the direct shares.

    Args:
        cid (str):
        uid (str):
        remove_from_teams (bool | Unset):  Default: True.
        remove_direct_shares (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveUserFromCompanyResponseDefault]
    """

    kwargs = _get_kwargs(
        cid=cid,
        uid=uid,
        remove_from_teams=remove_from_teams,
        remove_direct_shares=remove_direct_shares,
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
    remove_from_teams: bool | Unset = True,
    remove_direct_shares: bool | Unset = True,
) -> RemoveUserFromCompanyResponseDefault | None:
    """Remove a user from a company, company teams, and all the direct shares.

    Args:
        cid (str):
        uid (str):
        remove_from_teams (bool | Unset):  Default: True.
        remove_direct_shares (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveUserFromCompanyResponseDefault
    """

    return sync_detailed(
        cid=cid,
        uid=uid,
        client=client,
        remove_from_teams=remove_from_teams,
        remove_direct_shares=remove_direct_shares,
    ).parsed


async def asyncio_detailed(
    cid: str,
    uid: str,
    *,
    client: AuthenticatedClient,
    remove_from_teams: bool | Unset = True,
    remove_direct_shares: bool | Unset = True,
) -> Response[RemoveUserFromCompanyResponseDefault]:
    """Remove a user from a company, company teams, and all the direct shares.

    Args:
        cid (str):
        uid (str):
        remove_from_teams (bool | Unset):  Default: True.
        remove_direct_shares (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveUserFromCompanyResponseDefault]
    """

    kwargs = _get_kwargs(
        cid=cid,
        uid=uid,
        remove_from_teams=remove_from_teams,
        remove_direct_shares=remove_direct_shares,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    uid: str,
    *,
    client: AuthenticatedClient,
    remove_from_teams: bool | Unset = True,
    remove_direct_shares: bool | Unset = True,
) -> RemoveUserFromCompanyResponseDefault | None:
    """Remove a user from a company, company teams, and all the direct shares.

    Args:
        cid (str):
        uid (str):
        remove_from_teams (bool | Unset):  Default: True.
        remove_direct_shares (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveUserFromCompanyResponseDefault
    """

    return (
        await asyncio_detailed(
            cid=cid,
            uid=uid,
            client=client,
            remove_from_teams=remove_from_teams,
            remove_direct_shares=remove_direct_shares,
        )
    ).parsed
